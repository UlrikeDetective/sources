install.packages("broadcast")

library(broadcast)
x <- array(1:10, c(10, 1))
y <- array(1:10, c(1, 10))
broadcaster(x) <- TRUE
broadcaster(y) <- TRUE
result <- x / (y + 2) 

########### Retail Example using broadcaster function

months <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# Seasonal multipliers (holiday season boost in Nov/Dec)
seasonal <- c(0.85, 0.80, 0.90, 0.95, 1.00, 1.05, 
              1.10, 1.08, 1.00, 0.95, 1.20, 1.35)

# Store base performance levels (different store sizes/markets)
store_bases <- c(120, 95, 110,      # West region stores
                 150, 145, 130, 125, # Central region stores (higher performers)
                 100, 105, 90)       # East region stores

# Generate sales data with seasonal variation and random noise
sales_data <- matrix(nrow = 10, ncol = 12)
for(i in 1:10) {
  for(j in 1:12) {
    sales_data[i, j] <- store_bases[i] * seasonal[j] * 
      rnorm(1, mean = 1, sd = 0.1)
  }
}
sales_data
# Convert to array with proper dimensions
stores <- array(sales_data, dim = c(10, 12))
dimnames(stores) <- list(
  Store = paste0("Store_", 1:10),
  Month = months
)
stores  

regional_targets_data <- rbind(
  West = c(100, 95, 105, 110, 115, 120, 125, 123, 115, 110, 135, 150),
  Central = c(130, 125, 135, 140, 145, 150, 155, 153, 145, 140, 165, 180),
  East = c(95, 90, 100, 105, 110, 115, 120, 118, 110, 105, 130, 145)
)

# Expand to match store structure (stores in rows, months in columns)
regional <- array(dim = c(10, 12))
regional[1:3, ] <- matrix(rep(regional_targets_data[1,], each = 3), 
                          nrow = 3, byrow = FALSE)
regional[4:7, ] <- matrix(rep(regional_targets_data[2,], each = 4), 
                          nrow = 4, byrow = FALSE)
regional[8:10, ] <- matrix(rep(regional_targets_data[3,], each = 3), 
                           nrow = 3, byrow = FALSE)

dimnames(regional) <- list(
  Store = paste0("Store_", 1:10),
  Month = months
)  
regional

# National monthly targets (single value per month)
national <- c(110, 105, 115, 120, 125, 130, 135, 133, 125, 120, 145, 160)
names(national) <- months
national

broadcaster(stores) <- TRUE
broadcaster(regional) <- TRUE
broadcaster(national) <- TRUE

variance_from_regional <- (stores - regional) / regional

national_array <- array(national, dim = c(1, 12))
broadcaster(national_array) <- TRUE
variance_from_national <- ((stores - national_array) / national_array) * 100

cat("\n=== VARIANCE FROM REGIONAL TARGETS (%) ===\n")
print(round(variance_from_regional, 1))

cat("\n=== VARIANCE FROM NATIONAL TARGETS (%) ===\n")
print(round(variance_from_national, 1))


#
# SUMMARY INSIGHTS
#  
# Stores consistently beating regional targets
regional_performers <- rowMeans(variance_from_regional)
#Average Regional Performance by Store
print(round(sort(regional_performers, decreasing = TRUE), 1))

# Best performing months overall
monthly_performance <- colMeans(variance_from_national)
# Average National Performance by Month
print(round(monthly_performance, 1))