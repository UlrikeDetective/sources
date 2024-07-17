import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import networkx as nx

# List of places (cities) you want to visualize
places = [
    "Manhattan, New York, USA",
    "Los Angeles, California, USA",
    "Chicago, Illinois, USA",
    "San Francisco, California, USA",
    "Boston, Massachusetts, USA",
    "Seattle, Washington, USA",
    "Washington, D.C., USA",
    "Philadelphia, Pennsylvania, USA",
    "Miami, Florida, USA",
    "Atlanta, Georgia, USA",
    "Denver, Colorado, USA",
    "Houston, Texas, USA"
]

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

# Set the font properties
font_properties = FontProperties(fname='/usr/share/fonts/truetype/nanum/NanumGothic.ttf', size=15)  # Adjust path and size as necessary

for i, place_name in enumerate(places):
    # Download the street network data
    graph = ox.graph_from_place(place_name, network_type='drive')

    # Select a color pair (cycling through the list)
    background_color, edge_color = color_palette_actual[i % len(color_palette_actual)]

    # Plot the street network
    fig, ax = ox.plot_graph(graph, node_size=0, edge_color=edge_color, edge_linewidth=1.5, bgcolor=background_color, show=False, close=False)

    # Add the city and country name at the top of the visualization
    ax.text(0.5, 1.05, place_name, transform=ax.transAxes, fontsize=20, fontproperties=font_properties, ha='center', va='center')

    # Save the plot to a file
    filename = f'urban_network_{place_name.replace(", ", "_").replace(" ", "_")}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
