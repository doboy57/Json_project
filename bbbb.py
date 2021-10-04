import json
infile = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')
eq_data = json.load(infile)
json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data["features"]
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['lng']


from plotly.graphs_objs import Scattergeo, Layout
from plotly import offline 

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global earthquake 1 day')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='globalearthquake1day.html')