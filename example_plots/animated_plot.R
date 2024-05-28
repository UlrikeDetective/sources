install.packages("gganimate")

library(ggplot2)
library(gganimate)

# Create a basic ggplot
p <- ggplot(mtcars, aes(x = wt, y = mpg, color = as.factor(gear))) + 
  geom_point() +
  labs(title = 'Gear: {closest_state}') +
  transition_states(gear, transition_length = 2, state_length = 1)

# Render animation
animate(p, renderer = gifski_renderer(loop = TRUE))
