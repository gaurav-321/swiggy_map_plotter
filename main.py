import pandas as pd
import plotly.express as px
from temp import get_cords
df = pd.DataFrame(get_cords(50))
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="lat",
    lon="lng",
    center={"lat": 22.9734, "lon": 78.6569},  # where map will be centered
    width=1920,  # Width of map
    height=1080,
    zoom=4.5,
    size="size"
)
fig.update_layout(mapbox_style="open-street-map")  # adding beautiful street layout to map
fig.show()
