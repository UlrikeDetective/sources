""" Now, let’s have a look at how to create a practical Circos chart using this library.
I will simulate a real-world problem.

Suppose we have a traffic dataset for an intersection. We want to visualise how many 
vehicles have entered this intersection from each direction.

First of all, we need to import the Circos graph type from the PyCirclize library. 
Then, let’s import Numpy as well to generate some dummy data. """

# Next, let’s create the four directions and the x-axis representing 24 hours in a day.

# Sectors represent different directions of the intersection,
# with the x-axis representing 24 hours of the day

# Then, in the loop of each sector for sector in circos.sectors, we need to simulate the x (24 hours) and y (number of vehicles).

### Please be advised that the code below needs to run in the sectors for-loop

"""As the first step, let’s add a bar chart as follows. The tuple (10, 50) means 
that we want the circle to start at the 10th pixel away from the centre, and stop at 
the 50th. In this ring-shaped area, the bar chart will be rendered."""

from pycirclize import Circos
import numpy as np
import matplotlib.pyplot as plt

# Define the sectors and initialize Circos
circos = Circos()
sector_labels = ["North", "East", "South", "West"]

# Add sectors to Circos
for label in sector_labels:
    circos.add_sector(label, 24)

# Iterate over each sector to add tracks and simulate data
for sector in circos.sectors:
    # Simulate x (24 hours) and y (number of vehicles)
    x = np.linspace(0, 24, 24)
    y = np.random.randint(10, 1000, 24)  # Simulated hourly vehicle numbers
    
    # Add a bar track to the current sector
    track = sector.add_track(radii=(0.7, 0.9))  # Adjusted radii for better visualization
    track.bar(x, y)

# Render and save the Circos plot
fig = circos.plotfig()
fig.savefig("circos_diagram.png")
plt.show()
