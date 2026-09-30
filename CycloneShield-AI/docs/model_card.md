# Model Card

## Current model

CycloneShield AI currently uses a transparent weighted heuristic for regional exposure prioritization. It combines demonstration wind, coastal exposure, population exposure, rainfall exposure, and elevation inputs.

## Why no trained model is claimed

The package does not ship a validated historical training dataset with independent time-based evaluation. Therefore MAE, RMSE, calibration, and operational forecast accuracy are intentionally reported as `N/A`.

## Safety boundary

The score describes prototype exposure prioritization. It is not predicted physical damage, an evacuation order, or a guarantee of safety. A future model must use time-split validation, baseline comparison, uncertainty output, and an explicit model/data card before operational use.
