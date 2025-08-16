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

# Custom CSS for modern styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
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
    
    .project-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 32px;
        margin: 24px 0;
        backdrop-filter: blur(20px);
        transition: all 0.4s ease;
        position: relative;
        cursor: pointer;
    }
    
    .project-card:hover {
        border-color: rgba(135, 206, 250, 0.3);
        box-shadow: 0 25px 50px -12px rgba(135, 206, 250, 0.25);
        transform: translateY(-4px);
    }
    
    .project-preview {
        background: rgba(0, 0, 0, 0.8);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(135, 206, 250, 0.2);
    }
    
    .project-preview iframe {
        width: 100%;
        height: 400px;
        border: none;
        border-radius: 8px;
        background: white;
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
    
    .fullscreen-modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.95);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }
    
    .modal-content {
        background: #1a1a1a;
        border-radius: 20px;
        padding: 30px;
        max-width: 90%;
        max-height: 90%;
        overflow: auto;
        border: 1px solid rgba(135, 206, 250, 0.3);
    }
    
    .modal-close {
        position: absolute;
        top: 20px;
        right: 20px;
        background: none;
        border: none;
        color: white;
        font-size: 2rem;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Portfolio data
portfolio_data = {
    'personal': {
        'name': "Mukesh Yadav",
        'title': "MLOPS & DEVOPS ENGINEER",
        'subtitle': "Building Intelligent Systems on Azure & AWS Cloud",
        'description': "Specializing in end-to-end MLOps pipelines, automated CI/CD workflows, and scalable cloud infrastructure. Passionate about deploying production-ready AI/ML systems with robust monitoring and observability.",
        'email': "mukeshyadavp91@gmail.com",
        'linkedin': "linkedin.com/in/mukesh-mlops",
        'github': "github.com/MukeshPyatla"
    },
    'metrics': [
        {'value': "80%", 'label': "Faster Deployments"},
        {'value': "70%", 'label': "Reduced MTTR"},
        {'value': "47", 'label': "Technical Skills"},
        {'value': "6", 'label': "Live Projects"}
    ],
    'skills': {
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
    },
    'projects': [
        {
            'title': 'DeFi Fraud Detection',
            'description': 'Comprehensive MLOps pipeline for detecting fraud in Decentralized Finance transactions with private-by-design approach and modern Streamlit dashboard.',
            'status': 'LIVE',
            'tech': ['Python', 'Streamlit', 'MLOps'],
            'github': 'https://github.com/MukeshPyatla/DeFi_Fraud-Detection_MLOps_Pipeline',
            'demo': 'https://defifraud-detectionmlopspipeline.streamlit.app/',
            'icon': '🛡️',
            'preview_url': 'https://defifraud-detectionmlopspipeline.streamlit.app/',
            'features': [
                'Real-time fraud detection',
                'Private-by-design architecture',
                'MLOps pipeline automation',
                'Interactive dashboard'
            ]
        },
        {
            'title': 'Guardian AI Auditor',
            'description': 'Zero-trust multi-modal compliance & risk auditor with privacy-preserving MLOps pipeline using Federated Learning and Homomorphic Encryption.',
            'status': 'LIVE',
            'tech': ['Federated Learning', 'Homomorphic Encryption', 'Blockchain'],
            'github': 'https://github.com/MukeshPyatla/guardian-ai-auditor',
            'demo': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
            'icon': '🤖',
            'preview_url': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
            'features': [
                'Zero-trust architecture',
                'Federated learning',
                'Homomorphic encryption',
                'Multi-modal compliance'
            ]
        },
        {
            'title': 'MLOps Q&A System',
            'description': 'LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo with real-time updates.',
            'status': 'LIVE',
            'tech': ['LLM', 'RAG', 'Vector DB'],
            'github': 'https://github.com/MukeshPyatla/mlops-qa-system',
            'demo': 'https://mlops-app-system.streamlit.app/',
            'icon': '💬',
            'preview_url': 'https://mlops-app-system.streamlit.app/',
            'features': [
                'LLM-powered Q&A',
                'Multi-source integration',
                'Automated freshness pipeline',
                'Real-time updates'
            ]
        },
        {
            'title': 'Azure Anomaly Detector',
            'description': 'End-to-End MLOps pipeline for anomaly detection on Azure with real-time monitoring and alerting system.',
            'status': 'LIVE',
            'tech': ['Azure', 'MLOps', 'Python'],
            'github': 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector',
            'demo': 'https://azure-mlops-anomaly-detector.streamlit.app/',
            'icon': '📡',
            'preview_url': 'https://azure-mlops-anomaly-detector.streamlit.app/',
            'features': [
                'Azure integration',
                'Real-time monitoring',
                'Anomaly detection',
                'Alerting system'
            ]
        },
        {
            'title': 'Secure Churn Prediction',
            'description': 'Privacy-preserving customer churn prediction with PII masking and SHAP explainability in Azure Databricks.',
            'status': 'LIVE',
            'tech': ['Azure Databricks', 'SHAP', 'Data Security'],
            'github': 'https://github.com/MukeshPyatla/MLOPS-Secure-Churn',
            'demo': 'https://mlops-secure-churn.streamlit.app/',
            'icon': '👤',
            'preview_url': 'https://mlops-secure-churn.streamlit.app/',
            'features': [
                'PII masking',
                'SHAP explainability',
                'Privacy preservation',
                'Azure Databricks'
            ]
        },
        {
            'title': 'Demand Forecasting',
            'description': 'Scalable demand forecasting system with integrated MLOps for continuous training and monitoring.',
            'status': 'LIVE',
            'tech': ['Python', 'Forecasting', 'MLOps'],
            'github': 'https://github.com/MukeshPyatla/MLOPS-Demand-Forecasting',
            'demo': 'https://mlops-demand-forecasting.streamlit.app/',
            'icon': '📈',
            'preview_url': 'https://mlops-demand-forecasting.streamlit.app/',
            'features': [
                'Scalable forecasting',
                'Continuous training',
                'MLOps integration',
                'Real-time monitoring'
            ]
        }
    ],
    'experience': [
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
}

def create_hero_section():
    st.markdown(f"""
    <div class="hero-section">
        <div style="position: relative; z-index: 1;">
            <h1 class="section-title">{portfolio_data['personal']['name']}</h1>
            <h2 style="font-size: 2.5rem; color: #87CEEB; margin-bottom: 20px; text-align: center; font-weight: 600;">{portfolio_data['personal']['title']}</h2>
            <h3 style="font-size: 1.5rem; color: #9CA3AF; margin-bottom: 40px; text-align: center; font-weight: 400;">{portfolio_data['personal']['subtitle']}</h3>
            <p style="font-size: 1.3rem; color: #D1D5DB; line-height: 1.8; margin-bottom: 40px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                {portfolio_data['personal']['description']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    for i, metric in enumerate(portfolio_data['metrics']):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            """, unsafe_allow_html=True)

def create_about_section():
    st.markdown('<h1 class="section-title">About Me</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Architecting the future of AI infrastructure</p>', unsafe_allow_html=True)
    
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

def create_skills_section():
    st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Comprehensive skills across the MLOps and DevOps ecosystem</p>', unsafe_allow_html=True)
    
    # Create tabs for different skill categories
    skill_tabs = st.tabs([f"{data['icon']} {category}" for category, data in portfolio_data['skills'].items()])
    
    for i, (category, data) in enumerate(portfolio_data['skills'].items()):
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

def create_projects_section():
    st.markdown('<h1 class="section-title">Featured Projects</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">End-to-end MLOps and DevOps solutions with live dashboards</p>', unsafe_allow_html=True)
    
    for project in portfolio_data['projects']:
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
            
            <div style="margin-bottom: 15px;">
                <h4 style="color: #87CEEB; margin-bottom: 10px;">Key Features:</h4>
                <ul style="color: #9CA3AF; margin-left: 20px;">
                    {''.join([f'<li style="margin-bottom: 5px;">{feature}</li>' for feature in project['features']])}
                </ul>
            </div>
            
            <div style="margin-bottom: 25px;">
                {''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech']])}
            </div>

            <!-- Live Preview Section -->
            <div style="margin-bottom: 25px;">
                <h4 style="color: #87CEEB; margin-bottom: 15px;">Live Preview:</h4>
                <div style="position: relative; border-radius: 12px; overflow: hidden; border: 1px solid rgba(135, 206, 250, 0.2); background: rgba(0, 0, 0, 0.8);">
                    <iframe 
                        src="{project['preview_url']}" 
                        title="{project['title']} Preview"
                        style="width: 100%; height: 300px; border: none; background: white; display: block;"
                        sandbox="allow-scripts allow-same-origin allow-forms"
                    ></iframe>
                    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.7); display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease;" 
                         onmouseover="this.style.opacity='1'" 
                         onmouseout="this.style.opacity='0'">
                        <button 
                            style="background: linear-gradient(135deg, #87CEEB, #B0E0E6); color: #000000; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; font-size: 0.9rem;"
                            onmouseover="this.style.transform='scale(1.05)'"
                            onmouseout="this.style.transform='scale(1)'"
                            onclick="openFullScreenModal('{project['preview_url']}', '{project['title']}', '{project['description']}', '{project['github']}', '{project['demo']}')"
                        >
                            🔍 View Full Screen
                        </button>
                    </div>
                </div>
            </div>
            
            <div style="display: flex; gap: 15px;">
                <a href="{project['github']}" target="_blank" class="btn-secondary">GitHub</a>
                <a href="{project['demo']}" target="_blank" class="btn-primary">Live Demo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Add JavaScript for full-screen modal functionality
    st.markdown("""
    <script>
    function openFullScreenModal(url, title, description, github, demo) {
        // Create modal overlay
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;
        
        // Create modal content
        const modalContent = document.createElement('div');
        modalContent.style.cssText = `
            background: #1a1a1a;
            border-radius: 20px;
            padding: 30px;
            max-width: 95%;
            max-height: 95%;
            overflow: auto;
            border: 1px solid rgba(135, 206, 250, 0.3);
            position: relative;
            transform: scale(0.8);
            transition: transform 0.3s ease;
        `;
        
        // Create close button
        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '✕';
        closeBtn.style.cssText = `
            position: absolute;
            top: 20px;
            right: 20px;
            background: none;
            border: none;
            color: white;
            font-size: 2rem;
            cursor: pointer;
            z-index: 10000;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        `;
        
        closeBtn.onmouseover = () => {
            closeBtn.style.color = '#87CEEB';
            closeBtn.style.background = 'rgba(135, 206, 250, 0.1)';
        };
        
        closeBtn.onmouseout = () => {
            closeBtn.style.color = 'white';
            closeBtn.style.background = 'none';
        };
        
        // Create modal header
        const modalHeader = document.createElement('div');
        modalHeader.style.cssText = 'margin-bottom: 20px; padding-right: 50px;';
        modalHeader.innerHTML = `
            <h2 style="color: white; font-size: 2rem; margin-bottom: 10px; font-weight: 600;">${title}</h2>
            <p style="color: #9CA3AF; font-size: 1.1rem; line-height: 1.6;">${description}</p>
        `;
        
        // Create iframe container
        const iframeContainer = document.createElement('div');
        iframeContainer.style.cssText = 'margin-bottom: 20px;';
        
        const iframe = document.createElement('iframe');
        iframe.src = url;
        iframe.title = title + ' Full Screen';
        iframe.style.cssText = 'width: 100%; height: 600px; border: none; border-radius: 12px; background: white;';
        iframe.sandbox = 'allow-scripts allow-same-origin allow-forms';
        
        iframeContainer.appendChild(iframe);
        
        // Create modal footer
        const modalFooter = document.createElement('div');
        modalFooter.style.cssText = 'text-align: center;';
        
        const modalLinks = document.createElement('div');
        modalLinks.style.cssText = 'display: flex; gap: 15px; justify-content: center;';
        modalLinks.innerHTML = `
            <a href="${github}" target="_blank" class="btn-secondary" style="min-width: 150px;">View on GitHub</a>
            <a href="${demo}" target="_blank" class="btn-primary" style="min-width: 150px;">Open in New Tab</a>
        `;
        
        modalFooter.appendChild(modalLinks);
        
        // Assemble modal
        modalContent.appendChild(closeBtn);
        modalContent.appendChild(modalHeader);
        modalContent.appendChild(iframeContainer);
        modalContent.appendChild(modalFooter);
        modal.appendChild(modalContent);
        
        // Add to page
        document.body.appendChild(modal);
        
        // Animate in
        setTimeout(() => {
            modal.style.opacity = '1';
            modalContent.style.transform = 'scale(1)';
        }, 10);
        
        // Close functionality
        const closeModal = () => {
            modal.style.opacity = '0';
            modalContent.style.transform = 'scale(0.8)';
            setTimeout(() => {
                document.body.removeChild(modal);
            }, 300);
        };
        
        closeBtn.onclick = closeModal;
        modal.onclick = (e) => {
            if (e.target === modal) closeModal();
        };
        
        // ESC key to close
        const handleEscape = (e) => {
            if (e.key === 'Escape') closeModal();
        };
        document.addEventListener('keydown', handleEscape);
        
        // Clean up event listener when modal closes
        modal.addEventListener('transitionend', () => {
            if (modal.style.opacity === '0') {
                document.removeEventListener('keydown', handleEscape);
            }
        });
    }
    </script>
    """, unsafe_allow_html=True)

def create_experience_section():
    st.markdown('<h1 class="section-title">Professional Journey</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Building the future of AI infrastructure</p>', unsafe_allow_html=True)
    
    for exp in portfolio_data['experience']:
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

def create_contact_section():
    st.markdown('<h1 class="section-title">Let\'s Connect</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #6366F1; font-size: 2.5rem; margin-bottom: 20px; font-weight: 600;">Ready to Build the Future Together</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 50px; max-width: 600px; margin-left: auto; margin-right: auto;">I\'m actively seeking opportunities to architect and scale AI solutions. If you\'re looking for a passionate engineer to solve complex challenges in MLOps and DevOps, let\'s connect.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    contact_info = [
        {'icon': '📧', 'title': 'Email', 'value': portfolio_data['personal']['email']},
        {'icon': '💼', 'title': 'LinkedIn', 'value': portfolio_data['personal']['linkedin']},
        {'icon': '🐙', 'title': 'GitHub', 'value': portfolio_data['personal']['github']}
    ]
    
    for i, contact in enumerate(contact_info):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 40px; background: rgba(255, 255, 255, 0.02); border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
                <span style="font-size: 3rem;">{contact['icon']}</span>
                <h3 style="color: white; margin: 20px 0; font-weight: 600;">{contact['title']}</h3>
                <p style="color: #9CA3AF; font-size: 1.1rem;">{contact['value']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="mailto:mukeshyadavp91@gmail.com" class="btn-primary">Get In Touch</a>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Hero Section
    create_hero_section()
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # About Section
    create_about_section()
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Skills Section
    create_skills_section()
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Projects Section
    create_projects_section()
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Experience Section
    create_experience_section()
    
    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Contact Section
    create_contact_section()

if __name__ == "__main__":
    main()
