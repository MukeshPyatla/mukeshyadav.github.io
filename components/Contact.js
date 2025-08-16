const { motion } = window.Motion;

function Contact({ data }) {
    return (
        <section id="contact" className="section">
            <div className="container">
                <motion.h1
                    className="section-title"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Let's Connect
                </motion.h1>
                
                <motion.h2
                    className="contact-subtitle"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    Ready to Build the Future Together
                </motion.h2>
                
                <motion.p
                    className="contact-description"
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.4, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    I'm actively seeking opportunities to architect and scale AI solutions. If you're looking for a passionate engineer to solve complex challenges in MLOps and DevOps, let's connect.
                </motion.p>

                <div className="contact-grid">
                    {[
                        {
                            icon: '📧',
                            title: 'Email',
                            value: data.email,
                            link: `mailto:${data.email}`,
                            color: '#87CEEB'
                        },
                        {
                            icon: '💼',
                            title: 'LinkedIn',
                            value: data.linkedin,
                            link: `https://${data.linkedin}`,
                            color: '#0077B5'
                        },
                        {
                            icon: '🐙',
                            title: 'GitHub',
                            value: data.github,
                            link: `https://${data.github}`,
                            color: '#333'
                        }
                    ].map((contact, index) => (
                        <motion.div
                            key={contact.title}
                            className="contact-card"
                            initial={{ opacity: 0, y: 50 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.6 + index * 0.1, duration: 0.8 }}
                            viewport={{ once: true }}
                            whileHover={{ y: -10, scale: 1.05 }}
                        >
                            <div className="contact-icon" style={{ color: contact.color }}>
                                {contact.icon}
                            </div>
                            <h3>{contact.title}</h3>
                            <p>{contact.value}</p>
                            <motion.a
                                href={contact.link}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="contact-link"
                                whileHover={{ scale: 1.1 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                Get in Touch
                            </motion.a>
                        </motion.div>
                    ))}
                </div>

                <motion.div
                    className="contact-cta"
                    initial={{ opacity: 0, y: 50 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.8, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    <div className="cta-content">
                        <h3>Ready to Start a Project?</h3>
                        <p>Let's discuss how we can work together to build amazing AI solutions.</p>
                        <motion.a
                            href={`mailto:${data.email}?subject=Portfolio Contact - Let's Work Together`}
                            className="btn btn-primary cta-button"
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            Start a Conversation
                        </motion.a>
                    </div>
                </motion.div>

                <motion.div
                    className="footer"
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    transition={{ delay: 1, duration: 0.8 }}
                    viewport={{ once: true }}
                >
                    <p>&copy; 2024 Mukesh Yadav. All rights reserved.</p>
                    <p>Built with ❤️ using React, JavaScript, and modern web technologies</p>
                </motion.div>
            </div>
        </section>
    );
}
