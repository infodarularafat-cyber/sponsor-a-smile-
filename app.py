import streamlit as st

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="Sponsor A Smile", page_icon="💚", layout="wide")

# ---------- CUSTOM CSS (COLORS & STYLING) ----------
st.markdown("""
    <style>
    .stApp { background-color: #f0f4f7; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 2px solid #2ecc71; }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #27ae60; border: none; }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- SIDEBAR (MENU WITH ICONS) ----------
with st.sidebar:
    st.markdown("<h2 style='color: #2ecc71;'>🏥 Menu</h2>", unsafe_allow_html=True)
    choice = st.radio(
        "Select an option:",
        ["🏠 Home", "📝 Book Appointment", "🎁 Donate Now", "ℹ️ Help Center"]
    )
    st.divider()
    st.write("Logged in as: **User**")

# ---------- HOME PAGE ----------
if choice == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>💚 Sponsor A Smile</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: grey;'>Helping hands for those in need.</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>❤️ 1200+</h3><p>Lives Impacted</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>💰 5M+</h3><p>Donations Raised</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>🤝 300+</h3><p>Volunteers</p></div>', unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", use_container_width=True)

# ---------- APPOINTMENT PAGE ----------
elif choice == "📝 Book Appointment":
    st.header("📝 Book Your Free Consultation")
    with st.container():
        name = st.text_input("Full Name")
        city = st.selectbox("Select City", ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"])
        problem = st.text_area("What is the health issue?")
        
        if st.button("Submit Request"):
            if name and problem:
                st.success(f"Thank you {name}! Your request has been sent to our doctors.")
                st.balloons()
            else:
                st.error("Please fill all details!")

# ---------- DONATE PAGE ----------
elif choice == "🎁 Donate Now":
    st.header("🎁 Active Medical Cases")
    st.write("Help us save lives by contributing to these urgent cases.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="card"><h4>Baby Sarah - Heart Surgery</h4><p>Target: Rs. 400,000</p></div>', unsafe_allow_html=True)
        st.progress(0.65)
        st.button("Donate for Sarah")
        
    with col_b:
        st.markdown('<div class="card"><h4>Mr. Khan - Kidney Dialysis</h4><p>Target: Rs. 150,000</p></div>', unsafe_allow_html=True)
        st.progress(0.30)
        st.button("Donate for Mr. Khan")

# ---------- HELP CENTER ----------
elif choice == "ℹ️ Help Center":
    st.header("ℹ️ How can we help you?")
    st.write("Contact us for any medical emergencies or financial support.")
    st.info("Emergency Helpline: 0800-SMILE-00")
