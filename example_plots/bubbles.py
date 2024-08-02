import matplotlib as plt

#ADD YOUR DATA HERE
browser_market_share = {
    'browsers': ['firefox', 'chrome', 'safari', 'edge', 'ie', 'opera'],
    'market_share': [8.61, 69.55, 8.36, 4.12, 2.76, 2.43],
    'color': ['#5A69AF', '#579E65', '#F9C784', '#FC944A', '#F24C00', '#00B825']
}
#STEP 3
bubble_chart = BubbleChart(area=browser_market_share['market_share'],
                           bubble_spacing=0.1)
#STEP 4
bubble_chart.collapse()

#STEP 5

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
bubble_chart.plot(
    ax, browser_market_share['browsers'], browser_market_share['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title('Browser market share')

plt.show()

# customization 1

bubble_chart = BubbleChart(area=browser_market_share['market_share'],
                           bubble_spacing=2)

# horizontel line

 def __init__(self, area, bubble_spacing=0):
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area

        # UPDATE: Position the bubbles in a horizontal row, touching each other
        self.bubbles[:, 0] = np.cumsum(r * 2 + self.bubble_spacing) - r - self.bubble_spacing / 2
        self.bubbles[:, 1] = 0  
