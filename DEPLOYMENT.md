# 🚀 Streamlit Cloud Deployment Guide

## Quick Deploy to Streamlit Cloud

### Option 1: Deploy from GitHub (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Add main portfolio app for Streamlit Cloud"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `mukeshyadav/mukeshyadav.github.io`
   - Set the main file path: `main_portfolio.py`
   - Click "Deploy"

### Option 2: Direct File Upload

1. **Upload `main_portfolio.py`** to Streamlit Cloud
2. **Upload `requirements.txt`** (optional - Streamlit will auto-detect)
3. **Deploy instantly**

## 🎯 What's Included

The `main_portfolio.py` file is completely self-contained and includes:

- ✅ **All CSS styles** embedded in the Python file
- ✅ **All portfolio data** (experience, projects, skills)
- ✅ **Real project links** with live demos
- ✅ **Responsive design** for all devices
- ✅ **Modern glassmorphism effects**
- ✅ **Animated background** and hover effects
- ✅ **No external dependencies** except Streamlit

## 📁 File Structure for Deployment

```
mukeshyadav.github.io/
├── main_portfolio.py      # 🎯 Main file for Streamlit Cloud
├── requirements.txt       # Minimal dependencies
├── DEPLOYMENT.md         # This guide
└── README.md            # Project documentation
```

## 🔧 Customization

To modify the portfolio content, edit the `get_portfolio_data()` function in `main_portfolio.py`:

```python
def get_portfolio_data():
    return {
        'name': 'Your Name',
        'title': 'Your Title',
        'email': 'your.email@example.com',
        # ... modify other data
    }
```

## 🌐 Live Demo

Once deployed, your portfolio will be available at:
`https://your-app-name.streamlit.app`

## ✨ Features

- **Dark theme** with animated background
- **Glassmorphism effects** on all cards
- **Real project demos** with working links
- **Responsive design** for mobile and desktop
- **Professional MLOps content**
- **Interactive hover effects**
- **Modern typography** with Space Grotesk and Inter fonts

## 🚀 Performance

- **Fast loading** - All assets embedded
- **No external requests** - Self-contained
- **Optimized CSS** - Minimal file size
- **Mobile-friendly** - Responsive design

---

**Ready to deploy?** Just push to GitHub and connect to Streamlit Cloud! 🎉
