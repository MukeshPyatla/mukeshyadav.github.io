const { motion } = window.Motion;

function Hero({ data, metrics }) {
    return (
        <section id="home" className="hero-section">
            <div className="container">
                <div className="hero-content">
                    <motion.div
                        className="hero-text"
                        initial={{ opacity: 0, y: 50 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8 }}
                    >
                        <motion.h1
                            className="hero-title"
                            initial={{ opacity: 0, y: 30 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2, duration: 0.8 }}
                        >
                            {data.name}
                        </motion.h1>
                        
                        <motion.h2
                            className="hero-subtitle"
                            initial={{ opacity: 0, y: 30 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.4, duration: 0.8 }}
                        >
                            {data.title}
                        </motion.h2>
                        
                        <motion.h3
                            className="hero-description"
                            initial={{ opacity: 0, y: 30 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.6, duration: 0.8 }}
                        >
                            {data.subtitle}
                        </motion.h3>
                        
                        <motion.p
                            className="hero-bio"
                            initial={{ opacity: 0, y: 30 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.8, duration: 0.8 }}
                        >
                            {data.description}
                        </motion.p>
                    </motion.div>

                    <motion.div
                        className="hero-metrics"
                        initial={{ opacity: 0, y: 50 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 1, duration: 0.8 }}
                    >
                        <div className="metrics-grid">
                            {metrics.map((metric, index) => (
                                <motion.div
                                    key={metric.label}
                                    className="metric-card"
                                    initial={{ opacity: 0, scale: 0.8 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    transition={{ delay: 1.2 + index * 0.1, duration: 0.6 }}
                                    whileHover={{ y: -5, scale: 1.05 }}
                                >
                                    <div className="metric-value">{metric.value}</div>
                                    <div className="metric-label">{metric.label}</div>
                                </motion.div>
                            ))}
                        </div>
                    </motion.div>
                </div>

                <motion.div
                    className="hero-background"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 1.5, duration: 1 }}
                >
                    <div className="floating-shapes">
                        <motion.div
                            className="shape shape-1"
                            animate={{
                                y: [0, -20, 0],
                                rotate: [0, 180, 360]
                            }}
                            transition={{
                                duration: 6,
                                repeat: Infinity,
                                ease: "easeInOut"
                            }}
                        />
                        <motion.div
                            className="shape shape-2"
                            animate={{
                                y: [0, 20, 0],
                                rotate: [360, 180, 0]
                            }}
                            transition={{
                                duration: 8,
                                repeat: Infinity,
                                ease: "easeInOut"
                            }}
                        />
                        <motion.div
                            className="shape shape-3"
                            animate={{
                                y: [0, -15, 0],
                                x: [0, 10, 0]
                            }}
                            transition={{
                                duration: 7,
                                repeat: Infinity,
                                ease: "easeInOut"
                            }}
                        />
                    </div>
                </motion.div>
            </div>
        </section>
    );
}
