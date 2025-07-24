import streamlit as st
import base64

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Sujal Dhandre | ML Portfolio",
    page_icon="🔮",
    layout="wide",
)

# --- CUSTOM STYLING (inserted very early) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Global Base Styling */
html, body, [class*="st-"] {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background-color: #111111;
    color: #e0e0e0;
    background-image: linear-gradient(to right top, #111111, #161319, #1a151f, #1e1725, #22182b);
}
/*--- Fixed Navbar ---*/
.navbar {
    position: fixed;
    top: 0; left: 0; width: 100vw;
    background-color: rgba(17, 17, 17, 0.92);
    backdrop-filter: blur(10px);
    z-index: 1000;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    display: flex; justify-content: center; align-items: center;
    padding: 1.1rem 0;
}
.navbar a {
    color: #e0e0e0;
    margin: 0 18px; text-decoration: none; font-weight: 500;
    position: relative;
    padding-bottom: 5px;
    transition: color 0.3s;
}
.navbar a:hover { color: #c77dff; }
.navbar a::after {
    content: '';
    position: absolute; width: 0; height: 2px; bottom: 0; left: 0;
    background-color: #c77dff;
    transition: width 0.3s;
}
.navbar a:hover::after { width: 100%; }
.main .block-container {    /* Space for navbar */
    padding-top: 7.5rem;
    max-width: 900px;
    margin: auto;
}

/*--- Card Container ---*/
.card {
    background-color: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 2.2rem;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 2rem;
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
}
.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 40px rgba(199, 125, 255, 0.3);
    border-color: rgba(199,125,255,0.5);
}

/*--- Responsive Profile Image ---*/
.profile-img {
    width: 320px; height: 320px;
    border-radius: 20%; object-fit: cover;
    border: 4px solid #c77dff;
    box-shadow: 0 0 30px rgba(199,125,255,0.5);
    margin: 17px auto 1.5rem auto; display: block;
}

/*--- Skills List ---*/
.skills-list { list-style-type: none; padding: 0; margin:0; }
.skills-list li {
    background-color: rgba(199,125,255,0.1);
    color: #c77dff;
    padding: .5rem 1rem; margin: .4rem;
    border-radius: 7px; display: inline-block;
    font-weight: 500;
    border: 1px solid rgba(199,125,255,0.2);
}
/*--- Social Icons ---*/
.social-icons {
    display: flex; justify-content: center; gap: 2rem; margin-top: 2rem;
}
.social-icons a { transition: transform 0.3s; }
.social-icons a:hover { transform: scale(1.2); }
.social-icons svg { stroke: #e0e0e0; transition: stroke 0.3s; }
.social-icons a:hover svg { stroke: #c77dff; }
/*--- Responsive ---*/
@media (max-width: 768px) {
    .main .block-container { padding-left: 1.2rem; padding-right: 1.2rem; padding-top: 9.5rem;}
    h1 { font-size: 2.3rem; }
    h2 { font-size: 1.6rem; }
    .navbar { padding: .8rem 0.3rem; }
    .navbar a { margin: 6px 7px; font-size: 0.97rem; }
    .section-anchor { scroll-margin-top: 140px; }
    .card { padding: 1.0rem; }
}

/*--- Section Anchor for Smooth Scroll ---*/
.section-anchor { scroll-margin-top: 100px; }
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <a href="#about">About Me</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# --- PROFILE IMAGE ---
try:
    with open("SUJALPIC.png", "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<img src="data:image/png;base64,{encoded_image}" class="profile-img">',
            unsafe_allow_html=True
        )
except FileNotFoundError:
    st.markdown('<img src="https://placehold.co/360x360/111111/c77dff?text=SD" class="profile-img">', unsafe_allow_html=True)

# --- HERO ---

st.markdown('<h1 style="text-align:center;">Sujal Dhandre</h1>', unsafe_allow_html=True)
st.info("Why Streamlit? Because as a data scientist, I like my websites like my models: built in Python and deployed before lunch.")

# --- SOCIAL LINKS ---
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Email": "mailto:sujal.dhandre@gmail.com",
}
SOCIAL_ICONS = {
    "LinkedIn": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    "GitHub": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>',
    "Email": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
}
social_icons_html = '<div class="social-icons">'
for name, link in SOCIAL_MEDIA.items():
    icon_svg = SOCIAL_ICONS.get(name, "")
    social_icons_html += f'<a href="{link}" target="_blank" title="{name}">{icon_svg}</a>'
social_icons_html += '</div>'
st.markdown(social_icons_html, unsafe_allow_html=True)

# --- ABOUT ---
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>About Me</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
Hello! I'm **Sujal Dhandre**, a passionate Machine Learning enthusiast. My journey into AI and ML began with a fascination for how data becomes insight and intelligence. I thrive on complex problems, exploring new algorithms and building impactful models. My strengths: Python, statistical modeling, and frameworks like Scikit-learn, TensorFlow, and PyTorch. My goal: to build innovative solutions for real-world problems.
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
st.write("Here are some key projects, showcasing my skills in deep learning, computer vision, and recommendation systems.")

st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.5])
with col1:
    try:
        with open("agriscan.png", "rb") as img_file:
            agriscan_base64 = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f'<img src="data:image/png;base64,{agriscan_base64}" class="profile-img">',
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.image("https://placehold.co/600x400/161b22/c77dff?text=AgriScan", use_container_width=True)
with col2:
    st.subheader("Plant Leaf Disease Detection App - AgriScan")
    st.write("""
    - Built a deep learning model to detect plant diseases from leaf images using CNNs.
    - Classified 13+ plant diseases using 10,000+ images.
    - **92% accuracy achieved.**
    """)
    st.markdown("`Python` `TensorFlow` `Keras` `CNN`")
    st.link_button("View Source Code", "https://github.com/Sdhandre/plant-disease-streamlit")
