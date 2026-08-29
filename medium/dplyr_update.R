installed.packages("dplyr")
library(dplyr)

## Sample customer orders dataset
orders <- data.frame(
  order_id = 1:10,
  customer = c("Ana", "Ben", "Cara", "Dan", "Eve",
               "Fay", "Gil", "Han", "Ida", "Jon"),
  amount   = c(120, -999, 45, 0, 88, -999, 210, 33, NA, 75),
  region   = c("East", "West", "East", "South", "West",
               "East", "West", "South", "East", "West"),
  status   = c(1, 2, 3, 4, 5, 2, 3, 1, 4, 5),
  priority = c("high", "low", "med", "high", "med",
               "low", "high", "med", "low", "high")
)

clean_orders <- orders |>
  filter_out(amount == -999 | amount == 0)

clean_orders

## Drop rows where amount equals -999 OR order_id equals -999
orders |>
  filter_out(when_any(
    amount == -999,
    order_id == -999
  ))

## Keep rows where amount is positive AND order_id is positive
orders |>
  filter(when_all(
    amount > 0,
    order_id > 0
  ))


## Recode numeric status codes to readable labels
orders |>
  mutate(
    status_label = recode_values(
      status,
      1 ~ "Pending",
      2 ~ "Processing",
      3 ~ "Shipped",
      4 ~ "Delivered",
      5 ~ "Cancelled"
    )
  )


## Define a reusable lookup table
status_lookup <- data.frame(
  from = 1:5,
  to   = c("Pending", "Processing", "Shipped",
           "Delivered", "Cancelled")
)

## Apply across a single column
orders |>
  mutate(
    status_label = recode_values(
      status,
      from = status_lookup$from,
      to   = status_lookup$to
    )
  )

## Apply the same lookup across multiple columns using across()
priority_lookup <- data.frame(
  from = c("high", "med", "low"),
  to   = c("High Priority", "Medium Priority", "Low Priority")
)

orders |>
  mutate(across(
    priority,
    ~ recode_values(.x,
                    from = priority_lookup$from,
                    to   = priority_lookup$to)
  ))

## Standardize two region abbreviations in place
orders |>
  mutate(
    region = replace_values(
      region,
      "E" ~ "East",
      "W" ~ "West"
    )
  )

# Convert sentinel values and fill missing amounts
orders |>
  mutate(
    amount = amount |>
      replace_when(
        is.na(amount)  ~ 0,
        amount == -999 ~ NA_real_
      )
  )