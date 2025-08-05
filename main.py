import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

try:
    if place:
        st.subheader(f"{option} for the next {days} days in {place}")
        dates, data = get_data(place, days)
        if option == "Temperature":
            data = [(data[i]['main']['temp']) for i in range(len(data))]

            figure = px.line(x=dates, y=data, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)
        elif option == "Sky":
            data = [(data[i]['weather'][0]['main']) for i in range(len(data))]
            image_paths = []
            for sky in data:
                if sky == "Clear":
                    image_paths.append("images/clear.png")
                elif sky == "Rain":
                    image_paths.append("images/rain.png")
                elif sky == "Snow":
                    image_paths.append("images/snow.png")
                elif sky == "Cloud":
                    image_paths.append("images/cloud.png")
            st.image(image_paths, width=80)
except KeyError as error:
    st.write("We couldn't get that information. Check to see if the place is spelled correctly!")