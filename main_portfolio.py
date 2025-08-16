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
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Profile Section */
    .profile-section {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .profile-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #28e98c;
        margin: 0 auto 1rem;
    }
    
    .profile-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #28e98c;
        margin: 0 0 0.5rem 0;
    }
    
    .profile-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0 0 1rem 0;
    }
    
    .status-badge {
        display: inline-block;
        background: #28e98c;
        color: #000;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .social-links a {
        color: #28e98c;
        text-decoration: none;
        font-size: 0.9rem;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        background: rgba(40, 233, 140, 0.1);
        border: 1px solid rgba(40, 233, 140, 0.3);
    }
    
    .contact-info {
        margin: 1rem 0;
    }
    
    .contact-info p {
        margin: 0.25rem 0;
        font-size: 0.9rem;
        color: #c2c2c2;
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
    
    # Profile Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
    st.markdown("## Say Hello 👋")
    st.markdown(f"# Hi, I'm {data['name']}")
    st.markdown(f"### {data['title']}")
    st.markdown("""
    Passionate about building scalable, secure, and efficient MLOps pipelines. 
    I specialize in cloud infrastructure, AI/ML deployment, and DevOps automation. 
    With expertise in AWS, Azure, Kubernetes, and modern AI frameworks, 
    I help organizations deploy and maintain production-ready machine learning systems.
    """)
    
    # Stats Section
    st.markdown("---")
    cols = st.columns(4)
    for i, stat in enumerate(data['stats']):
        with cols[i]:
            st.metric(stat['label'], stat['number'])
    
    # Experience Section
    st.markdown("---")
    st.markdown("## Experience")
    
    for exp in data['experience']:
        with st.container():
            st.markdown(f"### {exp['title']}")
            st.markdown(f"**{exp['company']}** • {exp['period']}")
            for achievement in exp['achievements']:
                st.markdown(f"• {achievement}")
            st.markdown("---")
    
    # Projects Section
    st.markdown("## Projects")
    
    for project in data['projects']:
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(project['image'], use_column_width=True)
            with col2:
                st.markdown(f"### {project['title']}")
                st.markdown(project['description'])
                st.markdown(f"**Tech Stack:** {', '.join(project['tech'])}")
                col3, col4 = st.columns(2)
                with col3:
                    st.link_button("Live Demo", project['demo'])
                with col4:
                    st.link_button("GitHub", project['github'])
        st.markdown("---")
    
    # Skills Section
    st.markdown("## Skills & Tools")
    
    for skill_category in data['skills']:
        st.markdown(f"### {skill_category['category']}")
        cols = st.columns(len(skill_category['skills']))
        for i, skill in enumerate(skill_category['skills']):
            with cols[i]:
                st.markdown(f"`{skill}`")
        st.markdown("---")
    
    # Contact Section
    st.markdown("## Let's Get In Touch!")
    st.markdown("Ready to collaborate? Let's discuss your next project!")
    st.markdown(f"✉️ **{data['email']}**")
    st.markdown(f"🔗 **{data['linkedin']}**")
    
    # Footer
    st.markdown("---")
    st.markdown("*Built with ❤️ using Streamlit*")
    st.markdown("*© Mukesh Yadav 2024*")

if __name__ == "__main__":
    main()
