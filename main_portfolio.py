import streamlit as st
import base64
from PIL import Image
import io
import requests

# Page configuration
st.set_page_config(
    page_title="Mukesh Yadav - MLOps & DevOps Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the enhanced portfolio design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    
    /* Enhanced Portfolio Styles */
    html, body, .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    
    /* Animated background particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(40, 233, 140, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(59, 130, 246, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
        animation: backgroundShift 20s ease-in-out infinite;
    }
    
    @keyframes backgroundShift {
        0%, 100% { transform: translate(0, 0) scale(1); }
        25% { transform: translate(-10px, -10px) scale(1.05); }
        50% { transform: translate(10px, -5px) scale(0.95); }
        75% { transform: translate(-5px, 10px) scale(1.02); }
    }
    
    /* Main Container */
    .portfolio-container {
        max-width: 1440px;
        margin: 0 auto;
        padding: 60px 40px;
        position: relative;
        z-index: 1;
    }
    
    /* Profile Section */
    .profile-section {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px 30px;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .profile-section:hover {
        transform: translateY(-10px);
        box-shadow: 0 35px 70px rgba(0, 0, 0, 0.4);
        border-color: #28e98c;
    }
    
    .profile-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #28e98c;
        margin: 0 auto 20px;
        box-shadow: 0 10px 30px rgba(40, 233, 140, 0.3);
        transition: all 0.3s ease;
    }
    
    .profile-image:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(40, 233, 140, 0.5);
        border-color: #8b5cf6;
    }
    
    .profile-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 10px 0;
        line-height: 1.1;
    }
    
    .profile-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #28e98c;
        margin: 0 0 20px 0;
    }
    
    .status-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #fff;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 14px;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        animation: pulse 2s infinite;
        margin-bottom: 20px;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .social-links a {
        color: #666;
        text-decoration: none;
        font-size: 14px;
        transition: color 0.3s;
        padding: 8px 16px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .social-links a:hover {
        color: #28e98c;
        background: rgba(40, 233, 140, 0.1);
        border-color: #28e98c;
    }
    
    .contact-info {
        margin: 1.5rem 0;
    }
    
    .contact-info p {
        margin: 0.5rem 0;
        font-size: 14px;
        color: #666;
    }
    
    /* Hero Section */
    .hero-section {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        margin: 40px 0;
        text-align: center;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    
    .hero-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 1rem 0;
        line-height: 1.1;
    }
    
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 600;
        color: #28e98c;
        margin: 0 0 2rem 0;
    }
    
    .hero-description {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        line-height: 1.8;
        color: #c2c2c2;
        margin: 0;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Stats Section */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    .stat-item {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 30px 20px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .stat-item:hover::before {
        transform: scaleX(1);
    }
    
    .stat-item:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border-color: #28e98c;
    }
    
    .stat-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #666;
        margin: 8px 0 0 0;
    }
    
    /* Section Styles */
    .section {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        margin: 40px 0;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.5rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0 0 30px 0;
        text-align: center;
        position: relative;
        display: inline-block;
        width: 100%;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transition: width 0.5s ease;
    }
    
    .section:hover .section-title::after {
        width: 100px;
    }
    
    /* Experience Items */
    .experience-item {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .experience-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        border-color: #28e98c;
    }
    
    .experience-item h3 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0 0 0.5rem 0;
    }
    
    .experience-item .company {
        font-size: 14px;
        color: #28e98c;
        margin: 0 0 1rem 0;
        font-weight: 500;
    }
    
    .achievements {
        list-style: none;
        padding: 0;
        margin: 1rem 0 0 0;
    }
    
    .achievements li {
        position: relative;
        padding-left: 1.5rem;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        line-height: 1.6;
        color: #c2c2c2;
    }
    
    .achievements li::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: #28e98c;
        font-weight: bold;
    }
    
    /* Project Styles */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
    }
    
    .project-item {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .project-item:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        border-color: #28e98c;
    }
    
    .project-preview {
        position: relative;
        height: 200px;
        overflow: hidden;
    }
    
    .project-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.3s ease;
    }
    
    .project-item:hover .project-image {
        transform: scale(1.05);
    }
    
    .project-overlay {
        position: absolute;
        top: 1rem;
        right: 1rem;
    }
    
    .project-status {
        background: #28e98c;
        color: #000;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .project-content {
        padding: 1.5rem;
    }
    
    .project-content h3 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0 0 1rem 0;
    }
    
    .project-content p {
        font-size: 0.9rem;
        line-height: 1.6;
        color: #c2c2c2;
        margin: 0 0 1rem 0;
    }
    
    .project-tech {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .project-tech span {
        background: rgba(40, 233, 140, 0.1);
        color: #28e98c;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .project-links {
        display: flex;
        gap: 1rem;
    }
    
    .demo-link, .github-link {
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        font-size: 0.85rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .demo-link {
        background: #28e98c;
        color: #000;
    }
    
    .github-link {
        background: transparent;
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .demo-link:hover, .github-link:hover {
        transform: translateY(-2px);
    }
    
    /* Skills Grid */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }
    
    .skill-category {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    .skill-category:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border-color: #28e98c;
    }
    
    .skill-category h3 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0 0 1.5rem 0;
        text-align: center;
    }
    
    .skill-items {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        justify-content: center;
    }
    
    .skill-tag {
        background: rgba(40, 233, 140, 0.1);
        color: #28e98c;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid rgba(40, 233, 140, 0.2);
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        background: #28e98c;
        color: #000;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(40, 233, 140, 0.3);
    }
    
    /* Contact Form */
    .contact-form {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    
    .form-input {
        width: 100%;
        height: 50px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 15px 20px;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    
    .form-input:focus {
        border-color: #28e98c;
        outline: none;
        box-shadow: 0 0 20px rgba(40, 233, 140, 0.3);
        transform: translateY(-2px);
    }
    
    .form-textarea {
        min-height: 120px;
        resize: vertical;
    }
    
    .submit-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #fff;
        border: none;
        border-radius: 12px;
        padding: 15px 30px;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    
    .submit-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .portfolio-container {
            padding: 20px;
        }
        
        .hero-name {
            font-size: 2.5rem;
        }
        
        .hero-title {
            font-size: 1.5rem;
        }
        
        .profile-name {
            font-size: 2rem;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .projects-grid {
            grid-template-columns: 1fr;
        }
        
        .skills-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Portfolio data
def get_portfolio_data():
    return {
        'name': 'Mukesh Yadav',
        'title': 'MLOps & DevOps Engineer',
        'email': 'mukeshyadavp91@gmail.com',
        'location': 'United States',
        'linkedin': 'https://linkedin.com/in/mukesh-mlops',
        'github': 'https://github.com/MukeshPyatla',
        'profile_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face',
        'stats': [
            {'number': '30+', 'label': 'Completed Projects'},
            {'number': '8+', 'label': 'Years of Experience'},
            {'number': '36+', 'label': 'Happy Clients'},
            {'number': '10+', 'label': 'Awards Received'}
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
        ],
        'projects': [
            {
                'title': '🛡️ DeFi Fraud Detection',
                'description': 'Comprehensive MLOps pipeline for detecting fraud in Decentralized Finance transactions with private-by-design approach and modern Streamlit dashboard.',
                'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=250&fit=crop',
                'tech': ['Python', 'Streamlit', 'MLOps'],
                'demo': 'https://defifraud-detectionmlopspipeline.streamlit.app/',
                'github': 'https://github.com/MukeshPyatla/DeFi_Fraud-Detection_MLOps_Pipeline'
            },
            {
                'title': '🤖 Guardian AI Auditor',
                'description': 'Zero-trust multi-modal compliance & risk auditor with privacy-preserving MLOps pipeline using Federated Learning and Homomorphic Encryption.',
                'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=250&fit=crop',
                'tech': ['Federated Learning', 'Homomorphic Encryption', 'Blockchain'],
                'demo': 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
                'github': 'https://github.com/MukeshPyatla/guardian-ai-auditor'
            },
            {
                'title': '💬 MLOps Q&A System',
                'description': 'LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo with real-time updates.',
                'image': 'https://images.unsplash.com/photo-1673187735164-9b6b1c0c0c0c?w=400&h=250&fit=crop',
                'tech': ['LLM', 'RAG', 'Vector DB'],
                'demo': 'https://mlops-app-system.streamlit.app/',
                'github': 'https://github.com/MukeshPyatla/mlops-qa-system'
            },
            {
                'title': '📡 Azure Anomaly Detector',
                'description': 'End-to-End MLOps pipeline for anomaly detection on Azure with real-time monitoring and alerting system.',
                'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=250&fit=crop',
                'tech': ['Azure', 'MLOps', 'Python'],
                'demo': 'https://azure-mlops-anomaly-detector.streamlit.app/',
                'github': 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector'
            }
        ],
        'skills': [
            {
                'category': '☁️ Cloud & DevOps',
                'skills': ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD']
            },
            {
                'category': '🧠 AI/ML Frameworks',
                'skills': ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML']
            },
            {
                'category': '💻 Programming Languages',
                'skills': ['Python', 'Go', 'C++', 'Bash', 'SQL']
            },
            {
                'category': '📊 Data & Databases',
                'skills': ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant']
            },
            {
                'category': '📈 Monitoring & Observability',
                'skills': ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B']
            },
            {
                'category': '🔧 CI/CD Tools',
                'skills': ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions']
            }
        ]
    }

def main():
    data = get_portfolio_data()
    
    # Main container
    st.markdown('<div class="portfolio-container">', unsafe_allow_html=True)
    
    # Profile Section
    st.markdown(f"""
    <div class="profile-section">
        <img src="{data['profile_image']}" alt="{data['name']}" class="profile-image">
        <h1 class="profile-name">{data['name']}</h1>
        <p class="profile-title">{data['title']}</p>
        <span class="status-badge">🟢 Available for work</span>
        
        <div class="social-links">
            <a href="{data['linkedin']}" target="_blank">LinkedIn</a>
            <a href="{data['github']}" target="_blank">GitHub</a>
            <a href="mailto:{data['email']}" target="_blank">Email</a>
        </div>
        
        <div class="contact-info">
            <p>✉️ {data['email']}</p>
            <p>📍 {data['location']}</p>
            <p>🔗 linkedin.com/in/mukesh-mlops</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown(f"""
    <div class="hero-section">
        <h2 class="section-title">Say Hello 👋</h2>
        <h1 class="hero-name">Hi, I'm {data['name']}</h1>
        <h2 class="hero-title">{data['title']}</h2>
        <p class="hero-description">
            Passionate about building scalable, secure, and efficient MLOps pipelines. 
            I specialize in cloud infrastructure, AI/ML deployment, and DevOps automation. 
            With expertise in AWS, Azure, Kubernetes, and modern AI frameworks, 
            I help organizations deploy and maintain production-ready machine learning systems.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    stats_html = '<div class="stats-grid">'
    for stat in data['stats']:
        stats_html += f"""
        <div class="stat-item">
            <h3 class="stat-number">{stat['number']}</h3>
            <p class="stat-label">{stat['label']}</p>
        </div>
        """
    stats_html += '</div>'
    st.markdown(stats_html, unsafe_allow_html=True)
    
    # Experience Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)
    
    for exp in data['experience']:
        achievements_html = '<ul class="achievements">'
        for achievement in exp['achievements']:
            achievements_html += f'<li>{achievement}</li>'
        achievements_html += '</ul>'
        
        st.markdown(f"""
        <div class="experience-item">
            <h3>{exp['title']}</h3>
            <p class="company">{exp['company']} • {exp['period']}</p>
            {achievements_html}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Projects Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
    
    projects_html = '<div class="projects-grid">'
    for project in data['projects']:
        tech_html = ''
        for tech in project['tech']:
            tech_html += f'<span>{tech}</span>'
        
        projects_html += f"""
        <div class="project-item">
            <div class="project-preview">
                <img src="{project['image']}" alt="{project['title']}" class="project-image">
                <div class="project-overlay">
                    <span class="project-status">LIVE</span>
                </div>
            </div>
            <div class="project-content">
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
                <div class="project-tech">
                    {tech_html}
                </div>
                <div class="project-links">
                    <a href="{project['demo']}" target="_blank" class="demo-link">Live Demo</a>
                    <a href="{project['github']}" target="_blank" class="github-link">GitHub</a>
                </div>
            </div>
        </div>
        """
    projects_html += '</div>'
    st.markdown(projects_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Skills & Tools</h2>', unsafe_allow_html=True)
    
    skills_html = '<div class="skills-grid">'
    for skill_category in data['skills']:
        skills_html += f"""
        <div class="skill-category">
            <h3>{skill_category['category']}</h3>
            <div class="skill-items">
        """
        for skill in skill_category['skills']:
            skills_html += f'<span class="skill-tag">{skill}</span>'
        skills_html += '</div></div>'
    skills_html += '</div>'
    st.markdown(skills_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Let\'s Get In Touch!</h2>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="contact-form">
        <div style="margin-bottom: 30px;">
            <p style="color: #c2c2c2; margin-bottom: 20px;">Ready to collaborate? Let's discuss your next project!</p>
            <p style="color: #28e98c; font-weight: 600;">✉️ {data['email']}</p>
            <p style="color: #28e98c; font-weight: 600;">🔗 {data['linkedin']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 60px; padding: 40px; border-top: 1px solid rgba(255,255,255,0.1);">
        <p style="color: #666; margin: 0;">Built with ❤️ using Streamlit</p>
        <p style="color: #666; margin: 10px 0 0 0;">© Mukesh Yadav 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
