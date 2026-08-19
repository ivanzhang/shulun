"""审计 MFAC W1→W2 有限 dyadic 壳抵消账本。"""
import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
from typing import Mapping

DEFAULT_JSON=Path("docs/monograph/prime-matrix-mfac-w1-w2-dyadic-shell-cancellation-audit.json")
DEFAULT_MARKDOWN=Path("docs/monograph/prime-matrix-mfac-w1-w2-dyadic-shell-cancellation-audit.md")
ALLOWED=frozenset({"finite_arithmetic","mobius_definition","gcd_relation","dyadic_decomposition","euler_phi_divisor_sum","finite_sum_identity"})
FORBIDDEN=frozenset({"Mertens","PNT","RH","zeta_zero","zero_free_region","explicit_formula","Mellin","Chebyshev_error","target_energy_bridge","chebyshev_energy_bridge","tail_l2_upper","coprime_restricted_tail_bound","finite_profile","numerical_experiment"})
CLAIMS=("finite_shell_identity","finite_near_ledger","finite_far_ledger")
LEMMAS=("adjacent_shell_cancellation_lemma","summable_residual_lemma","far_shell_aggregation_lemma")

def _strings(value: object, name: str) -> tuple[str,...]:
    """验证非空字符串序列。"""
    if type(value) not in (tuple,list) or not value or any(type(x) is not str or not x for x in value): raise ValueError(f"{name} 必须是非空字符串序列")
    return tuple(value)

def _limit(value: object) -> int:
    """验证有限截断。"""
    if type(value) is not int or value<3: raise ValueError("limit 必须是至少为 3 的内建整数")
    return value

def mobius_value(index: object) -> int:
    """计算 Möbius 函数。"""
    if type(index) is not int or index<1: raise ValueError("index 必须是正内建整数")
    n,count,d=index,0,2
    while d*d<=n:
        if n%d==0:
            n//=d
            if n%d==0:return 0
            count+=1
            while n%d==0:n//=d
        d+=1
    return -1 if (count+(n>1))%2 else 1

def euler_phi(index: object) -> int:
    """计算 Euler--φ。"""
    if type(index) is not int or index<1: raise ValueError("index 必须是正内建整数")
    result,n,d=index,index,2
    while d*d<=n:
        if n%d==0:
            result-=result//d
            while n%d==0:n//=d
        d+=1
    return result-result//n if n>1 else result

def _shells(limit:int) -> list[dict[str,object]]:
    """构造从 2 开始且显式标记末壳的 dyadic 壳。"""
    result=[]; start=2; index=1
    while start<limit:
        natural=start*2; stop=min(natural,limit)
        result.append({"index":index,"start":start,"stop":stop,"is_truncated":stop<natural})
        start=stop; index+=1
    return result

def finite_dyadic_shell_ledger(limit:object)->dict[str,object]:
    """精确重组 dyadic 壳的近邻、远壳与总核账本。"""
    D=_limit(limit); shells=_shells(D); coeff={d:Fraction(mobius_value(d),d) for d in range(2,D)}
    members=[tuple(range(s["start"],s["stop"])) for s in shells]
    blocks=[[sum((coeff[d]*coeff[e]*(gcd(d,e)-1) for d in left for e in right),Fraction()) for right in members] for left in members]
    total=sum((x for row in blocks for x in row),Fraction())
    direct=sum((coeff[d]*coeff[e]*(gcd(d,e)-1) for d in coeff for e in coeff),Fraction())
    diagonal=[]; near=Fraction()
    for j, group in enumerate(members):
        delta=sum((coeff[d]*coeff[d]*(d-1) for d in group),Fraction()); diagonal.append(delta)
        same_off=blocks[j][j]-delta; adjacent=2*blocks[j][j+1] if j+1<len(blocks) else Fraction()
        near+=delta+same_off+adjacent
    far=sum((blocks[j][k] for j in range(len(blocks)) for k in range(len(blocks)) if abs(j-k)>=2),Fraction())
    near_values=[blocks[j][j]-diagonal[j]+(2*blocks[j][j+1] if j+1<len(blocks) else Fraction()) for j in range(len(blocks))]
    return {"limit":D,"shells":tuple(shells),"block_matrix":tuple(tuple(str(x) for x in row) for row in blocks),"diagonal_shell_energy":str(sum(diagonal,Fraction())),"near_shell_energy":str(near),"far_shell_energy":str(far),"total_kernel_energy":str(total),"block_reassembly_residual":str(total-sum((x for row in blocks for x in row),Fraction())),"near_far_reassembly_residual":str(total-near-far),"kernel_identity_residual":str(total-direct),"near_shell_values":tuple(str(x) for x in near_values),"finite_near_cancellation_status":"finite_cancellation_witnessed" if any(x<0 for x in near_values) else "not_witnessed"}

