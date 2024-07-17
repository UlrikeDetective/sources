import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx

# Specify the place
place_name = "Manhattan, New York, USA"

# Download the street network data
graph = ox.graph_from_place(place_name, network_type='drive') # walk

# Define color palette pairs
color_palette_actual = [
    ('#D2042D', '#FFF5EE'),  # CherryRed and OffWhite
    ('#FF7F50', '#FFFF00'),  # Coral and Yellow
    ('#FFC1CC', '#D2042D')   # BubblegumPink and CherryRed
]

# Extend with additional colors if necessary
additional_colors = [
    ('#0000FF', '#ADD8E6'),  # Blue and LightBlue
    ('#008000', '#00FF00'),  # Green and Lime
    ('#FFA500', '#FFD700'),  # Orange and Gold
    ('#800080', '#EE82EE'),  # Purple and Violet
    ('#A52A2A', '#FFDEAD'),  # Brown and NavajoWhite
    ('#000000', '#808080'),  # Black and Gray
    ('#FF1493', '#FFB6C1'),  # DeepPink and LightPink
    ('#4B0082', '#8A2BE2'),  # Indigo and BlueViolet
    ('#5F9EA0', '#E0FFFF')   # CadetBlue and LightCyan
]

# Combine the colors to make 12 pairs
color_palette_actual.extend(additional_colors[:9])

# Select a color pair (e.g., the first pair in the list)
background_color, edge_color = color_palette_actual[0]

# Plot the street network
fig, ax = ox.plot_graph(graph, node_size=0, edge_color=edge_color, edge_linewidth=1.5, bgcolor=background_color)

# Save the plot to a file
plt.savefig('urban_network.png', dpi=300, bbox_inches='tight')
plt.show()
