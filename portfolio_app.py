import streamlit as st
import requests
from PIL import Image

# ----------------- PAGE CONFIG ----------------- #
st.set_page_config(
    page_title="Mukesh Yadav | Digital CV",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------- CUSTOM CSS ----------------- #
# This function will inject our custom CSS.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# We will create the CSS as a string and then "write" it to a virtual file.
# This is a workaround to keep everything in one .py file for Streamlit Cloud.
CSS = """
/* General Body Styles */
body {
    background-color: #0E1117;
    color: #FAFAFA;
    font-family: 'Inter', sans-serif; /* A cleaner font */
}

/* Main App Container */
.stApp {
    background-color: #0E1117;
}

/* Remove Streamlit Header/Footer */
header, footer {
    visibility: hidden;
}

/* Main Content Area Styling */
.main .block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

/* --- Sticky Left Column --- */
/* This is the magic that makes the left column sticky */
div[data-testid="stHorizontalBlock"] > div:first-child {
    position: -webkit-sticky; /* For Safari */
    position: sticky;
    top: 3rem; /* Adjust this value to control the top offset */
    z-index: 100;
}


/* Card-like container styling */
.css-1d391kg, .css-1avcm0n, .st-emotion-cache-1d391kg, .st-emotion-cache-1avcm0n {
    border-radius: 1rem;
    padding: 1.5rem;
    background-color: #1E1E1E; /* Darker card background */
    border: 1px solid #2c2c2c;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}
.css-1d391kg:hover, .css-1avcm0n:hover, .st-emotion-cache-1d391kg:hover, .st-emotion-cache-1avcm0n:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}


/* Profile Section Specifics */
#profile-section {
    background-color: #161b22; /* Slightly different background for profile card */
    border: 1px solid #30363d;
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
}

#profile-section img {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
    border: 3px solid #1DB954; /* Green accent border */
    margin-bottom: 1rem;
}

/* Custom styled link to look like a button */
.button-link {
    display: block;
    width: 100%;
    padding: 0.75rem 0;
    margin-top: 1rem;
    border-radius: 0.5rem;
    background-color: #1DB954;
    color: #ffffff !important; /* Important to override default link color */
    text-align: center;
    text-decoration: none;
    transition: background-color 0.3s;
    font-weight: bold;
}
.button-link:hover {
    background-color: #1ed760;
    color: #ffffff !important;
}


.stDownloadButton>button {
    background-color: #333333;
    color: #ffffff;
    width: 100%;
    border-radius: 0.5rem;
}
.stDownloadButton>button:hover {
    background-color: #444444;
}

/* Social Icons Styling */
.social-icons {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin: 1.5rem 0;
}
.social-icons a {
    color: #ccc;
    font-size: 1.2rem; /* Adjusted size */
    text-decoration: none;
    transition: color 0.3s;
}
.social-icons a:hover {
    color: #1DB954;
}

/* Section Headers */
h1, h2, h3 {
    font-weight: 600;
}
h2 {
    color: #FAFAFA;
    border-bottom: 2px solid #1DB954;
    padding-bottom: 0.5rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}
"""

# "Write" the CSS to a virtual file and load it
with open("style.css", "w") as f:
    f.write(CSS)
local_css("style.css")

# ----------------- SETTINGS & DATA ----------------- #
# --- PERSONAL INFO ---
NAME = "Mukesh Yadav"
TAGLINE = "Framer Expert & UI/UX Designer"
DESCRIPTION = """
I specialize in creating clean, user-friendly digital experiences by blending creativity with functionality. With a strong background in interactive design, I focus on crafting designs that not only look great but also provide smooth and engaging user interactions, helping ideas come to life seamlessly.
"""
EMAIL = "contact@mukesh.dev"
PHONE = "+91 12345 67890"
ADDRESS = "New Delhi, India"
PROFILE_PIC_URL = "https://i.ibb.co/3s9gKcf/profile-pic.png"  # Replace with your image URL
CV_FILE_PATH = "Mukesh_Yadav_CV.pdf"  # Place your CV in the same folder

# --- SOCIAL MEDIA ---
SOCIAL_MEDIA = {
    "Instagram": "https://instagram.com",
    "Twitter": "https://twitter.com",
    "Dribbble": "https://dribbble.com",
    "Behance": "https://www.behance.net",
}

# --- STATS ---
STATS = {
    "Completed Projects": "30+",
    "Years of Experience": "8+",
    "Happy Clients": "36+",
    "Awards Received": "10+",
}

# --- EXPERIENCE ---
EXPERIENCE = [
    {
        "title": "Framer & UI/UX Designer",
        "company": "Deckim Tech",
        "period": "2023 - Present",
        "description": "Designing interactive prototypes with Framer, focusing on seamless user experiences and scalable solutions through user feedback and collaboration.",
    },
    {
        "title": "UI/UX Designer",
        "company": "CoreOS",
        "period": "2021 - 2023",
        "description": "Created intuitive web and mobile designs, conducted user research, and collaborated with developers to ensure pixel-perfect implementation.",
    },
]

# --- PROJECTS ---
PROJECTS = {
    "🏆 HelloBot - Revolutionize Your Customer Experience": "https://example.com/hellobot",
    "🏆 Flexisoft - Full-Suite Software Solutions for Startups": "https://example.com/flexisoft",
    "🏆 Excludia - Transform your digital presence": "https://example.com/excludia",
    "🏆 CryptoraHub - Trusted platform for crypto investments": "https://example.com/cryptorahub",
}

# --- EDUCATION ---
EDUCATION = [
    {
        "degree": "UI/UX Design Certification",
        "institution": "Interaction Design Foundation, Online",
        "period": "2018 - 2019",
        "description": "Gained hands-on experience in UX research, prototyping, wireframing, and usability testing, focusing on designing seamless, user-friendly digital experiences.",
    },
    {
        "degree": "Bachelor of Design in Interaction Design",
        "institution": "National University of Singapore",
        "period": "2015 - 2017",
        "description": "Completed a comprehensive program focused on designing user-centered digital products, integrating aesthetics and functionality through practical interaction design principles.",
    }
]

# --- SKILLS ---
SKILLS = {
    "Figma": "🎨",
    "Framer": "💻",
    "Lemon Squeezy": "🍋",
    "Notion": "📝",
    "Illustrator": "✍️",
    "SS Icons": "✨",
}

# ----------------- LAYOUT ----------------- #
# Create a two-column layout: Left for profile, Right for main content
left_col, right_col = st.columns([1, 2.5], gap="large")

# ----------------- LEFT COLUMN (PROFILE) ----------------- #
with left_col:
    st.markdown('<div id="profile-section">', unsafe_allow_html=True)

    st.image(PROFILE_PIC_URL)
    st.markdown(f"## {NAME}")
    st.success("🟢 Available for work")

    # --- Social Icons ---
    social_icons_html = '<div class="social-icons">'
    for platform, link in SOCIAL_MEDIA.items():
        social_icons_html += f'<a href="{link}" target="_blank">{platform}</a>'
    social_icons_html += '</div>'
    st.markdown(social_icons_html, unsafe_allow_html=True)

    # --- Buttons ---
    try:
        with open(CV_FILE_PATH, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download CV",
            data=PDFbyte,
            file_name=CV_FILE_PATH.split('/')[-1],
            mime="application/octet-stream",
            use_container_width=True,
        )
    except FileNotFoundError:
        st.warning(f"CV file not found. Please add '{CV_FILE_PATH}' to your project folder.")
    
    # --- Contact Button (Scrolls to form) ---
    st.markdown('<a href="#contact-form" class="button-link">✉️ Contact Me</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ----------------- RIGHT COLUMN (MAIN CONTENT) ----------------- #
with right_col:
    # --- Introduction ---
    st.markdown("### Say Hello 👋")
    st.markdown(f"# I'm {NAME},")
    st.markdown(f"### {TAGLINE}")
    st.write(DESCRIPTION)

    # --- Stats ---
    st.markdown("---")
    cols = st.columns(len(STATS))
    for i, (title, value) in enumerate(STATS.items()):
        with cols[i]:
            st.markdown(f"<h3 style='text-align: center;'>{value}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'>{title}</p>", unsafe_allow_html=True)

    # --- Experience ---
    st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
    for exp in EXPERIENCE:
        with st.container(border=True):
            st.markdown(f"**{exp['title']} | {exp['company']}**")
            st.caption(exp['period'])
            st.write(exp['description'])

    # --- Projects ---
    st.markdown("<h2 id='projects'>Projects</h2>", unsafe_allow_html=True)
    for project, link in PROJECTS.items():
        with st.container(border=True):
            st.markdown(f"[{project}]({link})")

    # --- Education ---
    st.markdown("<h2 id='education'>Education</h2>", unsafe_allow_html=True)
    for edu in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{edu['degree']} | {edu['institution']}**")
            st.caption(edu['period'])
            st.write(edu['description'])

    # --- Skills ---
    st.markdown("<h2 id='skills'>Skills & Tools</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    skill_items = list(SKILLS.items())
    for i in range(len(skill_items)):
        with cols[i % 3]:
            skill, icon = skill_items[i]
            st.markdown(f"<div style='background-color:#2c2c2c; border-radius:0.5rem; padding:1rem; text-align:center;'>{icon} {skill}</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True) # Add space between skill cards

    # --- Contact Form ---
    st.markdown("<h2 id='contact-form'>Let's Get In Touch!</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.text(f"📞 {PHONE}")
            st.text(f"✉️ {EMAIL}")
            st.text(f"📍 {ADDRESS}")
        with col2:
            with st.form("contact_form", clear_on_submit=True):
                name = st.text_input("Full Name", placeholder="Your Name")
                email = st.text_input("Email", placeholder="your.email@example.com")
                message = st.text_area("Message", placeholder="Your message here...")
                submitted = st.form_submit_button("Send Message", use_container_width=True)

                if submitted:
                    st.success("Message sent successfully! I will get back to you soon.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>© {NAME} 2024</p>", unsafe_allow_html=True)
