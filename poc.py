import folium
import poc_db
from folium import plugins

map_obj = folium.Map(location=[27.00, 00.01], zoom_start=2.4, tiles=None, world_copy_jump=True)

folium.TileLayer('openstreetmap').add_to(map_obj)
# other layers -------------------------------------------------------------------------------------
# folium.TileLayer('stamenterrain', attr='stamenterrain').add_to(map_obj)
# folium.TileLayer('cartodb positron', attr='cartodb positron').add_to(map_obj)
# folium.TileLayer('stamenwatercolor', attr='stamenwatercolor').add_to(map_obj)
# folium.TileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDBdark',
#                  attr="CartoDB.DarkMatter", class_name="mapLayer").add_to(map_obj)

# folium.LayerControl(position='topleft').add_to(map_obj)

# float image not fitted on desktop and mobile version on the same place -----------------------------
# url = 'https://snos.ro/media/compass.png'
# folium.plugins.FloatImage(url, bottom=88, left=5, kwargs="height='30px'").add_to(map_obj)

# https://python-visualization.github.io/folium/latest/advanced_guide/piechart_icons.html


folium.plugins.MiniMap(
    position='topright',
    toggle_display=True,
    tile_layer='cartodb positron',
    width=170,
    height=100,
    bottom=25,
    zoom_animation=True,
    collapsed_width=24,
    collapsed_height=24
).add_to(map_obj)

formatter = "function(num) {return L.Util.formatNum(num, 3) + ' &deg; ';};"
folium.plugins.MousePosition(
    position='topright',
    separator='/ ',
    empty_string='Coordinates:',
    prefix='Location:',
    num_digits=4,
    lat_formatter=formatter,
    lng_formatter=formatter
).add_to(map_obj)

folium.plugins.LocateControl(position="topright", strings={"title": "Find my location!", "popup": "Here you are!"},
                             auto_start=False).add_to(map_obj)

folium.plugins.Fullscreen(position='topleft', title='Full Screen', title_cancel='Normal Screen',
                          force_separate_button=True).add_to(map_obj)

flights = [
    [(44.4268, 26.1025), (25.2854, 51.5310)],  # Bucharest - Doha
    [(25.2854, 51.5310), (-6.776, 39.178)],  # Doha - Dar es-Salaam
    [(31.221, 121.482), (51.5000, -0.1250)],  # Shanghai - London
    [(51.5000, -0.1250), (44.4268, 26.1025)],  # London - Bucharest
    [(44.4268, 26.1025), (41.0082, 28.9784)],  # Bucharest - Istanbul
    [(41.0082, 28.9784), (39.4670, -0.3750)],  # Istanbul - Valencia
    [(36.7213, -4.4213), (41.9028, 12.4964)],  # Malaga - Rome
    [(41.9028, 12.4964), (44.4268, 26.1025)],  # Rome - Bucharest
    [(44.4268, 26.1025), (35.8992, 14.5141)],  # Bucharest - Malta
    [(35.8992, 14.5141), (46.7712, 23.6236)],  # Malta - Cluj-Napoca
    [(35.8992, 14.5141), (41.0082, 28.9784)],  # Malta - Istanbul
    [(41.0082, 28.9784), (22.543, 114.063)],  # Istanbul - Shenzen
    [(36.7213, -4.4213), (52.3676, 4.9041)],  # Malaga - Amsterdam
    [(52.3676, 4.9041), (44.4268, 26.1025)],  # Amsterdam - Bucharest
    [(52.3676, 4.9041), (42.6977, 23.3219)],  # Amsterdam - Sofia
    [(52.3676, 4.9041), (8.3730, -81.534)],  # Amsterdam - Panama
    [(8.3730, -81.534), (41.0082, 28.9784)],  # Panama - Istanbul
    [(44.4268, 26.1025), (50.1109, 8.6821)],  # Bucharest - Frankfurt
    [(50.1109, 8.6821), (55.7284, 9.1124)],  # Frankfurt - Billund
    [(55.7284, 9.1124), (52.3676, 4.9041)],  # Billund - Amsterdam
    [(52.3676, 4.9041), (40.7360, -74.1720)],  # Amsterdam - New York
    [(40.7360, -74.1720), (52.2297, 21.0122)],  # New York - Warsaw
    [(52.2297, 21.0122), (44.4268, 26.1025)],  # Warsaw - Bucharest
    [(52.3676, 4.9041), (34.0549, -118.2426)],  # Amsterdam - Los Angeles
    [(34.0549, -118.2426), (48.8566, 2.3522)],  # Los Angeles - Paris
    [(48.8566, 2.3522), (44.4268, 26.1025)],  # Paris -  Bucharest
    [(44.4268, 26.1025), (48.2082, 16.3738)],  # Bucharest -  Vienna
    [(48.2082, 16.3738), (53.5510, 9.9940)],  # Vienna -  Hamburg
]

for flight in flights:
    folium.PolyLine(
        smooth_factor=1,
        locations=flight,
        color='darkblue',
        weight=0.5,
        tooltip=folium.Tooltip(f"""<img src="https://snos.ro/media/airplane_e.png" height='16rem' style="margin-left:-0.6rem;
                margin-top:-1.4rem;" alt="image_airplane">""", permanent=True)
    ).add_to(map_obj)

