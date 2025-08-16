import streamlit as st
import requests
import json
import base64
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="John Anderson - UI/UX Designer",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for exact Framer clone
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    .main {
        background: #1a1a1a;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .stApp {
        background: #1a1a1a;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Main Layout Container */
    .portfolio-container {
        display: flex;
        min-height: 100vh;
        background: #1a1a1a;
    }
    
    /* Fixed Left Sidebar */
    .sidebar {
        width: 350px;
        background: #1a1a1a;
        border-right: 1px solid #333;
        position: fixed;
        height: 100vh;
        overflow-y: auto;
        padding: 40px 30px;
        box-sizing: border-box;
    }
    
    /* Profile Card */
    .profile-card {
        background: #2a2a2a;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        border: 1px solid #333;
        margin-bottom: 30px;
    }
    
    .profile-avatar {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: #333;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin: 0 auto 20px;
        overflow: hidden;
    }
    
    .profile-avatar img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }
    
    .availability-badge {
        background: #10b981;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 20px;
    }
    
    .availability-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: white;
    }
    
    .profile-name {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .profile-title {
        font-size: 1.1rem;
        color: #999;
        margin-bottom: 25px;
        font-weight: 500;
    }
    
    /* Social Links */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 30px;
    }
    
    .social-icon {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background: #333;
        border: 1px solid #444;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .social-icon:hover {
        background: #444;
        transform: translateY(-2px);
    }
    
    /* Action Buttons */
    .action-buttons {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    
    .btn-download {
        background: #333;
        color: white;
        padding: 15px 25px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        border: 1px solid #444;
        cursor: pointer;
    }
    
    .btn-download:hover {
        background: #444;
        transform: translateY(-2px);
    }
    
    .btn-contact {
        background: #10b981;
        color: white;
        padding: 15px 25px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        border: none;
        cursor: pointer;
    }
    
    .btn-contact:hover {
        background: #059669;
        transform: translateY(-2px);
    }
    
    /* Main Content Area */
    .main-content {
        flex: 1;
        margin-left: 350px;
        padding: 40px;
        background: #1a1a1a;
        overflow-y: auto;
    }
    
    /* Hero Section */
    .hero-section {
        margin-bottom: 60px;
    }
    
    .hero-greeting {
        font-size: 1.2rem;
        color: #999;
        margin-bottom: 20px;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 15px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 2.5rem;
        color: #10b981;
        margin-bottom: 25px;
        font-weight: 700;
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: #999;
        line-height: 1.7;
        margin-bottom: 40px;
        max-width: 600px;
    }
    
    /* Stats Section */
    .stats-section {
        margin-bottom: 60px;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 25px;
    }
    
    .stat-card {
        background: #2a2a2a;
        border-radius: 16px;
        padding: 30px 20px;
        text-align: center;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 8px;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #999;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Section Styles */
    .section {
        margin-bottom: 80px;
    }
    
    .section-header {
        margin-bottom: 40px;
    }
    
    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .section-icon {
        font-size: 2rem;
        color: #10b981;
    }
    
    .section-subtitle {
        font-size: 1.1rem;
        color: #999;
        line-height: 1.6;
        max-width: 500px;
    }
    
    /* Experience Section */
    .experience-grid {
        display: grid;
        gap: 25px;
    }
    
    .experience-card {
        background: #2a2a2a;
        border-radius: 16px;
        padding: 30px;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .experience-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .experience-header {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    
    .company-icon {
        width: 60px;
        height: 60px;
        border-radius: 12px;
        background: #ff6b35;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    .experience-info h3 {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 5px 0;
    }
    
    .experience-info h4 {
        font-size: 1.1rem;
        color: #10b981;
        margin: 0 0 5px 0;
        font-weight: 600;
    }
    
    .experience-period {
        font-size: 0.9rem;
        color: #999;
        font-weight: 500;
    }
    
    .experience-description {
        font-size: 1rem;
        color: #999;
        line-height: 1.6;
    }
    
    /* Projects Section */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }
    
    .project-card {
        background: #2a2a2a;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    }
    
    .project-image {
        width: 100%;
        height: 200px;
        background: #333;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 3rem;
        position: relative;
    }
    
    .project-arrow {
        position: absolute;
        bottom: 15px;
        right: 15px;
        width: 35px;
        height: 35px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.2rem;
    }
    
    .project-content {
        padding: 25px;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .project-category {
        font-size: 0.9rem;
        color: #10b981;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    .project-pages {
        font-size: 0.9rem;
        color: #999;
        margin-bottom: 20px;
    }
    
    .project-actions {
        display: flex;
        gap: 10px;
    }
    
    .btn-view {
        background: #333;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 600;
        transition: all 0.3s ease;
        flex: 1;
        text-align: center;
        border: 1px solid #444;
    }
    
    .btn-view:hover {
        background: #444;
    }
    
    /* Skills Section */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
    }
    
    .skill-category {
        background: #2a2a2a;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .skill-category:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .skill-icon {
        font-size: 2.5rem;
        margin-bottom: 20px;
    }
    
    .skill-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 15px;
    }
    
    .skill-description {
        font-size: 0.95rem;
        color: #999;
        line-height: 1.6;
    }
    
    /* Contact Section */
    .contact-section {
        background: #2a2a2a;
        border-radius: 20px;
        padding: 40px;
        border: 1px solid #333;
    }
    
    .contact-header {
        text-align: center;
        margin-bottom: 40px;
    }
    
    .contact-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .contact-subtitle {
        font-size: 1.1rem;
        color: #999;
    }
    
    .contact-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
        align-items: start;
    }
    
    .contact-info {
        display: grid;
        gap: 20px;
    }
    
    .contact-item {
        background: #333;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #444;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .contact-icon {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background: #10b981;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.2rem;
    }
    
    .contact-details h4 {
        font-size: 0.9rem;
        color: #999;
        margin-bottom: 5px;
        font-weight: 500;
    }
    
    .contact-details p {
        font-size: 1rem;
        color: #ffffff;
        font-weight: 600;
        margin: 0;
    }
    
    .contact-form {
        background: #333;
        border-radius: 12px;
        padding: 30px;
        border: 1px solid #444;
    }
    
    .form-group {
        margin-bottom: 20px;
    }
    
    .form-group label {
        display: block;
        font-size: 0.9rem;
        color: #999;
        margin-bottom: 8px;
        font-weight: 500;
    }
    
    .form-input {
        width: 100%;
        padding: 12px 16px;
        border: 1px solid #444;
        border-radius: 8px;
        font-size: 1rem;
        background: #2a2a2a;
        color: #ffffff;
        transition: all 0.3s ease;
    }
    
    .form-input:focus {
        outline: none;
        border-color: #10b981;
        background: #333;
    }
    
    .form-textarea {
        width: 100%;
        padding: 12px 16px;
        border: 1px solid #444;
        border-radius: 8px;
        font-size: 1rem;
        background: #2a2a2a;
        color: #ffffff;
        min-height: 120px;
        resize: vertical;
        transition: all 0.3s ease;
    }
    
    .form-textarea:focus {
        outline: none;
        border-color: #10b981;
        background: #333;
    }
    
    .btn-send-message {
        background: #10b981;
        color: white;
        padding: 15px 30px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        display: inline-block;
        border: none;
        cursor: pointer;
        width: 100%;
    }
    
    .btn-send-message:hover {
        background: #059669;
        transform: translateY(-2px);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 40px 0;
        border-top: 1px solid #333;
        margin-top: 60px;
    }
    
    .footer-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .footer-text {
        font-size: 0.9rem;
        color: #999;
    }
    
    .footer-signature {
        font-size: 1.1rem;
        color: #ffffff;
        font-weight: 600;
        font-style: italic;
    }
    
    .footer-badges {
        display: flex;
        gap: 10px;
    }
    
    .footer-badge {
        background: #333;
        color: #999;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        border: 1px solid #444;
    }
    
    /* Responsive Design */
    @media (max-width: 1200px) {
        .sidebar {
            width: 300px;
        }
        
        .main-content {
            margin-left: 300px;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .projects-grid {
            grid-template-columns: 1fr;
        }
        
        .skills-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .contact-content {
            grid-template-columns: 1fr;
            gap: 30px;
        }
    }
    
    @media (max-width: 768px) {
        .portfolio-container {
            flex-direction: column;
        }
        
        .sidebar {
            width: 100%;
            position: relative;
            height: auto;
            padding: 30px 20px;
        }
        
        .main-content {
            margin-left: 0;
            padding: 30px 20px;
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 2rem;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
        
        .skills-grid {
            grid-template-columns: 1fr;
        }
        
        .footer-content {
            flex-direction: column;
            gap: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Portfolio data - Exact copy of John Anderson's content
portfolio_data = {
    'personal': {
        'name': "John Anderson",
        'title': "UI/UX Designer",
        'description': "I specialize in creating clean, user-friendly digital experiences by blending creativity with functionality. With a strong background in interactive design, I focus on crafting designs that not only look great but also provide smooth and engaging user interactions, helping ideas come to life seamlessly.",
        'email': "andrew@website.com",
        'phone': "+(02) 4057 2930",
        'address': "Beverly Hills, Los Angeles, California, USA"
    },
    'stats': [
        {'number': "24", 'label': "Completed Projects"},
        {'number': "1+", 'label': "Years of Experience"},
        {'number': "26", 'label': "Happy Clients"},
        {'number': "1+", 'label': "Awards Received"}
    ],
    'experience': [
        {
            'title': 'Framer & UI/UX Designer',
            'company': 'Circlum Tech',
            'period': '2023 - Present',
            'description': 'Designing interactive prototypes with Framer, focusing on seamless user experiences and scalable solutions through user feedback and collaboration.'
        },
        {
            'title': 'UI/UX Designer',
            'company': 'CoreOS',
            'period': '2021 - 2023',
            'description': 'Created intuitive web and mobile designs, conducted user research, and collaborated with developers to ensure consistent and functional design delivery.'
        },
        {
            'title': 'Graphics Designer',
            'company': 'Pixel Square',
            'period': '2020 - 2021',
            'description': 'Designed marketing assets, UI components, and brand visuals, enhancing digital campaigns and overall visual identity through creative collaboration.'
        }
    ],
    'projects': [
        {
            'title': 'HelloBot',
            'category': 'SaaS & Startup',
            'pages': '8 Pages',
            'icon': '🤖',
            'github': '#',
            'demo': 'https://hellobot.framer.website'
        },
        {
            'title': 'Flexisoft',
            'category': 'SaaS & Startup',
            'pages': '6 Pages',
            'icon': '💻',
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'Excludia',
            'category': 'Digital Agency',
            'pages': '8 Pages',
            'icon': '🎨',
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'CryptoraHub',
            'category': 'Crypto & Web3',
            'pages': '7 Pages',
            'icon': '₿',
            'github': '#',
            'demo': '#'
        }
    ],
    'skills': [
        {
            'title': 'Figma',
            'icon': '🎨',
            'description': 'Design Tool'
        },
        {
            'title': 'Framer',
            'icon': '⚡',
            'description': 'No Code Development'
        },
        {
            'title': 'Lemon Squeezy',
            'icon': '🍋',
            'description': 'Payment'
        },
        {
            'title': 'Notion',
            'icon': '📝',
            'description': 'Notion'
        },
        {
            'title': 'Illustrators',
            'icon': '✏️',
            'description': 'Illustrators'
        },
        {
            'title': 'SS Icons',
            'icon': '🔗',
            'description': 'Icon Library'
        }
    ]
}

def create_sidebar():
    st.markdown(f"""
    <div class="sidebar">
        <div class="profile-card">
            <div class="profile-avatar">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face" alt="John Anderson">
            </div>
            <div class="availability-badge">
                <div class="availability-dot"></div>
                Available for work
            </div>
            <h1 class="profile-name">{portfolio_data['personal']['name']}</h1>
            <p class="profile-title">{portfolio_data['personal']['title']}</p>
            
            <div class="social-links">
                <a href="#" class="social-icon">📷</a>
                <a href="#" class="social-icon">🐦</a>
                <a href="#" class="social-icon">▶️</a>
                <a href="#" class="social-icon">🏀</a>
                <a href="#" class="social-icon">Bē</a>
            </div>
            
            <div class="action-buttons">
                <a href="#" class="btn-download">
                    📥 Download CV
                </a>
                <a href="#contact" class="btn-contact">
                    ✉️ Contact Me
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_main_content():
    st.markdown("""
    <div class="main-content">
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-greeting">
            👋 Say Hello
        </div>
        <h1 class="hero-title">I'm {portfolio_data['personal']['name']},</h1>
        <h2 class="hero-subtitle">Based in Los Angeles, CA.</h2>
        <p class="hero-description">{portfolio_data['personal']['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="stats-section">
        <div class="stats-grid">
    """, unsafe_allow_html=True)
    
    for stat in portfolio_data['stats']:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{stat['number']}+</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Experience Section
    st.markdown("""
    <div class="section">
        <div class="section-header">
            <h2 class="section-title">
                <span class="section-icon">💼</span>
                Experience
            </h2>
        </div>
        <div class="experience-grid">
    """, unsafe_allow_html=True)
    
    for exp in portfolio_data['experience']:
        company_initials = ''.join([word[0] for word in exp['company'].split()])
        st.markdown(f"""
        <div class="experience-card">
            <div class="experience-header">
                <div class="company-icon">{company_initials}</div>
                <div class="experience-info">
                    <h3>{exp['title']}</h3>
                    <h4>{exp['company']}</h4>
                    <div class="experience-period">{exp['period']}</div>
                </div>
            </div>
            <p class="experience-description">{exp['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Projects Section
    st.markdown("""
    <div class="section">
        <div class="section-header">
            <h2 class="section-title">
                <span class="section-icon">🚀</span>
                Projects
            </h2>
        </div>
        <div class="projects-grid">
    """, unsafe_allow_html=True)
    
    for project in portfolio_data['projects']:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-image">
                {project['icon']}
                <div class="project-arrow">↗</div>
            </div>
            <div class="project-content">
                <h3 class="project-title">{project['title']}</h3>
                <div class="project-category">{project['category']}</div>
                <div class="project-pages">{project['pages']}</div>
                <div class="project-actions">
                    <a href="{project['github']}" target="_blank" class="btn-view">View</a>
                    <a href="{project['demo']}" target="_blank" class="btn-view">Demo</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Skills Section
    st.markdown("""
    <div class="section">
        <div class="section-header">
            <h2 class="section-title">
                <span class="section-icon">🎯</span>
                Stakes
            </h2>
        </div>
        <div class="skills-grid">
    """, unsafe_allow_html=True)
    
    for skill in portfolio_data['skills']:
        st.markdown(f"""
        <div class="skill-category">
            <div class="skill-icon">{skill['icon']}</div>
            <h3 class="skill-title">{skill['title']}</h3>
            <p class="skill-description">{skill['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Contact Section
    st.markdown(f"""
    <div class="section" id="contact">
        <div class="contact-section">
            <div class="contact-header">
                <h2 class="contact-title">Contact</h2>
                <p class="contact-subtitle">Let's Get in Touch!</p>
            </div>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon">📞</div>
                        <div class="contact-details">
                            <h4>Contact No</h4>
                            <p>{portfolio_data['personal']['phone']}</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">📧</div>
                        <div class="contact-details">
                            <h4>Email</h4>
                            <p>{portfolio_data['personal']['email']}</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">📍</div>
                        <div class="contact-details">
                            <h4>Address</h4>
                            <p>{portfolio_data['personal']['address']}</p>
                        </div>
                    </div>
                </div>
                <div class="contact-form">
                    <div class="form-group">
                        <label>Full Name</label>
                        <input type="text" class="form-input" placeholder="Enter your full name">
                    </div>
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" class="form-input" placeholder="Enter your email">
                    </div>
                    <div class="form-group">
                        <label>Phone Number</label>
                        <input type="tel" class="form-input" placeholder="Enter your phone number">
                    </div>
                    <div class="form-group">
                        <label>Message</label>
                        <textarea class="form-textarea" placeholder="Enter your message"></textarea>
                    </div>
                    <button class="btn-send-message">Send Message</button>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div class="footer-text">Built in Framer</div>
            <div class="footer-signature">John Anderson</div>
            <div class="footer-badges">
                <div class="footer-badge">Create</div>
                <div class="footer-badge">Made in Framer</div>
            </div>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Main Layout Container
    st.markdown("""
    <div class="portfolio-container">
    """, unsafe_allow_html=True)
    
    # Fixed Left Sidebar
    create_sidebar()
    
    # Scrollable Main Content
    create_main_content()
    
    # Close container
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
