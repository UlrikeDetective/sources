data("AirPassengers")
str(AirPassengers)

plot(AirPassengers, col="#f47c20")
AirPassengers

library(ggplot2)
library(dplyr)


# line chart
# 1. Convert the AirPassengers time-series to a Data Frame
# We create a sequence of months and extract the numeric passenger counts
df_passengers <- data.frame(
  Month = factor(month.abb, levels = month.abb), # Jan, Feb, Mar...
  Year = as.numeric(floor(time(AirPassengers))),
  Passengers = as.numeric(AirPassengers)
)

# 2. Filter for the specific years you requested
plot_data <- df_passengers %>%
  filter(Year %in% c(1949, 1955, 1960)) %>%
  mutate(Year = as.factor(Year)) # Convert to factor for distinct colors

# 3. Create the line chart
ggplot(plot_data, aes(x = Month, y = Passengers, color = Year, group = Year)) +
  geom_line(linewidth = 1) +
  geom_point() +
  scale_color_manual(values = c("1949" = "steelblue", 
                                "1955" = "darkorange", 
                                "1960" = "firebrick")) +
  labs(
    title = "Air Passengers Comparison: 1949, 1955, and 1960",
    x = "Month",
    y = "Total Passengers (Thousands)",
    color = "Year"
  ) +
  theme_minimal()

# convert to data frame with Year and month
df <- data.frame(
  Year = floor(time(AirPassengers)),
  Month = cycle(AirPassengers),
  Passengers = as.numeric(AirPassengers)
)
head(df)

library(ggplot2)

# boxplot
library(ggplot2)

# 1. Convert time series to data frame
df_all <- data.frame(
  Year = as.factor(floor(time(AirPassengers))),
  Passengers = as.numeric(AirPassengers)
)

# 2. Create the box plot with your specific hex color
ggplot(df_all, aes(x = Year, y = Passengers)) +
  geom_boxplot(fill = "#a9d6e5", color = "black") + # 'fill' is now global
  labs(
    title = "Annual Distribution of Air Passengers (1949-1960)",
    x = "Year",
    y = "Passengers (Thousands)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Box plot per Month in the dataset
library(ggplot2)

# 1. Convert the AirPassengers time-series to a Data Frame
df_months <- data.frame(
  # Extract month names (Jan, Feb, etc.) and keep them in order
  Month = factor(month.abb, levels = month.abb), 
  Passengers = as.numeric(AirPassengers)
)

# 2. Create the box plot by Month
ggplot(df_months, aes(x = Month, y = Passengers)) +
  geom_boxplot(fill = "#6e7f3f", color = "black") +
  labs(
    title = "Monthly Passenger Distribution (1949-1960)",
    subtitle = "Aggregated data across all 12 years",
    x = "Month",
    y = "Passengers (Thousands)"
  ) +
  theme_minimal()
