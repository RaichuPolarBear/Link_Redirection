import streamlit as st
from datetime import datetime
import webbrowser

st.set_page_config(
    page_title="Bhavishya - Vedic Astrology",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .header-container {
        text-align: center;
        padding: 2rem 0;
    }
    .feature-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .info-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-container">
    <h1>🔮 Bhavishya</h1>
    <h3>Modern Vedic Astrology Birth Chart Calculator</h3>
    </div>
""", unsafe_allow_html=True)

# Call to Action at the top
st.markdown("### 🚀 Access Bhavishya Now!")

# Create columns for better button positioning
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌟 Open Bhavishya Application", key="main_cta", use_container_width=True):
        webbrowser.open("https://bhavishya-e80x.onrender.com/")
        st.success("Opening Bhavishya in your browser! 🎉")

    # Show the direct link visibly under the button so users can copy or open it manually
    st.markdown("""
    <div style="text-align:center; margin-top:0.5rem;">
    <small>Direct link: </small>
    <a href="https://bhavishya-e80x.onrender.com/" target="_blank">https://bhavishya-e80x.onrender.com/</a>
    </div>
    """, unsafe_allow_html=True)

    # Also show the plain URL for easy copy-paste
    st.code("https://bhavishya-e80x.onrender.com/")

st.markdown("---")

# Introduction
st.markdown("""
---
### Welcome to Bhavishya

**Bhavishya** is a modern web-based Vedic astrology tool that calculates your complete birth chart using traditional **Parashari methods**. Whether you're new to astrology or a seasoned enthusiast, Bhavishya makes it easy to understand your cosmic blueprint.
""")

# Main sections
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h4>✨ What You Get</h4>
    <ul>
    <li><strong>Birth Chart Analysis</strong> - Complete planetary positions</li>
    <li><strong>Parashari Calculations</strong> - Traditional Vedic astrology methods</li>
    <li><strong>Instant Results</strong> - Get insights immediately</li>
    <li><strong>Easy to Use</strong> - Just enter your birth details</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <h4>🌟 How It Works</h4>
    <ol>
    <li>Enter your <strong>date of birth</strong></li>
    <li>Enter your <strong>time of birth</strong></li>
    <li>Enter your <strong>place of birth</strong></li>
    <li>Get your complete <strong>Vedic birth chart</strong></li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# Features section
st.markdown("### 🎯 Key Features")

features = {
    "📍 Accurate Calculations": "Uses traditional Parashari methods for precise planetary positions",
    "🌍 Global Location Support": "Works with birth locations from anywhere in the world",
    "⚡ Instant Results": "Get your complete birth chart within seconds",
    "📊 Comprehensive Analysis": "Detailed insights into your astrological profile",
    "🎨 Beautiful Interface": "Modern, intuitive design for easy navigation",
    "🔐 Secure & Private": "Your birth details are processed securely"
}

cols = st.columns(2)
for idx, (feature, description) in enumerate(features.items()):
    with cols[idx % 2]:
        st.info(f"**{feature}**\n\n{description}")

# Additional Information
st.markdown("---")
st.markdown("""
### ℹ️ About This Project

**Status:** 🚧 In Development

Bhavishya is currently in active development. We're continuously improving features and adding new calculations to provide you with the most accurate Vedic astrology insights.

### 📚 Vedic Astrology 101

Vedic astrology, also known as Jyotisha, is an ancient Indian science of light. It uses the positions of celestial bodies at the time of your birth to understand your personality, life path, and future possibilities.

**Key Components:**
- **Grahas (Planets):** The 9 celestial bodies that influence our lives
- **Rashis (Zodiac Signs):** 12 divisions of the zodiac
- **Bhavas (Houses):** 12 divisions representing different life areas
- **Nakshatras (Lunar Mansions):** 27 divisions of the ecliptic
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; padding: 1rem;">
<p>Built with ❤️ | Vedic Astrology Calculator | In Development</p>
<p style="font-size: 0.8rem;">Disclaimer: This tool is for educational and entertainment purposes.</p>
</div>
""", unsafe_allow_html=True)
