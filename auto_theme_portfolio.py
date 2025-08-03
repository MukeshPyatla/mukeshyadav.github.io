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

# Custom CSS for auto dark/light mode and red theme
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Auto dark/light mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-primary: #0a0a0a;
            --bg-secondary: #1a1a1a;
            --text-primary: #ffffff;
            --text-secondary: #e0e0e0;
            --accent-red: #ff4444;
            --accent-red-hover: #ff6666;
            --card-bg: #1a1a1a;
            --border-color: #333333;
        }
    }
    
    @media (prefers-color-scheme: light) {
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --accent-red: #dc3545;
            --accent-red-hover: #c82333;
            --card-bg: #ffffff;
            --border-color: #e9ecef;
        }
    }
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: var(--bg-primary);
        color: var(--text-primary);
    }
    
    .stApp {
        background: var(--bg-primary);
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
        padding: 4rem 2rem;
        text-align: center;
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
        background: 
            radial-gradient(circle at 20% 50%, rgba(255, 68, 68, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 68, 68, 0.05) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, var(--accent-red), #ff8888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: var(--text-secondary);
        max-width: 600px;
        margin: 0 auto 2rem;
        line-height: 1.6;
    }
    
    /* Social Profiles */
    .social-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .social-card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .social-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 68, 68, 0.2);
        border-color: var(--accent-red);
    }
    
    .social-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: var(--accent-red);
    }
    
    .social-title {
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.25rem;
    }
    
    .social-desc {
        color: var(--text-secondary);
        font-size: 0.9rem;
    }
    
    /* MLOps/DevOps Visual */
    .mlops-visual {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
        position: relative;
        overflow: hidden;
    }
    
    .mlops-visual::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            linear-gradient(45deg, transparent 30%, rgba(255, 68, 68, 0.05) 50%, transparent 70%);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .pipeline-step {
        display: inline-block;
        background: linear-gradient(45deg, var(--accent-red), #ff6666);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.5rem;
        font-weight: 500;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Buttons */
    .btn-primary {
        background: linear-gradient(45deg, var(--accent-red), #ff6666);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 68, 68, 0.3);
        color: white;
        text-decoration: none;
    }
    
    .btn-secondary {
        background: transparent;
        color: var(--text-primary);
        border: 2px solid var(--accent-red);
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .btn-secondary:hover {
        background: var(--accent-red);
        color: white;
        transform: translateY(-2px);
        text-decoration: none;
    }
    
    /* Cards */
    .card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border-color: var(--accent-red);
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .card-content {
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    /* Skills */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .skill-category {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .skill-category:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 68, 68, 0.15);
        border-color: var(--accent-red);
    }
    
    .skill-category h3 {
        color: var(--accent-red);
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }
    
    .skill-tag {
        display: inline-block;
        background: rgba(255, 68, 68, 0.1);
        color: var(--accent-red);
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        margin: 0.25rem;
        font-size: 0.9rem;
        border: 1px solid rgba(255, 68, 68, 0.2);
    }
    
    /* Projects */
    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .project-card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(255, 68, 68, 0.15);
        border-color: var(--accent-red);
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .project-desc {
        color: var(--text-secondary);
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    
    .project-link {
        color: var(--accent-red);
        text-decoration: none;
        font-weight: 500;
    }
    
    .project-link:hover {
        text-decoration: underline;
    }
    
    /* Section dividers */
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--accent-red), transparent);
        margin: 3rem 0;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .social-grid {
            grid-template-columns: 1fr;
        }
        
        .project-grid {
            grid-template-columns: 1fr;
        }
    }
    
    /* Streamlit specific overrides */
    .stButton > button {
        background: linear-gradient(45deg, var(--accent-red), #ff6666);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 68, 68, 0.3);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        background: var(--card-bg);
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary);
        border-radius: 8px;
        margin: 0.25rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--accent-red);
        color: white;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 68, 68, 0.1);
        color: var(--accent-red);
    }
    </style>
    """, unsafe_allow_html=True)

# Data
skills_data = {
    "Cloud/DevOps": [
        "Azure", "AWS", "Terraform (IaC)", "Kubernetes", "Docker", 
        "CI/CD (GitLab CI, Jenkins, ArgoCD, Tekton)", "GitOps"
    ],
    "AI/ML Frameworks": [
        "LangChain", "PyTorch", "TensorFlow", "FastAPI", "TensorRT", 
        "Flower", "MLflow", "BentoML"
    ],
    "Data & Databases": [
        "SQL", "Vector Databases (Pinecone, Qdrant)", "Pandas", 
        "Spark", "DVC", "LakeFS"
    ],
    "Monitoring & Observability": [
        "Prometheus", "Grafana", "ELK Stack", "Backstage", 
        "Weights & Biases (W&B)"
    ],
    "Languages": [
        "Python", "SQL", "Bash", "C++", "Go (learning)"
    ],
    "AI/ML Concepts": [
        "MLOps", "GenAI", "RAG", "Federated Learning (FL)", 
        "Homomorphic Encryption (HE)", "Transformers", "NLP"
    ],
    "Blockchain": [
        "Ethereum", "Smart Contracts (Solidity)", "Immutable Ledgers"
    ],
    "Operating Systems": [
        "Linux (RHEL, Ubuntu)", "Windows"
    ],
    "Networking": [
        "VPC/VNet", "DNS", "Load Balancers", "Security Groups"
    ]
}

projects_data = [
    {
        "title": "Guardian AI: Zero-Trust Multi-Modal Compliance & Risk Auditor",
        "description": "Engineered a privacy-preserving MLOps pipeline using Federated Learning (FL) and Homomorphic Encryption (HE) to securely audit multi-modal data, and integrated a private blockchain to provide an immutable, verifiable audit trail.",
        "link": "https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/"
    },
    {
        "title": "DeFi Fraud Detection MLOps Pipeline",
        "description": "A comprehensive MLOps pipeline for detecting fraud in Decentralized Finance (DeFi) transactions with a private-by-design approach and modern Streamlit dashboard.",
        "link": "https://defifraud-detectionmlopspipeline.streamlit.app/"
    },
    {
        "title": "MLOps QA System",
        "description": "LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo",
        "link": "https://mlops-app-system.streamlit.app/"
    },
    {
        "title": "Azure MLOps Anomaly Detector",
        "description": "End-to-End MLOps pipeline for anomaly detection on Azure",
        "link": "https://azure-mlops-anomaly-detector.streamlit.app/"
    },
    {
        "title": "MLOps Secure Churn",
        "description": "Secure customer churn prediction with MLOps pipeline",
        "link": "https://mlops-secure-churn.streamlit.app/"
    },
    {
        "title": "MLOps Demand Forecasting",
        "description": "Advanced demand forecasting with MLOps pipeline",
        "link": "https://mlops-demand-forecasting.streamlit.app/"
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

social_profiles = [
    {
        "name": "GitHub",
        "icon": "🐙",
        "description": "View My Code",
        "link": "https://github.com/MukeshPyatla"
    },
    {
        "name": "LinkedIn",
        "icon": "💼",
        "description": "Connect With Me",
        "link": "https://linkedin.com/in/mukesh-yadav-mlops"
    },
    {
        "name": "Portfolio",
        "icon": "🎯",
        "description": "See My Work",
        "link": "https://mukeshyadav.github.io"
    },
    {
        "name": "Email",
        "icon": "📧",
        "description": "Get In Touch",
        "link": "mailto:mukeshyadavp91@gmail.com"
    }
]

def create_mlops_visual():
    """Create an eye-catching MLOps/DevOps pipeline visualization"""
    fig = go.Figure()
    
    # Pipeline steps with coordinates
    steps = [
        {"name": "Data Ingestion", "x": 0, "y": 0, "color": "#ff4444"},
        {"name": "Model Training", "x": 2, "y": 0, "color": "#ff6666"},
        {"name": "Deployment", "x": 4, "y": 0, "color": "#ff8888"},
        {"name": "Monitoring", "x": 6, "y": 0, "color": "#ffaaaa"}
    ]
    
    # Add pipeline nodes
    for step in steps:
        fig.add_trace(go.Scatter(
            x=[step["x"]],
            y=[step["y"]],
            mode='markers+text',
            marker=dict(
                size=30,
                color=step["color"],
                line=dict(width=2, color='white')
            ),
            text=step["name"],
            textposition="bottom center",
            textfont=dict(size=12, color='white'),
            name=step["name"],
            showlegend=False
        ))
    
    # Add connecting lines
    for i in range(len(steps) - 1):
        fig.add_trace(go.Scatter(
            x=[steps[i]["x"], steps[i+1]["x"]],
            y=[steps[i]["y"], steps[i+1]["y"]],
            mode='lines',
            line=dict(color='#ff4444', width=3),
            showlegend=False
        ))
    
    # Add floating elements
    floating_elements = [
        {"name": "K8s", "x": 1, "y": 1, "color": "#ff4444"},
        {"name": "Docker", "x": 3, "y": -1, "color": "#ff6666"},
        {"name": "Terraform", "x": 5, "y": 1, "color": "#ff8888"},
        {"name": "Prometheus", "x": 2, "y": -1, "color": "#ffaaaa"}
    ]
    
    for elem in floating_elements:
        fig.add_trace(go.Scatter(
            x=[elem["x"]],
            y=[elem["y"]],
            mode='markers+text',
            marker=dict(
                size=20,
                color=elem["color"],
                symbol='diamond',
                line=dict(width=1, color='white')
            ),
            text=elem["name"],
            textposition="middle center",
            textfont=dict(size=10, color='white'),
            name=elem["name"],
            showlegend=False
        ))
    
    fig.update_layout(
        title="MLOps Pipeline Architecture",
        title_font=dict(size=20, color='#ff4444'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, showticklabels=False, range=[-1, 7]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-2, 2]),
        margin=dict(l=0, r=0, t=50, b=0),
        height=300
    )
    
    return fig

def main():
    load_css()
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Hello, I'm Mukesh</h1>
        <h2 class="hero-subtitle">MLOps Engineer</h2>
        <p class="hero-description">
            A passionate MLOps Engineer building scalable and secure AI pipelines on Azure. 
            Specialized in automation, data-driven solutions, and robust model deployment with expertise in 
            Federated Learning, Homomorphic Encryption, and blockchain-based audit trails.
        </p>
        <div>
            <a href="#contact" class="btn-primary">Hire Me</a>
            <a href="mailto:mukeshyadavp91@gmail.com" class="btn-secondary">Get In Touch</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Social Profiles
    st.markdown("""
    <div class="social-grid">
    """, unsafe_allow_html=True)
    
    for profile in social_profiles:
        st.markdown(f"""
        <div class="social-card" onclick="window.open('{profile['link']}', '_blank')">
            <div class="social-icon">{profile['icon']}</div>
            <div class="social-title">{profile['name']}</div>
            <div class="social-desc">{profile['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # MLOps Visual
    st.markdown("""
    <div class="mlops-visual">
        <h2 style="color: var(--accent-red); margin-bottom: 1rem;">🚀 MLOps Pipeline Architecture</h2>
        <div style="text-align: center;">
            <span class="pipeline-step">Data Ingestion</span>
            <span class="pipeline-step">Model Training</span>
            <span class="pipeline-step">Deployment</span>
            <span class="pipeline-step">Monitoring</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive MLOps Visualization
    fig = create_mlops_visual()
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown("""
    <h2 style="color: var(--accent-red); margin-bottom: 2rem;">🛠️ Technical Skills</h2>
    """, unsafe_allow_html=True)
    
    skills_col1, skills_col2 = st.columns(2)
    
    with skills_col1:
        for i, (category, skills) in enumerate(skills_data.items()):
            if i % 2 == 0:
                st.markdown(f"""
                <div class="skill-category">
                    <h3>{category}</h3>
                    <div>
                """, unsafe_allow_html=True)
                
                for skill in skills:
                    st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
                
                st.markdown("</div></div>", unsafe_allow_html=True)
    
    with skills_col2:
        for i, (category, skills) in enumerate(skills_data.items()):
            if i % 2 == 1:
                st.markdown(f"""
                <div class="skill-category">
                    <h3>{category}</h3>
                    <div>
                """, unsafe_allow_html=True)
                
                for skill in skills:
                    st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
                
                st.markdown("</div></div>", unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Projects Section
    st.markdown("""
    <h2 style="color: var(--accent-red); margin-bottom: 2rem;">🚀 Live Projects & Dashboards</h2>
    """, unsafe_allow_html=True)
    
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <h3 class="project-title">{project['title']}</h3>
            <p class="project-desc">{project['description']}</p>
            <a href="{project['link']}" target="_blank" class="project-link">🌐 View Live Dashboard →</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Experience Section
    st.markdown("""
    <h2 style="color: var(--accent-red); margin-bottom: 2rem;">💼 Professional Experience</h2>
    """, unsafe_allow_html=True)
    
    for exp in experience_data:
        st.markdown(f"""
        <div class="card">
            <h3 class="card-title">{exp['company']} - {exp['position']}</h3>
            <p style="color: var(--accent-red); font-weight: 500; margin-bottom: 1rem;">
                {exp['period']}{' - ' + exp['location'] if 'location' in exp else ''}
            </p>
            <div class="card-content">
        """, unsafe_allow_html=True)
        
        for desc in exp['description']:
            st.markdown(f"• {desc}", unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Contact Section
    st.markdown("""
    <h2 style="color: var(--accent-red); margin-bottom: 2rem;">📞 Get In Touch</h2>
    """, unsafe_allow_html=True)
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">📧 Email</h3>
            <p class="card-content">mukeshyadavp91@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3 class="card-title">📱 Phone</h3>
            <p class="card-content">+1-573-639-8737</p>
        </div>
        """, unsafe_allow_html=True)
    
    with contact_col2:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">🎓 Education</h3>
            <p class="card-content">Master of Science, Computer Science<br>Missouri University of Science and Technology</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3 class="card-title">🏆 Certifications</h3>
            <p class="card-content">Azure Administrator Associate (AZ-104)<br>AWS Certified Developer - Associate</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 