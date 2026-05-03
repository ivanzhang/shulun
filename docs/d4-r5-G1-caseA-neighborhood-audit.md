# D4/R5 G1 Case A 邻域复核审计

**状态：** `top20_tail_route_refuted_locally_but_Neff64_survives`

密邻域复核显示：固定 top20_56/tail44 路线不是局部稳定的，top20 Cauchy bound 可达约 67.39；但原始 Neff<=64 仍稳定，邻域最大 Neff≈47.78。因此应放弃固定 top-r 半质量闭合，回到直接二阶能量 Neff 证明。

## 最坏记录
- Neff 最坏：{'x': 1023427, 'count': 95, 'total': 0.13741097199809407, 'l2_sqrt': 0.019878973066740763, 'neff': 47.780966769787746, 'ratio': 6.912377794202784, 'top20_share': 0.555234863781443, 'top20_cauchy_bound': 64.87487580337218, 'tail20_over_head20': 0.8010396414761697, 'far_over_head20': 0.4198590085697809}
- top20 Cauchy bound 最坏：{'x': 1023415, 'count': 94, 'total': 0.1426116155294303, 'l2_sqrt': 0.020652177915348728, 'neff': 47.68459339858085, 'ratio': 6.905403203186679, 'top20_share': 0.5447693391058611, 'top20_cauchy_bound': 67.3914316756959, 'tail20_over_head20': 0.8356392847683324, 'far_over_head20': 0.4074405355279125}
- top20 bound violations：`13`
- Neff64 violations：`0`

## 下一路线
- 直接证明 S^2<=64Q，而不是通过固定 top20 头部质量
- 利用 Case A 邻域中 Neff 最大约 47.78 的余量，寻找二阶能量下界机制
- 保留 top-r 证书作为启发，但不作为正式闭合接口
