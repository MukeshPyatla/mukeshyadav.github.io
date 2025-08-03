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
    page_title="Mukesh Yadav - Ubuntu MLOps Desktop",
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Ubuntu desktop simulation
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    * {
        font-family: 'Ubuntu', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: #000000;
        color: #E2E8F0;
        overflow-x: hidden;
    }
    
    .main {
        background: #000000;
        color: #E2E8F0;
    }
    
    .stApp {
        background: #000000;
    }
    
    /* Ubuntu Desktop Simulation */
    .ubuntu-desktop {
        min-height: 100vh;
        background: #000000;
        position: relative;
        overflow: hidden;
    }
    
    /* Desktop Background with Grid */
    .desktop-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(135, 206, 250, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(173, 216, 230, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(176, 224, 230, 0.05) 0%, transparent 50%);
        z-index: -2;
    }
    
    .desktop-grid {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
        background-size: 50px 50px;
        z-index: -1;
    }
    
    /* Top Panel (Ubuntu-style) */
    .top-panel {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 40px;
        background: rgba(26, 32, 44, 0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        z-index: 1000;
        font-size: 14px;
    }
    
    .panel-left {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .panel-center {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .panel-right {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .panel-item {
        color: #E2E8F0;
        padding: 5px 10px;
        border-radius: 6px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .panel-item:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    /* Desktop Icons */
    .desktop-icons {
        position: absolute;
        top: 60px;
        left: 20px;
        display: flex;
        flex-direction: column;
        gap: 20px;
        z-index: 10;
    }
    
    .desktop-icon {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        padding: 10px;
        border-radius: 8px;
        transition: all 0.3s ease;
        cursor: pointer;
        text-align: center;
        max-width: 80px;
    }
    
    .desktop-icon:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: scale(1.05);
    }
    
    .icon-image {
        width: 48px;
        height: 48px;
        background: linear-gradient(135deg, #87CEEB, #B0E0E6);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: #000000;
    }
    
    .icon-label {
        font-size: 12px;
        color: #E2E8F0;
        text-align: center;
        line-height: 1.2;
    }
    
    /* Application Windows */
    .app-window {
        background: rgba(26, 32, 44, 0.95);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        backdrop-filter: blur(20px);
        margin: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        overflow: hidden;
    }
    
    .window-header {
        background: rgba(45, 55, 72, 0.8);
        padding: 12px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .window-title {
        font-size: 16px;
        font-weight: 600;
        color: #E2E8F0;
    }
    
    .window-controls {
        display: flex;
        gap: 8px;
    }
    
    .window-btn {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .window-btn.close { background: #F56565; }
    .window-btn.minimize { background: #ED8936; }
    .window-btn.maximize { background: #48BB78; }
    
    .window-btn:hover {
        transform: scale(1.1);
    }
    
    .window-content {
        padding: 30px;
        min-height: 400px;
    }
    
    /* Terminal Style */
    .terminal-window {
        background: #1A202C;
        border: 1px solid #2D3748;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        padding: 20px;
        margin: 20px 0;
    }
    
    .terminal-header {
        color: #A0AEC0;
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .terminal-line {
        color: #E2E8F0;
        margin: 5px 0;
        font-size: 14px;
    }
    
    .terminal-prompt {
        color: #48BB78;
    }
    
    .terminal-command {
        color: #4299E1;
    }
    
    .terminal-output {
        color: #A0AEC0;
    }
    
    /* File Explorer Style */
    .file-explorer {
        display: grid;
        grid-template-columns: 200px 1fr;
        gap: 20px;
        height: 500px;
    }
    
    .sidebar {
        background: rgba(45, 55, 72, 0.5);
        border-radius: 8px;
        padding: 20px;
    }
    
    .sidebar-item {
        padding: 10px;
        margin: 5px 0;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .sidebar-item:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-item.active {
        background: rgba(135, 206, 250, 0.2);
        color: #87CEEB;
    }
    
    .main-content {
        background: rgba(45, 55, 72, 0.3);
        border-radius: 8px;
        padding: 20px;
        overflow-y: auto;
    }
    
    /* Project Cards */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .project-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }
    
    .project-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #87CEEB, #B0E0E6);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        color: #000000;
    }
    
    .project-title {
        font-size: 18px;
        font-weight: 600;
        color: #E2E8F0;
    }
    
    .project-desc {
        color: #A0AEC0;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .project-links {
        display: flex;
        gap: 10px;
    }
    
    .project-link {
        padding: 8px 16px;
        background: rgba(135, 206, 250, 0.2);
        color: #87CEEB;
        text-decoration: none;
        border-radius: 6px;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    
    .project-link:hover {
        background: rgba(135, 206, 250, 0.3);
        text-decoration: none;
    }
    
    /* Skills Grid */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin-top: 20px;
    }
    
    .skill-item {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .skill-item:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .skill-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }
    
    .skill-name {
        font-size: 14px;
        font-weight: 500;
        color: #E2E8F0;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .desktop-icons {
            position: relative;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: center;
            top: 0;
            left: 0;
            margin: 20px;
        }
        
        .file-explorer {
            grid-template-columns: 1fr;
        }
        
        .top-panel {
            padding: 0 10px;
        }
        
        .panel-left, .panel-right {
            display: none;
        }
    }
    
    /* Streamlit overrides */
    .stButton > button {
        background: linear-gradient(135deg, #87CEEB, #B0E0E6);
        color: #000000;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(135, 206, 250, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Data
projects_data = [
    {
        'title': 'DeFi Fraud Detection',
        'description': 'Comprehensive MLOps pipeline for detecting fraud in Decentralized Finance transactions with private-by-design approach.',
        'icon': '🛡️',
        'demo': 'https://defifraud-detectionmlopspipeline.streamlit.app/',
        'github': 'https://github.com/MukeshPyatla/DeFi_Fraud-Detection_MLOps_Pipeline'
    },
    {
        'title': 'Guardian AI Auditor',
        'description': 'Zero-trust multi-modal compliance & risk auditor with privacy-preserving MLOps pipeline.',
        'icon': '🤖',
        'demo': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
        'github': 'https://github.com/MukeshPyatla/guardian-ai-auditor'
    },
    {
        'title': 'MLOps QA System',
        'description': 'LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline.',
        'icon': '💬',
        'demo': 'https://mlops-app-system.streamlit.app/',
        'github': 'https://github.com/MukeshPyatla/mlops-qa-system'
    },
    {
        'title': 'Azure Anomaly Detector',
        'description': 'End-to-End MLOps pipeline for anomaly detection on Azure with real-time monitoring.',
        'icon': '📡',
        'demo': 'https://azure-mlops-anomaly-detector.streamlit.app/',
        'github': 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector'
    },
    {
        'title': 'Secure Churn Prediction',
        'description': 'Privacy-preserving customer churn prediction with PII masking and SHAP explainability.',
        'icon': '👤',
        'demo': 'https://mlops-secure-churn.streamlit.app/',
        'github': 'https://github.com/MukeshPyatla/MLOPS-Secure-Churn'
    },
    {
        'title': 'Demand Forecasting',
        'description': 'Scalable demand forecasting system with integrated MLOps for continuous training.',
        'icon': '📈',
        'demo': 'https://mlops-demand-forecasting.streamlit.app/',
        'github': 'https://github.com/MukeshPyatla/MLOPS-Demand-Forecasting'
    }
]

skills_data = {
    'Cloud & DevOps': ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD'],
    'AI/ML Frameworks': ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML'],
    'Programming': ['Python', 'Go', 'C++', 'Bash', 'SQL'],
    'Data & Databases': ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant'],
    'Monitoring': ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B'],
    'CI/CD Tools': ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions'],
    'AI/ML Concepts': ['MLOps', 'GenAI', 'RAG', 'Federated Learning', 'Homomorphic Encryption'],
    'Blockchain': ['Ethereum', 'Solidity', 'Blockchain'],
    'Operating Systems': ['Linux', 'Windows'],
    'Networking': ['VPC/VNet', 'DNS', 'Load Balancers', 'Security Groups']
}

def create_mlops_visualization():
    """Create an MLOps pipeline visualization"""
    fig = go.Figure()
    
    # Pipeline steps
    pipeline_steps = [
        {"name": "Data Ingestion", "x": 0, "y": 0, "color": "#87CEEB", "icon": "📥"},
        {"name": "Preprocessing", "x": 2, "y": 0, "color": "#B0E0E6", "icon": "🔧"},
        {"name": "Model Training", "x": 4, "y": 0, "color": "#ADD8E6", "icon": "🤖"},
        {"name": "Validation", "x": 6, "y": 0, "color": "#E0F6FF", "icon": "✅"},
        {"name": "Deployment", "x": 8, "y": 0, "color": "#F0F8FF", "icon": "🚀"},
        {"name": "Monitoring", "x": 10, "y": 0, "color": "#E6F3FF", "icon": "📊"}
    ]
    
    # Add pipeline nodes
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
            textfont=dict(size=10, color='#A0AEC0'),
            showlegend=False
        ))
    
    # Add connecting lines
    for i in range(len(pipeline_steps) - 1):
        fig.add_trace(go.Scatter(
            x=[pipeline_steps[i]["x"], pipeline_steps[i+1]["x"]],
            y=[pipeline_steps[i]["y"], pipeline_steps[i+1]["y"]],
            mode='lines',
            line=dict(color='#87CEEB', width=4),
            showlegend=False
        ))
    
    fig.update_layout(
        title="MLOps Pipeline Architecture",
        title_font=dict(size=20, color='#E2E8F0'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, showticklabels=False, range=[-1, 11]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-2, 2]),
        margin=dict(l=0, r=0, t=60, b=0),
        height=300
    )
    
    return fig

def main():
    # Ubuntu Desktop Environment
    st.markdown("""
    <div class="ubuntu-desktop">
        <div class="desktop-bg"></div>
        <div class="desktop-grid"></div>
        
        <!-- Top Panel -->
        <div class="top-panel">
            <div class="panel-left">
                <div class="panel-item">
                    <i class="fas fa-bars"></i>
                </div>
                <div class="panel-item">Applications</div>
                <div class="panel-item">Places</div>
                <div class="panel-item">System</div>
            </div>
            
            <div class="panel-center">
                <div class="panel-item">MLOps Desktop</div>
            </div>
            
            <div class="panel-right">
                <div class="panel-item">
                    <i class="fas fa-wifi"></i>
                </div>
                <div class="panel-item">
                    <i class="fas fa-battery-three-quarters"></i>
                </div>
                <div class="panel-item">
                    <i class="fas fa-volume-up"></i>
                </div>
                <div class="panel-item">
                    <i class="fas fa-clock"></i>
                    <span id="time">12:00</span>
                </div>
            </div>
        </div>
        
        <!-- Desktop Icons -->
        <div class="desktop-icons">
            <div class="desktop-icon" onclick="openApp('terminal')">
                <div class="icon-image">💻</div>
                <div class="icon-label">Terminal</div>
            </div>
            <div class="desktop-icon" onclick="openApp('projects')">
                <div class="icon-image">📁</div>
                <div class="icon-label">Projects</div>
            </div>
            <div class="desktop-icon" onclick="openApp('skills')">
                <div class="icon-image">🛠️</div>
                <div class="icon-label">Skills</div>
            </div>
            <div class="desktop-icon" onclick="openApp('about')">
                <div class="icon-image">ℹ️</div>
                <div class="icon-label">About</div>
            </div>
            <div class="desktop-icon" onclick="openApp('contact')">
                <div class="icon-image">📧</div>
                <div class="icon-label">Contact</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Terminal Application
    st.markdown("""
    <div class="app-window" id="terminal-app">
        <div class="window-header">
            <div class="window-title">Terminal - MLOps Engineer</div>
            <div class="window-controls">
                <div class="window-btn minimize"></div>
                <div class="window-btn maximize"></div>
                <div class="window-btn close"></div>
            </div>
        </div>
        <div class="window-content">
            <div class="terminal-window">
                <div class="terminal-header">mukesh@mlops-desktop:~$</div>
                <div class="terminal-line">
                    <span class="terminal-prompt">$</span> 
                    <span class="terminal-command">whoami</span>
                </div>
                <div class="terminal-line terminal-output">mukesh</div>
                <div class="terminal-line">
                    <span class="terminal-prompt">$</span> 
                    <span class="terminal-command">cat /etc/mlops-profile</span>
                </div>
                <div class="terminal-line terminal-output">
                    Name: Mukesh Yadav<br>
                    Role: MLOps Engineer<br>
                    Company: Aidoc<br>
                    Location: United States<br>
                    Experience: 3+ years<br>
                    Specialization: AI/ML Infrastructure
                </div>
                <div class="terminal-line">
                    <span class="terminal-prompt">$</span> 
                    <span class="terminal-command">ls ~/projects/</span>
                </div>
                <div class="terminal-line terminal-output">
                    defi-fraud-detection/  guardian-ai-auditor/  mlops-qa-system/<br>
                    azure-anomaly-detector/  secure-churn/  demand-forecasting/
                </div>
                <div class="terminal-line">
                    <span class="terminal-prompt">$</span> 
                    <span class="terminal-command">systemctl status mlops-pipeline</span>
                </div>
                <div class="terminal-line terminal-output">
                    ● mlops-pipeline.service - MLOps Pipeline Service<br>
                    Loaded: loaded (/etc/systemd/system/mlops-pipeline.service; enabled)<br>
                    Active: active (running) since Mon 2024-01-15 10:00:00 UTC<br>
                    Status: "Pipeline operational - 99.9% uptime"
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Projects Application
    st.markdown("""
    <div class="app-window" id="projects-app">
        <div class="window-header">
            <div class="window-title">File Manager - Projects</div>
            <div class="window-controls">
                <div class="window-btn minimize"></div>
                <div class="window-btn maximize"></div>
                <div class="window-btn close"></div>
            </div>
        </div>
        <div class="window-content">
            <div class="file-explorer">
                <div class="sidebar">
                    <div class="sidebar-item active">📁 Projects</div>
                    <div class="sidebar-item">📊 Dashboards</div>
                    <div class="sidebar-item">🔗 GitHub</div>
                    <div class="sidebar-item">📈 Analytics</div>
                    <div class="sidebar-item">⚙️ Settings</div>
                </div>
                <div class="main-content">
                    <h3 style="color: #E2E8F0; margin-bottom: 20px;">Live MLOps Projects</h3>
    """, unsafe_allow_html=True)
    
    for project in projects_data:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-header">
                <div class="project-icon">{project['icon']}</div>
                <div class="project-title">{project['title']}</div>
            </div>
            <div class="project-desc">{project['description']}</div>
            <div class="project-links">
                <a href="{project['demo']}" target="_blank" class="project-link">Live Demo</a>
                <a href="{project['github']}" target="_blank" class="project-link">GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    # Skills Application
    st.markdown("""
    <div class="app-window" id="skills-app">
        <div class="window-header">
            <div class="window-title">Skills Manager - Technical Expertise</div>
            <div class="window-controls">
                <div class="window-btn minimize"></div>
                <div class="window-btn maximize"></div>
                <div class="window-btn close"></div>
            </div>
        </div>
        <div class="window-content">
            <h3 style="color: #E2E8F0; margin-bottom: 20px;">Technical Skills Overview</h3>
            <div class="skills-grid">
    """, unsafe_allow_html=True)
    
    for category, skills in skills_data.items():
        st.markdown(f"""
        <div class="skill-item">
            <div class="skill-icon">🛠️</div>
            <div class="skill-name">{category}</div>
            <div style="font-size: 12px; color: #A0AEC0; margin-top: 5px;">
                {len(skills)} skills
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    # About Application
    st.markdown("""
    <div class="app-window" id="about-app">
        <div class="window-header">
            <div class="window-title">About - Mukesh Yadav</div>
            <div class="window-controls">
                <div class="window-btn minimize"></div>
                <div class="window-btn maximize"></div>
                <div class="window-btn close"></div>
            </div>
        </div>
        <div class="window-content">
            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 30px;">
                <div>
                    <h3 style="color: #E2E8F0; margin-bottom: 20px;">Professional Profile</h3>
                    <p style="color: #A0AEC0; line-height: 1.6; margin-bottom: 15px;">
                        As an MLOps Engineer at Aidoc, I architect and deploy intelligent systems that process millions of data points daily. 
                        My expertise spans from building robust monitoring systems with Prometheus and Grafana to implementing CI/CD pipelines 
                        that reduce deployment time by 80%.
                    </p>
                    <p style="color: #A0AEC0; line-height: 1.6; margin-bottom: 15px;">
                        I specialize in privacy-preserving AI using Federated Learning and Homomorphic Encryption, ensuring compliance while 
                        maintaining model performance. My work includes developing containerized GenAI microservices with BentoML and Kubernetes.
                    </p>
                    <p style="color: #A0AEC0; line-height: 1.6;">
                        Currently exploring cutting-edge technologies like LLMOps, Vector Databases for RAG systems, and blockchain integration 
                        for immutable audit trails in MLOps pipelines.
                    </p>
                </div>
                <div style="text-align: center;">
                    <div style="width: 150px; height: 150px; background: linear-gradient(135deg, #87CEEB, #B0E0E6); 
                                border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; 
                                font-size: 3rem; color: #000000; box-shadow: 0 10px 30px rgba(135, 206, 250, 0.3);">
                        MY
                    </div>
                    <h4 style="color: #87CEEB; margin-bottom: 10px; font-weight: 600;">Mukesh Yadav</h4>
                    <p style="color: #A0AEC0;">MLOps & DevOps Engineer</p>
                    <p style="color: #A0AEC0; font-size: 14px;">Aidoc</p>
                </div>
            </div>
            
            <div style="margin-top: 30px;">
                <h4 style="color: #E2E8F0; margin-bottom: 15px;">MLOps Pipeline Visualization</h4>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add the MLOps visualization
    fig = create_mlops_visualization()
    st.plotly_chart(fig, use_container_width=True)
    
    # Contact Application
    st.markdown("""
    <div class="app-window" id="contact-app">
        <div class="window-header">
            <div class="window-title">Contact Manager</div>
            <div class="window-controls">
                <div class="window-btn minimize"></div>
                <div class="window-btn maximize"></div>
                <div class="window-btn close"></div>
            </div>
        </div>
        <div class="window-content">
            <h3 style="color: #E2E8F0; margin-bottom: 20px;">Get In Touch</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 10px;">📧</div>
                    <h4 style="color: #E2E8F0; margin-bottom: 10px;">Email</h4>
                    <p style="color: #A0AEC0;">mukeshyadavp91@gmail.com</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 10px;">💼</div>
                    <h4 style="color: #E2E8F0; margin-bottom: 10px;">LinkedIn</h4>
                    <p style="color: #A0AEC0;">linkedin.com/in/mukesh-mlops</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 10px;">🐙</div>
                    <h4 style="color: #E2E8F0; margin-bottom: 10px;">GitHub</h4>
                    <p style="color: #A0AEC0;">github.com/MukeshPyatla</p>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="mailto:mukeshyadavp91@gmail.com" style="
                    background: linear-gradient(135deg, #87CEEB, #B0E0E6);
                    color: #000000;
                    padding: 12px 24px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-weight: 600;
                    display: inline-block;
                    transition: all 0.3s ease;
                ">Send Message</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # JavaScript for desktop functionality
    st.markdown("""
    <script>
    function openApp(appName) {
        // Hide all apps
        const apps = document.querySelectorAll('.app-window');
        apps.forEach(app => app.style.display = 'none');
        
        // Show selected app
        const selectedApp = document.getElementById(appName + '-app');
        if (selectedApp) {
            selectedApp.style.display = 'block';
        }
    }
    
    // Update time
    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString('en-US', { 
            hour12: false, 
            hour: '2-digit', 
            minute: '2-digit' 
        });
        document.getElementById('time').textContent = timeString;
    }
    
    // Update time every second
    setInterval(updateTime, 1000);
    updateTime();
    
    // Initialize with terminal open
    document.addEventListener('DOMContentLoaded', function() {
        openApp('terminal');
    });
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 