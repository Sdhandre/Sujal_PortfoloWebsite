import streamlit as st
import base64
from pathlib import Path

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Sujal Dhandre | ML Portfolio",
    page_icon="🔮",
    layout="wide",
)

# --- HIDE STREAMLIT DEFAULTS FIRST ---
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- ROBUST CUSTOM STYLING ---
st.markdown("""
<style>
/* --- Font Import --- */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* --- Global Overrides --- */
* {
    font-family: 'Poppins', sans-serif !important;
}

/* --- Base Styles --- */
html {
    scroll-behavior: smooth;
}

.stApp {
    background-color: #111111 !important;
    color: #e0e0e0 !important;
    background-image: linear-gradient(to right top, #111111, #161319, #1a151f, #1e1725, #22182b) !important;
}

/* --- Main Content --- */
.main .block-container {
    padding-top: 8rem !important;
    padding-bottom: 3rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 900px !important;
    margin: auto !important;
}

/* --- Headers --- */
h1, h2, h3, h4, h5, h6 {
    font-weight: 700 !important;
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
}

h1 {
    font-size: 3.5rem !important;
    margin-bottom: 0.5rem !important;
    text-align: center !important;
    letter-spacing: -1px !important;
}

h2 {
    font-size: 2.5rem !important;
    color: #c77dff !important;
    border-bottom: 2px solid #c77dff !important;
    padding-bottom: 0.8rem !important;
    margin-top: 5rem !important;
    margin-bottom: 1.5rem !important;
    text-shadow: 0 0 10px rgba(199, 125, 255, 0.3) !important;
}

h3 {
    font-size: 1.75rem !important;
    margin-top: 0 !important;
    margin-bottom: 1rem !important;
    color: #c77dff !important;
}

/* --- Profile Image --- */
.profile-img {
    width: 320px !important;
    height: 320px !important;
    border-radius: 20% !important;
    object-fit: cover !important;
    border: 4px solid #c77dff !important;
    box-shadow: 0 0 30px rgba(199, 125, 255, 0.5) !important;
    margin: 60px auto 1.5rem auto !important;
    display: block !important;
}

/* --- SUPER ROBUST CONTAINER STYLING --- */
div[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stVerticalBlock"] > div[style*="border"],
.stContainer > div,
[class*="stVertical"] {
   background-color: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
    margin-bottom: 2rem;
    height:auto;
}

/* Enhanced hover effects */
div[data-testid="stVerticalBlockBorderWrapper"]:hover,
div[data-testid="stVerticalBlock"] > div[style*="border"]:hover {
   transform: translateY(-10px);
    box-shadow: 0 0 40px rgba(199, 125, 255, 0.3);
    border-color: rgba(199, 125, 255, 0.5);
}

/* --- BULLETPROOF NAVBAR --- */
.custom-navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    background: rgba(17, 17, 17, 0.95) !important;
    backdrop-filter: blur(20px) !important;
    padding: 1rem 2rem !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    z-index: 999999 !important;
    border-bottom: 1px solid rgba(199, 125, 255, 0.3) !important;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.5) !important;
    height: 70px !important;
}

.custom-navbar a {
    color: #e0e0e0 !important;
    margin: 0 20px !important;
    text-decoration: none !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    position: relative !important;
    padding: 10px 15px !important;
    border-radius: 25px !important;
}

.custom-navbar a:hover {
    color: #c77dff !important;
    background: rgba(199, 125, 255, 0.1) !important;
    transform: translateY(-2px) !important;
}

/* --- Alert/Info Box --- */
div[data-testid="stAlert"] {
    background: linear-gradient(135deg, rgba(199, 125, 255, 0.2), rgba(199, 125, 255, 0.1)) !important;
    border: 1px solid rgba(199, 125, 255, 0.4) !important;
    border-radius: 15px !important;
    color: #ffffff !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    margin: 2rem auto !important;
    max-width: 80% !important;
    padding: 1rem !important;
}

/* --- Skills List --- */
.skills-container {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.8rem !important;
    justify-content: center !important;
    margin: 2rem 0 !important;
}

.skill-tag {
    background: linear-gradient(135deg, rgba(199, 125, 255, 0.2), rgba(199, 125, 255, 0.1)) !important;
    color: #c77dff !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 25px !important;
    font-weight: 600 !important;
    border: 1px solid rgba(199, 125, 255, 0.3) !important;
    transition: all 0.3s ease !important;
    font-size: 0.9rem !important;
}

.skill-tag:hover {
    background: linear-gradient(135deg, rgba(199, 125, 255, 0.3), rgba(199, 125, 255, 0.2)) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 15px rgba(199, 125, 255, 0.2) !important;
}

/* --- Social Icons --- */
.social-links {
    display: flex !important;
    justify-content: center !important;
    gap: 2rem !important;
    margin: 2rem 0 !important;
}

.social-links a {
    color: #e0e0e0 !important;
    transition: all 0.3s ease !important;
    padding: 0.5rem !important;
    border-radius: 50% !important;
}

.social-links a:hover {
    color: #c77dff !important;
    background: rgba(199, 125, 255, 0.1) !important;
    transform: scale(1.2) !important;
}

/* --- Buttons --- */
.stButton > button {
    background: linear-gradient(135deg, transparent, rgba(199, 125, 255, 0.1)) !important;
    color: #c77dff !important;
    border: 2px solid #c77dff !important;
    border-radius: 25px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    font-family: 'Poppins', sans-serif !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #c77dff, rgba(199, 125, 255, 0.8)) !important;
    color: #ffffff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 20px rgba(199, 125, 255, 0.4) !important;
}

/* --- Project Images --- */
.project-image {
    width: 100% !important;
    height: auto !important;
    border-radius: 15px !important;
    margin-bottom: 1rem !important;
    border: 1px solid rgba(199, 125, 255, 0.2) !important;
    transition: all 0.3s ease !important;
}

.project-image:hover {
    transform: scale(1.02) !important;
    box-shadow: 0 5px 20px rgba(199, 125, 255, 0.2) !important;
}

/* --- Anchor Links --- */
.section-anchor {
    scroll-margin-top: 100px !important;
}

/* --- Mobile Responsiveness --- */
@media (max-width: 768px) {
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 10rem !important;
    }
    
    h1 {
        font-size: 2.5rem !important;
    }
    
    h2 {
        font-size: 2rem !important;
    }
    
    .custom-navbar {
        padding: 0.5rem 1rem !important;
        flex-wrap: wrap !important;
        height: auto !important;
        min-height: 60px !important;
    }
    
    .custom-navbar a {
        margin: 0.2rem 0.5rem !important;
        font-size: 0.9rem !important;
    }
    
    .profile-img {
        width: 250px !important;
        height: 250px !important;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"] {
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }
}
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION BAR ---
st.markdown("""
<nav class="custom-navbar">
    <a href="#about">About Me</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# --- SOCIAL LINKS ---
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com", 
    "Email": "mailto:sujal.dhandre@gmail.com",
}

