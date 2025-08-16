const { useState } = React;
const { motion } = window.Motion;

function Skills({ skills }) {
    const [activeCategory, setActiveCategory] = useState(Object.keys(skills)[0]);

    return (
        <section id="skills" className="section">
            <div className="container">
                <motion.h1
                    className="section-title"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Technical Skills
                </motion.h1>
                
                <motion.p
                    className="section-subtitle"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Comprehensive skills across the MLOps and DevOps ecosystem
                </motion.p>

                <div className="skills-container">
                    <motion.div
                        className="skills-categories"
                        initial={{ opacity: 0, x: -50 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.4, duration: 0.8 }}
                        viewport={{ once: true }}
                    >
                        {Object.entries(skills).map(([category, data], index) => (
                            <motion.button
                                key={category}
                                className={`skill-category ${activeCategory === category ? 'active' : ''}`}
                                onClick={() => setActiveCategory(category)}
                                initial={{ opacity: 0, y: 20 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.6 + index * 0.1, duration: 0.6 }}
                                viewport={{ once: true }}
                                whileHover={{ scale: 1.05 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <span className="category-icon">{data.icon}</span>
                                <div className="category-info">
                                    <h3>{category}</h3>
                                    <span className="skill-count">{data.count} skills</span>
                                </div>
                            </motion.button>
                        ))}
                    </motion.div>

                    <motion.div
                        className="skills-content"
                        initial={{ opacity: 0, x: 50 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.6, duration: 0.8 }}
                        viewport={{ once: true }}
                    >
                        <div className="skills-card">
                            <motion.h3
                                key={activeCategory}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ duration: 0.5 }}
                                style={{ color: skills[activeCategory].color }}
                            >
                                {activeCategory}
                            </motion.h3>
                            
                            <motion.div
                                className="skills-grid"
                                key={activeCategory}
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                transition={{ delay: 0.2, duration: 0.5 }}
                            >
                                {skills[activeCategory].skills.map((skill, index) => (
                                    <motion.div
                                        key={skill}
                                        className="skill-item"
                                        initial={{ opacity: 0, scale: 0.8 }}
                                        animate={{ opacity: 1, scale: 1 }}
                                        transition={{ delay: 0.4 + index * 0.05, duration: 0.4 }}
                                        whileHover={{ y: -3, scale: 1.05 }}
                                        style={{ borderColor: skills[activeCategory].color }}
                                    >
                                        <span style={{ color: skills[activeCategory].color }}>
                                            {skill}
                                        </span>
                                    </motion.div>
                                ))}
                            </motion.div>
                        </div>
                    </motion.div>
                </div>

                <motion.div
                    className="skills-summary"
                    initial={{ opacity: 0, y: 50 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.8, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    <div className="summary-card">
                        <h3>Total Skills: {Object.values(skills).reduce((sum, cat) => sum + cat.count, 0)}</h3>
                        <p>Spanning across {Object.keys(skills).length} major categories</p>
                        <div className="skill-categories-overview">
                            {Object.entries(skills).map(([category, data]) => (
                                <div key={category} className="category-overview">
                                    <span className="category-dot" style={{ backgroundColor: data.color }}></span>
                                    <span>{category}</span>
                                </div>
                            ))}
                        </div>
                    </div>
                </motion.div>
            </div>
        </section>
    );
}
