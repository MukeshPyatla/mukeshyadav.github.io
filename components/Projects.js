const { useState, useRef, useEffect } = React;
const { motion, AnimatePresence } = window.Motion;

function Projects({ projects, onProjectClick }) {
    const [activeModal, setActiveModal] = useState(null);
    const [isModalOpen, setIsModalOpen] = useState(false);

    const openProjectModal = (project) => {
        setActiveModal(project);
        setIsModalOpen(true);
        document.body.style.overflow = 'hidden';
    };

    const closeProjectModal = () => {
        setIsModalOpen(false);
        document.body.style.overflow = 'auto';
        setTimeout(() => setActiveModal(null), 300);
    };

    useEffect(() => {
        const handleEscape = (e) => {
            if (e.key === 'Escape') {
                closeProjectModal();
            }
        };

        if (isModalOpen) {
            document.addEventListener('keydown', handleEscape);
        }

        return () => {
            document.removeEventListener('keydown', handleEscape);
        };
    }, [isModalOpen]);

    return (
        <>
            <section id="projects" className="section">
                <div className="container">
                    <motion.h1
                        className="section-title"
                        initial={{ opacity: 0, y: 30 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8 }}
                        viewport={{ once: true }}
                    >
                        Featured Projects
                    </motion.h1>
                    
                    <motion.p
                        className="section-subtitle"
                        initial={{ opacity: 0, y: 30 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.2, duration: 0.8 }}
                        viewport={{ once: true }}
                    >
                        End-to-end MLOps and DevOps solutions with live dashboards
                    </motion.p>

                    <div className="projects-grid">
                        {projects.map((project, index) => (
                            <motion.div
                                key={project.title}
                                className="project-card"
                                initial={{ opacity: 0, y: 50 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.4 + index * 0.1, duration: 0.8 }}
                                viewport={{ once: true }}
                                whileHover={{ y: -8 }}
                            >
                                <div className="project-header">
                                    <div className="project-icon">{project.icon}</div>
                                    <div className="project-info">
                                        <h3>{project.title}</h3>
                                        <div className="project-status">
                                            <span className="status-live"></span>
                                            <span className="status-text">{project.status}</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <p className="project-description">{project.description}</p>
                                
                                <div className="project-features">
                                    <h4>Key Features:</h4>
                                    <ul>
                                        {project.features.map((feature, idx) => (
                                            <li key={idx}>{feature}</li>
                                        ))}
                                    </ul>
                                </div>
                                
                                <div className="project-tech">
                                    {project.tech.map((tech, techIndex) => (
                                        <span key={techIndex} className="tech-tag">
                                            {tech}
                                        </span>
                                    ))}
                                </div>

                                {/* Live Preview */}
                                <div className="project-preview-container">
                                    <h4>Live Preview:</h4>
                                    <div className="project-preview-frame">
                                        <iframe
                                            src={project.preview_url}
                                            title={`${project.title} Preview`}
                                            loading="lazy"
                                            sandbox="allow-scripts allow-same-origin allow-forms"
                                        />
                                        <div className="preview-overlay">
                                            <button 
                                                className="preview-fullscreen-btn"
                                                onClick={() => openProjectModal(project)}
                                            >
                                                🔍 View Full Screen
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                
                                <div className="project-links">
                                    <a
                                        href={project.github}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="btn btn-secondary"
                                    >
                                        GitHub
                                    </a>
                                    <a
                                        href={project.demo}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="btn btn-primary"
                                    >
                                        Live Demo
                                    </a>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Full Screen Modal */}
            <AnimatePresence>
                {isModalOpen && activeModal && (
                    <motion.div
                        className="project-modal"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 0.3 }}
                    >
                        <motion.div
                            className="modal-content"
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.8, opacity: 0 }}
                            transition={{ duration: 0.3 }}
                        >
                            <button className="modal-close" onClick={closeProjectModal}>
                                ✕
                            </button>
                            
                            <div className="modal-header">
                                <h2>{activeModal.title}</h2>
                                <p>{activeModal.description}</p>
                            </div>
                            
                            <div className="modal-iframe-container">
                                <iframe
                                    src={activeModal.preview_url}
                                    title={`${activeModal.title} Full Screen`}
                                    className="modal-iframe"
                                    sandbox="allow-scripts allow-same-origin allow-forms"
                                />
                            </div>
                            
                            <div className="modal-footer">
                                <div className="modal-links">
                                    <a
                                        href={activeModal.github}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="btn btn-secondary"
                                    >
                                        View on GitHub
                                    </a>
                                    <a
                                        href={activeModal.demo}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="btn btn-primary"
                                    >
                                        Open in New Tab
                                    </a>
                                </div>
                            </div>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </>
    );
}
