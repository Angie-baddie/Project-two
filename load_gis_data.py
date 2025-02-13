import geopandas as gpd
import matplotlib.pyplot as plt

# Load shapefiles
districts_shp = "DATA/SHAPEFILES/Uganda_Districts.shp"
subcounties_shp = "DATA/SHAPEFILES/Uganda_Subcounties.shp"
maize_shp = "DATA/SHAPEFILES/Crop_Type_Map_Maize.shp"
sorghum_shp = "DATA/SHAPEFILES/Crop_Type_Map_Sorghum.shp"

# Read the shapefiles into GeoDataFrames
uganda_districts = gpd.read_file(districts_shp)
uganda_subcounties = gpd.read_file(subcounties_shp)
maize_map = gpd.read_file(maize_shp)
sorghum_map = gpd.read_file(sorghum_shp)

# Display the first few rows
print("Uganda Districts Data:\n", uganda_districts.head())
print("\nUganda Subcounties Data:\n", uganda_subcounties.head())
print("\nMaize Crop Data:\n", maize_map.head())

# Plot districts and subcounties
fig, ax = plt.subplots(figsize=(10, 8))
uganda_districts.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.5)
uganda_subcounties.plot(ax=ax, color='none', edgecolor='blue', linewidth=0.5)
plt.title("Uganda Districts and Subcounties")
plt.show()
