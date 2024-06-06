#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 5,2024



import folium
import pandas as pd

inputfile = input("Enter CSV file name: ")
output = input("Enter output file: ")

collisions = pd.read_csv(inputfile)
collisionMap = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
for _, row in collisions.iterrows():
    folium.Marker(location=[row['LATITUDE'], row['LONGITUDE']]).add_to(collisionMap)


collisionMap.save(output)

