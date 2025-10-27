import streamlit as st
import requests

# 🧭 Page setup
st.set_page_config(page_title="Weather Forecasting App", page_icon="🌦️", layout="centered")

# 🎨 Page background and output styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1501630834273-4b5604d2ee31?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.block-container {
    background-color: rgba(255,255,255,0.85);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

/* 🌤️ Make all output text black */
h1, h2, h3, h4, h5, h6, p, div, span {
    color: black !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🖼️ App Header
st.image("https://cdn-icons-png.flaticon.com/512/1116/1116453.png", width=100)
st.markdown("<h1 style='text-align:center; color:#003366;'>🌤️ Weather Forecasting App</h1>", unsafe_allow_html=True)
st.write("---")

# 🏙️ City selection
city = st.selectbox(
    "Select your city:",
    [
        "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat",
        "Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala",
        "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
        "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
        "Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh",
        "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
        "National Capital Territory of Delhi","Puducherry"
    ]
)

# ☁️ Get weather button
if st.button("☁️ Get Weather"):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fcd668fc794914ac4cc924a3e2b3d590"
        data = requests.get(url).json()

        if data.get("weather"):
            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"].capitalize()
            temperature = int(data["main"]["temp"] - 273.15)
            pressure = data["main"]["pressure"]

            # Display data in black text
            st.markdown(f"<h3 style='color:black;'>📍 City: {city}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black; font-size:18px;'>🌤️ <b>Weather:</b> {weather}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black; font-size:18px;'>📝 <b>Description:</b> {description}</p>", unsafe_allow_html=True)
            st.metric(label="🌡️ Temperature (°C)", value=f"{temperature}°C")
            st.metric(label="💨 Pressure (hPa)", value=f"{pressure}")
        else:
            st.error("City not found. Please try again.")
    except Exception as e:
        st.error("Something went wrong. Check your connection or API key.")

st.write("---")
st.markdown("<p style='text-align:center; color:black;'>Created with ❤️ by Your Name</p>", unsafe_allow_html=True)
