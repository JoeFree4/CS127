#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 11,2024





import folium
import pandas as pd

def getData():
    """
    Asks the user for the name of the CSV and
    Returns a dataframe of the contents.
    """
    fileName = input("Enter CSV file name: ")
    df = pd.read_csv(fileName)
    return df

def getColumnNames():
    """
    Asks the user for the exact name of the columns that
    contains the latitude and longitude and
    Returns those values as a tuple.
    """
    latColName = input("Enter column name for latitude: ")
    lonColName = input("Enter column name for longitude: ")
    return (latColName, lonColName)

def getLocale():
    """
    Asks the user for latitude and longitude of the user's current location and
    Returns those floating points numbers.
    """
    lat = float(input("Enter current latitude: "))
    lon = float(input("Enter current longitude: "))
    return (lat, lon)

def computeDist(x1, y1, x2, y2):
    """
    Computes the squared distance between two points (x1,y1) and (x2,y2) and
    Returns (x1-x2)^2 + (y1-y2)^2
    """
    d = (x1-x2)**2 + (y1-y2)**2
    return d

def markClosestPoint(cMap, df, latCol, lonCol, cLat, cLon):
    """
    Finds the closest point to the specified location (cLat, cLon) in the dataframe df
    and marks it on the map cMap.
    """
    minDist = float('inf')
    closestLat, closestLon = None, None
    for index, row in df.iterrows():
        dist = computeDist(row[latCol], row[lonCol], cLat, cLon)
        if dist < minDist:
            minDist = dist
            closestLat = row[latCol]
            closestLon = row[lonCol]
    folium.Marker(location=[closestLat, closestLon], popup="Closest CUNY campus", icon=folium.Icon(color='green')).add_to(cMap)

def writeMap(cMap):
    """
    Writes the inputted map, cMap, to the file specified by the user.
    """
    outF = input("Enter output file: ")
    cMap.save(outfile=outF)

def main():
    dataF = getData()
    latColName, lonColName = getColumnNames()
    lat, lon = getLocale()
    cMap = folium.Map(location=[lat, lon], zoom_start=11)
    markClosestPoint(cMap, dataF, latColName, lonColName, lat, lon)
    writeMap(cMap)

if __name__ == "__main__":
    main()
