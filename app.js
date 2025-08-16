const { useState, useEffect } = React;
const { motion, AnimatePresence } = window.Motion;

// Portfolio data
const portfolioData = {
    personal: {
        name: "Mukesh Yadav",
        title: "MLOPS & DEVOPS ENGINEER",
        subtitle: "Building Intelligent Systems on Azure & AWS Cloud",
        description: "Specializing in end-to-end MLOps pipelines, automated CI/CD workflows, and scalable cloud infrastructure. Passionate about deploying production-ready AI/ML systems with robust monitoring and observability.",
        email: "mukeshyadavp91@gmail.com",
        linkedin: "linkedin.com/in/mukesh-mlops",
        github: "github.com/MukeshPyatla"
    },
    metrics: [
        { value: "80%", label: "Faster Deployments" },
        { value: "70%", label: "Reduced MTTR" },
        { value: "47", label: "Technical Skills" },
        { value: "6", label: "Live Projects" }
    ],
    skills: {
        'Cloud & DevOps': {
            icon: '☁️',
            color: '#87CEEB',
            skills: ['AWS', 'Azure', 'Terraform', 'Docker', 'Kubernetes', 'CI/CD'],
            count: 6
        },
        'AI/ML Frameworks': {
            icon: '🧠',
            color: '#B0E0E6',
            skills: ['PyTorch', 'TensorFlow', 'LangChain', 'FastAPI', 'MLflow', 'BentoML'],
            count: 6
        },
        'Programming Languages': {
            icon: '💻',
            color: '#ADD8E6',
            skills: ['Python', 'Go', 'C++', 'Bash', 'SQL'],
            count: 5
        },
        'Data & Databases': {
            icon: '🗄️',
            color: '#E0F6FF',
            skills: ['Pandas', 'Spark', 'DVC', 'Pinecone', 'Qdrant'],
            count: 5
        },
        'Monitoring & Observability': {
            icon: '📊',
            color: '#F0F8FF',
            skills: ['Prometheus', 'Grafana', 'ELK Stack', 'Backstage', 'W&B'],
            count: 5
        },
        'CI/CD Tools': {
            icon: '⚙️',
            color: '#E6F3FF',
            skills: ['GitLab CI', 'Jenkins', 'ArgoCD', 'Tekton', 'GitHub Actions'],
            count: 5
        },
        'AI/ML Concepts': {
            icon: '🤖',
            color: '#87CEEB',
            skills: ['MLOps', 'GenAI', 'RAG', 'Federated Learning', 'Homomorphic Encryption', 'NLP'],
            count: 6
        },
        'Blockchain': {
            icon: '🔗',
            color: '#B0E0E6',
            skills: ['Ethereum', 'Solidity', 'Blockchain'],
            count: 3
        },
        'Operating Systems': {
            icon: '🖥️',
            color: '#ADD8E6',
            skills: ['Linux', 'Windows'],
            count: 2
        },
        'Networking': {
            icon: '🌐',
            color: '#87CEEB',
            skills: ['VPC/VNet', 'DNS', 'Load Balancers', 'Security Groups'],
            count: 4
        }
    },
    projects: [
        {
            title: 'DeFi Fraud Detection',
            description: 'Comprehensive MLOps pipeline for detecting fraud in Decentralized Finance transactions with private-by-design approach and modern Streamlit dashboard.',
            status: 'LIVE',
            tech: ['Python', 'Streamlit', 'MLOps'],
            github: 'https://github.com/MukeshPyatla/DeFi_Fraud-Detection_MLOps_Pipeline',
            demo: 'https://defifraud-detectionmlopspipeline.streamlit.app/',
            icon: '🛡️',
            preview_url: 'https://defifraud-detectionmlopspipeline.streamlit.app/',
            features: [
                'Real-time fraud detection',
                'Private-by-design architecture',
                'MLOps pipeline automation',
                'Interactive dashboard'
            ]
        },
        {
            title: 'Guardian AI Auditor',
            description: 'Zero-trust multi-modal compliance & risk auditor with privacy-preserving MLOps pipeline using Federated Learning and Homomorphic Encryption.',
            status: 'LIVE',
            tech: ['Federated Learning', 'Homomorphic Encryption', 'Blockchain'],
            github: 'https://github.com/MukeshPyatla/guardian-ai-auditor',
            demo: 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
            icon: '🤖',
            preview_url: 'https://mukeshpyatla-guardian-ai-auditor-srcuiapp-c6jflx.streamlit.app/',
            features: [
                'Zero-trust architecture',
                'Federated learning',
                'Homomorphic encryption',
                'Multi-modal compliance'
            ]
        },
        {
            title: 'MLOps Q&A System',
            description: 'LLM-Powered Multi-Source Q&A System with Automated Freshness Pipeline - Advanced MLOps Demo with real-time updates.',
            status: 'LIVE',
            tech: ['LLM', 'RAG', 'Vector DB'],
            github: 'https://github.com/MukeshPyatla/mlops-qa-system',
            demo: 'https://mlops-app-system.streamlit.app/',
            icon: '💬',
            preview_url: 'https://mlops-app-system.streamlit.app/',
            features: [
                'LLM-powered Q&A',
                'Multi-source integration',
                'Automated freshness pipeline',
                'Real-time updates'
            ]
        },
        {
            title: 'Azure Anomaly Detector',
            description: 'End-to-End MLOps pipeline for anomaly detection on Azure with real-time monitoring and alerting system.',
            status: 'LIVE',
            tech: ['Azure', 'MLOps', 'Python'],
            github: 'https://github.com/MukeshPyatla/Azure-MLOPS-Anomaly-Detector',
            demo: 'https://azure-mlops-anomaly-detector.streamlit.app/',
            icon: '📡',
            preview_url: 'https://azure-mlops-anomaly-detector.streamlit.app/',
            features: [
                'Azure integration',
                'Real-time monitoring',
                'Anomaly detection',
                'Alerting system'
            ]
        },
        {
            title: 'Secure Churn Prediction',
            description: 'Privacy-preserving customer churn prediction with PII masking and SHAP explainability in Azure Databricks.',
            status: 'LIVE',
            tech: ['Azure Databricks', 'SHAP', 'Data Security'],
            github: 'https://github.com/MukeshPyatla/MLOPS-Secure-Churn',
            demo: 'https://mlops-secure-churn.streamlit.app/',
            icon: '👤',
            preview_url: 'https://mlops-secure-churn.streamlit.app/',
            features: [
                'PII masking',
                'SHAP explainability',
                'Privacy preservation',
                'Azure Databricks'
            ]
        },
        {
            title: 'Demand Forecasting',
            description: 'Scalable demand forecasting system with integrated MLOps for continuous training and monitoring.',
            status: 'LIVE',
            tech: ['Python', 'Forecasting', 'MLOps'],
            github: 'https://github.com/MukeshPyatla/MLOPS-Demand-Forecasting',
            demo: 'https://mlops-demand-forecasting.streamlit.app/',
            icon: '📈',
            preview_url: 'https://mlops-demand-forecasting.streamlit.app/',
            features: [
                'Scalable forecasting',
                'Continuous training',
                'MLOps integration',
                'Real-time monitoring'
            ]
        }
    ],
    experience: [
        {
            title: 'MLOps Engineer',
            company: 'Aidoc',
            period: 'Oct 2023 - Present',
            achievements: [
                'Engineered monitoring system with Prometheus and Grafana, reducing MTTR by 70%',
                'Deployed CI/CD pipeline for GenAI applications, decreasing deployment time by 80%',
                'Automated cloud infrastructure with Terraform, reducing costs by 20%',
                'Integrated private blockchain for immutable MLOps audit trail'
            ]
        },
        {
            title: 'Graduate Research Assistant',
            company: 'Missouri University of Science and Technology',
            period: 'Apr 2023 - Sep 2023',
            achievements: [
                'Managed Azure cloud resources for ML experiments supporting 10 researchers',
                'Implemented DVC for reproducible ML experiments',
                'Designed CI/CD pipelines with Prefect, reducing setup time by 90%',
                'Provided technical mentorship to junior researchers'
            ]
        },
        {
            title: 'Junior Systems Administrator | DevOps Engineer',
            company: 'PineLabs',
            period: 'Jun 2021 - Dec 2022',
            achievements: [
                'Developed CI/CD pipeline using Jenkins and Docker, reducing deployment errors by 30%',
                'Automated system administration tasks, saving 5 hours/week',
                'Maintained Linux servers achieving 99.9% uptime',
                'Implemented backup routines preventing data loss during system failures'
            ]
        }
    ]
};

