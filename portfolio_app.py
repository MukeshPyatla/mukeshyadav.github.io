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
    page_title="Mukesh Yadav - MLOps & DevOps Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Framer-style design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    .main {
        background: #ffffff;
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: #ffffff;
    }
    
    /* Header Section */
    .header-section {
        background: #ffffff;
        padding: 40px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    
    .header-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .profile-info {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .profile-avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2rem;
        font-weight: 700;
    }
    
    .profile-details h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 0 0 8px 0;
    }
    
    .profile-details p {
        font-size: 1.1rem;
        color: #666;
        margin: 0;
        font-weight: 500;
    }
    
    .availability-badge {
        background: #10b981;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    .header-actions {
        display: flex;
        gap: 15px;
        align-items: center;
    }
    
    .btn-download {
        background: #1a1a1a;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .btn-download:hover {
        background: #333;
        transform: translateY(-2px);
    }
    
    .btn-contact {
        background: #f8f9fa;
        color: #1a1a1a;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        border: 1px solid #e9ecef;
        transition: all 0.3s ease;
    }
    
    .btn-contact:hover {
        background: #e9ecef;
        transform: translateY(-2px);
    }
    
    /* Hero Section */
    .hero-section {
        background: #ffffff;
        padding: 80px 0;
        text-align: center;
    }
    
    .hero-content {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .hero-greeting {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: #1a1a1a;
        margin-bottom: 20px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 2rem;
        color: #666;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    .hero-description {
        font-size: 1.3rem;
        color: #666;
        line-height: 1.6;
        margin-bottom: 50px;
    }
    
    /* Stats Section */
    .stats-section {
        background: #f8f9fa;
        padding: 60px 0;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 40px;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .stat-card {
        text-align: center;
        background: white;
        padding: 40px 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        color: #1a1a1a;
        margin-bottom: 10px;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #666;
        font-weight: 500;
    }
    
    /* Section Styles */
    .section {
        padding: 80px 0;
        background: #ffffff;
    }
    
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 60px;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 20px;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #666;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Experience Section */
    .experience-grid {
        display: grid;
        gap: 30px;
    }
    
    .experience-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 30px;
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
    }
    
    .experience-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    .experience-info h3 {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 0 0 5px 0;
    }
    
    .experience-info h4 {
        font-size: 1.2rem;
        color: #666;
        margin: 0 0 5px 0;
        font-weight: 600;
    }
    
    .experience-period {
        font-size: 1rem;
        color: #999;
        font-weight: 500;
    }
    
    .experience-description {
        font-size: 1.1rem;
        color: #666;
        line-height: 1.6;
    }
    
    /* Projects Section */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 30px;
    }
    
    .project-card {
        background: #f8f9fa;
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
    }
    
    .project-image {
        width: 100%;
        height: 200px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 3rem;
    }
    
    .project-content {
        padding: 25px;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 10px;
    }
    
    .project-category {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 15px;
        font-weight: 500;
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
        background: #1a1a1a;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .btn-view:hover {
        background: #333;
    }
    
    /* Skills Section */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 30px;
    }
    
    .skill-category {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
    }
    
    .skill-category:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .skill-icon {
        font-size: 3rem;
        margin-bottom: 20px;
    }
    
    .skill-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 15px;
    }
    
    .skill-description {
        font-size: 1rem;
        color: #666;
        line-height: 1.6;
    }
    
    /* Contact Section */
    .contact-section {
        background: #f8f9fa;
        padding: 80px 0;
    }
    
    .contact-content {
        text-align: center;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .contact-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 20px;
    }
    
    .contact-info {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
        margin: 40px 0;
    }
    
    .contact-item {
        text-align: center;
    }
    
    .contact-icon {
        font-size: 2rem;
        margin-bottom: 15px;
        color: #667eea;
    }
    
    .contact-label {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 5px;
        font-weight: 500;
    }
    
    .contact-value {
        font-size: 1.1rem;
        color: #1a1a1a;
        font-weight: 600;
    }
    
    .btn-send-message {
        background: #1a1a1a;
        color: white;
        padding: 15px 30px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        display: inline-block;
        margin-top: 30px;
    }
    
    .btn-send-message:hover {
        background: #333;
        transform: translateY(-2px);
    }
    
    /* Footer */
    .footer {
        background: #1a1a1a;
        color: white;
        padding: 40px 0;
        text-align: center;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .footer-text {
        font-size: 1rem;
        color: #999;
        margin-bottom: 10px;
    }
    
    .footer-signature {
        font-size: 1.1rem;
        color: white;
        font-weight: 600;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .header-content {
            flex-direction: column;
            gap: 20px;
            text-align: center;
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
        
        .projects-grid {
            grid-template-columns: 1fr;
        }
        
        .skills-grid {
            grid-template-columns: 1fr;
        }
        
        .contact-info {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Portfolio data
portfolio_data = {
    'personal': {
        'name': "Mukesh Yadav",
        'title': "MLOps & DevOps Engineer",
        'location': "Based in United States",
        'description': "I specialize in building scalable, production-ready AI/ML systems and automating complex DevOps workflows. With expertise in cloud infrastructure, CI/CD pipelines, and MLOps best practices, I help organizations deploy intelligent solutions that drive business value.",
        'email': "mukeshyadavp91@gmail.com",
        'linkedin': "linkedin.com/in/mukesh-mlops",
        'github': "github.com/MukeshPyatla",
        'phone': "+1 (555) 123-4567",
        'address': "United States"
    },
    'stats': [
        {'number': "6", 'label': "Live Projects"},
        {'number': "47", 'label': "Technical Skills"},
        {'number': "3+", 'label': "Years Experience"},
        {'number': "100%", 'label': "Success Rate"}
    ],
    'experience': [
        {
            'title': 'MLOps Engineer',
            'company': 'Aidoc',
            'period': '2023 - Present',
            'description': 'Engineered monitoring systems with Prometheus and Grafana, reducing MTTR by 70%. Deployed CI/CD pipelines for GenAI applications, decreasing deployment time by 80%. Automated cloud infrastructure with Terraform, reducing costs by 20%.'
        },
        {
            'title': 'Graduate Research Assistant',
            'company': 'Missouri University of Science and Technology',
            'period': '2023',
            'description': 'Managed Azure cloud resources for ML experiments supporting 10 researchers. Implemented DVC for reproducible ML experiments. Designed CI/CD pipelines with Prefect, reducing setup time by 90%.'
        },
        {
            'title': 'Junior Systems Administrator | DevOps Engineer',
            'company': 'PineLabs',
            'period': '2021 - 2022',
            'description': 'Developed CI/CD pipeline using Jenkins and Docker, reducing deployment errors by 30%. Automated system administration tasks, saving 5 hours/week. Maintained Linux servers achieving 99.9% uptime.'
        }
    ],
    'projects': [
        {
            'title': 'DeFi Fraud Detection',
            'category': 'MLOps & AI',
            'pages': '8 Pages',
            'icon': '🛡️',
            'github': 'https://github.com/MukeshPyatla/DeFi_Fraud-Detection_MLOps_Pipeline',
            'demo': 'https://defifraud-detectionmlopspipeline.streamlit.app/'
        },
        {
            'title': 'Guardian AI Auditor',
            'category': 'AI & Security',
            'pages': '6 Pages',
            'icon': '🤖',
            'github': 'https://github.com/MukeshPyatla/guardian-ai-auditor',
            'demo': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/'
        },
        {
            'title': 'MLOps Q&A System',
            'category': 'LLM & RAG',
            'pages': '8 Pages',
            'icon': '💬',
            'github': 'https://github.com/MukeshPyatla/mlops-qa-system',
            'demo': 'https://mlops-app-system.streamlit.app/'
        },
        {
            'title': 'Azure Anomaly Detector',
            'category': 'Cloud & ML',
            'pages': '7 Pages',
            'icon': '📡',
            'github': 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector',
            'demo': 'https://azure-mlops-anomaly-detector.streamlit.app/'
        },
        {
            'title': 'Secure Churn Prediction',
            'category': 'Data Science',
            'pages': '6 Pages',
            'icon': '👤',
            'github': 'https://github.com/MukeshPyatla/MLOPS-Secure-Churn',
            'demo': 'https://mlops-secure-churn.streamlit.app/'
        },
        {
            'title': 'Demand Forecasting',
            'category': 'MLOps & Analytics',
            'pages': '5 Pages',
            'icon': '📈',
            'github': 'https://github.com/MukeshPyatla/MLOPS-Demand-Forecasting',
            'demo': 'https://mlops-demand-forecasting.streamlit.app/'
        }
    ],
    'skills': [
        {
            'title': 'Cloud & DevOps',
            'icon': '☁️',
            'description': 'AWS, Azure, Terraform, Docker, Kubernetes, CI/CD pipelines, Infrastructure as Code'
        },
        {
            'title': 'AI/ML Frameworks',
            'icon': '🧠',
            'description': 'PyTorch, TensorFlow, LangChain, FastAPI, MLflow, BentoML, MLOps pipelines'
        },
        {
            'title': 'Programming',
            'icon': '💻',
            'description': 'Python, Go, C++, Bash, SQL, JavaScript, React, Node.js'
        },
        {
            'title': 'Data & Monitoring',
            'icon': '📊',
            'description': 'Pandas, Spark, Prometheus, Grafana, ELK Stack, Data validation & monitoring'
        }
    ]
}

def create_header():
    st.markdown(f"""
    <div class="header-section">
        <div class="header-content">
            <div class="profile-info">
                <div class="profile-avatar">MY</div>
                <div class="profile-details">
                    <h1>{portfolio_data['personal']['name']}</h1>
                    <p>{portfolio_data['personal']['title']}</p>
                </div>
            </div>
            <div class="header-actions">
                <span class="availability-badge">Available for work</span>
                <a href="#" class="btn-download">Download CV</a>
                <a href="#contact" class="btn-contact">Contact Me</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_hero():
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-greeting">👋 Say Hello</div>
            <h1 class="hero-title">I'm {portfolio_data['personal']['name']},</h1>
            <h2 class="hero-subtitle">{portfolio_data['personal']['location']}</h2>
            <p class="hero-description">{portfolio_data['personal']['description']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_stats():
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

def create_experience():
    st.markdown("""
    <div class="section">
        <div class="section-container">
            <div class="section-header">
                <h2 class="section-title">Experience</h2>
                <p class="section-subtitle">My professional journey in MLOps and DevOps engineering</p>
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
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

def create_projects():
    st.markdown("""
    <div class="section">
        <div class="section-container">
            <div class="section-header">
                <h2 class="section-title">Projects</h2>
                <p class="section-subtitle">Featured MLOps and DevOps projects showcasing my expertise</p>
            </div>
            <div class="projects-grid">
    """, unsafe_allow_html=True)
    
    for project in portfolio_data['projects']:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-image">{project['icon']}</div>
            <div class="project-content">
                <h3 class="project-title">{project['title']}</h3>
                <div class="project-category">{project['category']}</div>
                <div class="project-pages">{project['pages']}</div>
                <div class="project-actions">
                    <a href="{project['github']}" target="_blank" class="btn-view">GitHub</a>
                    <a href="{project['demo']}" target="_blank" class="btn-view">Live Demo</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

def create_skills():
    st.markdown("""
    <div class="section">
        <div class="section-container">
            <div class="section-header">
                <h2 class="section-title">Skills</h2>
                <p class="section-subtitle">Technical expertise across the MLOps and DevOps ecosystem</p>
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
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)

def create_contact():
    st.markdown(f"""
    <div class="contact-section" id="contact">
        <div class="section-container">
            <div class="contact-content">
                <h2 class="contact-title">Let's Get in Touch!</h2>
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon">📞</div>
                        <div class="contact-label">Contact No</div>
                        <div class="contact-value">{portfolio_data['personal']['phone']}</div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">📧</div>
                        <div class="contact-label">Email</div>
                        <div class="contact-value">{portfolio_data['personal']['email']}</div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">📍</div>
                        <div class="contact-label">Address</div>
                        <div class="contact-value">{portfolio_data['personal']['address']}</div>
                    </div>
                </div>
                <a href="mailto:{portfolio_data['personal']['email']}" class="btn-send-message">Send Message</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <p class="footer-text">Built with ❤️ using Streamlit</p>
            <p class="footer-signature">Mukesh Yadav</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Header Section
    create_header()
    
    # Hero Section
    create_hero()
    
    # Stats Section
    create_stats()
    
    # Experience Section
    create_experience()
    
    # Projects Section
    create_projects()
    
    # Skills Section
    create_skills()
    
    # Contact Section
    create_contact()
    
    # Footer
    create_footer()

if __name__ == "__main__":
    main()
