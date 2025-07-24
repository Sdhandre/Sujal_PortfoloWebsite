import streamlit as st
import base64
from pathlib import Path

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Sujal Dhandre | ML Portfolio",
    page_icon="🔮",
    layout="wide",
)

# --- CUSTOM STYLING ---
st.markdown("""
<style>
/* --- Font Import --- */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* --- Base Styles --- */
html {
    scroll-behavior: smooth;
}

html, body, [class*="st-"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: #111111; /* Very dark background */
    color: #e0e0e0; /* Off-white text for readability */
    background-image: linear-gradient(to right top, #111111, #161319, #1a151f, #1e1725, #22182b);
}

/* --- Main Content Styling --- */
.main .block-container {
    padding-top: 8rem; /* Increased padding to account for navbar */
    padding-bottom: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 900px; 
    margin: auto;
}

/* --- Headers and Text --- */
h1, h2, h3 {
    font-weight: 700;
    color: #ffffff;
}

h1 {
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
    text-align: center;
    letter-spacing: -1px;
}

h2 {
    font-size: 2.5rem;
    color: #c77dff; /* Neon Purple Accent */
    border-bottom: 2px solid #c77dff;
    padding-bottom: 0.8rem;
    margin-top: 5rem;
    margin-bottom: 1.5rem; 
    text-shadow: 0 0 10px rgba(199, 125, 255, 0.3);
}

h3 {
    font-size: 1.75rem;
    margin-top: 0;
    margin-bottom: 1rem;
    color: #c77dff;
}

/* --- Profile Image --- */
.profile-img {
    width: 320px;
    height: 320px;
    border-radius: 20%;
    object-fit: cover;
    border: 4px solid #c77dff;
    box-shadow: 0 0 30px rgba(199, 125, 255, 0.5);
    margin: 15px auto 1.5rem auto;
    display: block;
}

/* --- Custom Info Box (st.info) --- */
.stAlert {
    background-color: rgba(199, 125, 255, 0.1);
    border-radius: 10px;
    text-align: center;
    padding: .25rem;
    font-size: 1.1rem;
    max-width: 70%; /* Adjust this percentage to make the box wider or narrower */
    margin: auto;
    border: 1px solid rgba(199, 125, 255, 0.2);
}

/* --- Social Icons --- */
.social-icons {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 2rem;
}

.social-icons a {
    transition: transform 0.3s;
}

.social-icons a:hover {
    transform: scale(1.2);
}

.social-icons svg {
    stroke: #e0e0e0;
    transition: stroke 0.3s;
}

.social-icons a:hover svg {
    stroke: #c77dff;
}


/* --- Custom Card Container --- */
.card {
    background-color: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 2.5rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
    margin-bottom: 2rem;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 40px rgba(199, 125, 255, 0.3);
    border-color: rgba(199, 125, 255, 0.5);
}

/* --- Link Button Styling --- */
.stButton>button {
    color: #c77dff;
    background-color: transparent;
    border: 1px solid #c77dff;
    border-radius: 25px;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    transition: all 0.3s ease-in-out;
}

.stButton>button:hover {
    background-color: #c77dff;
    color: #ffffff;
    border-color: #c77dff;
    box-shadow: 0 0 15px rgba(199, 125, 255, 0.5);
}

/* --- Skills List --- */
.skills-list {
    list-style-type: none;
    padding: 0;
}
.skills-list li {
    background-color: rgba(199, 125, 255, 0.1);
    color: #c77dff;
    padding: 0.5rem 1rem;
    margin: 0.4rem;
    border-radius: 7px;
    display: inline-block;
    font-weight: 500;
    border: 1px solid rgba(199, 125, 255, 0.2);
}

/* --- Navbar --- */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: rgba(17, 17, 17, 0.85);
    backdrop-filter: blur(10px);
    padding: 1rem 5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.navbar a {
    color: #e0e0e0;
    margin: 0 15px;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
    position: relative;
    padding-bottom: 5px;
}

.navbar a:hover {
    color: #c77dff;
}

.navbar a::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: 0;
    left: 0;
    background-color: #c77dff;
    transition: width 0.3s ease-in-out;
}

.navbar a:hover::after {
    width: 100%;
}


/* --- Anchor for Navbar Jumps --- */
.section-anchor {
    scroll-margin-top: 100px; /* Adjust this value based on navbar height */
}

/* --- Responsive Project Image --- */
.project-img {
    width: 100%;
    height: auto; /* This makes the image responsive */
    border-radius: 15px;
    margin-bottom: 1rem;
}

/* --- Mobile Optimization --- */
@media (max-width: 768px) {
    .main .block-container {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
    h1 {
        font-size: 2.5rem;
    }
    h2 {
        font-size: 1.8rem;
    }
    h3 {
        font-size: 1.4rem;
    }
    .navbar {
        padding: 1rem 0.5rem;
        flex-wrap: wrap; /* Allows links to wrap to the next line */
        justify-content: center;
    }
    .navbar a {
        margin: 5px 10px;
        font-size: 0.9rem;
    }
    .main .block-container {
        padding-top: 10rem;
    }
    .section-anchor {
        scroll-margin-top: 150px;
    }
    .card {
        padding: 1.5rem;
    }
}

</style>
""", unsafe_allow_html=True)


