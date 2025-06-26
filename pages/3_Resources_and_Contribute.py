import streamlit as st
from datetime import datetime

# Enhanced page configuration
st.set_page_config(
    page_title="Resources & Support | AI Wellness Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional resources page styling
def load_resources_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main > div { padding-top: 1rem; max-width: 1200px; margin: 0 auto; }
    .resources-header { background: linear-gradient(135deg, #059669, #10b981); padding: 3rem 2rem; border-radius: 20px; color: white; text-align: center; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(5, 150, 105, 0.3); }
    .resources-title { font-size: 3rem; font-weight: 700; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    .resources-subtitle { font-size: 1.3rem; opacity: 0.95; max-width: 800px; margin: 0 auto; }
    .crisis-section { background: linear-gradient(135deg, #fef2f2, #fee2e2); border: 2px solid #f87171; border-radius: 15px; padding: 2rem; margin: 2rem 0; position: relative; overflow: hidden; }
    .crisis-section::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, #dc2626, #ef4444, #f87171); }
    .crisis-title { color: #dc2626; font-size: 1.8rem; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }
    .crisis-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }
    .crisis-card { background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #dc2626; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; }
    .crisis-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(220, 38, 38, 0.15); }
    .crisis-card-title { font-size: 1.2rem; font-weight: 600; color: #dc2626; margin-bottom: 0.5rem; }
    .crisis-card-contact { font-size: 1.1rem; font-weight: 700; color: #1f2937; margin: 0.5rem 0; padding: 0.5rem; background: #f9fafb; border-radius: 6px; }
    .crisis-card-description { font-size: 0.95rem; color: #4b5563; line-height: 1.5; }
    .resource-category { background: white; border-radius: 15px; padding: 2rem; margin: 2rem 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08); border: 1px solid #e5e7eb; }
    .category-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 2px solid #e5e7eb; }
    .category-icon { font-size: 2.5rem; padding: 0.5rem; background: linear-gradient(135deg, #eff6ff, #dbeafe); border-radius: 12px; }
    .category-title { font-size: 1.8rem; font-weight: 600; color: #1f2937; }
    .resource-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
    .resource-item { background: linear-gradient(145deg, #f8fafc, #f1f5f9); padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0; transition: all 0.3s ease; }
    .resource-item:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.1); border-color: #3b82f6; }
    .resource-title { font-size: 1.1rem; font-weight: 600; color: #1e40af; margin-bottom: 0.5rem; }
    .resource-description { font-size: 0.9rem; color: #4b5563; line-height: 1.5; margin-bottom: 1rem; }
    .resource-link { display: inline-flex; align-items: center; gap: 0.5rem; color: #3b82f6; text-decoration: none; font-weight: 500; font-size: 0.9rem; padding: 0.5rem 1rem; background: white; border: 1px solid #3b82f6; border-radius: 6px; transition: all 0.3s ease; }
    .resource-link:hover { background: #3b82f6; color: white; text-decoration: none; }
    .contribute-section { background: linear-gradient(135deg, #f0f9ff, #e0f2fe); border: 2px solid #0ea5e9; border-radius: 20px; padding: 2.5rem; margin: 2rem 0; text-align: center; position: relative; overflow: hidden; }
    .contribute-section::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, #0ea5e9, #06b6d4, #0891b2); }
    .contribute-title { font-size: 2.2rem; font-weight: 700; color: #0c4a6e; margin-bottom: 1rem; }
    .contribute-description { font-size: 1.1rem; color: #164e63; line-height: 1.7; max-width: 800px; margin: 0 auto 2rem auto; }
    .cta-button { display: inline-flex; align-items: center; gap: 0.5rem; background: linear-gradient(135deg, #0ea5e9, #06b6d4); color: white; padding: 1rem 2rem; border-radius: 10px; text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3); }
    .cta-button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(14, 165, 233, 0.4); text-decoration: none; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Load custom styling
load_resources_css()

# --- HEADER SECTION ---
st.markdown("""
<div class="resources-header">
    <h1 class="resources-title">📚 Resources & Support</h1>
    <p class="resources-subtitle">A curated collection of mental health resources, crisis support, and ways to contribute to our community-driven platform.</p>
</div>
""", unsafe_allow_html=True)

# --- CRISIS SUPPORT SECTION ---
st.markdown("""
<div class="crisis-section">
    <h2 class="crisis-title">🚨 Immediate Crisis Support</h2>
    <p style="color: #7f1d1d; font-size: 1.1rem; margin-bottom: 1.5rem;">
        <strong>If you are in crisis or need immediate assistance, please reach out to these professional services. They are available 24/7 and completely confidential.</strong>
    </p>
    <div class="crisis-grid">
        <div class="crisis-card">
            <div class="crisis-card-title">💬 Crisis Text Line</div>
            <div class="crisis-card-contact">Text "HOME" to 741741</div>
            <div class="crisis-card-description">Available 24/7 from anywhere in the US for any type of crisis. Trained crisis counselors provide support via text message.</div>
        </div>
        <div class="crisis-card">
            <div class="crisis-card-title">📞 National Suicide Prevention Lifeline</div>
            <div class="crisis-card-contact">Call or Text 988</div>
            <div class="crisis-card-description">Free, confidential support 24/7 for people in suicidal crisis or emotional distress. Also provides resources for loved ones.</div>
        </div>
        <div class="crisis-card">
            <div class="crisis-card-title">🌈 The Trevor Project</div>
            <div class="crisis-card-contact">1-866-488-7386 or Text START to 678-678</div>
            <div class="crisis-card-description">Specialized crisis intervention and suicide prevention for LGBTQ+ young people under 25.</div>
        </div>
        <div class="crisis-card">
            <div class="crisis-card-title">🛡️ SAMHSA National Helpline</div>
            <div class="crisis-card-contact">1-800-662-4357</div>
            <div class="crisis-card-description">Treatment referral and information service for mental health and substance use disorders. Available 24/7.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- RESOURCE CATEGORIES ---
with st.container():
    st.markdown("<h2 style='text-align: center; color: #2d3748; margin: 3rem 0 2rem 0; font-weight: 600;'>Explore Verified Resources</h2>", unsafe_allow_html=True)
    
    # Mental Health Organizations
    st.markdown("""
    <div class="resource-category">
        <div class="category-header"><div class="category-icon">🏥</div><div class="category-title">Leading Mental Health Organizations</div></div>
        <div class="resource-grid">
            <div class="resource-item">
                <div class="resource-title">NAMI (National Alliance on Mental Illness)</div>
                <div class="resource-description">Comprehensive resources, support groups, and educational programs for individuals and families affected by mental illness.</div>
                <a href="https://nami.org" target="_blank" class="resource-link">Visit NAMI 🔗</a>
            </div>
            <div class="resource-item">
                <div class="resource-title">Mental Health America</div>
                <div class="resource-description">Mental health screening tools, resources, and advocacy for mental health policies and programs.</div>
                <a href="https://mhanational.org" target="_blank" class="resource-link">Visit MHA 🔗</a>
            </div>
            <div class="resource-item">
                <div class="resource-title">American Psychological Association</div>
                <div class="resource-description">Evidence-based information about mental health conditions, treatments, and finding qualified providers.</div>
                <a href="https://apa.org" target="_blank" class="resource-link">Visit APA 🔗</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Therapy & Treatment Resources
    st.markdown("""
    <div class="resource-category">
        <div class="category-header"><div class="category-icon">🧠</div><div class="category-title">Therapy & Treatment Finders</div></div>
        <div class="resource-grid">
            <div class="resource-item">
                <div class="resource-title">Psychology Today Therapist Finder</div>
                <div class="resource-description">Comprehensive therapist directory with filters for location, insurance, specialties, and treatment approaches.</div>
                <a href="https://www.psychologytoday.com/us/therapists" target="_blank" class="resource-link">Find Therapists 🔗</a>
            </div>
            <div class="resource-item">
                <div class="resource-title">Open Path Collective</div>
                <div class="resource-description">Affordable therapy options with sessions ranging from $40-$70 for those without adequate insurance coverage.</div>
                <a href="https://openpathcollective.org" target="_blank" class="resource-link">Find Affordable Care 🔗</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CONTRIBUTION SECTION ---
st.markdown("""
<div class="contribute-section">
    <h2 class="contribute-title">🚀 Help Improve AI for Everyone</h2>
    <p class="contribute-description">
        Our AI Wellness Hub is a community-driven platform. By sharing your anonymous experiences, you're helping us build smarter, more effective mental health tools for workplaces everywhere.
    </p>
    <div style="margin-top: 2rem;">
        <a href="https://forms.gle/your-google-form-link-here" target="_blank" class="cta-button">
            📝 Contribute Your Experience Anonymously
        </a>
    </div>
    <div style="margin-top: 2rem; padding: 1rem; background: rgba(255,255,255,0.7); border-radius: 10px;">
        <p style="font-size: 0.9rem; color: #475569; margin: 0;">
            <strong>Your Privacy is Our Priority:</strong> All submissions are used exclusively for model training and research. No individual responses are ever shared or published.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #6b7280;'>AI Wellness Hub © {datetime.now().year} | AITHON 2024 Project for Social Good</div>", unsafe_allow_html=True)