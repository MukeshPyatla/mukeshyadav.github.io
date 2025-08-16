# Mukesh Yadav - Portfolio Website

A modern, interactive portfolio website showcasing Mukesh Yadav's expertise in Framer, UI/UX design, and interactive prototyping. Built with multiple approaches including Streamlit, React, and a standalone Framer-inspired HTML/CSS implementation.

## 🚀 Features

### Modern Web Technologies
- **React.js** - Interactive UI components with state management
- **JavaScript (ES6+)** - Modern JavaScript features and async operations
- **HTML5** - Semantic markup and accessibility
- **CSS3** - Advanced styling with animations and responsive design
- **Framer Motion** - Smooth animations and transitions
- **Responsive Design** - Mobile-first approach with breakpoints

### Live Project Previews
- **Embedded iframes** - Real-time project previews directly on the page
- **Full-screen modals** - Click to view projects in large format
- **Interactive overlays** - Hover effects and smooth transitions
- **Cross-origin support** - Sandboxed iframes for security

### Streamlit Integration
- **Python backend** - Streamlit app for deployment on Streamlit Cloud
- **Data management** - Centralized portfolio data structure
- **API integration** - Fetch and display modern web components
- **Cloud deployment** - Ready for Streamlit Cloud hosting

### Framer-Inspired Design
- **Modern dark theme** - Professional dark color scheme
- **Clean typography** - Space Grotesk and Inter fonts
- **Responsive layout** - Two-column desktop, single-column mobile
- **Interactive elements** - Hover effects and smooth transitions
- **Contact form** - Functional contact form with validation

## 🛠️ Tech Stack

### Frontend
- **React 18** - Latest React features and hooks
- **Framer Motion** - Animation library for smooth transitions
- **CSS Grid & Flexbox** - Modern layout techniques
- **CSS Custom Properties** - Dynamic theming and colors
- **Intersection Observer** - Scroll-based animations

### Backend
- **Streamlit** - Python web framework for data apps
- **Python 3.8+** - Modern Python features
- **JSON** - Data serialization and storage

### Static HTML/CSS
- **HTML5** - Semantic markup and accessibility
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript** - Interactive form handling and animations
- **Google Fonts** - Space Grotesk and Inter typography

### Development Tools
- **Babel** - JavaScript transpilation for browser compatibility
- **CDN Resources** - External libraries for rapid development
- **Git** - Version control and collaboration

## 📁 Project Structure

```
mukeshyadav.github.io/
├── portfolio_app.py          # Main Streamlit application
├── streamlit_portfolio.py    # Alternative Streamlit implementation
├── framer_portfolio.html     # Framer-inspired HTML portfolio
├── framer_styles.css         # Framer portfolio styles
├── index.html               # HTML entry point
├── styles.css               # Global CSS styles
├── app.js                   # Main React application
├── components/              # React components
│   ├── Navbar.js           # Navigation component
│   ├── Hero.js             # Hero section component
│   ├── About.js            # About section component
│   ├── Skills.js           # Skills section component
│   ├── Projects.js         # Projects with live previews
│   ├── Experience.js       # Experience timeline
│   └── Contact.js          # Contact section
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 🎨 Design Features

### Color Scheme
- **Primary**: `#87CEEB` (Sky Blue)
- **Secondary**: `#B0E0E6` (Powder Blue)
- **Accent**: `#6366F1` (Indigo)
- **Background**: `#000000` (Black)
- **Text**: `#FFFFFF` (White) / `#9CA3AF` (Gray)

### Animations
- **Fade-in effects** - Smooth entrance animations
- **Hover interactions** - Interactive element feedback
- **Scroll-triggered** - Elements animate on scroll
- **Loading states** - Animated loading screens
- **Modal transitions** - Smooth open/close animations

### Components
- **Glass morphism** - Modern glass-like effects
- **Gradient backgrounds** - Dynamic color gradients
- **Floating shapes** - Animated background elements
- **Interactive cards** - Hover and click effects
- **Responsive grids** - Adaptive layouts

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Git for version control

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mukeshyadav/mukeshyadav.github.io.git
   cd mukeshyadav.github.io
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run portfolio_app.py
   ```

4. **Open in browser**
   - Navigate to `http://localhost:8501` for Streamlit app
   - Open `framer_portfolio.html` for Framer-inspired portfolio
   - The portfolio will load with live project previews

### Development

1. **Edit portfolio data** - Modify `portfolio_app.py` to update content
2. **Customize styling** - Edit `styles.css` for visual changes
3. **Add components** - Create new React components in `components/`
4. **Update projects** - Add new projects to the portfolio data
5. **Framer portfolio** - Edit `framer_portfolio.html` and `framer_styles.css`

## 📱 Responsive Design

### Breakpoints
- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

### Mobile Features
- **Touch-friendly** - Optimized for touch interactions
- **Hamburger menu** - Collapsible navigation
- **Stacked layouts** - Single-column mobile layouts
- **Optimized images** - Responsive image sizing
- **Fast loading** - Optimized for mobile networks

## 🔧 Customization

### Adding New Projects
1. Add project data to `portfolio_data['projects']` in `portfolio_app.py`
2. Include `preview_url` for live preview functionality
3. Add project features and tech stack
4. Update GitHub and demo links

### Modifying Styles
1. Edit CSS variables in `styles.css`
2. Update color scheme and gradients
3. Modify animations and transitions
4. Adjust responsive breakpoints

### Adding New Sections
1. Create new React component in `components/`
2. Add section data to portfolio structure
3. Include in main app rendering
4. Add navigation links

## 🌐 Deployment

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect repository to Streamlit Cloud
3. Deploy with `streamlit run portfolio_app.py`
4. Configure custom domain (optional)

### GitHub Pages
1. Enable GitHub Pages in repository settings
2. Set source to main branch
3. Configure custom domain (optional)
4. Update DNS settings

### Other Platforms
- **Netlify** - Drag and drop deployment
- **Vercel** - Git-based deployment
- **Heroku** - Container deployment
- **AWS S3** - Static hosting

## 📊 Performance

### Optimization Features
- **Lazy loading** - Images and iframes load on demand
- **CDN resources** - Fast external library loading
- **Minified assets** - Reduced file sizes
- **Caching** - Browser caching for static assets
- **Compression** - Gzip compression for faster loading

### Performance Metrics
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **First Input Delay**: < 100ms

## 🔒 Security

### Security Features
- **Sandboxed iframes** - Secure project previews
- **Content Security Policy** - XSS protection
- **HTTPS only** - Secure connections
- **Input validation** - Sanitized user inputs
- **CORS headers** - Cross-origin security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mukesh Yadav**
- Email: mukeshyadavp91@gmail.com
- LinkedIn: [linkedin.com/in/mukesh-mlops](https://linkedin.com/in/mukesh-mlops)
- GitHub: [github.com/MukeshPyatla](https://github.com/MukeshPyatla)

## 🙏 Acknowledgments

- **Streamlit** - For the amazing Python web framework
- **React** - For the powerful frontend library
- **Framer Motion** - For smooth animations
- **Google Fonts** - For beautiful typography
- **React Icons** - For comprehensive icon library

## 📈 Future Enhancements

- [ ] Dark/Light theme toggle
- [ ] Blog section integration
- [ ] Contact form functionality
- [ ] Analytics integration
- [ ] SEO optimization
- [ ] PWA features
- [ ] Multi-language support
- [ ] Advanced animations
- [ ] Performance monitoring
- [ ] A/B testing capabilities

---

**Built with ❤️ using React, JavaScript, HTML, CSS, and Streamlit** 