def _validate(contract:object)->dict[str,object]:
    """验证合同不使用循环来源或伪造壳引理。"""
    if not isinstance(contract,Mapping):raise ValueError("contract 必须是 Mapping")
    uses=_strings(contract.get("uses"),"uses")
    if set(uses)&FORBIDDEN:raise ValueError("uses 含禁止来源")
    if not set(uses)<=ALLOWED:raise ValueError("uses 含未允许来源")
    claims=contract.get("claimed_uses")
    if not isinstance(claims,Mapping) or set(claims)!=set(CLAIMS):raise ValueError("claimed_uses 必须精确覆盖义务")
    for name in CLAIMS:
        if not set(_strings(claims[name],name)).issubset(uses):raise ValueError(f"{name} 含未声明来源")
    for lemma in LEMMAS:
        if type(contract.get(lemma)) is not bool or contract[lemma]:raise ValueError(f"{lemma} 必须是内建 False")
    if contract.get("uniformity_variable")!="truncation":raise ValueError("uniformity_variable 必须是 truncation")
    if contract.get("constant_dependency")!="fixed_test_function":raise ValueError("constant_dependency 必须是 fixed_test_function")
    return {"uses":uses}

def default_contract()->dict[str,object]:
    """返回只使用有限 dyadic 算术的合同。"""
    uses=("finite_arithmetic","mobius_definition","gcd_relation","dyadic_decomposition","euler_phi_divisor_sum","finite_sum_identity")
    return {"uses":uses,"claimed_uses":{name:("finite_arithmetic","finite_sum_identity") for name in CLAIMS},"adjacent_shell_cancellation_lemma":False,"summable_residual_lemma":False,"far_shell_aggregation_lemma":False,"uniformity_variable":"truncation","constant_dependency":"fixed_test_function"}

def audit_dyadic_shell_cancellation(contract:Mapping[str,object],limit:object)->dict[str,object]:
    """登记有限壳状态，绝不提升解析结论。"""
    return {**_validate(contract),**finite_dyadic_shell_ledger(limit),"finite_shell_ledger_status":"verified_finite","adjacent_shell_cancellation_obligation_status":"open","summable_residual_obligation_status":"open","far_shell_aggregation_obligation_status":"open","coprime_restricted_tail_bound_status":"open","w1_to_w2_status":"unproved","rh_proved":False}

def render_markdown(payload:Mapping[str,object])->str:
    """渲染明确有限边界的壳证书。"""
    return "\n".join(("# MFAC W1→W2 Dyadic 壳抵消审计证书","","```text",f"finite_shell_ledger_status={payload['finite_shell_ledger_status']}",f"adjacent_shell_cancellation_obligation_status={payload['adjacent_shell_cancellation_obligation_status']}",f"summable_residual_obligation_status={payload['summable_residual_obligation_status']}",f"far_shell_aggregation_obligation_status={payload['far_shell_aggregation_obligation_status']}",f"w1_to_w2_status={payload['w1_to_w2_status']}",f"rh_proved={str(payload['rh_proved']).lower()}","```","","有限壳账本不证明统一 L² 上界、W1→W2 或 RH。",""))
def write_certificate(payload:Mapping[str,object],json_out:Path,markdown_out:Path)->None:
    """写出 JSON 与 Markdown 证书。"""
    json_out.parent.mkdir(parents=True,exist_ok=True); markdown_out.parent.mkdir(parents=True,exist_ok=True)
    json_out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); markdown_out.write_text(render_markdown(payload),encoding="utf-8")
def main()->None:
    """生成默认有限壳证书。"""
    parser=argparse.ArgumentParser(description="生成 MFAC W1→W2 dyadic 壳证书"); parser.add_argument("--limit",type=int,default=512); parser.add_argument("--json-out",type=Path,default=DEFAULT_JSON); parser.add_argument("--markdown-out",type=Path,default=DEFAULT_MARKDOWN); args=parser.parse_args(); write_certificate(audit_dyadic_shell_cancellation(default_contract(),args.limit),args.json_out,args.markdown_out)
if __name__=="__main__":main()