// Main App Component
function App() {
    const [loading, setLoading] = useState(true);
    const [activeModal, setActiveModal] = useState(null);

    useEffect(() => {
        // Simulate loading
        setTimeout(() => setLoading(false), 1000);
    }, []);

    const openProjectModal = (project) => {
        setActiveModal(project);
    };

    const closeProjectModal = () => {
        setActiveModal(null);
    };

    if (loading) {
        return <Loading />;
    }

    return (
        <div className="App">
            <AnimatePresence>
                <Navbar />
                
                <main>
                    <Hero data={portfolioData.personal} metrics={portfolioData.metrics} />
                    
                    <About data={portfolioData.personal} />
                    
                    <Skills skills={portfolioData.skills} />
                    
                    <Projects 
                        projects={portfolioData.projects} 
                        onProjectClick={openProjectModal}
                    />
                    
                    <Experience experience={portfolioData.experience} />
                    
                    <Contact data={portfolioData.personal} />
                </main>

                {activeModal && (
                    <ProjectModal 
                        project={activeModal} 
                        onClose={closeProjectModal} 
                    />
                )}
            </AnimatePresence>
        </div>
    );
}

// Loading Component
function Loading() {
    return (
        <div className="loading-container">
            <motion.div
                className="loading-content"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
            >
                <motion.div
                    className="loading-logo"
                    animate={{ 
                        rotate: 360,
                        scale: [1, 1.1, 1]
                    }}
                    transition={{ 
                        rotate: { duration: 2, repeat: Infinity, ease: "linear" },
                        scale: { duration: 1.5, repeat: Infinity, ease: "easeInOut" }
                    }}
                >
                    🚀
                </motion.div>
                
                <motion.h1
                    className="loading-title"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.3, duration: 0.6 }}
                >
                    Mukesh Yadav
                </motion.h1>
                
                <motion.p
                    className="loading-subtitle"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.6, duration: 0.6 }}
                >
                    MLOps & DevOps Engineer
                </motion.p>
                
                <motion.div
                    className="loading-spinner"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                >
                    <div className="spinner-ring"></div>
                    <div className="spinner-ring"></div>
                    <div className="spinner-ring"></div>
                </motion.div>
                
                <motion.p
                    className="loading-text"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.9, duration: 0.6 }}
                >
                    Loading portfolio...
                </motion.p>
            </motion.div>
        </div>
    );
}

// Render the app
ReactDOM.render(<App />, document.getElementById('root'));
