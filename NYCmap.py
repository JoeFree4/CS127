#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 3,2024


import folium

def create_nyc_map():
   
    nycmap = folium.Map(location=[40.75, -74.125], zoom_start=10)

   #adds hunter college marker
    marker = folium.Marker(location=[40.768731, -73.964915], popup="Hunter College")
    marker.add_to(nycmap)

    
    nycmap.save("nycMap.html")

def main():
    create_nyc_map()
    print("Check nycMap.html")

if __name__ == "__main__":
    main()
