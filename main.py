

import streamlit as st
from PIL import Image
import base64

#  PAGE CONFIG
st.set_page_config(page_title="Himani Dobriyal | Developer Portfolio", page_icon="💻", layout="wide")

# CUSTOM CSS 
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            color: #e0e0e0;
        }
        .main-title { font-size: 3em; color: #72FACA; font-weight: bold; }
        .subtitle { font-size: 1.3em; color: #B8B8FF; margin-bottom: 1rem; }
        .section-title { font-size: 2em; color: #FF6AC1; border-bottom: 2px solid #FF6AC1; padding-bottom: 0.3rem; margin-top: 2rem; }
        .card { background-color: #1a1a1a; padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(255, 255, 255, 0.05); margin-bottom: 1.5rem; }
        a { color: #72FACA; text-decoration: none; }
        ul { padding-left: 1.2rem; }
            .project-tech {
            margin-top: 0.5rem;
        }
        .tech-tag {
            display: inline-block;
            background-color: #333;
            color: #72FACA;
            padding: 0.2rem 0.5rem;
            margin: 0.2rem;
            border-radius: 5px;
            font-size: 0.85rem;
        }
        .card:hover {
            transform: scale(1.02);
            transition: all 0.3s ease;
            box-shadow: 0 0 12px rgba(114, 250, 202, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

#HEADER 
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("profile.png", width=220)
    except:
        st.warning("⚠️ Add a 'profile.jpg' image to the directory to show your profile photo.")

with col2:
    st.markdown("<div class='main-title'>Himani Dobriyal</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Full-Stack Developer | GIS Researcher | ISRO Intern</div>", unsafe_allow_html=True)
    st.markdown("""
        📍 Uttarakhand, India  
        ✉️ [himanidobriyal8@gmail.com](mailto:himanidobriyal8@gmail.com)  
        🔗 [LinkedIn](https://linkedin.com/in/himani-dobriyal) | [Website](https://himanidobriyal.streamlit.app)
    """)

# RESUME DOWNLOAD 
with open("Himani_resume.pdf", "rb") as f:
    resume_data = f.read()
    st.download_button(
        label="📄 Download My Resume",
        data=resume_data,
        file_name="Himani_Dobriyal_Resume.pdf",
        mime="application/pdf",
        help="Click to download Himani's resume"
    )

#  ABOUT 
st.markdown("<div class='section-title'>👩‍💻 About Me</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
I'm an Information Technology undergrad passionate about solving real-world problems through technology. From analyzing satellite imagery at ISRO to building full-stack platforms and clean UI web apps, I love building impactful products with scalable code and thoughtful design.
</div>
""", unsafe_allow_html=True)

# SKILLS 
st.markdown("<div class='section-title'>🛠️ Skills & Tools</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
<b>Languages:</b> C, C++, Python, JavaScript<br>
<b>Frontend:</b> HTML5, CSS3, ReactJS, Tailwind CSS, Vite<br>
<b>Backend:</b> NodeJS, MongoDB, REST APIs<br>
<b>Other Tools:</b> Google Earth Engine, Git, Oracle DB, VS Code<br>
<b>Soft Skills:</b> Team Collaboration, Communication, Leadership
</div>
""", unsafe_allow_html=True)

#EXPERIENCE
st.markdown("<div class='section-title'>💼 Experience</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
<b>🌍 Project Intern – IIRS–ISRO (May 2025 - July 2025)</b><br>
- Analyzed urban green space using Sentinel satellite imagery<br>
- Used Google Earth Engine for LULC classification and time-series analysis<br>
- Built an urban planning tool for visualizing geospatial data
</div>

<div class='card'>
<b>💻 Web Developer Intern – Codsoft (June 2024 - July 2024)</b><br>
- Developed responsive websites and personal portfolio pages<br>
- Focused on clean UI/UX and cross-device compatibility
</div>
""", unsafe_allow_html=True)

#PROJECTS
st.markdown("<div class='section-title'>🚀 Featured Projects</div>", unsafe_allow_html=True)

project_data = [
    {
        "title": "Urban Green Space Monitoring Tool",
        "description": "A GEE-powered dashboard to monitor changes in urban greenery using satellite data.",
        "image": "aai.png",
        "link": "https://github.com/himanidobriyal/geospatial_land_classification",
        "tech": ["GEE", "Python", "JavaScript"]
    },
    {
        "title": "Mentor-Mentee System",
        "description": "Full-stack academic management platform with login/auth, tracking, and communication.",
        "image": "mms.png",
        "link": "https://github.com/himanidobriyal/mentor_mentee_system",
        "tech": ["MongoDB", "NodeJS", "React"]
    }
]

cols = st.columns(2)

for idx, project in enumerate(project_data):
    with cols[idx % 2]:
        with st.container():
            st.image(project["image"], use_container_width=True)
            st.markdown(f"<h4 style='color:#72FACA;'>{project['title']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p>{project['description']}</p>", unsafe_allow_html=True)
            tech_html = ''.join([f"<span class='tech-tag'>{tech}</span>" for tech in project["tech"]])
            st.markdown(f"<div class='project-tech'>{tech_html}</div>", unsafe_allow_html=True)
            st.markdown(f"<a href='{project['link']}' target='_blank'> Visit on GitHub</a>", unsafe_allow_html=True)

#EDUCATION
st.markdown("<div class='section-title'>🎓 Education</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
<b>B.Tech in Information Technology</b><br>
Banasthali Vidyapith, Rajasthan (2022 – 2026)<br>
CGPA: 8.78<br>
<b>Relevant Courses:</b> Data Structures, Web Development, Remote Sensing & GIS
</div>
""", unsafe_allow_html=True)

# LEADERSHIP & EXTRAS 
st.markdown("<div class='section-title'>🌟 Leadership & Extras</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
<b>🌊 Core Organizer – Tech Fest (MAYUKH)</b><br>
Led and managed "Pirates of the Silicon Sea" fest — bridging tech innovation and Indian culture.<br><br>
<b>📢 Youth Parliament – 2nd Place</b><br>
Represented university and awarded for debating and leadership.<br><br>
<b>🌿 NSS Volunteer</b><br>
2 years of community service: plantation drives, donations, and awareness campaigns.
</div>
""", unsafe_allow_html=True)

# CONTACT FORM
st.markdown("<div class='section-title'>📬 Contact Me</div>", unsafe_allow_html=True)
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("✅ Thanks, your message has been sent!")

#FOOTER
st.markdown("""
<hr style='border-top: 1px solid #444; margin-top: 3rem;'>
<center>
Made with ❤️ by Himani Dobriyal | Built using Streamlit
</center>
""", unsafe_allow_html=True)
