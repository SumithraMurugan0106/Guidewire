import streamlit as st

# Page config
st.set_page_config(page_title="SecureClaim AI", page_icon="🔐", layout="centered")

# Title Section
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🔐 SecureClaim AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Anti-Spoofing Insurance Claim System</h4>", unsafe_allow_html=True)
st.write("---")

# Input Section
st.subheader("📋 Enter Claim Details")

col1, col2 = st.columns(2)

with col1:
    gps_location = st.text_input("📍 GPS Location", placeholder="e.g., Coimbatore")

with col2:
    network_location = st.text_input("🌐 Network Location", placeholder="e.g., Coimbatore")

col3, col4 = st.columns(2)

with col3:
    user_weather = st.selectbox("🌧 User Claimed Weather", ["Rain", "No Rain"])

with col4:
    api_weather = st.selectbox("☁ Actual Weather (API)", ["Rain", "No Rain"])

speed = st.slider("🚴 User Speed (km/h)", 0, 200, 40)

st.write("---")

# Logic Functions
def check_location(gps, network):
    return gps.strip().lower() == network.strip().lower()

def check_weather(api, user):
    return api == user

def behavior(speed):
    return speed < 120

def risk_score(loc, weather, behav):
    score = 0
    if not loc:
        score += 30
    if not weather:
        score += 40
    if not behav:
        score += 20
    return score

def decision(score):
    if score < 30:
        return "APPROVED"
    elif score < 60:
        return "FLAGGED"
    else:
        return "REJECTED"

# Button
if st.button("🔍 Analyze Claim"):
    loc = check_location(gps_location, network_location)
    weather = check_weather(api_weather, user_weather)
    behav = behavior(speed)

    score = risk_score(loc, weather, behav)
    result = decision(score)

    st.write("---")
    st.subheader("📊 Analysis Result")

    # Metrics display
    col1, col2, col3 = st.columns(3)
    col1.metric("Location Match", "✅" if loc else "❌")
    col2.metric("Weather Match", "✅" if weather else "❌")
    col3.metric("Behavior OK", "✅" if behav else "❌")

    st.write("### 🔢 Risk Score:", score)

    # Colored decision box
    if result == "APPROVED":
        st.success("✅ Claim Approved")
    elif result == "FLAGGED":
        st.warning("⚠ Claim Flagged for Review")
    else:
        st.error("❌ Claim Rejected")

    st.info("💡 This decision is based on multi-factor verification and risk scoring.")