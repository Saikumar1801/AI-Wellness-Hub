# =======================================================================================
# AI WELLNESS HUB - ENHANCED PROFESSIONAL HOME PAGE
# =======================================================================================

import streamlit as st
from PIL import Image
import base64

# Set the main configuration for the entire app
st.set_page_config(
    page_title="AI Wellness Hub | Workplace Mental Health Solutions",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styling */
    .main > div {
        padding-top: 2rem;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 300;
        opacity: 0.95;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Mission Section */
    .mission-card {
        background: linear-gradient(145deg, #f8fafc, #e2e8f0);
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 5px solid #667eea;
        margin: 2rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    }
    
    .mission-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #4a5568;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        font-size: 1rem;
        line-height: 1.6;
        color: #4a5568;
        margin-bottom: 1.5rem;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
    }
    
    .feature-list li {
        background: #f7fafc;
        margin: 0.5rem 0;
        padding: 0.8rem 1rem;
        border-radius: 8px;
        border-left: 3px solid #667eea;
        font-size: 0.95rem;
    }
    
    /* Stats Section */
    .stats-container {
        background: linear-gradient(135deg, #2d3748, #4a5568);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        color: white;
        text-align: center;
    }
    
    .stat-item {
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #90cdf4;
    }
    
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    /* CTA Section */
    .cta-container {
        background: linear-gradient(135deg, #48bb78, #38a169);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 2rem 0;
    }
    
    .cta-title {
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .hero-subtitle {
            font-size: 1.2rem;
        }
        .feature-card {
            margin-bottom: 2rem;
        }
    }
    
    /* Custom Streamlit Element Styling */
    .stAlert > div {
        background: linear-gradient(135deg, #e6fffa, #b2f5ea);
        border: 1px solid #81e6d9;
        border-radius: 10px;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f7fafc, #edf2f7);
    }
    </style>
    """, unsafe_allow_html=True)

# Load custom styling
load_custom_css()

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">🧠 AI Wellness Hub</h1>
    <p class="hero-subtitle">Transforming workplace mental health through intelligent, data-driven solutions that empower both leadership and employees</p>
</div>
""", unsafe_allow_html=True)

# --- MISSION SECTION ---
st.markdown("""
<div class="mission-card">
    <h2 style="color: #2d3748; font-weight: 600; margin-bottom: 1.5rem;">🎯 Our Mission</h2>
    <div class="mission-text">
        In today's rapidly evolving work landscape, supporting employee mental well-being has become a strategic imperative. Yet many organizations find themselves caught between good intentions and meaningful action, lacking the sophisticated tools needed to understand their unique cultural dynamics and implement evidence-based support strategies.
        <br><br>
        The <strong>AI Wellness Hub</strong> was engineered to eliminate this gap. Developed for the <strong>AITHON: 14 Days of AI for Social Good</strong>, our platform combines cutting-edge artificial intelligence with proven mental health frameworks to deliver both comprehensive organizational insights for leadership and accessible, personalized support for every team member.
    </div>
</div>
""", unsafe_allow_html=True)

# --- STATISTICS SECTION ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">76%</div>
        <div class="stat-label">Of employees report workplace stress</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">$300B</div>
        <div class="stat-label">Annual cost of workplace stress</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">60%</div>
        <div class="stat-label">Improvement with proper support</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">4:1</div>
        <div class="stat-label">ROI on mental health programs</div>
    </div>
    """, unsafe_allow_html=True)

# --- FEATURES SECTION ---
st.markdown("<h2 style='text-align: center; color: #2d3748; margin: 3rem 0 2rem 0; font-weight: 600;'>🚀 Our Intelligent Solutions</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📊</span>
        <h3 class="feature-title">Workplace Wellness Advisor</h3>
        <p class="feature-description">
            An enterprise-grade diagnostic platform designed for managers, HR leaders, and organizational development professionals. Delivers comprehensive, actionable insights into your workplace mental health landscape.
        </p>
        <ul class="feature-list">
            <li><strong>🎯 Predictive Analytics:</strong> AI-powered forecasting of mental health treatment likelihood with 85%+ accuracy</li>
            <li><strong>📈 Wellness Scorecard:</strong> Quantified assessment of Support Structures and Cultural Openness metrics</li>
            <li><strong>🔍 SHAP Analysis:</strong> Explainable AI revealing the precise factors driving your organizational outcomes</li>
            <li><strong>🤖 AI Strategy Advisor:</strong> Personalized recommendations from our advanced language model</li>
            <li><strong>⚡ Action Automation:</strong> Generate professional communications and meeting frameworks instantly</li>
            <li><strong>📑 Executive Reports:</strong> Publication-ready PDF summaries for stakeholder presentation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">💬</span>
        <h3 class="feature-title">Mental Health Resource Assistant</h3>
        <p class="feature-description">
            A secure, anonymous information resource available 24/7 to all team members. Provides evidence-based mental health education and crisis intervention protocols.
        </p>
        <ul class="feature-list">
            <li><strong>🧠 Comprehensive Knowledge Base:</strong> Expert information on therapy modalities, treatment options, and healthcare navigation</li>
            <li><strong>🔒 Privacy-First Design:</strong> Zero data collection, completely anonymous interactions</li>
            <li><strong>🚨 Crisis Intervention:</strong> Intelligent detection and immediate connection to professional 24/7 support services</li>
            <li><strong>🎓 Educational Resources:</strong> Understanding insurance coverage, finding providers, and preparing for therapy</li>
            <li><strong>🌍 Cultural Sensitivity:</strong> Inclusive guidance respecting diverse backgrounds and experiences</li>
            <li><strong>📱 Multi-Platform Access:</strong> Seamless experience across desktop, tablet, and mobile devices</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- CALL TO ACTION ---
st.markdown("""
<div class="cta-container">
    <h3 class="cta-title">Ready to Transform Your Workplace Wellness?</h3>
    <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">Choose your path to better mental health support</p>
</div>
""", unsafe_allow_html=True)

# Enhanced info box
st.info("👈 **Get Started Now** - Select your preferred tool from the navigation sidebar to begin your wellness journey!", icon="🚀")

# --- FOOTER SECTION ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**🏆 AITHON 2024**")
    st.markdown("*14 Days of AI for Social Good*")

with footer_col2:
    st.markdown("**🛡️ Privacy & Security**")
    st.markdown("*Your data remains confidential*")

with footer_col3:
    st.markdown("**💡 Evidence-Based**")
    st.markdown("*Powered by research & AI*")

st.markdown("<div style='text-align: center; color: #718096; margin-top: 2rem; font-size: 0.9rem;'>Built with ❤️ for workplace mental health • AI Wellness Hub © 2024</div>", unsafe_allow_html=True)