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
font_properties = FontProperties(family='DejaVu Sans', size=20)  # Adjust to a suitable font available on your system
# Available fonts:  ['.Aqua Kana', '.Keyboard', '.New York', '.New York', '.SF Arabic', '.SF Arabic Rounded', '.SF Armenian', '.SF Armenian Rounded', '.SF Camera', '.SF Compact', '.SF Compact', '.SF Compact Rounded', '.SF Georgian', '.SF Georgian Rounded', '.SF Hebrew', '.SF Hebrew Rounded', '.SF NS Mono', '.SF NS Mono', '.SF NS Rounded', '.SF Soft Numeric', '.ThonburiUI', 'Abolition', 'Academy Engraved LET', 'Al Bayan', 'Al Nile', 'Al Tarikh', 'Alegreya', 'Alegreya', 'Alegreya', 'American Typewriter', 'Andale Mono', 'Apple Braille', 'Apple Braille', 'Apple Braille', 'Apple Braille', 'Apple Braille', 'Apple Chancery', 'Apple SD Gothic Neo', 'Apple Symbols', 'AppleGothic', 'AppleMyungjo', 'Arial', 'Arial', 'Arial', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial Narrow', 'Arial Narrow', 'Arial Narrow', 'Arial Narrow', 'Arial Rounded MT Bold', 'Arial Unicode MS', 'Arial Unicode MS', 'Athelas', 'Avenir', 'Avenir Next', 'Avenir Next Condensed', 'Ayuthaya', 'Baghdad', 'Bangla MN', 'Bangla Sangam MN', 'Baskerville', 'Beirut', 'Big Caslon', 'Bodoni 72', 'Bodoni 72 Oldstyle', 'Bodoni 72 Smallcaps', 'Bodoni Ornaments', 'Bradley Hand', 'Brush Script MT', 'Calibri', 'Capitana', 'Capitana', 'Chalkboard', 'Chalkboard SE', 'Chalkduster', 'Charter', 'Classico URW', 'Cochin', 'Comic Sans MS', 'Comic Sans MS', 'Copperplate', 'Corsiva Hebrew', 'Courier', 'Courier New', 'Courier New', 'Courier New', 'Courier New', 'DIN Alternate', 'DIN Condensed', 'Damascus', 'DecoType Naskh', 'DejaVu Sans', 'DejaVu Sans', 'DejaVu Sans', 'DejaVu Sans', 'DejaVu Sans Display', 'DejaVu Sans Mono', 'DejaVu Sans Mono', 'DejaVu Sans Mono', 'DejaVu Sans Mono', 'DejaVu Serif', 'DejaVu Serif', 'DejaVu Serif', 'DejaVu Serif', 'DejaVu Serif Display', 'Devanagari MT', 'Devanagari Sangam MN', 'Didot', 'Diwan Kufi', 'Diwan Thuluth', 'Economica', 'Euphemia UCAS', 'Farah', 'Farisi', 'Futura', 'Galvji', 'Geeza Pro', 'Geneva', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Gill Sans', 'Gujarati MT', 'Gujarati Sangam MN', 'Gurmukhi MN', 'Gurmukhi MT', 'Gurmukhi Sangam MN', 'Hack', 'Heiti TC', 'Heiti TC', 'Helvetica', 'Helvetica Neue', 'Herculanum', 'Hiragino Maru Gothic Pro', 'Hiragino Mincho ProN', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans', 'Hiragino Sans GB', 'Hoefler Text', 'Hoefler Text', 'ITF Devanagari', 'Impact', 'InaiMathi', 'Iowan Old Style', 'Kailasa', 'Kannada MN', 'Kannada Sangam MN', 'Kefa', 'Khmer MN', 'Khmer Sangam MN', 'Kohinoor Bangla', 'Kohinoor Devanagari', 'Kohinoor Gujarati', 'Kohinoor Telugu', 'Kokonor', 'Krungthep', 'KufiStandardGK', 'LTC Broadway', 'Lao MN', 'Lao Sangam MN', 'LoRes 9 OT', 'Lucida Grande', 'Luminari', 'Malayalam MN', 'Malayalam Sangam MN', 'Marion', 'Marker Felt', 'Menlo', 'MesloLGS NF', 'MesloLGS NF', 'MesloLGS NF', 'MesloLGS NF', 'Microsoft Sans Serif', 'MinervaModern', 'Mishafi', 'Mishafi Gold', 'Monaco', 'Mshtakan', 'Mukta Mahee', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 'Nadeem', 'New Peninim MT', 'Noteworthy', 'Noto Nastaliq Urdu', 'Noto Sans', 'Noto Sans Adlam', 'Noto Sans Armenian', 'Noto Sans Avestan', 'Noto Sans Bamum', 'Noto Sans Bassa Vah', 'Noto Sans Batak', 'Noto Sans Bhaiksuki', 'Noto Sans Brahmi', 'Noto Sans Buginese', 'Noto Sans Buhid', 'Noto Sans Canadian Aboriginal', 'Noto Sans Carian', 'Noto Sans Caucasian Albanian', 'Noto Sans Chakma', 'Noto Sans Cham', 'Noto Sans Coptic', 'Noto Sans Cuneiform', 'Noto Sans Cypriot', 'Noto Sans Duployan', 'Noto Sans Egyptian Hieroglyphs', 'Noto Sans Elbasan', 'Noto Sans Glagolitic', 'Noto Sans Gothic', 'Noto Sans Gunjala Gondi', 'Noto Sans Hanifi Rohingya', 'Noto Sans Hanunoo', 'Noto Sans Hatran', 'Noto Sans Imperial Aramaic', 'Noto Sans Inscriptional Pahlavi', 'Noto Sans Inscriptional Parthian', 'Noto Sans Javanese', 'Noto Sans Kaithi', 'Noto Sans Kannada', 'Noto Sans Kayah Li', 'Noto Sans Kharoshthi', 'Noto Sans Khojki', 'Noto Sans Khudawadi', 'Noto Sans Lepcha', 'Noto Sans Limbu', 'Noto Sans Linear A', 'Noto Sans Linear B', 'Noto Sans Lisu', 'Noto Sans Lycian', 'Noto Sans Lydian', 'Noto Sans Mahajani', 'Noto Sans Mandaic', 'Noto Sans Manichaean', 'Noto Sans Marchen', 'Noto Sans Masaram Gondi', 'Noto Sans Meetei Mayek', 'Noto Sans Mende Kikakui', 'Noto Sans Meroitic', 'Noto Sans Miao', 'Noto Sans Modi', 'Noto Sans Mongolian', 'Noto Sans Mro', 'Noto Sans Multani', 'Noto Sans Myanmar', 'Noto Sans NKo', 'Noto Sans Nabataean', 'Noto Sans New Tai Lue', 'Noto Sans Newa', 'Noto Sans Ol Chiki', 'Noto Sans Old Hungarian', 'Noto Sans Old Italic', 'Noto Sans Old North Arabian', 'Noto Sans Old Permic', 'Noto Sans Old Persian', 'Noto Sans Old South Arabian', 'Noto Sans Old Turkic', 'Noto Sans Oriya', 'Noto Sans Osage', 'Noto Sans Osmanya', 'Noto Sans Pahawh Hmong', 'Noto Sans Palmyrene', 'Noto Sans Pau Cin Hau', 'Noto Sans PhagsPa', 'Noto Sans Phoenician', 'Noto Sans Psalter Pahlavi', 'Noto Sans Rejang', 'Noto Sans Samaritan', 'Noto Sans Saurashtra', 'Noto Sans Sharada', 'Noto Sans Siddham', 'Noto Sans Sora Sompeng', 'Noto Sans Sundanese', 'Noto Sans Syloti Nagri', 'Noto Sans Syriac', 'Noto Sans Tagalog', 'Noto Sans Tagbanwa', 'Noto Sans Tai Le', 'Noto Sans Tai Tham', 'Noto Sans Tai Viet', 'Noto Sans Takri', 'Noto Sans Thaana', 'Noto Sans Tifinagh', 'Noto Sans Tirhuta', 'Noto Sans Ugaritic', 'Noto Sans Vai', 'Noto Sans Wancho', 'Noto Sans Warang Citi', 'Noto Sans Yi', 'Noto Serif Ahom', 'Noto Serif Balinese', 'Noto Serif Hmong Nyiakeng', 'Noto Serif Myanmar', 'Noto Serif Yezidi', 'Optima', 'Oriya MN', 'Oriya Sangam MN', 'PT Mono', 'PT Sans', 'PT Serif', 'PT Serif Caption', 'Palatino', 'Papyrus', 'Party LET', 'Phosphate', 'PingFang HK', 'Plantagenet Cherokee', 'Playfair Display', 'Poppins', 'Raanana', 'Roboto', 'Rockwell', 'Rounded M+ 1m', 'STIX Two Math', 'STIX Two Text', 'STIX Two Text', 'STIXGeneral', 'STIXGeneral', 'STIXGeneral', 'STIXGeneral', 'STIXGeneral', 'STIXGeneral', 'STIXGeneral', 'STIXGeneral', 'STIXIntegralsD', 'STIXIntegralsD', 'STIXIntegralsSm', 'STIXIntegralsSm', 'STIXIntegralsUp', 'STIXIntegralsUp', 'STIXIntegralsUpD', 'STIXIntegralsUpD', 'STIXIntegralsUpSm', 'STIXIntegralsUpSm', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXNonUnicode', 'STIXSizeFiveSym', 'STIXSizeFiveSym', 'STIXSizeFourSym', 'STIXSizeFourSym', 'STIXSizeFourSym', 'STIXSizeFourSym', 'STIXSizeOneSym', 'STIXSizeOneSym', 'STIXSizeOneSym', 'STIXSizeOneSym', 'STIXSizeThreeSym', 'STIXSizeThreeSym', 'STIXSizeThreeSym', 'STIXSizeThreeSym', 'STIXSizeTwoSym', 'STIXSizeTwoSym', 'STIXSizeTwoSym', 'STIXSizeTwoSym', 'STIXVariants', 'STIXVariants', 'Sana', 'Sarina', 'Sathu', 'Savoye LET', 'Seravek', 'Shree Devanagari 714', 'SignPainter', 'Signo', 'Silom', 'Sinhala MN', 'Sinhala Sangam MN', 'Skia', 'Smoothy', 'Snell Roundhand', 'Sniglet', 'Songti SC', 'Source Code Pro', 'Source Code Pro', 'Source Code Pro', 'Source Code Pro', 'Source Code Pro', 'Source Code Pro', 'Source Code Pro', 'Source Serif 4', 'Sukhumvit Set', 'Superclarendon', 'Symbol', 'System Font', 'System Font', 'Tahoma', 'Tahoma', 'Tamil MN', 'Tamil Sangam MN', 'Telugu MN', 'Telugu Sangam MN', 'Thonburi', 'Times', 'Times New Roman', 'Times New Roman', 'Times New Roman', 'Times New Roman', 'Trattatello', 'Trebuchet MS', 'Trebuchet MS', 'Trebuchet MS', 'Trebuchet MS', 'Verdana', 'Verdana', 'Verdana', 'Verdana', 'Vortice', 'Waseem', 'Webdings', 'Wingdings', 'Wingdings 2', 'Wingdings 3', 'Yanone Kaffeesatz', 'Zapf Dingbats', 'Zapfino', 'cmb10', 'cmex10', 'cmmi10', 'cmr10', 'cmss10', 'cmsy10', 'cmtt10']

for i, place_name in enumerate(places):
    # Download the street network data
    graph = ox.graph_from_place(place_name, network_type='drive')

    # Select a color pair (cycling through the list)
    background_color, edge_color = color_palette_actual[i % len(color_palette_actual)]

    # Plot the street network
    fig, ax = ox.plot_graph(graph, node_size=0, edge_color=edge_color, edge_linewidth=1.5, bgcolor=background_color, show=False, close=False)

    # Add the city and country name inside the visualization on the background color
    ax.text(0.5, 0.95, place_name, transform=ax.transAxes, fontsize=20, fontproperties=font_properties, color=edge_color, ha='center', va='top')

    # Save the plot to a file
    filename = f'urban_network_{place_name.replace(", ", "_").replace(" ", "_")}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
