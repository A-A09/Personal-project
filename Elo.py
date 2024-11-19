import time
import random
import streamlit as st

st.title("**Sport Spottrs**")

# Initialize session state
if "last_notification_time" not in st.session_state:
    st.session_state.last_notification_time = time.time()
if "current_notification" not in st.session_state:
    st.session_state.current_notification = "Welcome!."

# List of notifications
notifications = [
    "🚨 **Football match today!!!** ",
    "📢 **Padel Tryout next week!** 😌",
    "💡 **Volleyball tournment tmrw** 🌟",
     "🚨 **Time to hydrate!** 🚰",
    "📢 **Take a deep breath and relax!** 😌",
    "💡 **Did you know? Streamlit is awesome!** 🌟",
    "⏳ **Stay focused on your goals!** 🎯",
    "🎉 **You're doing great! Keep it up!** 🙌",
    "💻 **Code a little, learn a lot!** 🧠",
    "🌟 **Success is a journey, not a destination!** 🚀",
]


# Check the time and update the notification every second
current_time = time.time()
if current_time - st.session_state.last_notification_time >= 1:  # 1 second
    # Choose a random notification
    st.session_state.current_notification = random.choice(notifications)
    st.session_state.last_notification_time = current_time

# Show the current notification
st.write(st.session_state.current_notification)


# Streamlit app
with st.sidebar: 

    st.title("**Navigation**")
    choice = st.radio("Choose an option", ["Intro","Football","Volleyball","Basketball","Padel","Tennis","Handball"])

if choice == "Intro":
    st.markdown("Welcome! We are a team of Saudi students from Dhahran Ahliya Schools dedicated to promoting accessibility and inclusivity. Our mission is to create opportunities for individuals with disabilities to engage in sports and recreation. Through this platform, we showcase accessible venues and inclusive events, fostering a community that values diversity and participation for all. Join us in making sports accessible for everyone!")

elif choice == "Football":
    st.text("Football section")

elif choice =="Volleyball":
    st.text("Volleyball section")

elif choice =="Basketball":
    st.text("Basketball section")

elif choice=="Padel":
    st.text("Padel section")

elif choice == "Tennis":
    st.text("Tennis section")

elif choice=="Handball":
    st.text("Handball section")


# to run streamlit use this command: python -m streamlit run Elo.py            
# streamlit run c:/Users/abdul/OneDrive/Desktop/projects/Fatoom/Elo.py