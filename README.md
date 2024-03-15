# Store-Sales---Time-Series-Forecasting
## Goal of the Competition
In this “getting started” competition, you’ll use time-series forecasting to forecast store sales on data from Corporación Favorita, a large Ecuadorian-based grocery retailer.\
\
For more information, please visit Kaggle : https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview

## Evaluation
![image](https://github.com/suusuu00/Store-Sales---Time-Series-Forecasting/assets/124228791/410e9ba5-6238-407e-807c-b149319b557d)
\
`models/linear_model5.pt` is best model.
- val RMSLE : 0.238221
- submit한 RMSLE : 0.82765

## Caution
Please use `np.expm1()` because of predicting the y value as the log value.
