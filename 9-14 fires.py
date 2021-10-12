import json

infile = open("US_fires_9_14.json", "r")
outfile = open("readable_fire9-1_data.json", "w")
fire_data = json.load(infile)
json.dump(fire_data, outfile, indent=4)

f = [ x for x in fire_data if x["brightness"] > 450]
brightns=[x["brightness"] for x in f]
lat = [x["latitude"] for x in f]
lon = [x['longitude'] for x in f]

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [
    {
        "type": "scattergeo",
        "lon": lon,
        "lat": lat,
        "text": brightns,
        "marker": {
            "size": [.05 * b for b in brightns],
            "color": brightns,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]
my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="USFIRES914920.html")
print(brightns)
print(lon)
 