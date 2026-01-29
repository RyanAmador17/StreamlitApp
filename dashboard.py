import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

# in the terminal run: streamlit run dashboard.py
# if prompts you to enter email, just press enter/return
# if streamlit not recognized, run:
# python -m streamlit run dashboard.py


st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4, = st.tabs(
    ["Descriptive Statistics",
     "2d Plots",
     "3d Plots",
     "NASA's astronomy"]
)

with tab1:
    st.info("Working on this")
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    fig1 = px.line(df, x = "Time", y = "Temperature (c)")
    st.plotly_chart(fig1)

    fig2 = px.scatter(df, x = "ODO mg/L", y = "Temperature (c)", color = "pH")
    st.plotly_chart(fig2)

with tab3:
    fig3 = px.scatter_3d(df, x = "Longitude", y = "Latitude", z = "Total Water Column (m)")
    fig3.update_scenes(zaxis_autorange = "reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("NASA's astronomy picture of the day")
    url = "https://api.nasa.gov/planetary/apod?api_key="
    response = apod_generator(url,os.getenv("NASA_API_KEY"))

    # Media (image or video)
    if response.get("media_type") == "image":
        st.image(
            response.get("url"),
            caption=response.get("title"),
            use_container_width=True
        )
    elif response.get("media_type") == "video":
        st.video(response.get("url"))

    # Explanation
    st.markdown("### Explanation")
    st.write(response.get("explanation", "No description available."))

    # Optional copyright
    if "copyright" in response:
        st.caption(f"© {response['copyright']}")






