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

# Custom CSS for modern minimal styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: #000000;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: #000000;
    }
    
    .hero-section {
        background: linear-gradient(135deg, rgba(135, 206, 250, 0.05), rgba(176, 224, 230, 0.05));
        border-radius: 24px;
        padding: 60px 40px;
        margin: 40px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
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
        background: linear-gradient(135deg, #87CEEB 0%, #B0E0E6 100%);
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
    
    .category-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 32px 24px;
        margin: 16px 0;
        backdrop-filter: blur(20px);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .category-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(135, 206, 250, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .category-card:hover::before {
        left: 100%;
    }
    
    .category-card:hover {
        transform: translateY(-8px);
        border-color: rgba(135, 206, 250, 0.3);
        box-shadow: 0 20px 40px -12px rgba(135, 206, 250, 0.2);
    }
    
    .project-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 32px;
        margin: 24px 0;
        backdrop-filter: blur(20px);
        transition: all 0.4s ease;
        position: relative;
    }
    
    .project-card:hover {
        border-color: rgba(135, 206, 250, 0.3);
        box-shadow: 0 25px 50px -12px rgba(135, 206, 250, 0.25);
        transform: translateY(-4px);
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(135, 206, 250, 0.1), rgba(176, 224, 230, 0.1));
        border: 1px solid rgba(135, 206, 250, 0.2);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin: 12px;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px -10px rgba(135, 206, 250, 0.3);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #87CEEB, #B0E0E6);
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
    
    .tech-tag {
        background: rgba(135, 206, 250, 0.1);
        color: #87CEEB;
        font-size: 0.75rem;
        font-weight: 500;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 4px;
        display: inline-block;
        border: 1px solid rgba(135, 206, 250, 0.2);
    }
    
    .timeline-item {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        position: relative;
        border-left: 4px solid #87CEEB;
        backdrop-filter: blur(20px);
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #87CEEB, #B0E0E6);
        color: #000000;
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
        box-shadow: 0 10px 25px rgba(135, 206, 250, 0.4);
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
        border-color: #87CEEB;
        color: white;
        transform: translateY(-2px);
    }
    
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(135, 206, 250, 0.3), transparent);
        margin: 80px 0;
        border-radius: 1px;
    }
    
    /* Style tabs for skills */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 12px;
        padding: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(135, 206, 250, 0.1);
        border: 1px solid rgba(135, 206, 250, 0.2);
        border-radius: 8px;
        color: white;
        font-weight: 500;
        padding: 10px 16px;
        margin: 2px;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(135, 206, 250, 0.2);
        border-color: rgba(135, 206, 250, 0.4);
        color: white;
        box-shadow: 0 4px 12px rgba(135, 206, 250, 0.2);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(135, 206, 250, 0.15);
        border-color: rgba(135, 206, 250, 0.3);
    }
    
    .devops-visual {
        background: linear-gradient(135deg, rgba(135, 206, 250, 0.1), rgba(176, 224, 230, 0.1));
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        border: 1px solid rgba(135, 206, 250, 0.2);
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
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100"><defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(135,206,250,0.1)" stroke-width="0.5"/></pattern></defs><rect width="200" height="100" fill="url(%23grid)"/></svg>');
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
        background: rgba(135, 206, 250, 0.1);
        border-color: rgba(135, 206, 250, 0.3);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Skills data
skills_data = {
    'Cloud & DevOps': {
        'icon': '☁️',
        'color': '#87CEEB',
        'skills': ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD'],
        'count': 6
    },
    'AI/ML Frameworks': {
        'icon': '🧠',
        'color': '#B0E0E6',
        'skills': ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML'],
        'count': 6
    },
    'Programming Languages': {
        'icon': '💻',
        'color': '#ADD8E6',
        'skills': ['Python', 'Go', 'C++', 'Bash', 'SQL'],
        'count': 5
    },
    'Data & Databases': {
        'icon': '🗄️',
        'color': '#E0F6FF',
        'skills': ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant'],
        'count': 5
    },
    'Monitoring & Observability': {
        'icon': '📊',
        'color': '#F0F8FF',
        'skills': ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B'],
        'count': 5
    },
    'CI/CD Tools': {
        'icon': '⚙️',
        'color': '#E6F3FF',
        'skills': ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions'],
        'count': 5
    },
    'AI/ML Concepts': {
        'icon': '🤖',
        'color': '#87CEEB',
        'skills': ['MLOps', 'GenAI', 'RAG', 'Federated Learning', 'Homomorphic Encryption', 'NLP'],
        'count': 6
    },
    'Blockchain': {
        'icon': '🔗',
        'color': '#B0E0E6',
        'skills': ['Ethereum', 'Solidity', 'Blockchain'],
        'count': 3
    },
    'Operating Systems': {
        'icon': '🖥️',
        'color': '#ADD8E6',
        'skills': ['Linux', 'Windows'],
        'count': 2
    },
    'Networking': {
        'icon': '🌐',
        'color': '#87CEEB',
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
        'icon': '🛡️'
    },
    {
        'title': 'Guardian AI Auditor',
        'description': 'Zero-trust multi-modal compliance & risk auditor with privacy-preserving MLOps pipeline using Federated Learning and Homomorphic Encryption.',
        'status': 'LIVE',
        'tech': ['Federated Learning', 'Homomorphic Encryption', 'Blockchain'],
        'github': 'https://github.com/MukeshPyatla/guardian-ai-auditor',
        'demo': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
        'icon': '🤖'
    },
    {
        'title': 'MLOps Q&A System',
        'description': 'LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo with real-time updates.',
        'status': 'LIVE',
        'tech': ['LLM', 'RAG', 'Vector DB'],
        'github': 'https://github.com/MukeshPyatla/mlops-qa-system',
        'demo': 'https://mlops-app-system.streamlit.app/',
        'icon': '💬'
    },
    {
        'title': 'Azure Anomaly Detector',
        'description': 'End-to-End MLOps pipeline for anomaly detection on Azure with real-time monitoring and alerting system.',
        'status': 'LIVE',
        'tech': ['Azure', 'MLOps', 'Python'],
        'github': 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector',
        'demo': 'https://azure-mlops-anomaly-detector.streamlit.app/',
        'icon': '📡'
    },
    {
        'title': 'Secure Churn Prediction',
        'description': 'Privacy-preserving customer churn prediction with PII masking and SHAP explainability in Azure Databricks.',
        'status': 'LIVE',
        'tech': ['Azure Databricks', 'SHAP', 'Data Security'],
        'github': 'https://github.com/MukeshPyatla/MLOPS-Secure-Churn',
        'demo': 'https://mlops-secure-churn.streamlit.app/',
        'icon': '👤'
    },
    {
        'title': 'Demand Forecasting',
        'description': 'Scalable demand forecasting system with integrated MLOps for continuous training and monitoring.',
        'status': 'LIVE',
        'tech': ['Python', 'Forecasting', 'MLOps'],
        'github': 'https://github.com/MukeshPyatla/MLOPS-Demand-Forecasting',
        'demo': 'https://mlops-demand-forecasting.streamlit.app/',
        'icon': '📈'
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
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div style="position: relative; z-index: 1;">
            <h1 class="section-title">Mukesh Yadav</h1>
            <h2 style="font-size: 2.5rem; color: #87CEEB; margin-bottom: 20px; text-align: center; font-weight: 600;">MLOPS & DEVOPS ENGINEER</h2>
            <h3 style="font-size: 1.5rem; color: #9CA3AF; margin-bottom: 40px; text-align: center; font-weight: 400;">Building Intelligent Systems on Azure & AWS Cloud</h3>
            <p style="font-size: 1.3rem; color: #D1D5DB; line-height: 1.8; margin-bottom: 40px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                Specializing in end-to-end MLOps pipelines, automated CI/CD workflows, and scalable cloud infrastructure. 
                Passionate about deploying production-ready AI/ML systems with robust monitoring and observability.
            </p>
            <div style="display: flex; gap: 20px; margin-top: 40px; justify-content: center;">
                <a href="#projects" class="btn-primary">View Projects</a>
                <a href="#dashboards" class="btn-secondary">Live Dashboards</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">80%</div>
            <div class="metric-label">Faster Deployments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">70%</div>
            <div class="metric-label">Reduced MTTR</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">47</div>
            <div class="metric-label">Technical Skills</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">6</div>
            <div class="metric-label">Live Projects</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # About Section with DevOps Visual
    st.markdown('<h1 class="section-title">About Me</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Architecting the future of AI infrastructure</p>', unsafe_allow_html=True)
    
    # DevOps Visual Representation
    st.markdown("""
    <div class="devops-visual">
        <div style="position: relative; z-index: 1;">
            <h3 style="color: white; font-size: 1.5rem; margin-bottom: 20px; text-align: center;">MLOps Pipeline Architecture</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 30px;">
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1);">
                    <span style="font-size: 2rem; margin-bottom: 10px; display: block;">📊</span>
                    <h4 style="color: #6366F1; margin: 10px 0;">Data Ingestion</h4>
                    <p style="color: #9CA3AF; font-size: 0.9rem;">Real-time data processing with Apache Kafka</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1);">
                    <span style="font-size: 2rem; margin-bottom: 10px; display: block;">🤖</span>
                    <h4 style="color: #6366F1; margin: 10px 0;">Model Training</h4>
                    <p style="color: #9CA3AF; font-size: 0.9rem;">Automated ML pipeline with MLflow</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1);">
                    <span style="font-size: 2rem; margin-bottom: 10px; display: block;">🚀</span>
                    <h4 style="color: #6366F1; margin: 10px 0;">Deployment</h4>
                    <p style="color: #9CA3AF; font-size: 0.9rem;">Kubernetes orchestration with ArgoCD</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1);">
                    <span style="font-size: 2rem; margin-bottom: 10px; display: block;">📈</span>
                    <h4 style="color: #6366F1; margin: 10px 0;">Monitoring</h4>
                    <p style="color: #9CA3AF; font-size: 0.9rem;">Prometheus & Grafana observability</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.02); border-radius: 20px; padding: 40px; margin: 20px 0; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
            <p style="font-size: 1.1rem; line-height: 1.8; color: #D1D5DB; margin-bottom: 20px;">
                As an MLOps Engineer at Aidoc, I architect and deploy intelligent systems that process millions of data points daily. 
                My expertise spans from building robust monitoring systems with Prometheus and Grafana to implementing CI/CD pipelines 
                that reduce deployment time by 80%.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #D1D5DB; margin-bottom: 20px;">
                I specialize in privacy-preserving AI using Federated Learning and Homomorphic Encryption, ensuring compliance while 
                maintaining model performance. My work includes developing containerized GenAI microservices with BentoML and Kubernetes, 
                solving the classic "it works on my machine" problem.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #D1D5DB;">
                Currently exploring cutting-edge technologies like LLMOps, Vector Databases for RAG systems, and blockchain integration 
                for immutable audit trails in MLOps pipelines.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #6366F1, #A855F7); 
                        border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; 
                        font-size: 4rem; color: white; box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3);">
                MY
            </div>
            <h3 style="color: #6366F1; margin-bottom: 10px; font-weight: 600;">Mukesh Yadav</h3>
            <p style="color: #9CA3AF;">MLOps & DevOps Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Comprehensive skills across the MLOps and DevOps ecosystem</p>', unsafe_allow_html=True)
    
    # Create columns for skill categories
    cols = st.columns(3)
    
    for i, (category, data) in enumerate(skills_data.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="category-card">
                <div style="text-align: center; margin-bottom: 20px;">
                    <span style="font-size: 3rem;">{data['icon']}</span>
                </div>
                <h3 style="color: white; font-size: 1.3rem; margin-bottom: 10px; text-align: center; font-weight: 600;">{category}</h3>
                <p style="color: #9CA3AF; font-size: 0.9rem; text-align: center; margin-bottom: 15px;">
                    {', '.join(data['skills'][:3])}{'...' if len(data['skills']) > 3 else ''}
                </p>
                <div style="text-align: center;">
                    <span style="color: {data['color']}; font-size: 0.8rem; font-weight: 500;">{data['count']} skills</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Skills details with interactive tabs
    st.markdown('<h2 style="color: white; margin-top: 60px; text-align: center; font-size: 2rem;">Detailed Skills Breakdown</h2>', unsafe_allow_html=True)
    
    # Create tabs for different skill categories
    skill_tabs = st.tabs([f"{data['icon']} {category}" for category, data in skills_data.items()])
    
    for i, (category, data) in enumerate(skills_data.items()):
        with skill_tabs[i]:
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.02); border-radius: 16px; padding: 30px; margin: 10px 0; border: 1px solid rgba(255, 255, 255, 0.1);">
                <h3 style="color: {data['color']}; font-size: 1.8rem; margin-bottom: 25px; text-align: center; font-weight: 600;">{category}</h3>
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
    st.markdown('<h1 class="section-title">Featured Projects</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">End-to-end MLOps and DevOps solutions with live dashboards</p>', unsafe_allow_html=True)
    
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <span style="font-size: 2.5rem; margin-right: 20px;">{project['icon']}</span>
                <div>
                    <h3 style="color: white; font-size: 1.8rem; margin: 0; font-weight: 600;">{project['title']}</h3>
                    <div style="display: flex; align-items: center; margin-top: 8px;">
                        <span class="status-live"></span>
                        <span style="color: #10B981; font-size: 1rem; font-weight: 600;">{project['status']}</span>
                    </div>
                </div>
            </div>
            <p style="color: #9CA3AF; line-height: 1.7; margin-bottom: 20px; font-size: 1.1rem;">{project['description']}</p>
            <div style="margin-bottom: 25px;">
                {''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech']])}
            </div>
            <div style="display: flex; gap: 15px;">
                <a href="{project['github']}" target="_blank" class="btn-secondary">GitHub</a>
                <a href="{project['demo']}" target="_blank" class="btn-primary">Live Demo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Dashboards Section
    st.markdown('<h1 class="section-title">Live Dashboards</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Real-time monitoring and analytics dashboards for my projects</p>', unsafe_allow_html=True)
    
    for project_name, metrics in dashboard_metrics.items():
        st.markdown(f"""
        <div class="project-card">
            <h3 style="color: white; font-size: 1.8rem; margin-bottom: 15px; font-weight: 600;">{project_name} Dashboard</h3>
            <p style="color: #9CA3AF; margin-bottom: 25px; font-size: 1.1rem;">Real-time metrics and performance monitoring</p>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 25px;">
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
            <div style="display: flex; gap: 15px;">
                <a href="#" class="btn-primary">View Dashboard</a>
                <a href="#" class="btn-secondary">Source Code</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Experience Section
    st.markdown('<h1 class="section-title">Professional Journey</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Building the future of AI infrastructure</p>', unsafe_allow_html=True)
    
    for exp in experience_data:
        st.markdown(f"""
        <div class="timeline-item">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h3 style="color: white; font-size: 1.5rem; margin: 0; font-weight: 600;">{exp['title']}</h3>
                <span style="color: #10B981; font-size: 1rem; font-weight: 500;">{exp['period']}</span>
            </div>
            <h4 style="color: #6366F1; font-size: 1.3rem; margin-bottom: 20px; font-weight: 600;">{exp['company']}</h4>
            <ul style="color: #9CA3AF; line-height: 1.8; font-size: 1.1rem;">
        """, unsafe_allow_html=True)
        
        for achievement in exp['achievements']:
            st.markdown(f'<li style="margin-bottom: 8px;">{achievement}</li>', unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<h1 class="section-title">Let\'s Connect</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #6366F1; font-size: 2.5rem; margin-bottom: 20px; font-weight: 600;">Ready to Build the Future Together</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 50px; max-width: 600px; margin-left: auto; margin-right: auto;">I\'m actively seeking opportunities to architect and scale AI solutions. If you\'re looking for a passionate engineer to solve complex challenges in MLOps and DevOps, let\'s connect.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: rgba(255, 255, 255, 0.02); border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
            <span style="font-size: 3rem;">📧</span>
            <h3 style="color: white; margin: 20px 0; font-weight: 600;">Email</h3>
            <p style="color: #9CA3AF; font-size: 1.1rem;">mukeshyadavp91@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: rgba(255, 255, 255, 0.02); border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
            <span style="font-size: 3rem;">💼</span>
            <h3 style="color: white; margin: 20px 0; font-weight: 600;">LinkedIn</h3>
            <p style="color: #9CA3AF; font-size: 1.1rem;">linkedin.com/in/mukesh-mlops</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: rgba(255, 255, 255, 0.02); border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
            <span style="font-size: 3rem;">🐙</span>
            <h3 style="color: white; margin: 20px 0; font-weight: 600;">GitHub</h3>
            <p style="color: #9CA3AF; font-size: 1.1rem;">github.com/MukeshPyatla</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="mailto:mukeshyadavp91@gmail.com" class="btn-primary">Get In Touch</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 