# 1. Install the package (only do this once)
install.packages("chattr")

# 2. Load the library (do this EVERY time you open RStudio)
library(chattr)
remotes::install_github("mlverse/chattr")
# Specify the exact model name from your 'ollama list'
my_chat <- ellmer::chat_ollama(model = "llama3.2")
chattr_use(my_chat)

#Submit a prompt directly
chattr("Create a ggplot visualizing the relationship between mpg and horsepower in mtcars", stream =T)
library(ggplot2)
library(readr)

# Load tidyverse packages
tidyverse::readr # read CSV from file or dataframe 

mtcars %>% read_csv() 

ggplot(mtcars, aes(x = hp, y = mpg)) + 
  geom_point() + geom_smooth(method="loess")

chattr_defaults()
chattr_defaults(max_data_frames = 5, max_data_files = 5)
chattr_defaults_save()

## new project

getwd()

library(chattr)
library(dplyr)

# Load your data
sales_data <- read.csv("sales_data.csv")

# Quick structure check
str(sales_data)

#Set the model before launching
my_chat <- ellmer::chat_ollama(model = "llama3.2")
chattr_use(my_chat)

# Verify the connection is live
chattr_test()

chattr("Suggest five exploratory visualizations for this sales dataset sales_data", stream = T)
```r
library(ggplot2)
library(tidyr)

sales_data %>%
  select(region, product, sales) %>%
  group_by(region, product) %>%
  summarise(avg_sales = mean(sales))
```
This would give the average sales per region and product. 

# Exploratory visualizations

1. Bar plot: avg_sales vs product
2. Boxplot: sales by region
3. Heatmap: correlation between variables
4. Scatterplot: sales vs price
5. Violinplot: sales distribution for each product
