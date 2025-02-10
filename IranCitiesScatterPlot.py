import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

cities = ['Tehran', 'Esfahan', 'Mashhad', 'Tabriz', 'Shiraz', 'Kerman']
x = [51.2323, 51.4013, 59.3236, 46.1757, 52.3233, 57.4]
y = [35.4120, 32.3955, 36.1935, 38.0454, 29.3636, 30.17]
population = [9800000, 2220000, 3400000, 1700000, 1565572, 3164719]

# Scale population for better visualization
scaled_population = [i / 1000 for i in population]

plt.figure(figsize=(10, 10))
map_ax = plt.axes(projection=ccrs.Mercator())
map_ax.set_extent([44, 63, 25, 40], crs=ccrs.PlateCarree())

map_ax.add_feature(cfeature.COASTLINE)
map_ax.add_feature(cfeature.BORDERS)
map_ax.add_feature(cfeature.LAND, edgecolor='black')
map_ax.add_feature(cfeature.OCEAN)

# Plot the scatter points
plt.scatter(x, y, s=scaled_population, alpha=0.5, color='#00FFFF', transform=ccrs.PlateCarree())

# Define font properties
font_properties = {'family': 'Times New Roman', 'size': 14, 'color': 'darkblue', 'weight': 'bold'}

# Annotate the cities with the new font
for i, city in enumerate(cities):
    plt.text(x[i], y[i], city, fontdict=font_properties, transform=ccrs.PlateCarree())

plt.title('Scatter plot of cities on Iran map')
plt.show()