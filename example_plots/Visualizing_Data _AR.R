# Visualizing Data in AR (Augmented reality)

install.packages("ari")
install.packages("rgl")

library(ari)
library(rgl)

library(ari)
ls("package:ari")

# Create a 3D plot
plot3d(mtcars$wt, mtcars$mpg, mtcars$hp, col = mtcars$cyl)

# Save the plot as a WebGL file (which can be viewed in a web browser)
rglwidget()
