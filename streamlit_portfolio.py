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

# Custom CSS for modern styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Lexend:wght@300;400&display=swap');
    
    .main {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        color: #c9d1d9;
        font-family: 'Lexend', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    }
    
    .hero-section {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(52, 211, 153, 0.1));
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
    
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #e5e7eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
    }
    
    .category-card {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin: 12px 0;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
    }
    
    .category-card:hover {
        transform: translateY(-4px);
        border-color: rgba(139, 92, 246, 0.3);
        box-shadow: 0 20px 40px -12px rgba(139, 92, 246, 0.2);
    }
    
    .project-card {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        border-color: rgba(139, 92, 246, 0.3);
        box-shadow: 0 20px 40px -12px rgba(139, 92, 246, 0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(52, 211, 153, 0.15));
        border: 1px solid rgba(139, 92, 246, 0.4);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin: 8px;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #34D399, #10B981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #D1D5DB;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-live {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #10B981;
        box-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
        margin-right: 8px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .tech-tag {
        background: rgba(55, 65, 81, 0.5);
        color: #10B981;
        font-size: 0.75rem;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 9999px;
        margin: 4px;
        display: inline-block;
    }
    
    .timeline-item {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin: 16px 0;
        position: relative;
        border-left: 4px solid #8B5CF6;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #8B5CF6, #34D399);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3);
    }
    
    .btn-secondary {
        background: rgba(55, 65, 81, 0.5);
        color: #D1D5DB;
        border: 1px solid rgba(75, 85, 99, 1);
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .btn-secondary:hover {
        background: rgba(75, 85, 99, 0.5);
        border-color: #8B5CF6;
        color: white;
    }
    
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.5), transparent);
        margin: 60px 0;
        border-radius: 1px;
    }
    
    /* Improve expandable sections */
    .streamlit-expanderHeader {
        background: rgba(139, 92, 246, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
        margin: 8px 0 !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(139, 92, 246, 0.2) !important;
        border-color: rgba(139, 92, 246, 0.5) !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
        border-radius: 8px !important;
        margin: 8px 0 !important;
        padding: 16px !important;
    }
    
    /* Style tabs for skills */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 8px;
        padding: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 6px;
        color: white;
        font-weight: 600;
        padding: 8px 16px;
        margin: 2px;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(139, 92, 246, 0.3);
        border-color: rgba(139, 92, 246, 0.6);
        color: white;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(139, 92, 246, 0.2);
        border-color: rgba(139, 92, 246, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Skills data
skills_data = {
    'Cloud & DevOps': {
        'icon': '☁️',
        'color': '#3B82F6',
        'skills': ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD'],
        'count': 6
    },
    'AI/ML Frameworks': {
        'icon': '🧠',
        'color': '#F59E0B',
        'skills': ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML'],
        'count': 6
    },
    'Programming Languages': {
        'icon': '💻',
        'color': '#10B981',
        'skills': ['Python', 'Go', 'C++', 'Bash', 'SQL'],
        'count': 5
    },
    'Data & Databases': {
        'icon': '🗄️',
        'color': '#8B5CF6',
        'skills': ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant'],
        'count': 5
    },
    'Monitoring & Observability': {
        'icon': '📊',
        'color': '#EF4444',
        'skills': ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B'],
        'count': 5
    },
    'CI/CD Tools': {
        'icon': '⚙️',
        'color': '#F59E0B',
        'skills': ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions'],
        'count': 5
    },
    'AI/ML Concepts': {
        'icon': '🤖',
        'color': '#3B82F6',
        'skills': ['MLOps', 'GenAI', 'RAG', 'Federated Learning', 'Homomorphic Encryption', 'NLP'],
        'count': 6
    },
    'Blockchain': {
        'icon': '🔗',
        'color': '#10B981',
        'skills': ['Ethereum', 'Solidity', 'Blockchain'],
        'count': 3
    },
    'Operating Systems': {
        'icon': '🖥️',
        'color': '#6B7280',
        'skills': ['Linux', 'Windows'],
        'count': 2
    },
    'Networking': {
        'icon': '🌐',
        'color': '#3B82F6',
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
        <h1 class="section-title">Mukesh Yadav</h1>
        <h2 style="font-size: 2rem; color: #34D399; margin-bottom: 20px;">MLOPS & DEVOPS ENGINEER</h2>
        <h3 style="font-size: 1.5rem; color: #9CA3AF; margin-bottom: 30px;">Building Intelligent Systems on Azure & AWS Cloud</h3>
        <p style="font-size: 1.2rem; color: #D1D5DB; line-height: 1.6; margin-bottom: 30px;">
            Specializing in end-to-end MLOps pipelines, automated CI/CD workflows, and scalable cloud infrastructure. 
            Passionate about deploying production-ready AI/ML systems with robust monitoring and observability.
        </p>
        <div style="display: flex; gap: 20px; margin-top: 30px;">
            <a href="#projects" class="btn-primary">View Projects</a>
            <a href="#dashboards" class="btn-secondary">Live Dashboards</a>
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
    
    # About Section
    st.markdown('<h1 class="section-title">About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="background: rgba(0, 0, 0, 0.6); border-radius: 16px; padding: 30px; margin: 20px 0;">
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
            <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #8B5CF6, #34D399); 
                        border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; 
                        font-size: 4rem; color: white;">
                MY
            </div>
            <h3 style="color: #34D399; margin-bottom: 10px;">Mukesh Yadav</h3>
            <p style="color: #9CA3AF;">MLOps & DevOps Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 40px;">Comprehensive skills across the MLOps and DevOps ecosystem</p>', unsafe_allow_html=True)
    
    # Create columns for skill categories
    cols = st.columns(3)
    
    for i, (category, data) in enumerate(skills_data.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="category-card">
                <div style="text-align: center; margin-bottom: 20px;">
                    <span style="font-size: 3rem;">{data['icon']}</span>
                </div>
                <h3 style="color: white; font-size: 1.3rem; margin-bottom: 10px; text-align: center;">{category}</h3>
                <p style="color: #9CA3AF; font-size: 0.9rem; text-align: center; margin-bottom: 15px;">
                    {', '.join(data['skills'][:3])}{'...' if len(data['skills']) > 3 else ''}
                </p>
                <div style="text-align: center;">
                    <span style="color: {data['color']}; font-size: 0.8rem;">{data['count']} skills</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Skills details with interactive buttons
    st.markdown('<h2 style="color: white; margin-top: 40px; text-align: center;">Detailed Skills Breakdown</h2>', unsafe_allow_html=True)
    
    # Create tabs for different skill categories
    skill_tabs = st.tabs([f"{data['icon']} {category}" for category, data in skills_data.items()])
    
    for i, (category, data) in enumerate(skills_data.items()):
        with skill_tabs[i]:
            st.markdown(f"""
            <div style="background: rgba(0, 0, 0, 0.4); border-radius: 12px; padding: 20px; margin: 10px 0;">
                <h3 style="color: {data['color']}; font-size: 1.5rem; margin-bottom: 20px; text-align: center;">{category}</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px;">
            """, unsafe_allow_html=True)
            
            for skill in data['skills']:
                st.markdown(f"""
                <div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); 
                            border-radius: 8px; padding: 15px; text-align: center; margin: 5px 0; transition: all 0.3s ease;">
                    <span style="color: {data['color']}; font-weight: 600; font-size: 1rem;">{skill}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Projects Section
    st.markdown('<h1 class="section-title">Featured Projects</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 40px;">End-to-end MLOps and DevOps solutions with live dashboards</p>', unsafe_allow_html=True)
    
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="font-size: 2rem; margin-right: 15px;">{project['icon']}</span>
                <div>
                    <h3 style="color: white; font-size: 1.5rem; margin: 0;">{project['title']}</h3>
                    <div style="display: flex; align-items: center; margin-top: 5px;">
                        <span class="status-live"></span>
                        <span style="color: #10B981; font-size: 0.9rem; font-weight: 600;">{project['status']}</span>
                    </div>
                </div>
            </div>
            <p style="color: #9CA3AF; line-height: 1.6; margin-bottom: 15px;">{project['description']}</p>
            <div style="margin-bottom: 20px;">
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
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 40px;">Real-time monitoring and analytics dashboards for my projects</p>', unsafe_allow_html=True)
    
    for project_name, metrics in dashboard_metrics.items():
        st.markdown(f"""
        <div class="project-card">
            <h3 style="color: white; font-size: 1.5rem; margin-bottom: 10px;">{project_name} Dashboard</h3>
            <p style="color: #9CA3AF; margin-bottom: 20px;">Real-time metrics and performance monitoring</p>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 20px;">
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
    
    for exp in experience_data:
        st.markdown(f"""
        <div class="timeline-item">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <h3 style="color: white; font-size: 1.3rem; margin: 0;">{exp['title']}</h3>
                <span style="color: #10B981; font-size: 0.9rem;">{exp['period']}</span>
            </div>
            <h4 style="color: #8B5CF6; font-size: 1.1rem; margin-bottom: 15px;">{exp['company']}</h4>
            <ul style="color: #9CA3AF; line-height: 1.8;">
        """, unsafe_allow_html=True)
        
        for achievement in exp['achievements']:
            st.markdown(f'<li>{achievement}</li>', unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<h1 class="section-title">Let\'s Connect</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #34D399; font-size: 2rem; margin-bottom: 20px;">Ready to Build the Future Together</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.1rem; margin-bottom: 40px;">I\'m actively seeking opportunities to architect and scale AI solutions. If you\'re looking for a passionate engineer to solve complex challenges in MLOps and DevOps, let\'s connect.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 30px; background: rgba(0, 0, 0, 0.6); border-radius: 16px;">
            <span style="font-size: 3rem;">📧</span>
            <h3 style="color: white; margin: 15px 0;">Email</h3>
            <p style="color: #9CA3AF;">mukeshyadavp91@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 30px; background: rgba(0, 0, 0, 0.6); border-radius: 16px;">
            <span style="font-size: 3rem;">💼</span>
            <h3 style="color: white; margin: 15px 0;">LinkedIn</h3>
            <p style="color: #9CA3AF;">linkedin.com/in/mukesh-mlops</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 30px; background: rgba(0, 0, 0, 0.6); border-radius: 16px;">
            <span style="font-size: 3rem;">🐙</span>
            <h3 style="color: white; margin: 15px 0;">GitHub</h3>
            <p style="color: #9CA3AF;">github.com/MukeshPyatla</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <a href="mailto:mukeshyadavp91@gmail.com" class="btn-primary">Get In Touch</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 