flags_w = ['BELGIUM.GIF', 'ENGLAND.jpg', 'GREECE.GIF', 'HONGKONG.png', 'GERMANY.GIF', 'AUSTRIA.GIF', 'DENMARK.GIF',
           'NED.GIF',
           'MALAYSIA.GIF', 'CHINA.GIF', 'ITALY.GIF', 'EGYPT.GIF', 'JAPAN.GIF', 'FRANCE.GIF', 'MOROCCO.GIF',
           'NIGERIA.GIF',
           'EGUINEA.jpg', 'GHANA.JPG', 'MALTA.GIF', 'BULGARIA.GIF', 'COTEDIVOIRE.GIF', ]
flags_e = ['TANZANIA.GIF',
           'THAILAND.GIF',
           'SINGAPORE.GIF',
           'UNITEDSTATES.GIF',
           'SOUTH-KOREA.GIF',
           'TAIWAN.GIF',
           'PHILIPPINES.GIF',
           'RUSSIA.GIF',
           'SPAIN.GIF',
           'SENEGAL.GIF',
           'PORTUGAL.GIF',
           'TURKEY.GIF',
           'SAUDI.GIF',
           'UAE.jpg',
           'PANAMA.GIF',
           'OMAN.GIF',
           'SRILANKA.JPG',
           'VIETNAM.GIF',
           'QATAR.GIF',
           'POLAND.GIF',
           'ROMANIA.GIF'
           ]

long_start_w = -216
for flag in sorted(flags_w):
    folium.Circle(
        location=[-57.50, long_start_w], color='transparent', tooltip=folium.Tooltip(
            f"""<img src="https://snos.ro/media/flags/{flag}" height='15.5rem' style="margin-left:-0.6rem; 
            margin-top:-1.4rem;" alt="image_city">""", permanent=True)).add_to(map_obj)
    long_start_w += 10.25
long_start_e = 216
for flag in sorted(flags_e, reverse=True):
    folium.Circle(
        location=[-57.50, long_start_e], color='transparent', tooltip=folium.Tooltip(
            f"""<img src="https://snos.ro/media/flags/{flag}" height='15.5rem' style="margin-left:-1.24rem; 
            margin-top:-1.4rem;" alt="image_city">""", permanent=True)).add_to(map_obj)
    long_start_e -= 10.25


def create_marker(name_city, name_country, location, last_visit, type_visit, clr, ph_city, ph_flag):
    folium.Marker(location=location,
                  popup=folium.Popup(
                      f"""
                      <img src={ph_city}
                      class="img_city" alt="image_city">
                      <h3 class='title_city'>{name_city} ({name_country}) <img src={ph_flag}
                      class="img_flag" alt="img_flag"></h3> 
                      <h5 class='last_visit'>last visit: {last_visit}</h4>
                      """),
                  icon=folium.Icon(icon=type_visit, prefix='fa', color=clr)).add_to(map_obj)


map_obj.get_root().html.add_child(folium.Element("""
<style>

.leaflet-control-zoom-in,
.leaflet-control-zoom-out {
	font: bold 15px Monaco, monospace;
	font-size: 23px;
}

.leaflet-control-zoom{
    box-shadow: #000 0px 55px 15px -5px;
}



.leaflet-tooltip{
    background-color: transparent;
    height: 0.9rem;
    width: 1.8rem;
    border-radius:5%;
    box-shadow: #000 0px 15px 12px -5px;
}

.leaflet-control-container{
    box-shadow: #000 0px 15px 15px -5px;
}

.leaflet-oldie .leaflet-control-minimap a {
	background-color: #AAD4E1;
}

.leaflet-control-minimap{
    box-shadow: #000 2px 5px 7px 1px;
    border-radius: 8px;
    border:solid #AAD4E1 3px;
}

.leaflet-control-zoom-fullscreen {
    box-shadow: #000 0px 10px 10px -5px;
}

.leaflet-control-layers-toggle {
    box-shadow: #000 0px 15px 15px -5px;
}

.leaflet-control-locate a{
    background-color:transparent;
    border-radius: 5%;
    padding-top: -1rem
}


.top_title {
    white-space: nowrap;
    color:darkblue;
    font: bold 55px;
    position: fixed;
    font-size:x-large;
    text-shadow: 0 7px 5px rgba(0,0,0,0.65);
}

.title_city {
    white-space: nowrap;
    color:darkblue;
    padding: 0.1rem;
    font: bold 15px Verdana;
    text-shadow: 0 3px 5px rgba(0,0,0,0.65);

}

.last_visit {
    color: #000;
    padding: 0.1rem;
    text-shadow: 0 3px 5px darkblue;
}

.leaflet-popup-content-wrapper, .leaflet-popup-tip {
  background-color: #DDF9FF;
  margin:0;
  opacity: 0.96;
  border-radius: 5%;
  box-shadow: #000 0px 23px 15px -5px;
}

.img_city {
    height: 19rem;
    border-radius: 2%;
}

.img_flag {
    height: 3rem;
    margin-left: 0.5rem;
    box-shadow: 0 4px 5px rgba(0,0,0,0.65);
}

.leaflet-container {
	background: #A5D5E4;
	outline-offset: 1px;
	}



</style>

"""))

#  mouse_position.css = <link rel="stylesheet" href="https://snos.ro/media/css/mouse_position.css"/>

for row in poc_db.show_table():
    create_marker(row[1], row[2], [row[3], row[4]], row[5], row[6], row[7], row[8], row[9])

map_obj.save('sn_visits.html')
