# Learn R the easy way: Data manipulation in R

#end to end data wrangling program
#1. Create two small example datasets

df1 <- data.frame(
  id = 1:6,
  groupe = c("A", "A", "B", "B", "B", "A"),
  score = c(10, NA, 15, 20, NA, 18)
)

df2 <- data.frame(
  id = c(1, 2, 3, 7),
  bonus = c(2, 3, 1, 5)
) 

# 2. Fix missing values (impute with mean)
mean_score <- mean(df1$score, na.rm = TRUE)
df1$score[is.na(df1$score)] <- mean_score

# 3. Filter rows (keep only group B)
df_B <- df1[df1$group == "B", ]
# 4. Select rows & columns
df_small <- df1[df1$score > 12, c("id", "score")]
# 5. Sort and order
df_sorted <- df1[order(df1$score, decreasing = TRUE), ]
# 6. Create & transform variables
df1$scaled_score <-  (df1$score - mean (df1$score)) / sd(df1$score)
# 7. combine datasets (merge)
df_merged <- merge(df1, df2, by = "id", all.x = TRUE)
# 8. Summarise & aggregate data
summary_table <- aggregate(score ~groupe, data = df1, FUN = mean)

# 9. Reshape data (wide - long)
# Wide to long
long <- reshape(df1,
                varying = c("score", "scaled_score"),
                v.names = "value",
                timevar = "variable",
                times = c("score", "scaled_score"),
                direction = "long")
# long to wide
wide <- reshape(long,
                idvar = "id",
                timevar = "variable",
                direction = "wide")

# 10. print outputs
df1
df_B
df_small
df_sorted
df_merged
summary_table
long
wide