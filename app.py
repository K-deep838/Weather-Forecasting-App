import streamlit as st
import requests

# --- Page Setup ---
st.set_page_config(page_title="Weather Forecasting App", page_icon="🌦️", layout="centered")

# --- Custom Background, Layout, and Styles ---
page_bg = """
<style>
/* Background Image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1501630834273-4b5604d2ee31?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Center Content in a Fixed Width Box (acts like window size) */
.block-container {
    background-color: rgba(255,255,255,0.85);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    max-width: 900px;         /* <---- FIXED WIDTH (like window size) */
    margin: auto;             /* center content */
}

/* Label (Select your city) text white */
label, .stSelectbox label {
    color: white !important;
    font-weight: bold;
    font-size: 18px;
}

/* Button design (white text, dark blue background) */
div.stButton > button {
    background-color: #003366;
    color: white;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    padding: 0.5em 1em;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #0059b3;
    color: #fff;
}

/* Black font color for output text */
.output-text {
    color: black !important;
    font-size: 20px;
    font-weight: 500;
}

/* Footer styling */
.footer {
    text-align: center;
    color: white;
    font-size: 16px;
    margin-top: 1rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- App Title ---
st.image("https://cdn-icons-png.flaticon.com/512/1116/1116453.png", width=100)
st.markdown("<h1 style='text-align:center; color:#003366;'>🌤️ Weather Forecasting App</h1>", unsafe_allow_html=True)
st.write("---")

# --- City Dropdown ---
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

# --- Get Weather Button ---
if st.button("☁️ Get Weather"):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fcd668fc794914ac4cc924a3e2b3d590"
        data = requests.get(url).json()

        if data.get("weather"):
            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"].capitalize()
            temperature = int(data["main"]["temp"] - 273.15)
            pressure = data["main"]["pressure"]

            st.markdown(f"<p class='output-text'>📍 <b>City:</b> {city}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='output-text'>🌤️ <b>Weather:</b> {weather}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='output-text'>📝 <b>Description:</b> {description}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='output-text'>🌡️ <b>Temperature (°C):</b> {temperature}°C</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='output-text'>💨 <b>Pressure (hPa):</b> {pressure}</p>", unsafe_allow_html=True)
        else:
            st.error("City not found. Please try again.")
    except Exception as e:
        st.error("Something went wrong. Check your connection or API key.")


