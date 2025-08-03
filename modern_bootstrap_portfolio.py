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

# Custom CSS with Bootstrap and modern design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    /* Auto dark/light mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-primary: #0a0a0a;
            --bg-secondary: #111111;
            --bg-card: #1a1a1a;
            --text-primary: #ffffff;
            --text-secondary: #e0e0e0;
            --accent-red: #ff4444;
            --accent-red-hover: #ff6666;
            --border-color: #333333;
            --shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
    }
    
    @media (prefers-color-scheme: light) {
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --bg-card: #ffffff;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --accent-red: #dc3545;
            --accent-red-hover: #c82333;
            --border-color: #e9ecef;
            --shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
    }
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .main {
        background: var(--bg-primary);
        color: var(--text-primary);
    }
    
    .stApp {
        background: var(--bg-primary);
    }
    
    /* Hero Section - Full Screen */
    .hero-section {
        min-height: 100vh;
        background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 2rem;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(255, 68, 68, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 68, 68, 0.05) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .hero-content {
        text-align: center;
        max-width: 800px;
        z-index: 2;
        position: relative;
    }
    
    .hero-logo {
        width: 120px;
        height: 120px;
        background: linear-gradient(45deg, var(--accent-red), #ff6666);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 2rem;
        font-size: 3rem;
        color: white;
        box-shadow: var(--shadow);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, var(--accent-red), #ff8888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: var(--text-secondary);
        margin-bottom: 3rem;
        line-height: 1.6;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Social Buttons - Working */
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
        background: var(--bg-card);
        color: var(--text-primary);
        border: 2px solid var(--border-color);
        padding: 12px 24px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .social-btn:hover {
        background: var(--accent-red);
        color: white;
        border-color: var(--accent-red);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(255, 68, 68, 0.3);
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
        background: linear-gradient(45deg, var(--accent-red), #ff6666);
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
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(255, 68, 68, 0.4);
        color: white;
        text-decoration: none;
    }
    
    .btn-secondary {
        background: transparent;
        color: var(--text-primary);
        border: 2px solid var(--accent-red);
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
        background: var(--accent-red);
        color: white;
        transform: translateY(-3px);
        text-decoration: none;
    }
    
    /* Section Styles */
    .section {
        padding: 5rem 2rem;
        background: var(--bg-secondary);
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 3rem;
        color: var(--text-primary);
    }
    
    .section-subtitle {
        text-align: center;
        color: var(--accent-red);
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
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .skill-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--accent-red), #ff6666);
    }
    
    .skill-card:hover {
        transform: translateY(-10px);
        box-shadow: var(--shadow);
        border-color: var(--accent-red);
    }
    
    .skill-icon {
        font-size: 2.5rem;
        color: var(--accent-red);
        margin-bottom: 1rem;
    }
    
    .skill-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .skill-tag {
        background: rgba(255, 68, 68, 0.1);
        color: var(--accent-red);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        border: 1px solid rgba(255, 68, 68, 0.2);
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
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--accent-red), #ff6666);
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: var(--shadow);
        border-color: var(--accent-red);
    }
    
    .project-icon {
        font-size: 2rem;
        color: var(--accent-red);
        margin-bottom: 1rem;
    }
    
    .project-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .project-desc {
        color: var(--text-secondary);
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .project-link {
        color: var(--accent-red);
        text-decoration: none;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .project-link:hover {
        color: var(--accent-red-hover);
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
        background: var(--accent-red);
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
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        position: relative;
        transition: all 0.3s ease;
    }
    
    .timeline-content:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow);
        border-color: var(--accent-red);
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
        border-left-color: var(--bg-card);
    }
    
    .timeline-item:nth-child(even) .timeline-content::before {
        left: -20px;
        border-right-color: var(--bg-card);
    }
    
    .timeline-dot {
        position: absolute;
        top: 20px;
        width: 20px;
        height: 20px;
        background: var(--accent-red);
        border-radius: 50%;
        border: 4px solid var(--bg-primary);
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
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .timeline-company {
        color: var(--accent-red);
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .timeline-period {
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .timeline-desc {
        color: var(--text-secondary);
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
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .contact-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow);
        border-color: var(--accent-red);
    }
    
    .contact-icon {
        font-size: 2.5rem;
        color: var(--accent-red);
        margin-bottom: 1rem;
    }
    
    .contact-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .contact-value {
        color: var(--text-secondary);
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
            border-right-color: var(--bg-card) !important;
        }
    }
    
    /* Streamlit overrides */
    .stButton > button {
        background: linear-gradient(45deg, var(--accent-red), #ff6666);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(255, 68, 68, 0.4);
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
        {"name": "Data Ingestion", "x": 0, "y": 0, "color": "#ff4444", "icon": "📥"},
        {"name": "Preprocessing", "x": 2, "y": 0, "color": "#ff6666", "icon": "🔧"},
        {"name": "Model Training", "x": 4, "y": 0, "color": "#ff8888", "icon": "🤖"},
        {"name": "Validation", "x": 6, "y": 0, "color": "#ffaaaa", "icon": "✅"},
        {"name": "Deployment", "x": 8, "y": 0, "color": "#ffcccc", "icon": "🚀"},
        {"name": "Monitoring", "x": 10, "y": 0, "color": "#ffeeee", "icon": "📊"}
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
            textfont=dict(size=10, color='#666666'),
            showlegend=False
        ))
    
    # Add connecting lines with gradient
    for i in range(len(pipeline_steps) - 1):
        fig.add_trace(go.Scatter(
            x=[pipeline_steps[i]["x"], pipeline_steps[i+1]["x"]],
            y=[pipeline_steps[i]["y"], pipeline_steps[i+1]["y"]],
            mode='lines',
            line=dict(color='#ff4444', width=4),
            showlegend=False
        ))
    
    # Add floating tech elements
    tech_elements = [
        {"name": "K8s", "x": 1, "y": 1.5, "color": "#ff4444", "icon": "☸️"},
        {"name": "Docker", "x": 3, "y": -1.5, "color": "#ff6666", "icon": "🐳"},
        {"name": "Terraform", "x": 5, "y": 1.5, "color": "#ff8888", "icon": "🏗️"},
        {"name": "Prometheus", "x": 7, "y": -1.5, "color": "#ffaaaa", "icon": "📈"},
        {"name": "Grafana", "x": 9, "y": 1.5, "color": "#ffcccc", "icon": "📊"}
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
        title_font=dict(size=24, color='#ff4444'),
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
    
    # Hero Section - Full Screen
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
    <div class="section" style="background: var(--bg-primary);">
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
    <div class="section" style="background: var(--bg-primary);">
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