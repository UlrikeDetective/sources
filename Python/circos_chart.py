from pycirclize import Circos

# Initialize circos sectors
sectors = {"A": 1, "B": 2, "C": 3, "D": 4}
circos = Circos(sectors, space=5)

# Loop the sectors and generate the graph
for sector in circos.sectors:
    sector.axis(lw=2)
    sector.text(f"Sector: {sector.name}={sector.size}", size=15)

# Plot it
fig = circos.plotfig()
