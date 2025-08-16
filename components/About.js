const { motion } = window.Motion;

function About({ data }) {
    return (
        <section id="about" className="section">
            <div className="container">
                <motion.h1
                    className="section-title"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    About Me
                </motion.h1>
                
                <motion.p
                    className="section-subtitle"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Architecting the future of AI infrastructure
                </motion.p>

                <div className="about-content">
                    <motion.div
                        className="about-text"
                        initial={{ opacity: 0, x: -50 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.4, duration: 0.8 }}
                        viewport={{ once: true }}
                    >
                        <div className="about-card">
                            <p>
                                As an MLOps Engineer at Aidoc, I architect and deploy intelligent systems that process millions of data points daily. 
                                My expertise spans from building robust monitoring systems with Prometheus and Grafana to implementing CI/CD pipelines 
                                that reduce deployment time by 80%.
                            </p>
                            <p>
                                I specialize in privacy-preserving AI using Federated Learning and Homomorphic Encryption, ensuring compliance while 
                                maintaining model performance. My work includes developing containerized GenAI microservices with BentoML and Kubernetes, 
                                solving the classic "it works on my machine" problem.
                            </p>
                            <p>
                                Currently exploring cutting-edge technologies like LLMOps, Vector Databases for RAG systems, and blockchain integration 
                                for immutable audit trails in MLOps pipelines.
                            </p>
                        </div>
                    </motion.div>

                    <motion.div
                        className="about-visual"
                        initial={{ opacity: 0, x: 50 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.6, duration: 0.8 }}
                        viewport={{ once: true }}
                    >
                        <div className="avatar-container">
                            <motion.div
                                className="avatar"
                                whileHover={{ scale: 1.05 }}
                                animate={{ y: [0, -10, 0] }}
                                transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                            >
                                <div className="avatar-inner">
                                    <span className="avatar-text">MY</span>
                                </div>
                            </motion.div>
                            <h3>Mukesh Yadav</h3>
                            <p>MLOps & DevOps Engineer</p>
                        </div>
                    </motion.div>
                </div>

                <motion.div
                    className="mlops-pipeline"
                    initial={{ opacity: 0, y: 50 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.8, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    <h3>MLOps Pipeline Overview</h3>
                    <div className="pipeline-steps">
                        {[
                            { icon: '📊', title: 'Data Ingestion', desc: 'Real-time data collection' },
                            { icon: '🔧', title: 'Preprocessing', desc: 'Data cleaning & validation' },
                            { icon: '🤖', title: 'Model Training', desc: 'Automated ML training' },
                            { icon: '📦', title: 'Containerization', desc: 'Docker & Kubernetes' },
                            { icon: '🚀', title: 'Deployment', desc: 'CI/CD automation' },
                            { icon: '📈', title: 'Monitoring', desc: 'Real-time observability' }
                        ].map((step, index) => (
                            <motion.div
                                key={step.title}
                                className="pipeline-step"
                                initial={{ opacity: 0, scale: 0.8 }}
                                whileInView={{ opacity: 1, scale: 1 }}
                                transition={{ delay: 1 + index * 0.1, duration: 0.6 }}
                                viewport={{ once: true }}
                                whileHover={{ y: -5 }}
                            >
                                <div className="step-icon">{step.icon}</div>
                                <h4>{step.title}</h4>
                                <p>{step.desc}</p>
                            </motion.div>
                        ))}
                    </div>
                </motion.div>
            </div>
        </section>
    );
}
