import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Mukesh Yadav - MLOps & DevOps Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with light aesthetic and Bootstrap
def load_css():
    st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        color: #334155;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border-radius: 24px;
        padding: 80px 40px;
        margin: 40px 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
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
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(59,130,246,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    .section-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .section-subtitle {
        font-size: 1.3rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 50px;
        font-weight: 400;
    }
    
    .category-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 40px 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
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
        background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .category-card:hover::before {
        left: 100%;
    }
    
    .category-card:hover {
        transform: translateY(-8px);
        border-color: #3b82f6;
        box-shadow: 0 25px 50px rgba(59, 130, 246, 0.15);
    }
    
    .project-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
        transition: all 0.4s ease;
        position: relative;
    }
    
    .project-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 30px 60px rgba(59, 130, 246, 0.15);
        transform: translateY(-4px);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border: 1px solid #93c5fd;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 15px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.2);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #64748b;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .status-live {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #10b981;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.6);
        margin-right: 10px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.1); }
    }
    
    .tech-tag {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        color: #1e40af;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 8px 16px;
        border-radius: 25px;
        margin: 5px;
        display: inline-block;
        border: 1px solid #93c5fd;
        transition: all 0.3s ease;
    }
    
    .tech-tag:hover {
        background: linear-gradient(135deg, #bfdbfe 0%, #93c5fd 100%);
        transform: translateY(-2px);
    }
    
    .timeline-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        position: relative;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #3b82f6, #1e40af);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 15px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        font-size: 1rem;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
        color: white;
    }
    
    .btn-secondary {
        background: #ffffff;
        color: #3b82f6;
        border: 2px solid #3b82f6;
        padding: 15px 30px;
        border-radius: 15px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        font-size: 1rem;
    }
    
    .btn-secondary:hover {
        background: #3b82f6;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #3b82f6, transparent);
        margin: 100px 0;
        border-radius: 1px;
    }
    
    .devops-visual {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 24px;
        padding: 50px;
        margin: 40px 0;
        border: 1px solid #bae6fd;
        position: relative;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.1);
    }
    
    .devops-visual::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100"><defs><pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse"><path d="M 25 0 L 0 0 0 25" fill="none" stroke="rgba(59,130,246,0.1)" stroke-width="0.5"/></pattern></defs><rect width="200" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    .skill-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 15px;
        margin-top: 25px;
    }
    
    .skill-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }
    
    .skill-item:hover {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-color: #3b82f6;
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.15);
    }
    
    .icon-large {
        font-size: 3rem;
        margin-bottom: 15px;
        display: block;
        color: #3b82f6;
    }
    
    .contact-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .contact-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.15);
        border-color: #3b82f6;
    }
    
    /* Style tabs for skills */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: #ffffff;
        border-radius: 15px;
        padding: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        color: #64748b;
        font-weight: 500;
        padding: 12px 20px;
        margin: 2px;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6, #1e40af);
        border-color: #3b82f6;
        color: white;
        box-shadow: 0 5px 15px rgba(59, 130, 246, 0.3);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: #dbeafe;
        border-color: #3b82f6;
        color: #1e40af;
    }
    
    @media (max-width: 768px) {
        .section-title {
            font-size: 2.5rem;
        }
        
        .hero-section {
            padding: 40px 20px;
        }
        
        .category-card {
            padding: 30px 20px;
        }
        
        .project-card {
            padding: 30px 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Skills data with soft icons
skills_data = {
    'Cloud & DevOps': {
        'icon': '☁️',
        'color': '#3b82f6',
        'skills': ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD'],
        'count': 6
    },
    'AI/ML Frameworks': {
        'icon': '🧠',
        'color': '#f59e0b',
        'skills': ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML'],
        'count': 6
    },
    'Programming Languages': {
        'icon': '💻',
        'color': '#10b981',
        'skills': ['Python', 'Go', 'C++', 'Bash', 'SQL'],
        'count': 5
    },
    'Data & Databases': {
        'icon': '🗄️',
        'color': '#8b5cf6',
        'skills': ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant'],
        'count': 5
    },
    'Monitoring & Observability': {
        'icon': '📊',
        'color': '#ef4444',
        'skills': ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B'],
        'count': 5
    },
    'CI/CD Tools': {
        'icon': '⚙️',
        'color': '#f59e0b',
        'skills': ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions'],
        'count': 5
    },
    'AI/ML Concepts': {
        'icon': '🤖',
        'color': '#3b82f6',
        'skills': ['MLOps', 'GenAI', 'RAG', 'Federated Learning', 'Homomorphic Encryption', 'NLP'],
        'count': 6
    },
    'Blockchain': {
        'icon': '🔗',
        'color': '#10b981',
        'skills': ['Ethereum', 'Solidity', 'Blockchain'],
        'count': 3
    },
    'Operating Systems': {
        'icon': '🖥️',
        'color': '#6b7280',
        'skills': ['Linux', 'Windows'],
        'count': 2
    },
    'Networking': {
        'icon': '🌐',
        'color': '#3b82f6',
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
            <h2 style="font-size: 2.5rem; color: #1e40af; margin-bottom: 20px; text-align: center; font-weight: 600;">MLOPS & DEVOPS ENGINEER</h2>
            <h3 style="font-size: 1.5rem; color: #64748b; margin-bottom: 40px; text-align: center; font-weight: 400;">Building Intelligent Systems on Azure & AWS Cloud</h3>
            <p style="font-size: 1.3rem; color: #475569; line-height: 1.8; margin-bottom: 40px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
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
            <h3 style="color: #1e40af; font-size: 1.8rem; margin-bottom: 30px; text-align: center; font-weight: 600;">MLOps Pipeline Architecture</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px; margin-top: 40px;">
                <div style="background: #ffffff; border-radius: 15px; padding: 25px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);">
                    <span style="font-size: 2.5rem; margin-bottom: 15px; display: block;">📊</span>
                    <h4 style="color: #1e40af; margin: 15px 0; font-weight: 600;">Data Ingestion</h4>
                    <p style="color: #64748b; font-size: 1rem;">Real-time data processing with Apache Kafka</p>
                </div>
                <div style="background: #ffffff; border-radius: 15px; padding: 25px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);">
                    <span style="font-size: 2.5rem; margin-bottom: 15px; display: block;">🤖</span>
                    <h4 style="color: #1e40af; margin: 15px 0; font-weight: 600;">Model Training</h4>
                    <p style="color: #64748b; font-size: 1rem;">Automated ML pipeline with MLflow</p>
                </div>
                <div style="background: #ffffff; border-radius: 15px; padding: 25px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);">
                    <span style="font-size: 2.5rem; margin-bottom: 15px; display: block;">🚀</span>
                    <h4 style="color: #1e40af; margin: 15px 0; font-weight: 600;">Deployment</h4>
                    <p style="color: #64748b; font-size: 1rem;">Kubernetes orchestration with ArgoCD</p>
                </div>
                <div style="background: #ffffff; border-radius: 15px; padding: 25px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);">
                    <span style="font-size: 2.5rem; margin-bottom: 15px; display: block;">📈</span>
                    <h4 style="color: #1e40af; margin: 15px 0; font-weight: 600;">Monitoring</h4>
                    <p style="color: #64748b; font-size: 1rem;">Prometheus & Grafana observability</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="background: #ffffff; border-radius: 20px; padding: 40px; margin: 20px 0; border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);">
            <p style="font-size: 1.1rem; line-height: 1.8; color: #475569; margin-bottom: 20px;">
                As an MLOps Engineer at Aidoc, I architect and deploy intelligent systems that process millions of data points daily. 
                My expertise spans from building robust monitoring systems with Prometheus and Grafana to implementing CI/CD pipelines 
                that reduce deployment time by 80%.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #475569; margin-bottom: 20px;">
                I specialize in privacy-preserving AI using Federated Learning and Homomorphic Encryption, ensuring compliance while 
                maintaining model performance. My work includes developing containerized GenAI microservices with BentoML and Kubernetes, 
                solving the classic "it works on my machine" problem.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #475569;">
                Currently exploring cutting-edge technologies like LLMOps, Vector Databases for RAG systems, and blockchain integration 
                for immutable audit trails in MLOps pipelines.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #3b82f6, #1e40af); 
                        border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; 
                        font-size: 4rem; color: white; box-shadow: 0 20px 40px rgba(59, 130, 246, 0.3);">
                MY
            </div>
            <h3 style="color: #1e40af; margin-bottom: 10px; font-weight: 600;">Mukesh Yadav</h3>
            <p style="color: #64748b;">MLOps & DevOps Engineer</p>
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
                    <span class="icon-large">{data['icon']}</span>
                </div>
                <h3 style="color: #1e40af; font-size: 1.4rem; margin-bottom: 15px; text-align: center; font-weight: 600;">{category}</h3>
                <p style="color: #64748b; font-size: 1rem; text-align: center; margin-bottom: 20px;">
                    {', '.join(data['skills'][:3])}{'...' if len(data['skills']) > 3 else ''}
                </p>
                <div style="text-align: center;">
                    <span style="color: {data['color']}; font-size: 0.9rem; font-weight: 600;">{data['count']} skills</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Skills details with interactive tabs
    st.markdown('<h2 style="color: #1e40af; margin-top: 80px; text-align: center; font-size: 2.5rem; font-weight: 600;">Detailed Skills Breakdown</h2>', unsafe_allow_html=True)
    
    # Create tabs for different skill categories
    skill_tabs = st.tabs([f"{data['icon']} {category}" for category, data in skills_data.items()])
    
    for i, (category, data) in enumerate(skills_data.items()):
        with skill_tabs[i]:
            st.markdown(f"""
            <div style="background: #ffffff; border-radius: 20px; padding: 40px; margin: 15px 0; border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);">
                <h3 style="color: {data['color']}; font-size: 2rem; margin-bottom: 30px; text-align: center; font-weight: 600;">{category}</h3>
                <div class="skill-grid">
            """, unsafe_allow_html=True)
            
            for skill in data['skills']:
                st.markdown(f"""
                <div class="skill-item">
                    <span style="color: {data['color']}; font-weight: 600; font-size: 1.1rem;">{skill}</span>
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
            <div style="display: flex; align-items: center; margin-bottom: 25px;">
                <span style="font-size: 3rem; margin-right: 25px;">{project['icon']}</span>
                <div>
                    <h3 style="color: #1e40af; font-size: 2rem; margin: 0; font-weight: 600;">{project['title']}</h3>
                    <div style="display: flex; align-items: center; margin-top: 10px;">
                        <span class="status-live"></span>
                        <span style="color: #10b981; font-size: 1.1rem; font-weight: 600;">{project['status']}</span>
                    </div>
                </div>
            </div>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 25px; font-size: 1.2rem;">{project['description']}</p>
            <div style="margin-bottom: 30px;">
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
            <h3 style="color: #1e40af; font-size: 2rem; margin-bottom: 20px; font-weight: 600;">{project_name} Dashboard</h3>
            <p style="color: #64748b; margin-bottom: 30px; font-size: 1.2rem;">Real-time metrics and performance monitoring</p>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 25px; margin-bottom: 30px;">
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
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
                <h3 style="color: #1e40af; font-size: 1.8rem; margin: 0; font-weight: 600;">{exp['title']}</h3>
                <span style="color: #10b981; font-size: 1.1rem; font-weight: 600;">{exp['period']}</span>
            </div>
            <h4 style="color: #3b82f6; font-size: 1.5rem; margin-bottom: 25px; font-weight: 600;">{exp['company']}</h4>
            <ul style="color: #64748b; line-height: 1.8; font-size: 1.2rem;">
        """, unsafe_allow_html=True)
        
        for achievement in exp['achievements']:
            st.markdown(f'<li style="margin-bottom: 12px;">{achievement}</li>', unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<h1 class="section-title">Let\'s Connect</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #1e40af; font-size: 2.5rem; margin-bottom: 20px; font-weight: 600;">Ready to Build the Future Together</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #64748b; font-size: 1.3rem; margin-bottom: 60px; max-width: 700px; margin-left: auto; margin-right: auto;">I\'m actively seeking opportunities to architect and scale AI solutions. If you\'re looking for a passionate engineer to solve complex challenges in MLOps and DevOps, let\'s connect.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-card">
            <span style="font-size: 3.5rem; color: #3b82f6;">📧</span>
            <h3 style="color: #1e40af; margin: 25px 0; font-weight: 600;">Email</h3>
            <p style="color: #64748b; font-size: 1.2rem;">mukeshyadavp91@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
            <span style="font-size: 3.5rem; color: #3b82f6;">💼</span>
            <h3 style="color: #1e40af; margin: 25px 0; font-weight: 600;">LinkedIn</h3>
            <p style="color: #64748b; font-size: 1.2rem;">linkedin.com/in/mukesh-mlops</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-card">
            <span style="font-size: 3.5rem; color: #3b82f6;">🐙</span>
            <h3 style="color: #1e40af; margin: 25px 0; font-weight: 600;">GitHub</h3>
            <p style="color: #64748b; font-size: 1.2rem;">github.com/MukeshPyatla</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 60px;">
        <a href="mailto:mukeshyadavp91@gmail.com" class="btn-primary">Get In Touch</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 