SOCIAL_ICONS = {
    "LinkedIn": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    "GitHub": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>',
    "Email": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
}

# --- HERO SECTION ---
try:
    with open("SUJALPIC.png", "rb") as f:
        data = f.read()
        encoded_image = base64.b64encode(data).decode()
        st.markdown(
            f'<img src="data:image/png;base64,{encoded_image}" class="profile-img">',
            unsafe_allow_html=True,
        )
except FileNotFoundError:
    st.markdown('<img src="https://placehold.co/360x360/111111/c77dff?text=SD" class="profile-img">', unsafe_allow_html=True)

st.markdown('<h1>Sujal Dhandre</h1>', unsafe_allow_html=True)
st.info("Why Streamlit? Because as a data scientist, I like my websites like my models: built in Python and deployed before lunch.")

# Social Links
social_html = '<div class="social-links">'
for name, link in SOCIAL_MEDIA.items():
    icon = SOCIAL_ICONS.get(name, "")
    social_html += f'<a href="{link}" target="_blank" title="{name}">{icon}</a>'
social_html += '</div>'
st.markdown(social_html, unsafe_allow_html=True)

# --- ABOUT ME ---
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>About Me</h2>', unsafe_allow_html=True)
st.write("""
Hello! I'm **Sujal Dhandre**, a passionate and driven Machine Learning enthusiast. My journey into the world of AI and ML began with a fascination for how data can be transformed into actionable insights and intelligent systems. I thrive on tackling complex problems and am constantly exploring new algorithms and techniques to build efficient and impactful models. I have a strong foundation in Python, statistical modeling, and popular ML frameworks like Scikit-learn, TensorFlow, and PyTorch. My goal is to leverage my skills to contribute to innovative projects that solve real-world challenges.
""")

