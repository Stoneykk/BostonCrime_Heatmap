import pandas as pd

# Loading the datasets with the correct encoding (ISO-8859-1)
data_2019 = pd.read_csv('D:/BostonCrime_Heatmap/crime_data/2019.csv', encoding='ISO-8859-1')
data_2020 = pd.read_csv('D:/BostonCrime_Heatmap/crime_data/2020.csv', encoding='ISO-8859-1')
data_2021 = pd.read_csv('D:/BostonCrime_Heatmap/crime_data/2021.csv', encoding='ISO-8859-1')
data_2022 = pd.read_csv('D:/BostonCrime_Heatmap/crime_data/2022.csv', encoding='ISO-8859-1')
data_2023 = pd.read_csv('D:/BostonCrime_Heatmap/crime_data/2023.csv', encoding='ISO-8859-1')

# Checking the first few rows of each dataset to understand the structure, especially looking for latitude and longitude columns
data_2019.head(), data_2020.head(), data_2021.head(), data_2022.head(), data_2023.head()

import folium
from folium.plugins import HeatMap

# Function to generate a heatmap
def generate_heatmap(data, year):
    # Filter out invalid locations
    valid_data = data.dropna(subset=['Lat', 'Long'])
    valid_data = valid_data[(valid_data['Lat'] != 0) & (valid_data['Long'] != 0)]
    
    # Create a map centered around a general point
    base_map = folium.Map(location=[42.361145, -71.057083], zoom_start=11)
    
    # Add heatmap
    HeatMap(data=valid_data[['Lat', 'Long']], radius=10).add_to(base_map)
    
    return base_map

# Generate heatmaps for each year
heatmap_2019 = generate_heatmap(data_2019, 2019)
heatmap_2020 = generate_heatmap(data_2020, 2020)
heatmap_2021 = generate_heatmap(data_2021, 2021)
heatmap_2022 = generate_heatmap(data_2022, 2022)
heatmap_2023 = generate_heatmap(data_2023, 2023)
# Saving the maps as HTML files to visualize and then combine
heatmap_2019.save('D:/BostonCrime_Heatmap/heatmap_2019.html')
heatmap_2020.save('D:/BostonCrime_Heatmap/heatmap_2020.html')
heatmap_2021.save('D:/BostonCrime_Heatmap/heatmap_2021.html')
heatmap_2022.save('D:/BostonCrime_Heatmap/heatmap_2022.html')
heatmap_2023.save('D:/BostonCrime_Heatmap/heatmap_2023.html')

'/mnt/data/heatmap_2019.html', '/mnt/data/heatmap_2020.html', '/mnt/data/heatmap_2021.html', '/mnt/data/heatmap_2022.html'
# Creating a base map
base_map = folium.Map(location=[42.361145, -71.057083], zoom_start=11, control_scale=True)

# Function to generate a heatmap layer
def generate_heatmap_layer(data, year):
    # Filter out invalid locations
    valid_data = data.dropna(subset=['Lat', 'Long'])
    valid_data = valid_data[(valid_data['Lat'] != 0) & (valid_data['Long'] != 0)]
    
    # Creating a HeatMap layer
    heatmap_layer = HeatMap(data=valid_data[['Lat', 'Long']], radius=10, name=str(year), show=False)
    
    return heatmap_layer

# Generating heatmap layers for each year and adding to the base map
heatmap_layer_2019 = generate_heatmap_layer(data_2019, 2019)
heatmap_layer_2020 = generate_heatmap_layer(data_2020, 2020)
heatmap_layer_2021 = generate_heatmap_layer(data_2021, 2021)
heatmap_layer_2022 = generate_heatmap_layer(data_2022, 2022)
heatmap_layer_2023 = generate_heatmap_layer(data_2023, 2023)

heatmap_layer_2019.add_to(base_map)
heatmap_layer_2020.add_to(base_map)
heatmap_layer_2021.add_to(base_map)
heatmap_layer_2022.add_to(base_map)
heatmap_layer_2023.add_to(base_map)

# Adding layer control to switch between years
folium.LayerControl().add_to(base_map)

# Save the combined map to an HTML file
combined_heatmap_path = 'D:/BostonCrime_Heatmap/combined_heatmap.html'
base_map.save(combined_heatmap_path)

combined_heatmap_path
