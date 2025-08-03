import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Mukesh Yadav - MLOps Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with Bootstrap and light theme
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    @import url('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css');
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #f1f5f9 100%);
        color: #1e293b;
        scroll-behavior: smooth;
        overflow-x: hidden;
        line-height: 1.6;
    }
    
    .main {
        background: transparent;
        color: #1e293b;
    }
    
    .stApp {
        background: transparent;
    }
    
    /* Ultra Modern Animated Background */
    .gradient-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: -2;
        background: 
            radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(139, 92, 246, 0.05) 0%, transparent 50%),
            linear-gradient(135deg, rgba(248, 250, 252, 0.9) 0%, rgba(241, 245, 249, 0.7) 100%);
    }
    
    .gradient-blob {
        position: absolute;
        border-radius: 100%;
        filter: blur(150px);
        opacity: 0.6;
    }
    
    .blob1 {
        width: 800px;
        height: 800px;
        background: linear-gradient(45deg, #3b82f6, #8b5cf6, #06b6d4);
        top: -300px;
        left: -300px;
        animation: float 25s ease-in-out infinite;
    }
    
    .blob2 {
        width: 900px;
        height: 900px;
        background: linear-gradient(45deg, #10b981, #3b82f6, #06b6d4);
        bottom: -400px;
        right: -400px;
        animation: float 30s ease-in-out infinite reverse;
    }
    
    .blob3 {
        width: 600px;
        height: 600px;
        background: linear-gradient(45deg, #f59e0b, #ef4444, #8b5cf6);
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        animation: pulse 20s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        33% { transform: translate(30px, -30px) rotate(120deg); }
        66% { transform: translate(-20px, 20px) rotate(240deg); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.3; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 0.6; transform: translate(-50%, -50%) scale(1.1); }
    }
    
    /* Ultra Modern Glass Navigation */
    .glass-nav {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border-bottom: 1px solid rgba(59, 130, 246, 0.2);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.1);
        position: relative;
    }
    
    .glass-nav::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.3), transparent);
    }
    
    /* Hero Section */
    .hero-section {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 2rem;
    }
    
    .hero-content {
        text-align: center;
        max-width: 1000px;
        z-index: 2;
        position: relative;
    }
    
    .hero-logo {
        width: 120px;
        height: 120px;
        background: linear-gradient(45deg, #3b82f6, #8b5cf6);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 2rem;
        font-size: 3rem;
        color: white;
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.3);
        animation: pulse 2s infinite;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #1e293b, #475569);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #64748b;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 3rem;
        line-height: 1.6;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Social Buttons */
    .social-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 3rem;
        flex-wrap: wrap;
    }
    
    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.9);
        color: #1e293b;
        border: 2px solid rgba(59, 130, 246, 0.2);
        padding: 12px 24px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(10px);
    }
    
    .social-btn:hover {
        background: #3b82f6;
        color: white;
        border-color: #3b82f6;
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
        text-decoration: none;
    }
    
    .social-btn i {
        font-size: 1.2rem;
    }
    
    /* CTA Buttons */
    .cta-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: linear-gradient(45deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 1.1rem;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
        color: white;
        text-decoration: none;
    }
    
    .btn-secondary {
        background: transparent;
        color: #1e293b;
        border: 2px solid #3b82f6;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 1.1rem;
    }
    
    .btn-secondary:hover {
        background: #3b82f6;
        color: white;
        transform: translateY(-3px);
        text-decoration: none;
    }
    
    /* Section Styles */
    .section {
        padding: 5rem 2rem;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        margin: 2rem 0;
        border-radius: 20px;
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 3rem;
        color: #1e293b;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4);
        border-radius: 2px;
        animation: shimmer 2s ease-in-out infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .section-subtitle {
        text-align: center;
        color: #3b82f6;
        font-weight: 600;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.9rem;
    }
    
    /* Skills Grid */
    .skills-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .skill-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .skill-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    }
    
    .skill-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.2);
        border-color: #3b82f6;
    }
    
    .skill-icon {
        font-size: 2.5rem;
        color: #3b82f6;
        margin-bottom: 1rem;
    }
    
    .skill-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .skill-tag {
        background: rgba(59, 130, 246, 0.1);
        color: #3b82f6;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        border: 1px solid rgba(59, 130, 246, 0.2);
        font-weight: 500;
    }
    
    /* Projects Grid */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .project-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.2);
        border-color: #3b82f6;
    }
    
    .project-icon {
        font-size: 2rem;
        color: #3b82f6;
        margin-bottom: 1rem;
    }
    
    .project-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .project-desc {
        color: #64748b;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .project-link {
        color: #3b82f6;
        text-decoration: none;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .project-link:hover {
        color: #1d4ed8;
        text-decoration: none;
        transform: translateX(5px);
    }
    
    /* Experience Timeline */
    .timeline {
        max-width: 800px;
        margin: 0 auto;
        position: relative;
    }
    
    .timeline::before {
        content: '';
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, #3b82f6, #8b5cf6);
        transform: translateX(-50%);
    }
    
    .timeline-item {
        position: relative;
        margin-bottom: 3rem;
        width: 45%;
    }
    
    .timeline-item:nth-child(odd) {
        left: 0;
    }
    
    .timeline-item:nth-child(even) {
        left: 55%;
    }
    
    .timeline-content {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        position: relative;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .timeline-content:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(59, 130, 246, 0.2);
        border-color: #3b82f6;
    }
    
    .timeline-content::before {
        content: '';
        position: absolute;
        top: 20px;
        width: 0;
        height: 0;
        border: 10px solid transparent;
    }
    
    .timeline-item:nth-child(odd) .timeline-content::before {
        right: -20px;
        border-left-color: rgba(255, 255, 255, 0.9);
    }
    
    .timeline-item:nth-child(even) .timeline-content::before {
        left: -20px;
        border-right-color: rgba(255, 255, 255, 0.9);
    }
    
    .timeline-dot {
        position: absolute;
        top: 20px;
        width: 20px;
        height: 20px;
        background: #3b82f6;
        border-radius: 50%;
        border: 4px solid #f8fafc;
    }
    
    .timeline-item:nth-child(odd) .timeline-dot {
        right: -60px;
    }
    
    .timeline-item:nth-child(even) .timeline-dot {
        left: -60px;
    }
    
    .timeline-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .timeline-company {
        color: #3b82f6;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .timeline-period {
        color: #64748b;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .timeline-desc {
        color: #64748b;
        line-height: 1.6;
    }
    
    /* Contact Section */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .contact-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .contact-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(59, 130, 246, 0.2);
        border-color: #3b82f6;
    }
    
    .contact-icon {
        font-size: 2.5rem;
        color: #3b82f6;
        margin-bottom: 1rem;
    }
    
    .contact-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .contact-value {
        color: #64748b;
        font-size: 1rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .social-buttons {
            flex-direction: column;
            align-items: center;
        }
        
        .cta-buttons {
            flex-direction: column;
            align-items: center;
        }
        
        .timeline::before {
            left: 20px;
        }
        
        .timeline-item {
            width: 100%;
            left: 0 !important;
        }
        
        .timeline-item .timeline-dot {
            left: -40px !important;
        }
        
        .timeline-item .timeline-content::before {
            left: -20px !important;
            border-right-color: rgba(255, 255, 255, 0.9) !important;
        }
    }
    
    /* Streamlit overrides */
    .stButton > button {
        background: linear-gradient(45deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
    }
    
    /* Animation Classes */
    .fade-in {
        animation: fadeIn 0.6s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    </style>
    """, unsafe_allow_html=True)

# Data
skills_data = {
    "Cloud/DevOps": {
        "icon": "☁️",
        "skills": ["Azure", "AWS", "Terraform (IaC)", "Kubernetes", "Docker", "CI/CD (GitLab CI, Jenkins, ArgoCD, Tekton)", "GitOps"]
    },
    "AI/ML Frameworks": {
        "icon": "🤖",
        "skills": ["LangChain", "PyTorch", "TensorFlow", "FastAPI", "TensorRT", "Flower", "MLflow", "BentoML"]
    },
    "Data & Databases": {
        "icon": "📊",
        "skills": ["SQL", "Vector Databases (Pinecone, Qdrant)", "Pandas", "Spark", "DVC", "LakeFS"]
    },
    "Monitoring & Observability": {
        "icon": "📈",
        "skills": ["Prometheus", "Grafana", "ELK Stack", "Backstage", "Weights & Biases (W&B)"]
    },
    "Languages": {
        "icon": "💻",
        "skills": ["Python", "SQL", "Bash", "C++", "Go (learning)"]
    },
    "AI/ML Concepts": {
        "icon": "🧠",
        "skills": ["MLOps", "GenAI", "RAG", "Federated Learning (FL)", "Homomorphic Encryption (HE)", "Transformers", "NLP"]
    },
    "Blockchain": {
        "icon": "⛓️",
        "skills": ["Ethereum", "Smart Contracts (Solidity)", "Immutable Ledgers"]
    },
    "Operating Systems": {
        "icon": "🖥️",
        "skills": ["Linux (RHEL, Ubuntu)", "Windows"]
    },
    "Networking": {
        "icon": "🌐",
        "skills": ["VPC/VNet", "DNS", "Load Balancers", "Security Groups"]
    }
}

projects_data = [
    {
        "title": "Guardian AI: Zero-Trust Multi-Modal Compliance & Risk Auditor",
        "description": "Engineered a privacy-preserving MLOps pipeline using Federated Learning (FL) and Homomorphic Encryption (HE) to securely audit multi-modal data, and integrated a private blockchain to provide an immutable, verifiable audit trail.",
        "link": "https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/",
        "icon": "🛡️"
    },
    {
        "title": "DeFi Fraud Detection MLOps Pipeline",
        "description": "A comprehensive MLOps pipeline for detecting fraud in Decentralized Finance (DeFi) transactions with a private-by-design approach and modern Streamlit dashboard.",
        "link": "https://defifraud-detectionmlopspipeline.streamlit.app/",
        "icon": "💰"
    },
    {
        "title": "MLOps QA System",
        "description": "LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo",
        "link": "https://mlops-app-system.streamlit.app/",
        "icon": "❓"
    },
    {
        "title": "Azure MLOps Anomaly Detector",
        "description": "End-to-End MLOps pipeline for anomaly detection on Azure",
        "link": "https://azure-mlops-anomaly-detector.streamlit.app/",
        "icon": "🔍"
    },
    {
        "title": "MLOps Secure Churn",
        "description": "Secure customer churn prediction with MLOps pipeline",
        "link": "https://mlops-secure-churn.streamlit.app/",
        "icon": "📉"
    },
    {
        "title": "MLOps Demand Forecasting",
        "description": "Advanced demand forecasting with MLOps pipeline",
        "link": "https://mlops-demand-forecasting.streamlit.app/",
        "icon": "📈"
    }
]

experience_data = [
    {
        "company": "Aidoc",
        "position": "MLOps Engineer",
        "period": "Oct 2023 - Present",
        "description": [
            "Engineered and implemented a robust monitoring and alerting system with Prometheus and Grafana to track critical LLM performance metrics, ensuring GenAI model reliability and reducing the mean time to detection for issues by over 70%.",
            "Designed and deployed a CI/CD pipeline for GenAI applications using GitLab CI, decreasing model deployment time by 80% and enabling faster RAG framework updates and feature delivery.",
            "Automated the provisioning of cloud infrastructure on Azure using Terraform, to support a full RAG stack including Vector Databases, eliminating manual setup and reducing infrastructure costs by 20% by optimizing resource allocation.",
            "Developed containerized GenAI microservices with BentoML and Kubernetes, ensuring production environments were scalable and consistent with development, which solved the problem of 'it works on my machine' for multi-tool AI stacks.",
            "Architected and integrated a private blockchain as an immutable audit trail for MLOps pipeline activities, ensuring full compliance and providing a verifiable record of every model change and data event."
        ]
    },
    {
        "company": "Missouri University of Science and Technology",
        "position": "Graduate Research Assistant",
        "period": "Apr 2023 - Sep 2023",
        "location": "Rolla, MO",
        "description": [
            "Managed and scaled cloud computing resources on Azure to support computationally intensive machine learning experiments, ensuring project success and providing a stable environment for a team of 10 researchers.",
            "Implemented Data Version Control (DVC) for project data and machine learning models to solve the problem of reproducibility, establishing an auditable lineage for all experiments and enabling seamless team collaboration.",
            "Designed and executed CI/CD pipelines with Prefect for data processing and model training workflows, reducing environment setup time by 90% and streamlining the research workflow.",
            "Managed and secured access controls to cloud resources for multiple research projects, ensuring data privacy and preventing unauthorized access in compliance with academic standards.",
            "Provided technical support and mentorship to junior researchers on cloud computing best practices, which improved team efficiency and reduced resource mismanagement by 15%."
        ]
    },
    {
        "company": "PineLabs",
        "position": "Junior Systems Administrator | DevOps Engineer",
        "period": "Jun 2021 - Dec 2022",
        "location": "Bengaluru, India",
        "description": [
            "Contributed to the development of a CI/CD pipeline using Jenkins and Docker to automate software deployments, which reduced deployment errors by 30% and significantly improved the development cycle.",
            "Automated routine system administration tasks using Bash and Python scripts, which solved the problem of manual labor and saved the team an average of 5 hours per week in server maintenance.",
            "Managed and maintained Linux servers for a team of 5 developers, ensuring system stability and security, and achieving 99.9% uptime for internal applications.",
            "Implemented a daily backup routine for all project data, which successfully prevented data loss during two critical system failures and ensured project continuity.",
            "Assisted in troubleshooting and resolving infrastructure issues, which reduced downtime by 25% and allowed the development team to focus on coding."
        ]
    }
]

def create_mlops_animation():
    """Create an animated MLOps pipeline visualization"""
    fig = go.Figure()
    
    # Create a more sophisticated pipeline visualization
    pipeline_steps = [
        {"name": "Data Ingestion", "x": 0, "y": 0, "color": "#3b82f6", "icon": "📥"},
        {"name": "Preprocessing", "x": 2, "y": 0, "color": "#8b5cf6", "icon": "🔧"},
        {"name": "Model Training", "x": 4, "y": 0, "color": "#06b6d4", "icon": "🤖"},
        {"name": "Validation", "x": 6, "y": 0, "color": "#10b981", "icon": "✅"},
        {"name": "Deployment", "x": 8, "y": 0, "color": "#f59e0b", "icon": "🚀"},
        {"name": "Monitoring", "x": 10, "y": 0, "color": "#ef4444", "icon": "📊"}
    ]
    
    # Add pipeline nodes with icons
    for step in pipeline_steps:
        fig.add_trace(go.Scatter(
            x=[step["x"]],
            y=[step["y"]],
            mode='markers+text',
            marker=dict(
                size=40,
                color=step["color"],
                line=dict(width=3, color='white'),
                symbol='circle'
            ),
            text=step["icon"],
            textposition="middle center",
            textfont=dict(size=16, color='white'),
            name=step["name"],
            showlegend=False
        ))
        
        # Add step labels
        fig.add_trace(go.Scatter(
            x=[step["x"]],
            y=[step["y"] - 0.8],
            mode='text',
            text=step["name"],
            textposition="middle center",
            textfont=dict(size=10, color='#64748b'),
            showlegend=False
        ))
    
    # Add connecting lines with gradient
    for i in range(len(pipeline_steps) - 1):
        fig.add_trace(go.Scatter(
            x=[pipeline_steps[i]["x"], pipeline_steps[i+1]["x"]],
            y=[pipeline_steps[i]["y"], pipeline_steps[i+1]["y"]],
            mode='lines',
            line=dict(color='#3b82f6', width=4),
            showlegend=False
        ))
    
    # Add floating tech elements
    tech_elements = [
        {"name": "K8s", "x": 1, "y": 1.5, "color": "#3b82f6", "icon": "☸️"},
        {"name": "Docker", "x": 3, "y": -1.5, "color": "#8b5cf6", "icon": "🐳"},
        {"name": "Terraform", "x": 5, "y": 1.5, "color": "#06b6d4", "icon": "🏗️"},
        {"name": "Prometheus", "x": 7, "y": -1.5, "color": "#10b981", "icon": "📈"},
        {"name": "Grafana", "x": 9, "y": 1.5, "color": "#f59e0b", "icon": "📊"}
    ]
    
    for elem in tech_elements:
        fig.add_trace(go.Scatter(
            x=[elem["x"]],
            y=[elem["y"]],
            mode='markers+text',
            marker=dict(
                size=25,
                color=elem["color"],
                symbol='diamond',
                line=dict(width=2, color='white')
            ),
            text=elem["icon"],
            textposition="middle center",
            textfont=dict(size=12, color='white'),
            name=elem["name"],
            showlegend=False
        ))
    
    fig.update_layout(
        title="MLOps Pipeline Architecture",
        title_font=dict(size=24, color='#3b82f6'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, showticklabels=False, range=[-1, 11]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-2, 2]),
        margin=dict(l=0, r=0, t=80, b=0),
        height=400
    )
    
    return fig

def main():
    load_css()
    
    # Animated Background
    st.markdown("""
    <div class="gradient-bg">
        <div class="gradient-blob blob1"></div>
        <div class="gradient-blob blob2"></div>
        <div class="gradient-blob blob3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-logo">🚀</div>
            <h1 class="hero-title">Hello, I'm Mukesh</h1>
            <h2 class="hero-subtitle">MLOps Engineer</h2>
            <p class="hero-description">
                A passionate MLOps Engineer building scalable and secure AI pipelines on Azure. 
                Specialized in automation, data-driven solutions, and robust model deployment with expertise in 
                Federated Learning, Homomorphic Encryption, and blockchain-based audit trails.
            </p>
            
            <div class="social-buttons">
                <a href="https://github.com/MukeshPyatla" target="_blank" class="social-btn">
                    <i class="fab fa-github"></i>
                    GitHub
                </a>
                <a href="https://linkedin.com/in/mukesh-yadav-mlops" target="_blank" class="social-btn">
                    <i class="fab fa-linkedin"></i>
                    LinkedIn
                </a>
                <a href="https://mukeshyadav.github.io" target="_blank" class="social-btn">
                    <i class="fas fa-globe"></i>
                    Portfolio
                </a>
                <a href="mailto:mukeshyadavp91@gmail.com" class="social-btn">
                    <i class="fas fa-envelope"></i>
                    Email
                </a>
            </div>
            
            <div class="cta-buttons">
                <a href="#contact" class="btn-primary">Hire Me</a>
                <a href="mailto:mukeshyadavp91@gmail.com" class="btn-secondary">Get In Touch</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills Section
    st.markdown("""
    <div class="section">
        <div class="section-subtitle">Technical Expertise</div>
        <h2 class="section-title">Skills & Technologies</h2>
        <div class="skills-container">
            <div class="skills-grid">
    """, unsafe_allow_html=True)
    
    for category, data in skills_data.items():
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{data['icon']}</div>
            <h3 class="skill-title">{category}</h3>
            <div class="skill-tags">
        """, unsafe_allow_html=True)
        
        for skill in data['skills']:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    # Projects Section
    st.markdown("""
    <div class="section">
        <div class="section-subtitle">Live Demonstrations</div>
        <h2 class="section-title">Projects & Dashboards</h2>
        <div class="skills-container">
            <div class="projects-grid">
    """, unsafe_allow_html=True)
    
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-icon">{project['icon']}</div>
            <h3 class="project-title">{project['title']}</h3>
            <p class="project-desc">{project['description']}</p>
            <a href="{project['link']}" target="_blank" class="project-link">
                View Live Dashboard <i class="fas fa-external-link-alt"></i>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    # MLOps Animation Section
    st.markdown("""
    <div class="section">
        <div class="section-subtitle">Pipeline Architecture</div>
        <h2 class="section-title">MLOps Pipeline Visualization</h2>
    """, unsafe_allow_html=True)
    
    fig = create_mlops_animation()
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Experience Section
    st.markdown("""
    <div class="section">
        <div class="section-subtitle">Professional Journey</div>
        <h2 class="section-title">Work Experience</h2>
        <div class="timeline">
    """, unsafe_allow_html=True)
    
    for i, exp in enumerate(experience_data):
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h3 class="timeline-title">{exp['position']}</h3>
                <div class="timeline-company">{exp['company']}</div>
                <div class="timeline-period">{exp['period']}{' - ' + exp['location'] if 'location' in exp else ''}</div>
                <div class="timeline-desc">
        """, unsafe_allow_html=True)
        
        for desc in exp['description']:
            st.markdown(f"• {desc}<br>", unsafe_allow_html=True)
        
        st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Contact Section
    st.markdown("""
    <div class="section">
        <div class="section-subtitle">Get In Touch</div>
        <h2 class="section-title">Contact Information</h2>
        <div class="contact-grid">
            <div class="contact-card">
                <div class="contact-icon">📧</div>
                <div class="contact-title">Email</div>
                <div class="contact-value">mukeshyadavp91@gmail.com</div>
            </div>
            <div class="contact-card">
                <div class="contact-icon">📱</div>
                <div class="contact-title">Phone</div>
                <div class="contact-value">+1-573-639-8737</div>
            </div>
            <div class="contact-card">
                <div class="contact-icon">🎓</div>
                <div class="contact-title">Education</div>
                <div class="contact-value">Master of Science, Computer Science<br>Missouri University of Science and Technology</div>
            </div>
            <div class="contact-card">
                <div class="contact-icon">🏆</div>
                <div class="contact-title">Certifications</div>
                <div class="contact-value">Azure Administrator Associate (AZ-104)<br>AWS Certified Developer - Associate</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 