st.markdown('</div>', unsafe_allow_html=True)

# --- More projects follow the same "card" pattern ---


# --- EXPERIENCE SECTION ---
st.markdown('<div id="experience" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2>Internship Experience</h2>', unsafe_allow_html=True)
st.write("I've worked with and learned from talented teams in professional settings.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Data Science and Machine Learning Intern")
st.write("**Feynn Labs** | Apr 2025 - Present")
st.write("""
- Started with a machine learning product ideation task for a scalable business solution.
- Mapped real problems to ML models and conducted competitive analysis.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Frontend Developer Intern")
st.write("**Prodigy Infotech** | Jun 2024 - Jul 2024")
st.write("""
- Built 4+ projects including a Weather App, Stopwatch, Tic-Tac-Toe, and a responsive Landing Page using HTML, CSS, JavaScript.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- EDUCATION ---
st.markdown('<h2>Education</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Bachelor of Technology in Computer Science & Engineering")
st.write("**Medicaps University, Indore** | 2022 - 2026")
st.write("Current SGPA: **8.5/10.0**")
st.write("Relevant Coursework: `Data Structures`, `Algorithms`, `Machine Learning`, `Database Management Systems`, `Linear Algebra`.")
st.markdown('</div>', unsafe_allow_html=True)

# --- RESEARCH & CERTIFICATIONS ---
st.markdown('<h2>Research & Certifications</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("- **Research Paper (IJEART):** *Integrating Blockchain in 5G Technologies* (Feb 2024)")
st.write("- **Data Science Bootcamp (Udemy):** *Machine Learning and Data Analysis* (Jan 2025)")
st.write("- **Google Cybersecurity Certification:** *Cybersecurity Fundamentals* (Jun 2023)")
st.markdown('</div>', unsafe_allow_html=True)

# --- EXTRACURRICULAR ---
st.markdown('<h2>Extracurricular Activities</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
- **Treasurer at STIC:** Managed 50,000+ fund, handled event budgeting, organized finances.
- **Workshop Organizer:** Ran 3+ bootcamps/workshops with 200+ students, raised participation by 50%.
- **Content Co-Lead at E-Cell Medicaps:** Led content strategy for entrepreneurship awareness.
- **Content Creator:** Over 2 million engagement on Instagram.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACT SECTION ---
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
