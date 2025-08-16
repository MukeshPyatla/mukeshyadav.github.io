const { useState, useEffect } = React;
const { motion } = window.Motion;

function Navbar() {
    const [isScrolled, setIsScrolled] = useState(false);
    const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 50);
        };

        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const scrollToSection = (sectionId) => {
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
        setIsMobileMenuOpen(false);
    };

    const navItems = [
        { id: 'home', label: 'Home' },
        { id: 'about', label: 'About' },
        { id: 'skills', label: 'Skills' },
        { id: 'projects', label: 'Projects' },
        { id: 'experience', label: 'Experience' },
        { id: 'contact', label: 'Contact' }
    ];

    return (
        <motion.nav
            className={`navbar ${isScrolled ? 'scrolled' : ''}`}
            initial={{ y: -100 }}
            animate={{ y: 0 }}
            transition={{ duration: 0.8 }}
        >
            <div className="nav-container">
                <motion.div
                    className="nav-logo"
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                >
                    <span className="logo-icon">🚀</span>
                    <span className="logo-text">Mukesh Yadav</span>
                </motion.div>

                <div className={`nav-menu ${isMobileMenuOpen ? 'active' : ''}`}>
                    {navItems.map((item, index) => (
                        <motion.button
                            key={item.id}
                            className="nav-link"
                            onClick={() => scrollToSection(item.id)}
                            initial={{ opacity: 0, y: -20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.1 * index, duration: 0.5 }}
                            whileHover={{ y: -2 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            {item.label}
                        </motion.button>
                    ))}
                </div>

                <motion.button
                    className={`hamburger ${isMobileMenuOpen ? 'active' : ''}`}
                    onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                    whileTap={{ scale: 0.95 }}
                >
                    <span></span>
                    <span></span>
                    <span></span>
                </motion.button>
            </div>
        </motion.nav>
    );
}
