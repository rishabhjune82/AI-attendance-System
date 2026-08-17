
# ==========================================
# 3. STREAMLIT PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Smart Attendance",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# 4. TITLE
# ==========================================

st.title(
    "🎓 AI-Based Smart Attendance Monitoring System"
)

st.write(
    "Face Recognition Based Attendance System"
)


# ==========================================
# 5. SIDEBAR
# ==========================================

st.sidebar.title("Navigation")


menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Home",
        "Register Student",
        "Take Attendance",
        "Attendance Records"
    ]
)


# ==========================================
# 6. HOME
# ==========================================

if menu == "Home":

    st.header("🏠 Home")

    st.write(
        """
        Welcome to the AI-Based Smart Attendance
        Monitoring System.
        """
    )

    st.success(
        "Application is running successfully!"
    )


