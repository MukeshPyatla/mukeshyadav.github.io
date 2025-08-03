import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Mukesh Yadav - MLOps & DevOps Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern minimal styling and responsiveness
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');

    html, body, .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    .centered-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 0 15px;
    }

    .social-icons-top {
        text-align: center;
        margin-top: 20px;
    }

    .social-icon-link {
        font-size: 2rem;
        color: #e5e7eb;
        margin: 0 15px;
        transition: color 0.3s ease, transform 0.3s ease;
    }

    .social-icon-link:hover {
        color: #63b3ed; /* Light contrast blue */
        transform: translateY(-5px);
    }
    
    .hero-section {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.05), rgba(168, 85, 247, 0.05));
        border-radius: 24px;
        padding: 60px 40px;
        margin: 40px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
        animation: fadeIn 1s ease-out;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.5;
    }
    
    .section-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #e5e7eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #9CA3AF;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 400;
    }
    
    .category-card, .project-card, .dashboard-card, .experience-card, .contact-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 32px;
        margin: 24px 0;
        backdrop-filter: blur(20px);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        text-align: center;
    }

    .category-card:hover, .project-card:hover, .dashboard-card:hover, .experience-card:hover, .contact-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: #63b3ed; /* Light contrast blue */
        box-shadow: 0 20px 40px -12px rgba(99, 102, 241, 0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
        border: 1px solid #63b3ed; /* Light contrast blue */
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin: 12px;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px -10px rgba(99, 102, 241, 0.3);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #63b3ed, #9f7aea); /* Light contrast blue gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 8px;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #9CA3AF;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .status-live {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #10B981;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.6);
        margin-right: 8px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.1); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .tech-tag {
        background: #63b3ed; /* Light blue background as requested */
        color: #1a1a1a; /* Black text color for high contrast */
        font-size: 0.75rem;
        font-weight: 500;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 4px;
        display: inline-block;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    .timeline-item {
        border-left: 4px solid #63b3ed; /* Light contrast blue */
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #63b3ed, #9f7aea); /* Light contrast blue gradient */
        color: #1a1a1a; /* Black text color for high contrast */
        border: none;
        padding: 14px 28px;
        border-radius: 12px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        font-size: 0.95rem;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.4);
    }
    
    .btn-secondary {
        background: rgba(255, 255, 255, 0.05);
        color: #D1D5DB;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 14px 28px;
        border-radius: 12px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        font-size: 0.95rem;
    }
    
    .btn-secondary:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: #63b3ed; /* Light contrast blue */
        color: white;
        transform: translateY(-2px);
    }
    
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #63b3ed, transparent); /* Light contrast blue */
        margin: 80px 0;
        border-radius: 1px;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 12px;
        padding: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 8px;
        color: white;
        font-weight: 500;
        padding: 10px 16px;
        margin: 2px;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(99, 102, 241, 0.2);
        border-color: #63b3ed; /* Light contrast blue */
        color: #1a1a1a; /* Black text color on active tab */
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(99, 102, 241, 0.15);
        border-color: #63b3ed; /* Light contrast blue */
    }

    .stTabs [data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] p {
        color: white;
    }
    
    .devops-visual {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        border: 1px solid rgba(99, 102, 241, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .devops-visual::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100"><defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(99,102,241,0.1)" stroke-width="0.5"/></pattern></defs><rect width="200" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    .skill-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 12px;
        margin-top: 20px;
    }
    
    .skill-item {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .skill-item:hover {
        background: rgba(99, 102, 241, 0.1);
        border-color: #63b3ed; /* Light contrast blue */
        transform: translateY(-2px);
    }

    .project-card-grid, .dashboard-card-grid, .experience-card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin-top: 30px;
    }

    /* Responsive Design with Media Queries */
    @media (max-width: 1024px) {
        .section-title { font-size: 2.5rem; }
        .hero-section { padding: 40px 20px; }
        .metric-card { padding: 16px; margin: 8px; }
        .metric-value { font-size: 2rem; }
    }

    @media (max-width: 768px) {
        .section-title { font-size: 2rem; margin-bottom: 20px; }
        .hero-section { padding: 30px 15px; margin: 20px 0; }
        .hero-section > div > h2 { font-size: 1.8rem; }
        .hero-section > div > h3 { font-size: 1.2rem; }
        .hero-section > div > p { font-size: 1rem; }
        .metric-card { padding: 12px; margin: 4px; }
        .metric-value { font-size: 1.8rem; }
        .st-emotion-cache-1r650jc { gap: 10px; } /* Adjust column gap in Streamlit */
        .category-card, .project-card, .dashboard-card, .experience-card, .contact-card { padding: 20px; }
        .project-card-grid, .dashboard-card-grid, .experience-card-grid {
            grid-template-columns: 1fr;
        }
        .skill-grid {
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        }
    }

    @media (max-width: 480px) {
        .section-title { font-size: 1.8rem; }
        .hero-section > div > h2 { font-size: 1.5rem; }
        .hero-section > div > h3 { font-size: 1rem; }
        .hero-section > div > p { font-size: 0.9rem; }
        .hero-section > div > div { flex-direction: column; gap: 10px; }
        .metric-value { font-size: 1.5rem; }
        .metric-label { font-size: 0.75rem; }
        .skill-grid { grid-template-columns: 1fr; }
        .contact-card-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Social media links
SOCIAL_LINKS = {
    "LinkedIn": "https://linkedin.com/in/mukesh-mlops",
    "GitHub": "https://github.com/MukeshPyatla",
    "Email": "mailto:mukeshyadavp91@gmail.com"
}

# Skills data
skills_data = {
    'Cloud & DevOps': {
        'icon': '<i class="fa-solid fa-cloud"></i>',
        'color': '#63b3ed', # Light contrast blue
        'skills': ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD'],
        'count': 6
    },
    'AI/ML Frameworks': {
        'icon': '<i class="fa-solid fa-brain"></i>',
        'color': '#F59E0B',
        'skills': ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML'],
        'count': 6
    },
    'Programming Languages': {
        'icon': '<i class="fa-solid fa-code"></i>',
        'color': '#10B981',
        'skills': ['Python', 'Go', 'C++', 'Bash', 'SQL'],
        'count': 5
    },
    'Data & Databases': {
        'icon': '<i class="fa-solid fa-database"></i>',
        'color': '#9f7aea', # Light contrast purple
        'skills': ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant'],
        'count': 5
    },
    'Monitoring & Observability': {
        'icon': '<i class="fa-solid fa-chart-line"></i>',
        'color': '#EF4444',
        'skills': ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B'],
        'count': 5
    },
    'CI/CD Tools': {
        'icon': '<i class="fa-solid fa-gear"></i>',
        'color': '#F59E0B',
        'skills': ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions'],
        'count': 5
    },
    'AI/ML Concepts': {
        'icon': '<i class="fa-solid fa-robot"></i>',
        'color': '#63b3ed', # Light contrast blue
        'skills': ['MLOps', 'GenAI', 'RAG', 'Federated Learning', 'Homomorphic Encryption', 'NLP'],
        'count': 6
    },
    'Blockchain': {
        'icon': '<i class="fa-solid fa-link"></i>',
        'color': '#10B981',
        'skills': ['Ethereum', 'Solidity', 'Blockchain'],
        'count': 3
    },
    'Operating Systems': {
        'icon': '<i class="fa-solid fa-computer"></i>',
        'color': '#6B7280',
        'skills': ['Linux', 'Windows'],
        'count': 2
    },
    'Networking': {
        'icon': '<i class="fa-solid fa-globe"></i>',
        'color': '#63b3ed', # Light contrast blue
        'skills': ['VPC/VNet', 'DNS', 'Load Balancers', 'Security Groups'],
        'count': 4
    }
}

# Projects data
projects_data = [
    {
        'title': 'DeFi Fraud Detection',
        'description': 'Comprehensive MLOps pipeline for detecting fraud in Decentralized Finance transactions with private-by-design approach and modern Streamlit dashboard.',
        'status': 'LIVE',
        'tech': ['Python', 'Streamlit', 'MLOps'],
        'github': 'https://github.com/MukeshPyatla/DeFi_Fraud-Detection_MLOps_Pipeline',
        'demo': 'https://defifraud-detectionmlopspipeline.streamlit.app/',
        'icon': '<i class="fa-solid fa-shield-halved"></i>'
    },
    {
        'title': 'Guardian AI Auditor',
        'description': 'Zero-trust multi-modal compliance & risk auditor with privacy-preserving MLOps pipeline using Federated Learning and Homomorphic Encryption.',
        'status': 'LIVE',
        'tech': ['Federated Learning', 'Homomorphic Encryption', 'Blockchain'],
        'github': 'https://github.com/MukeshPyatla/guardian-ai-auditor',
        'demo': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
        'icon': '<i class="fa-solid fa-robot"></i>'
    },
    {
        'title': 'MLOps Q&A System',
        'description': 'LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo with real-time updates.',
        'status': 'LIVE',
        'tech': ['LLM', 'RAG', 'Vector DB'],
        'github': 'https://github.com/MukeshPyatla/mlops-qa-system',
        'demo': 'https://mlops-app-system.streamlit.app/',
        'icon': '<i class="fa-solid fa-comments"></i>'
    },
    {
        'title': 'Azure Anomaly Detector',
        'description': 'End-to-End MLOps pipeline for anomaly detection on Azure with real-time monitoring and alerting system.',
        'status': 'LIVE',
        'tech': ['Azure', 'MLOps', 'Python'],
        'github': 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector',
        'demo': 'https://azure-mlops-anomaly-detector.streamlit.app/',
        'icon': '<i class="fa-solid fa-satellite-dish"></i>'
    },
    {
        'title': 'Secure Churn Prediction',
        'description': 'Privacy-preserving customer churn prediction with PII masking and SHAP explainability in Azure Databricks.',
        'status': 'LIVE',
        'tech': ['Azure Databricks', 'SHAP', 'Data Security'],
        'github': 'https://github.com/MukeshPyatla/MLOPS-Secure-Churn',
        'demo': 'https://mlops-secure-churn.streamlit.app/',
        'icon': '<i class="fa-solid fa-user-secret"></i>'
    },
    {
        'title': 'Demand Forecasting',
        'description': 'Scalable demand forecasting system with integrated MLOps for continuous training and monitoring.',
        'status': 'LIVE',
        'tech': ['Python', 'Forecasting', 'MLOps'],
        'github': 'https://github.com/MukeshPyatla/MLOPS-Demand-Forecasting',
        'demo': 'https://mlops-demand-forecasting.streamlit.app/',
        'icon': '<i class="fa-solid fa-chart-simple"></i>'
    }
]

# Experience data
experience_data = [
    {
        'title': 'MLOps Engineer',
        'company': 'Aidoc',
        'period': 'Oct 2023 - Present',
        'achievements': [
            'Engineered monitoring system with Prometheus and Grafana, reducing MTTR by 70%',
            'Deployed CI/CD pipeline for GenAI applications, decreasing deployment time by 80%',
            'Automated cloud infrastructure with Terraform, reducing costs by 20%',
            'Integrated private blockchain for immutable MLOps audit trail'
        ]
    },
    {
        'title': 'Graduate Research Assistant',
        'company': 'Missouri University of Science and Technology',
        'period': 'Apr 2023 - Sep 2023',
        'achievements': [
            'Managed Azure cloud resources for ML experiments supporting 10 researchers',
            'Implemented DVC for reproducible ML experiments',
            'Designed CI/CD pipelines with Prefect, reducing setup time by 90%',
            'Provided technical mentorship to junior researchers'
        ]
    },
    {
        'title': 'Junior Systems Administrator | DevOps Engineer',
        'company': 'PineLabs',
        'period': 'Jun 2021 - Dec 2022',
        'achievements': [
            'Developed CI/CD pipeline using Jenkins and Docker, reducing deployment errors by 30%',
            'Automated system administration tasks, saving 5 hours/week',
            'Maintained Linux servers achieving 99.9% uptime',
            'Implemented backup routines preventing data loss during system failures'
        ]
    }
]

# Dashboard metrics data
dashboard_metrics = {
    'DeFi Fraud Detection': {
        'accuracy': '99.2%',
        'transactions': '1.2K',
        'response': '45ms',
        'false_positives': '0.8%'
    },
    'Guardian AI Auditor': {
        'privacy': '100%',
        'audits': '2.5K',
        'breaches': '0',
        'audit_trail': 'Immutable'
    },
    'MLOps Observability': {
        'monitoring': '24/7',
        'alerts': '0',
        'uptime': '99.9%',
        'response': '5min'
    }
}

def main():
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    
    # Top Social Icons
    st.markdown("""
    <div class="social-icons-top">
        <a href="https://linkedin.com/in/mukesh-mlops" target="_blank" class="social-icon-link"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/MukeshPyatla" target="_blank" class="social-icon-link"><i class="fab fa-github"></i></a>
        <a href="mailto:mukeshyadavp91@gmail.com" class="social-icon-link"><i class="fas fa-envelope"></i></a>
    </div>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div style="position: relative; z-index: 1;">
            <h1 class="section-title">Mukesh Yadav</h1>
            <h2 style="font-size: 2.5rem; color: #63b3ed; margin-bottom: 20px; text-align: center; font-weight: 600;">MLOPS & DEVOPS ENGINEER</h2>
            <h3 style="font-size: 1.5rem; color: #9CA3AF; margin-bottom: 40px; text-align: center; font-weight: 400;">Building Intelligent Systems on Azure & AWS Cloud</h3>
            <p style="font-size: 1.3rem; color: #D1D5DB; line-height: 1.8; margin-bottom: 40px; text-align: center;">
                Specializing in end-to-end MLOps pipelines, automated CI/CD workflows, and scalable cloud infrastructure. 
                Passionately deploying production-ready AI/ML systems with robust monitoring and observability.
            </p>
            <div style="display: flex; gap: 20px; margin-top: 40px; justify-content: center;">
                <a href="#projects" class="btn-primary">View Projects</a>
                <a href="#dashboards" class="btn-secondary">Live Dashboards</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    cols = st.columns(4)
    metric_data = [
        {'value': '80%', 'label': 'Faster Deployments'},
        {'value': '70%', 'label': 'Reduced MTTR'},
        {'value': '47', 'label': 'Technical Skills'},
        {'value': '6', 'label': 'Live Projects'},
    ]
    
    for col, data in zip(cols, metric_data):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{data['value']}</div>
                <div class="metric-label">{data['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # About Section
    st.markdown('<h1 class="section-title">About Me</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Architecting the future of AI infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 50px;">
        <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #63b3ed, #9f7aea);
                    border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;
                    font-size: 4rem; color: white; box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3);">
            MY
        </div>
        <h3 style="color: #63b3ed; margin-bottom: 10px; font-weight: 600;">Mukesh Yadav</h3>
        <p style="color: #9CA3AF;">MLOps & DevOps Engineer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="category-card">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #D1D5DB; text-align: left;">
            As an MLOps Engineer at Aidoc, I architect and deploy intelligent systems that process millions of data points daily. 
            My expertise spans from building robust monitoring systems with Prometheus and Grafana to implementing CI/CD pipelines 
            that reduce deployment time by 80%.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #D1D5DB; text-align: left;">
            I specialize in privacy-preserving AI using Federated Learning and Homomorphic Encryption, ensuring compliance while 
            maintaining model performance. My work includes developing containerized GenAI microservices with BentoML and Kubernetes, 
            solving the classic "it works on my machine" problem.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #D1D5DB; text-align: left;">
            Currently exploring cutting-edge technologies like LLMOps, Vector Databases for RAG systems, and blockchain integration 
            for immutable audit trails in MLOps pipelines.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Comprehensive skills across the MLOps and DevOps ecosystem</p>', unsafe_allow_html=True)
    
    # Skills details with interactive tabs
    st.markdown('<h2 style="color: white; margin-top: 60px; text-align: center; font-size: 2rem;">Detailed Skills Breakdown</h2>', unsafe_allow_html=True)
    
    # The fix: Create tabs with plain text titles.
    skill_tabs = st.tabs([category for category in skills_data.keys()])
    
    for i, (category, data) in enumerate(skills_data.items()):
        with skill_tabs[i]:
            # The fix: Render the icon and title inside the tab using markdown
            st.markdown(f"""
            <div class="category-card" style="padding-top: 20px;">
                <h3 style="color: {data['color']}; font-size: 1.8rem; margin-bottom: 25px; text-align: center; font-weight: 600;">
                    <span style="font-size: 2rem; vertical-align: middle; margin-right: 15px;">{data['icon']}</span>
                    {category}
                </h3>
                <div class="skill-grid">
            """, unsafe_allow_html=True)
            
            for skill in data['skills']:
                st.markdown(f"""
                <div class="skill-item">
                    <span style="color: {data['color']}; font-weight: 600; font-size: 1rem;">{skill}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Projects Section
    st.markdown('<h1 class="section-title" id="projects">Featured Projects</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">End-to-end MLOps and DevOps solutions with live dashboards</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card-grid">', unsafe_allow_html=True)
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <span style="font-size: 2.5rem; margin-bottom: 20px; display: block; color: #63b3ed;">{project['icon']}</span>
            <h3 style="color: white; font-size: 1.8rem; margin: 0; font-weight: 600;">{project['title']}</h3>
            <div style="display: flex; align-items: center; justify-content: center; margin-top: 8px;">
                <span class="status-live"></span>
                <span style="color: #10B981; font-size: 1rem; font-weight: 600;">{project['status']}</span>
            </div>
            <p style="color: #9CA3AF; line-height: 1.7; margin: 20px 0; font-size: 1.1rem;">{project['description']}</p>
            <div style="margin-bottom: 25px;">
                {''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech']])}
            </div>
            <div style="display: flex; gap: 15px; justify-content: center;">
                <a href="{project['github']}" target="_blank" class="btn-secondary">GitHub</a>
                <a href="{project['demo']}" target="_blank" class="btn-primary">Live Demo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Dashboards Section
    st.markdown('<h1 class="section-title" id="dashboards">Live Dashboards</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Real-time monitoring and analytics dashboards for my projects</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="dashboard-card-grid">', unsafe_allow_html=True)
    for project_name, metrics in dashboard_metrics.items():
        st.markdown(f"""
        <div class="dashboard-card">
            <h3 style="color: white; font-size: 1.8rem; margin-bottom: 15px; font-weight: 600;">{project_name} Dashboard</h3>
            <p style="color: #9CA3AF; margin-bottom: 25px; font-size: 1.1rem;">Real-time metrics and performance monitoring</p>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-bottom: 25px;">
        """, unsafe_allow_html=True)
        
        for metric_name, value in metrics.items():
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{metric_name.replace('_', ' ').title()}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            </div>
            <div style="display: flex; gap: 15px; justify-content: center;">
                <a href="#" class="btn-primary">View Dashboard</a>
                <a href="#" class="btn-secondary">Source Code</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Experience Section
    st.markdown('<h1 class="section-title">Professional Journey</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Building the future of AI infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="experience-card-grid">', unsafe_allow_html=True)
    for exp in experience_data:
        st.markdown(f"""
        <div class="experience-card" style="text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h3 style="color: white; font-size: 1.5rem; margin: 0; font-weight: 600;">{exp['title']}</h3>
                <span style="color: #10B981; font-size: 1rem; font-weight: 500;">{exp['period']}</span>
            </div>
            <h4 style="color: #63b3ed; font-size: 1.3rem; margin-bottom: 20px; font-weight: 600;">{exp['company']}</h4>
            <ul style="color: #9CA3AF; line-height: 1.8; font-size: 1.1rem; list-style-type: '—  '; padding-left: 20px;">
        """, unsafe_allow_html=True)
        
        for achievement in exp['achievements']:
            st.markdown(f'<li style="margin-bottom: 8px;">{achievement}</li>', unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<h1 class="section-title">Let\'s Connect</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #63b3ed; font-size: 2.5rem; margin-bottom: 20px; font-weight: 600;">Ready to Build the Future Together</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 50px;">I\'m actively seeking opportunities to architect and scale AI solutions. If you\'re looking for a passionate engineer to solve complex challenges in MLOps and DevOps, let\'s connect.</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card-grid contact-card-grid">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="contact-card">
        <span style="font-size: 3rem; color: #63b3ed;">📧</span>
        <h3 style="color: white; margin: 20px 0; font-weight: 600;">Email</h3>
        <p style="color: #9CA3AF; font-size: 1.1rem;">mukeshyadavp91@gmail.com</p>
    </div>
    <div class="contact-card">
        <span style="font-size: 3rem; color: #63b3ed;">💼</span>
        <h3 style="color: white; margin: 20px 0; font-weight: 600;">LinkedIn</h3>
        <p style="color: #9CA3AF; font-size: 1.1rem;">linkedin.com/in/mukesh-mlops</p>
    </div>
    <div class="contact-card">
        <span style="font-size: 3rem; color: #63b3ed;">🐙</span>
        <h3 style="color: white; margin: 20px 0; font-weight: 600;">GitHub</h3>
        <p style="color: #9CA3AF; font-size: 1.1rem;">github.com/MukeshPyatla</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="mailto:mukeshyadavp91@gmail.com" class="btn-primary">Get In Touch</a>
    </div>
    """, unsafe_allow_html=True)

    # Closing centered container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