# --- SKILLS ---
st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>Technical Skills</h2>', unsafe_allow_html=True)

skills = [
    "Python", "C++", "JavaScript", "SQL", "HTML/CSS", "Flask", "Bootstrap", 
    "Git", "GitHub", "Numpy", "Pandas", "Scikit-learn", "TensorFlow", 
    "Keras", "PyTorch", "Machine Learning", "Cybersecurity"
]

skills_html = '<div class="skills-container">'
for skill in skills:
    skills_html += f'<span class="skill-tag">{skill}</span>'
skills_html += '</div>'
st.markdown(skills_html, unsafe_allow_html=True)

# --- PROJECTS ---
st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>My Projects</h2>', unsafe_allow_html=True)
st.write("Below are some of my key projects, showcasing my skills in deep learning, computer vision, and recommendation systems.")

# Project 1
with st.container(border=True):
    col1, col2 = st.columns([1, 1.5])
    with col1:
        try:
            with open("agriscan.png", "rb") as img_file:
                agriscan_base64 = base64.b64encode(img_file.read()).decode()
                st.markdown(
                    f'<img src="data:image/png;base64,{agriscan_base64}" class="project-image">',
                    unsafe_allow_html=True
                )
        except FileNotFoundError:
            st.image("https://placehold.co/600x400/161b22/c77dff?text=AgriScan", use_container_width=True)
    with col2:
        st.subheader("Plant Leaf Disease Detection App - AgriScan")
        st.write("""
        - Developed a deep learning image classification model to detect plant diseases from leaf images using Convolutional Neural Networks (CNNs).
        - Classified 13+ plant diseases using a dataset of over 10,000 leaf images.
        - **Achieved a 92% accuracy rate with the final model.**
        """)
        st.markdown("`Python` `TensorFlow` `Keras` `CNN`")
        st.link_button("View Source Code and Link", "https://github.com/Sdhandre/plant-disease-streamlit")

# Project 2
with st.container(border=True):
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("CineMatch AI - Movie Recommendation Model")
        st.write("""
        - Trained a recommendation model on a dataset of over 25,000 user ratings.
        - **Achieved over 90% accuracy in predicting user movie preferences.**
        - Reduced absenteeism prediction error by 20% through feature selection and optimization.
        """)
        st.markdown("`Python` `Pandas` `Scikit-learn`")
        st.link_button("View Source Code and Link", "https://github.com/Sdhandre/Cinematch_AI")
    with col2:
        try:
            with open("cinematch.png", "rb") as img_file:
                cinematch_base64 = base64.b64encode(img_file.read()).decode()
                st.markdown(
                    f'<img src="data:image/png;base64,{cinematch_base64}" class="project-image">',
                    unsafe_allow_html=True
                )
        except FileNotFoundError:
            st.image("https://placehold.co/600x400/161b22/c77dff?text=CineMatch", use_container_width=True)

