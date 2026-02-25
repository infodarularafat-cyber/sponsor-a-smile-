import streamlit as st
import sqlite3
import pandas as pd
import hashlib
import datetime

# ---------- DATABASE ----------
conn = sqlite3.connect("sehatsahara.db", check_same_thread=False)
c = conn.cursor()

def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                role TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS appointments(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                city TEXT,
                specialist TEXT,
                date TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS loans(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                amount REAL,
                duration INTEGER,
                emi REAL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS campaigns(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient TEXT,
                disease TEXT,
                required REAL,
                raised REAL DEFAULT 0)''')

    conn.commit()

create_tables()

# ---------- HELPERS ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password, role):
    c.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)",
              (username, hash_password(password), role))
    conn.commit()

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, hash_password(password)))
    return c.fetchone()

# ---------- UI ----------
st.set_page_config(page_title="SehatSahara", layout="wide")
st.title("💚 SehatSahara - Healthcare Financing Platform")

menu = st.sidebar.selectbox("Menu",
                            ["Home", "Login", "Signup",
                             "Book Appointment",
                             "Apply Loan",
                             "Raise Funds",
                             "Donate",
                             "Admin Dashboard"])

# ---------- HOME ----------
if menu == "Home":
    st.write("### Welcome to SehatSahara")
    st.write("Book doctors, apply for medical loans, or raise funds.")

# ---------- SIGNUP ----------
elif menu == "Signup":
    st.subheader("Create Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type='password')
    role = st.selectbox("Role", ["Patient", "Doctor", "Donor"])

    if st.button("Signup"):
        add_user(new_user, new_pass, role)
        st.success("Account Created Successfully!")

# ---------- LOGIN ----------
elif menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.success(f"Welcome {username}")
        else:
            st.error("Invalid Credentials")

# ---------- APPOINTMENT ----------
elif menu == "Book Appointment":
    st.subheader("Book Doctor Appointment")

    name = st.text_input("Your Name")
    city = st.selectbox("City", ["Islamabad", "Rawalpindi", "Lahore"])
    specialist = st.selectbox("Specialist",
                              ["Cardiologist", "Dermatologist", "Oncologist"])
    date = st.date_input("Select Date")

    if st.button("Book"):
        c.execute("INSERT INTO appointments(name,city,specialist,date) VALUES(?,?,?,?)",
                  (name, city, specialist, str(date)))
        conn.commit()
        st.success("Appointment Booked!")

# ---------- LOAN ----------
elif menu == "Apply Loan":
    st.subheader("Medical Loan Calculator")

    name = st.text_input("Your Name")
    P = st.number_input("Treatment Cost (PKR)", min_value=0.0)
    rate = 0.12 / 12  # 12% yearly interest
    n = st.number_input("Duration (Months)", min_value=1)

    if st.button("Calculate & Apply"):
        emi = (P * rate * (1 + rate)**n) / ((1 + rate)**n - 1)
        c.execute("INSERT INTO loans(name,amount,duration,emi) VALUES(?,?,?,?)",
                  (name, P, n, emi))
        conn.commit()
        st.success(f"Loan Applied! Monthly EMI: {round(emi,2)} PKR")

# ---------- RAISE FUNDS ----------
elif menu == "Raise Funds":
    st.subheader("Create Fundraising Campaign")

    patient = st.text_input("Patient Name")
    disease = st.text_input("Disease")
    required = st.number_input("Required Amount (PKR)", min_value=0.0)

    if st.button("Create Campaign"):
        c.execute("INSERT INTO campaigns(patient,disease,required) VALUES(?,?,?)",
                  (patient, disease, required))
        conn.commit()
        st.success("Campaign Created Successfully!")

# ---------- DONATE ----------
elif menu == "Donate":
    st.subheader("Donate to Campaign")

    campaigns = pd.read_sql_query("SELECT * FROM campaigns", conn)

    if not campaigns.empty:
        campaign_id = st.selectbox("Select Campaign",
                                   campaigns["id"])

        amount = st.number_input("Donation Amount", min_value=0.0)

        if st.button("Donate"):
            c.execute("UPDATE campaigns SET raised = raised + ? WHERE id=?",
                      (amount, campaign_id))
            conn.commit()
            st.success("Thank you for your donation ❤️")

    else:
        st.info("No campaigns available.")

# ---------- ADMIN ----------
elif menu == "Admin Dashboard":
    st.subheader("Admin Dashboard")

    st.write("### Users")
    st.dataframe(pd.read_sql_query("SELECT * FROM users", conn))

    st.write("### Appointments")
    st.dataframe(pd.read_sql_query("SELECT * FROM appointments", conn))

    st.write("### Loans")
    st.dataframe(pd.read_sql_query("SELECT * FROM loans", conn))

    st.write("### Campaigns")
    st.dataframe(pd.read_sql_query("SELECT * FROM campaigns", conn))
