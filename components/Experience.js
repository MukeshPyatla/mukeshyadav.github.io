const { motion } = window.Motion;

function Experience({ experience }) {
    return (
        <section id="experience" className="section">
            <div className="container">
                <motion.h1
                    className="section-title"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Professional Journey
                </motion.h1>
                
                <motion.p
                    className="section-subtitle"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Building the future of AI infrastructure
                </motion.p>

                <div className="timeline">
                    {experience.map((exp, index) => (
                        <motion.div
                            key={exp.title + exp.company}
                            className="timeline-item"
                            initial={{ opacity: 0, x: index % 2 === 0 ? -50 : 50 }}
                            whileInView={{ opacity: 1, x: 0 }}
                            transition={{ delay: 0.4 + index * 0.2, duration: 0.8 }}
                            viewport={{ once: true }}
                            whileHover={{ y: -5 }}
                        >
                            <div className="timeline-content">
                                <div className="timeline-header">
                                    <div className="timeline-info">
                                        <h3>{exp.title}</h3>
                                        <h4>{exp.company}</h4>
                                        <span className="timeline-period">{exp.period}</span>
                                    </div>
                                    <div className="timeline-icon">
                                        <span>💼</span>
                                    </div>
                                </div>
                                
                                <div className="timeline-achievements">
                                    <h5>Key Achievements:</h5>
                                    <ul>
                                        {exp.achievements.map((achievement, achievementIndex) => (
                                            <motion.li
                                                key={achievementIndex}
                                                initial={{ opacity: 0, x: -20 }}
                                                whileInView={{ opacity: 1, x: 0 }}
                                                transition={{ delay: 0.6 + index * 0.2 + achievementIndex * 0.1, duration: 0.5 }}
                                                viewport={{ once: true }}
                                            >
                                                {achievement}
                                            </motion.li>
                                        ))}
                                    </ul>
                                </div>
                            </div>
                        </motion.div>
                    ))}
                </div>

                <motion.div
                    className="experience-summary"
                    initial={{ opacity: 0, y: 50 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.8, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    <div className="summary-stats">
                        <div className="stat-item">
                            <h3>{experience.length}</h3>
                            <p>Years of Experience</p>
                        </div>
                        <div className="stat-item">
                            <h3>3+</h3>
                            <p>Companies</p>
                        </div>
                        <div className="stat-item">
                            <h3>10+</h3>
                            <p>Major Projects</p>
                        </div>
                        <div className="stat-item">
                            <h3>100%</h3>
                            <p>Success Rate</p>
                        </div>
                    </div>
                </motion.div>
            </div>
        </section>
    );
}
