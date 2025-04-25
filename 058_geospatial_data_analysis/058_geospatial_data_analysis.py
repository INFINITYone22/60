import geopandas as gpd
import matplotlib.pyplot as plt

def geospatial_data_analysis():
    # Load a shapefile (replace with your actual shapefile)
    shapefile_path = gpd.datasets.get_path('naturalearth_lowres')
    try:
        world = gpd.read_file(shapefile_path)
    except FileNotFoundError:
        print("Shapefile not found. Please download it and place it in the same directory as the script.")
        print("Alternatively, update the shapefile_path variable with the correct path.")
        return

    # Filter the data to only include countries in Africa
    africa = world[world['continent'] == 'Africa']

    # Plot the map of Africa
    plt.figure(figsize=(12, 8))
    africa.plot(color='white', edgecolor='black')
    plt.title("Map of Africa")
    plt.savefig("africa_map.png")
    print("Map of Africa saved to africa_map.png")

geospatial_data_analysis()