# Project 3
with st.container(border=True):
    col1, col2 = st.columns([1, 1.5])
    with col1:
        try:
            with open("facescan.png", "rb") as img_file:
                facescan_base64 = base64.b64encode(img_file.read()).decode()
                st.markdown(
                    f'<img src="data:image/png;base64,{facescan_base64}" class="project-image">',
                    unsafe_allow_html=True
                )
        except FileNotFoundError:
            st.image("https://placehold.co/600x400/161b22/c77dff?text=FaceScan", use_container_width=True)
    with col2:
        st.subheader("Live Face Detection App")
        st.write("""
        - Real-Time Face Recognition: Instantly detects and identifies faces using advanced AI algorithms for fast and accurate results
        - User-Friendly Interface: Simple, intuitive design enables users to easily upload photos or use live camera for face detection.
        - High Accuracy & Security: Utilizes the latest machine learning technology to ensure precise detection while keeping user data secure and private.
        """)
        st.markdown("`Python` `OpenCV` `Tensorflow-GPU`")
        st.link_button("View Source Code and Link", "https://github.com/Sdhandre/REAL-TIME-FACE-DETECTION-MODEL")

# --- EXPERIENCE ---
st.markdown('<div id="experience" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>Internship Experience</h2>', unsafe_allow_html=True)
st.write("I have had the opportunity to work with and learn from talented teams in professional settings.")

with st.container(border=True):
    st.subheader("Data Science and Machine Learning Intern")
    st.write("**Feynn Labs** | Apr 2025 - Present")
    st.write("""
    - Initiated internship with a machine learning-based product ideation task for a scalable business solution.
    - Mapped real-world problems to ML models and conducted competitive analysis.
    """)

with st.container(border=True):
    st.subheader("Frontend Developer Intern")
    st.write("**Prodigy Infotech** | Jun 2024 - Jul 2024")
    st.write("""
    - Built 4+ projects including a Weather App with API integration, a functional Stopwatch, Tic-Tac-Toe, and a responsive Landing Page using HTML, CSS, and JavaScript.
    """)

# --- EDUCATION ---
st.markdown('<h2>Education</h2>', unsafe_allow_html=True)
st.write("My formal education has provided me with a strong foundation in computer science and engineering principles.")

with st.container(border=True):
    st.subheader("Bachelor of Technology in Computer Science & Engineering")
    st.write("**Medicaps University, Indore** | 2022 - 2026")
    st.write("Current SGPA: **8.5/10.0**")
    st.write("Relevant Coursework: `Data Structures`, `Algorithms`, `Machine Learning`, `Database Management Systems`, `Linear Algebra`.")

# --- CERTIFICATIONS ---
st.markdown('<h2>Research & Certifications</h2>', unsafe_allow_html=True)
st.write("I am committed to continuous learning and have pursued research and certifications to deepen my expertise.")

with st.container(border=True):
    st.write("- **Research Paper (IJEART):** *Integrating Blockchain in 5G Technologies* (Feb 2024)")
    st.write("- **Data Science Bootcamp (Udemy):** *Machine Learning and Data Analysis* (Jan 2025)")
    st.write("- **Google Cybersecurity Certification:** *Cybersecurity Fundamentals* (Jun 2023)")

# --- EXTRACURRICULAR ---
st.markdown('<h2>Extracurricular Activities</h2>', unsafe_allow_html=True)
st.write("Beyond my academic and professional work, I am actively involved in various leadership and community roles.")

with st.container(border=True):
    st.write("""
    - **Treasurer at STIC:** Managed a fund of over 50,000, handled event budgeting, and organized finances.
    - **Workshop Organizer:** Organized 3 workshops and bootcamps for over 200 students, increasing participation by 50%.
    - **Content Co-Lead at E-Cell Medicaps:** Led content strategy for promoting entrepreneurial awareness.
    - **Content Creator:** Achieved over 2 million engagement on Instagram as a content creator.
    """)

# --- CONTACT ---
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>Get In Touch!</h2>', unsafe_allow_html=True)
st.write("My inbox is always open. Whether you have a question, a project idea, or just want to connect, feel free to reach out!")

with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button(label='Send Message')

    if submit_button:
        if name and email and message:
            st.success("Thank you for your message! I will get back to you shortly.")
        else:
            st.error("Please fill out all the fields before sending.")
