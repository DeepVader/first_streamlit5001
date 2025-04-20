import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import plotly.figure_factory as ff
import datetime


st.title("Uber pickups in NYC")

DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text("Loading data...")
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Loading data...done!")

# data


# st.subheader("Raw data")
# st.write(data)
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)


st.subheader("Number of pickups by hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)


# st.subheader("Map of all pickups")
# st.map(data)
# hour_to_filter = 17
# Some number in the range 0-23
hour_to_filter = st.slider("hour", 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader("Map of all pickups at %s:00" % hour_to_filter)
st.map(filtered_data)


# Exercise
data_Ex = data.copy()

# 2 Use Date input
today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d_range = st.date_input(
    label="Select date range",
    value=(data_Ex["date/time"].min(), data_Ex["date/time"].max()),
    format="MM.DD.YYYY",
    min_value=data_Ex["date/time"].min(),
    max_value=data_Ex["date/time"].max(),
)

if len(d_range) == 2:
    start_date, end_date = d_range
    filtered_df = data_Ex[
        (data_Ex["date/time"] >= pd.to_datetime(start_date))
        & (data_Ex["date/time"] <= pd.to_datetime(end_date))
    ]
else:
    filtered_df = data

# 1  Convert 2D map to 3D map using PyDeck.
st.subheader("3D map")
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=data["lat"].mean(),
            longitude=data["lon"].mean(),
            zoom=11,
            pitch=50,  # เอียงมุมกล้องให้สูงขึ้น
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=filtered_df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=filtered_df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

# 3 selectbox
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

# 4 plotly
filtered_df2 = data.copy()
filtered_df2["date"] = filtered_df2["date/time"].dt.date

count_per_day = filtered_df2.groupby("date").size().reset_index(name="count")
fig = px.line(count_per_day, x="date", y="count")

st.plotly_chart(fig)

# 5
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("ADD (+)"):
    st.session_state.counter += 1

st.write(f"You have pressed the button {st.session_state.counter} times.")
