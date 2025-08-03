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

# Custom CSS with completely new design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    * {
        font-family: 'Space Grotesk', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: #0a0a0a;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    .main {
        background: #0a0a0a;
        color: #ffffff;
    }
    
    .stApp {
        background: #0a0a0a;
    }
    
    /* Animated Background */
    .bg-animation {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: 
            radial-gradient(circle at 25% 25%, rgba(255, 0, 100, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 75% 75%, rgba(0, 255, 200, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(100, 0, 255, 0.05) 0%, transparent 50%);
    }
    
    .floating-elements {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .floating-element {
        position: absolute;
        width: 4px;
        height: 4px;
        background: #ff0064;
        border-radius: 50%;
        animation: float 6s ease-in-out infinite;
    }
    
    .floating-element:nth-child(1) { top: 20%; left: 10%; animation-delay: 0s; }
    .floating-element:nth-child(2) { top: 60%; left: 80%; animation-delay: 1s; }
    .floating-element:nth-child(3) { top: 80%; left: 20%; animation-delay: 2s; }
    .floating-element:nth-child(4) { top: 40%; left: 90%; animation-delay: 3s; }
    .floating-element:nth-child(5) { top: 10%; left: 70%; animation-delay: 4s; }
    .floating-element:nth-child(6) { top: 90%; left: 60%; animation-delay: 5s; }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) scale(1); opacity: 0.3; }
        50% { transform: translateY(-20px) scale(1.2); opacity: 0.8; }
    }
    
    /* Navigation */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(10, 10, 10, 0.9);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .nav-logo {
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        color: #ffffff;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after {
        width: 100%;
    }
    
    /* Hero Section */
    .hero-section {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        position: relative;
    }
    
    .hero-content {
        text-align: center;
        max-width: 800px;
    }
    
    .hero-badge {
        display: inline-block;
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .hero-title span {
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #cccccc;
        margin-bottom: 2rem;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #999999;
        margin-bottom: 3rem;
        line-height: 1.6;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-bottom: 3rem;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #999999;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .hero-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 1rem;
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(255, 0, 100, 0.3);
        color: white;
        text-decoration: none;
    }
    
    .btn-secondary {
        background: transparent;
        color: #ffffff;
        border: 2px solid #ff0064;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 1rem;
    }
    
    .btn-secondary:hover {
        background: #ff0064;
        transform: translateY(-3px);
        text-decoration: none;
    }
    
    /* Section Styles */
    .section {
        padding: 6rem 2rem;
        position: relative;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 4rem;
    }
    
    .section-badge {
        display: inline-block;
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #999999;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Skills Grid */
    .skills-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
    }
    
    .skill-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
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
        height: 3px;
        background: linear-gradient(90deg, #ff0064, #00ffc8);
    }
    
    .skill-card:hover {
        transform: translateY(-10px);
        border-color: #ff0064;
        box-shadow: 0 20px 40px rgba(255, 0, 100, 0.2);
    }
    
    .skill-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .skill-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .skill-tag {
        background: rgba(255, 0, 100, 0.2);
        color: #ff0064;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        border: 1px solid rgba(255, 0, 100, 0.3);
        font-weight: 500;
    }
    
    /* Projects Grid */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
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
        height: 3px;
        background: linear-gradient(90deg, #ff0064, #00ffc8);
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        border-color: #ff0064;
        box-shadow: 0 20px 40px rgba(255, 0, 100, 0.2);
    }
    
    .project-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .project-icon {
        font-size: 2rem;
        color: #ff0064;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #ffffff;
        line-height: 1.3;
    }
    
    .project-desc {
        color: #999999;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .project-link {
        color: #ff0064;
        text-decoration: none;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .project-link:hover {
        color: #00ffc8;
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
        background: linear-gradient(to bottom, #ff0064, #00ffc8);
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
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        position: relative;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .timeline-content:hover {
        transform: translateY(-5px);
        border-color: #ff0064;
        box-shadow: 0 15px 30px rgba(255, 0, 100, 0.2);
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
        border-left-color: rgba(255, 255, 255, 0.05);
    }
    
    .timeline-item:nth-child(even) .timeline-content::before {
        left: -20px;
        border-right-color: rgba(255, 255, 255, 0.05);
    }
    
    .timeline-dot {
        position: absolute;
        top: 20px;
        width: 20px;
        height: 20px;
        background: #ff0064;
        border-radius: 50%;
        border: 4px solid #0a0a0a;
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
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .timeline-company {
        color: #ff0064;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .timeline-period {
        color: #999999;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .timeline-desc {
        color: #cccccc;
        line-height: 1.6;
    }
    
    /* Contact Grid */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        max-width: 1000px;
        margin: 0 auto;
    }
    
    .contact-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .contact-card:hover {
        transform: translateY(-5px);
        border-color: #ff0064;
        box-shadow: 0 15px 30px rgba(255, 0, 100, 0.2);
    }
    
    .contact-icon {
        font-size: 2.5rem;
        color: #ff0064;
        margin-bottom: 1rem;
    }
    
    .contact-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .contact-value {
        color: #999999;
        font-size: 1rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-stats {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-links {
            display: none;
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
            border-right-color: rgba(255, 255, 255, 0.05) !important;
        }
    }
    
    /* Streamlit overrides */
    .stButton > button {
        background: linear-gradient(45deg, #ff0064, #00ffc8);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(255, 0, 100, 0.3);
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

def create_mlops_visualization():
    """Create a modern MLOps pipeline visualization"""
    fig = go.Figure()
    
    # Create a more sophisticated pipeline visualization
    pipeline_steps = [
        {"name": "Data Ingestion", "x": 0, "y": 0, "color": "#ff0064", "icon": "📥"},
        {"name": "Preprocessing", "x": 2, "y": 0, "color": "#00ffc8", "icon": "🔧"},
        {"name": "Model Training", "x": 4, "y": 0, "color": "#ff0064", "icon": "🤖"},
        {"name": "Validation", "x": 6, "y": 0, "color": "#00ffc8", "icon": "✅"},
        {"name": "Deployment", "x": 8, "y": 0, "color": "#ff0064", "icon": "🚀"},
        {"name": "Monitoring", "x": 10, "y": 0, "color": "#00ffc8", "icon": "📊"}
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
            textfont=dict(size=10, color='#cccccc'),
            showlegend=False
        ))
    
    # Add connecting lines with gradient
    for i in range(len(pipeline_steps) - 1):
        fig.add_trace(go.Scatter(
            x=[pipeline_steps[i]["x"], pipeline_steps[i+1]["x"]],
            y=[pipeline_steps[i]["y"], pipeline_steps[i+1]["y"]],
            mode='lines',
            line=dict(color='#ff0064', width=4),
            showlegend=False
        ))
    
    # Add floating tech elements
    tech_elements = [
        {"name": "K8s", "x": 1, "y": 1.5, "color": "#ff0064", "icon": "☸️"},
        {"name": "Docker", "x": 3, "y": -1.5, "color": "#00ffc8", "icon": "🐳"},
        {"name": "Terraform", "x": 5, "y": 1.5, "color": "#ff0064", "icon": "🏗️"},
        {"name": "Prometheus", "x": 7, "y": -1.5, "color": "#00ffc8", "icon": "📈"},
        {"name": "Grafana", "x": 9, "y": 1.5, "color": "#ff0064", "icon": "📊"}
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
        title_font=dict(size=24, color='#ff0064'),
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
    <div class="bg-animation"></div>
    <div class="floating-elements">
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("""
    <div class="nav-container">
        <div class="nav-content">
            <div class="nav-logo">Mukesh Yadav</div>
            <div class="nav-links">
                <a href="#about" class="nav-link">About</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#experience" class="nav-link">Experience</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-badge">MLOps Engineer</div>
            <h1 class="hero-title">Building the Future of <span>AI Infrastructure</span></h1>
            <h2 class="hero-subtitle">Specialized in MLOps, DevOps, and Cloud Architecture</h2>
            <p class="hero-description">
                A passionate engineer building scalable and secure AI pipelines on Azure. 
                Expert in automation, data-driven solutions, and robust model deployment with expertise in 
                Federated Learning, Homomorphic Encryption, and blockchain-based audit trails.
            </p>
            
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-number">80%</div>
                    <div class="stat-label">Faster Deployments</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">70%</div>
                    <div class="stat-label">Reduced MTTR</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">20%</div>
                    <div class="stat-label">Cost Savings</div>
                </div>
            </div>
            
            <div class="hero-buttons">
                <a href="#projects" class="btn-primary">View Projects</a>
                <a href="mailto:mukeshyadavp91@gmail.com" class="btn-secondary">Get In Touch</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills Section
    st.markdown("""
    <div class="section" id="skills">
        <div class="section-header">
            <div class="section-badge">Technical Expertise</div>
            <h2 class="section-title">Skills & Technologies</h2>
            <p class="section-subtitle">Comprehensive expertise across the MLOps and DevOps ecosystem</p>
        </div>
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
    <div class="section" id="projects">
        <div class="section-header">
            <div class="section-badge">Live Demonstrations</div>
            <h2 class="section-title">Projects & Dashboards</h2>
            <p class="section-subtitle">End-to-end MLOps and DevOps solutions with live dashboards</p>
        </div>
        <div class="projects-grid">
    """, unsafe_allow_html=True)
    
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-header">
                <div class="project-icon">{project['icon']}</div>
                <h3 class="project-title">{project['title']}</h3>
            </div>
            <p class="project-desc">{project['description']}</p>
            <a href="{project['link']}" target="_blank" class="project-link">
                View Live Dashboard <i class="fas fa-external-link-alt"></i>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # MLOps Visualization Section
    st.markdown("""
    <div class="section">
        <div class="section-header">
            <div class="section-badge">Pipeline Architecture</div>
            <h2 class="section-title">MLOps Pipeline Visualization</h2>
            <p class="section-subtitle">Interactive visualization of the complete MLOps workflow</p>
        </div>
    """, unsafe_allow_html=True)
    
    fig = create_mlops_visualization()
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Experience Section
    st.markdown("""
    <div class="section" id="experience">
        <div class="section-header">
            <div class="section-badge">Professional Journey</div>
            <h2 class="section-title">Work Experience</h2>
            <p class="section-subtitle">My professional journey in MLOps and DevOps</p>
        </div>
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
    <div class="section" id="contact">
        <div class="section-header">
            <div class="section-badge">Get In Touch</div>
            <h2 class="section-title">Contact Information</h2>
            <p class="section-subtitle">Ready to build the future together? Let's connect!</p>
        </div>
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