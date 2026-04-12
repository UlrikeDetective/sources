install.packages("coretForecast")
library(caretForecast)
library(forecast)

## Convert monthly_data to a ts object
revenue_ts <- ts(
  c(
    45000, 42000, 48000, 51000, 53000, 55000,
    58000, 56000, 60000, 63000, 67000, 89000,
    47000, 44000, 50000, 54000, 57000, 59000,
    61000, 59000, 63000, 67000, 71000, 95000,
    49000, 46000, 52000, 57000, 60000, 62000,
    65000, 63000, 67000, 70000, 74000, 101000
  ),
  start     = c(2021, 1),
  frequency = 12
)

## Split into training and test using split_ts
dtlist       <- caretForecast::split_ts(revenue_ts, test_size = 6)
train_data   <- dtlist$train
test_data    <- dtlist$test

## Fit the ARml model with ranger
fit <- ARml(
  train_data,
  max_lag       = 12,
  caret_method  = "ranger",
  verbose       = FALSE
)

## Generate forecasts with prediction intervals
fc <- forecast(fit, h = length(test_data), level = c(80, 95))
fc

## Evaluate accuracy
accuracy(fc, test_data)

## Visualize
autoplot(fc) +
  autolayer(test_data, series = "Actual") +
  labs(
    title    = "Revenue Forecast vs. Actual: H2 2023",
    subtitle = "caretForecast ARml model using ranger engine",
    y        = "Revenue ($)"
  ) +
  theme_minimal(base_size = 13)

## Review algorithms recommended for ARml workflows
suggested_methods()