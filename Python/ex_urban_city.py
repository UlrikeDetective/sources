import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
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

# Check available fonts
available_fonts = sorted([f.name for f in fontManager.ttflist])
print("Available fonts: ", available_fonts)

# Set the font properties (use a different font if Nanum Gothic is not available)
font_properties_city = FontProperties(family='.aqua kana', size=30)  # Font for city name
font_properties_country = FontProperties(family='.aqua kana', size=20)  # Font for country name

for i, place_name in enumerate(places):
    # Split the place name into city and country
    city, state, country = place_name.split(', ')
    title_text = f"{city}\n{country}"

    # Download the street network data
    graph = ox.graph_from_place(place_name, network_type='drive')

    # Select a color pair (cycling through the list)
    background_color, edge_color = color_palette_actual[i % len(color_palette_actual)]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.subplots_adjust(top=0.92)  # Adjust to create space at the top

    # Plot the street network on the axis with the background color
    ax.set_facecolor(background_color)
    ox.plot_graph(graph, ax=ax, node_size=0, edge_color=edge_color, edge_linewidth=1.5, show=False, close=False)

    # Add the city and country name above the visualization
    fig.suptitle(city, fontsize=30, fontproperties=font_properties_city, color=background_color, ha='center', y=1.02)
    fig.text(0.5, 0.94, country, fontsize=20, fontproperties=font_properties_country, color=background_color, ha='center')

    # Save the plot to a file
    filename = f'urban_network_{place_name.replace(", ", "_").replace(" ", "_")}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