# --- NAVIGATION BAR ---
st.markdown("""
<div class="navbar">
    <a href="#about">About Me</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)


# --- SOCIAL LINKS (Optimized) ---
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Email": "mailto:sujal.dhandre@gmail.com",
}
SOCIAL_ICONS = {
    "LinkedIn": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-linkedin"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    "GitHub": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-github"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>',
    "Email": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mail"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
}


# --- HERO SECTION ---
# --- Profile Image ---
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

# --- Social Links ---
social_icons_html = '<div class="social-icons">'
for name, link in SOCIAL_MEDIA.items():
    icon_svg = SOCIAL_ICONS.get(name, "")
    social_icons_html += f'<a href="{link}" target="_blank" title="{name}">{icon_svg}</a>'
social_icons_html += '</div>'
st.markdown(social_icons_html, unsafe_allow_html=True)

# --- ABOUT ME ---
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>About Me</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
Hello! I'm **Sujal Dhandre**, a passionate and driven Machine Learning enthusiast. My journey into the world of AI and ML began with a fascination for how data can be transformed into actionable insights and intelligent systems. I thrive on tackling complex problems and am constantly exploring new algorithms and techniques to build efficient and impactful models. I have a strong foundation in Python, statistical modeling, and popular ML frameworks like Scikit-learn, TensorFlow, and PyTorch. My goal is to leverage my skills to contribute to innovative projects that solve real-world challenges.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- SKILLS ---
st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>Technical Skills</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
<ul class="skills-list">
  <li>Python</li>
  <li>C++</li>
  <li>JavaScript</li>
  <li>SQL</li>
  <li>HTML/CSS</li>
  <li>Flask</li>
  <li>Bootstrap</li>
  <li>Git</li>
  <li>GitHub</li>
  <li>Numpy</li>
  <li>Pandas</li>
  <li>Scikit-learn</li>
  <li>TensorFlow</li>
  <li>Keras</li>
  <li>PyTorch</li>
  <li>Machine Learning</li>
  <li>Cybersecurity</li>
</ul>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECTS ---
st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>My Projects</h2>', unsafe_allow_html=True)
st.write("Below are some of my key projects, showcasing my skills in deep learning, computer vision, and recommendation systems.")

st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.5])
with col1:
    try:
        with open("agriscan.png", "rb") as img_file:
            agriscan_base64 = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f'<img src="data:image/png;base64,{agriscan_base64}" class="project-img">',
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
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
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
                f'<img src="data:image/png;base64,{cinematch_base64}" class="project-img">',
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.image("https://placehold.co/600x400/161b22/c77dff?text=CineMatch", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.5])
with col1:
    try:
        with open("facescan.png", "rb") as img_file:
            facescan_base64 = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f'<img src="data:image/png;base64,{facescan_base64}" class="project-img">',
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.image("https://placehold.co/600x400/161b22/c77dff?text=FaceScan", use_container_width=True)
with col2:
    st.subheader("Live Face Detction App")
    st.write("""
    - Real-Time Face Recognition: Instantly detects and identifies faces using advanced AI algorithms for fast and accurate results
    - User-Friendly Interface: Simple, intuitive design enables users to easily upload photos or use live camera for face detection.
    - High Accuracy & Security: Utilizes the latest machine learning technology to ensure precise detection while keeping user data secure and private.
    """)
    st.markdown("`Python` `OpenCV` `Tensorflow-GPU`")
    st.link_button("View Source Code and Link", "https://github.com/Sdhandre/REAL-TIME-FACE-DETECTION-MODEL")
st.markdown('</div>', unsafe_allow_html=True)


# --- INTERNSHIPS ---
st.markdown('<div id="experience" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>Internship Experience</h2>', unsafe_allow_html=True)
st.write("I have had the opportunity to work with and learn from talented teams in professional settings.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Data Science and Machine Learning Intern")
st.write("**Feynn Labs** | Apr 2025 - Present")
st.write("""
- Initiated internship with a machine learning-based product ideation task for a scalable business solution.
- Mapped real-world problems to ML models and conducted competitive analysis.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Frontend Developer Intern")
st.write("**Prodigy Infotech** | Jun 2024 - Jul 2024")
st.write("""
- Built 4+ projects including a Weather App with API integration, a functional Stopwatch, Tic-Tac-Toe, and a responsive Landing Page using HTML, CSS, and JavaScript.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- EDUCATION ---
st.markdown('<h2>Education</h2>', unsafe_allow_html=True)
st.write("My formal education has provided me with a strong foundation in computer science and engineering principles.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Bachelor of Technology in Computer Science & Engineering")
st.write("**Medicaps University, Indore** | 2022 - 2026")
st.write("Current SGPA: **8.5/10.0**")
st.write("Relevant Coursework: `Data Structures`, `Algorithms`, `Machine Learning`, `Database Management Systems`, `Linear Algebra`.")
st.markdown('</div>', unsafe_allow_html=True)

# --- RESEARCH & CERTIFICATIONS ---
st.markdown('<h2>Research & Certifications</h2>', unsafe_allow_html=True)
st.write("I am committed to continuous learning and have pursued research and certifications to deepen my expertise.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("- **Research Paper (IJEART):** *Integrating Blockchain in 5G Technologies* (Feb 2024)")
st.write("- **Data Science Bootcamp (Udemy):** *Machine Learning and Data Analysis* (Jan 2025)")
st.write("- **Google Cybersecurity Certification:** *Cybersecurity Fundamentals* (Jun 2023)")
st.markdown('</div>', unsafe_allow_html=True)

# --- EXTRACURRICULAR ---
st.markdown('<h2>Extracurricular Activities</h2>', unsafe_allow_html=True)
st.write("Beyond my academic and professional work, I am actively involved in various leadership and community roles.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
- **Treasurer at STIC:** Managed a fund of over 50,000, handled event budgeting, and organized finances.
- **Workshop Organizer:** Organized 3 workshops and bootcamps for over 200 students, increasing participation by 50%.
- **Content Co-Lead at E-Cell Medicaps:** Led content strategy for promoting entrepreneurial awareness.
- **Content Creator:** Achieved over 2 million engagement on Instagram as a content creator.
""")
st.markdown('</div>', unsafe_allow_html=True)


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
            # This is a placeholder for sending an email.
            # For a real application, you would integrate an email service.
            st.success("Thank you for your message! I will get back to you shortly.")
        else:
            st.error("Please fill out all the fields before sending.")
