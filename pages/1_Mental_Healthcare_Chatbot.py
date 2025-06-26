# =======================================================================================
# ENHANCED MENTAL HEALTHCARE INFORMATION CHATBOT
# =======================================================================================

import streamlit as st
import google.generativeai as genai
import time
from datetime import datetime

# Enhanced page configuration
st.set_page_config(
    page_title="Mental Healthcare Assistant | AI Wellness Hub",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional chatbot styling
def load_chatbot_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styling */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main > div {
        padding-top: 1rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Header Section */
    .chatbot-header {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.3);
    }
    
    .chatbot-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .chatbot-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .disclaimer-badge {
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
        backdrop-filter: blur(10px);
    }
    
    /* Chat Interface Styling */
    .chat-container {
        background: white;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid #e5e7eb;
        margin-bottom: 2rem;
        overflow: hidden;
    }
    
    /* Enhanced message styling */
    .stChatMessage {
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
    }
    
    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(135deg, #eff6ff, #dbeafe);
        border-left: 4px solid #3b82f6;
    }
    
    .stChatMessage[data-testid="chat-message-assistant"] {
        background: linear-gradient(135deg, #f0fdf4, #dcfce7);
        border-left: 4px solid #10b981;
    }
    
    /* Info Cards */
    .info-card {
        background: linear-gradient(145deg, #f8fafc, #e2e8f0);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #4f46e5;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .feature-item {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-title {
        font-weight: 600;
        color: #374151;
        margin-bottom: 0.5rem;
    }
    
    .feature-description {
        font-size: 0.9rem;
        color: #6b7280;
        line-height: 1.5;
    }
    
    /* Crisis Resources */
    .crisis-alert {
        background: linear-gradient(135deg, #fef2f2, #fee2e2);
        border: 2px solid #f87171;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .crisis-title {
        color: #dc2626;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .crisis-resource {
        background: white;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 3px solid #dc2626;
    }
    
    /* Usage Statistics */
    .stats-container {
        background: linear-gradient(135deg, #1f2937, #374151);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 2rem 0;
        text-align: center;
    }
    
    .stat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
        color: #60a5fa;
    }
    
    .stat-label {
        font-size: 0.8rem;
        opacity: 0.8;
        margin-top: 0.25rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .chatbot-title {
            font-size: 2rem;
        }
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
    
    /* Custom Streamlit overrides */
    .stChatInput > div {
        border-radius: 25px !important;
        border: 2px solid #e5e7eb !important;
    }
    
    .stChatInput > div:focus-within {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }
    
    .stSpinner {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Load custom styling
load_chatbot_css()

# --- ENHANCED HEADER SECTION ---
st.markdown("""
<div class="chatbot-header">
    <h1 class="chatbot-title">🧠 Mental Healthcare Assistant</h1>
    <p class="chatbot-subtitle">Your trusted resource for mental health information and guidance</p>
    <div class="disclaimer-badge">
        ⚠️ For informational purposes only • Not medical advice
    </div>
</div>
""", unsafe_allow_html=True)

# --- FEATURES OVERVIEW ---
st.markdown("""
<div class="feature-grid">
    <div class="feature-item">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Therapy Information</div>
        <div class="feature-description">Learn about CBT, DBT, and other therapeutic approaches</div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">👥</div>
        <div class="feature-title">Provider Guidance</div>
        <div class="feature-description">Understand the difference between therapists, psychologists, and psychiatrists</div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">💰</div>
        <div class="feature-title">Insurance Help</div>
        <div class="feature-description">Navigate mental health coverage and costs</div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Finding Care</div>
        <div class="feature-description">Tips for finding the right mental health professional</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- CRISIS RESOURCES SECTION ---
st.markdown("""
<div class="crisis-alert">
    <div class="crisis-title">🚨 Need Immediate Help?</div>
    <div class="crisis-resource">
        <strong>Crisis Text Line:</strong> Text HOME to <strong>741741</strong>
    </div>
    <div class="crisis-resource">
        <strong>National Suicide Prevention Lifeline:</strong> Call or text <strong>988</strong>
    </div>
    <div class="crisis-resource">
        <strong>The Trevor Project (LGBTQ+):</strong> <strong>1-866-488-7386</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# Configure the Gemini API Key from secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    api_configured = True
except Exception:
    st.error("🔑 **API Configuration Error:** Gemini API Key not found. Please check your .streamlit/secrets.toml file.")
    st.info("💡 **For developers:** Add your GEMINI_API_KEY to the secrets.toml file to enable the chatbot functionality.")
    api_configured = False
    st.stop()

@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_chatbot_response(user_query):
    """Enhanced chatbot response function with better error handling and formatting"""
    
    system_prompt = """
    You are a professional Mental Healthcare Information Assistant designed to provide clear, evidence-based information about mental healthcare topics. You maintain a warm, empathetic, and professional tone while strictly adhering to safety guidelines.

    **YOUR CORE RESPONSIBILITIES:**
    
    1. **INFORMATION SCOPE:** Provide general information about:
       - Types of therapy (CBT, DBT, EMDR, etc.) and their applications
       - What to expect in therapy sessions
       - Differences between mental health professionals (therapists, psychologists, psychiatrists)
       - How to find mental health providers
       - Insurance coverage for mental health services
       - General mental health concepts and terminology
       - Self-care strategies and wellness practices
       - Mental health resources and support systems

    2. **STRICT LIMITATIONS:**
       - **NEVER provide medical advice or diagnoses**
       - **NEVER recommend specific medications**
       - **NEVER make clinical assessments**
       - **NEVER provide crisis counseling**

    3. **CRISIS INTERVENTION PROTOCOL:**
       If the user mentions self-harm, suicide, severe distress, or appears to be in crisis, respond ONLY with:
       
       "I'm concerned about what you're sharing. Please know that immediate help is available:
       
       🚨 **Crisis Text Line:** Text HOME to 741741
       📞 **National Suicide Prevention Lifeline:** Call or text 988
       🌈 **The Trevor Project (LGBTQ+):** 1-866-488-7386
       
       These services have trained professionals ready to help you right now. Please reach out to them immediately."

    4. **RESPONSE GUIDELINES:**
       - Use clear, accessible language
       - Provide structured, helpful information
       - Include relevant disclaimers when appropriate
       - Be empathetic but maintain professional boundaries
       - If unsure about a topic, acknowledge limitations and suggest consulting professionals

    5. **OFF-TOPIC HANDLING:**
       For non-mental health questions, politely redirect: "I specialize in mental healthcare information. For that topic, I'd recommend consulting other appropriate resources. Is there anything about mental health I can help you with?"
    """
    
    try:
        gemini_model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Enhanced prompt with context
        full_prompt = f"""
        {system_prompt}
        
        CURRENT CONTEXT: This is a mental healthcare information chatbot in a professional wellness platform.
        
        USER QUESTION: {user_query}
        
        Please provide a helpful, informative response following all guidelines above.
        """
        
        response = gemini_model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"⚠️ I apologize, but I'm experiencing technical difficulties right now. Please try again in a moment, or contact the crisis resources above if you need immediate help. Error details: {str(e)}"

# Initialize enhanced chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "👋 **Welcome!** I'm here to provide information about mental healthcare topics.\n\n💡 **I can help with:**\n- Understanding different types of therapy\n- Finding mental health providers\n- Insurance and coverage questions\n- What to expect from treatment\n\n❓ **Try asking:** *\"What's the difference between a therapist and a psychologist?\"* or *\"What is cognitive behavioral therapy?\"*"
        }
    ]

if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# --- CHAT INTERFACE ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat messages with enhanced styling
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else "👤"):
        st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Enhanced chat input with suggestions
sample_questions = [
    "What is cognitive behavioral therapy?",
    "How do I find a therapist?",
    "What's the difference between a psychologist and psychiatrist?",
    "Does insurance cover therapy?",
    "What should I expect in my first therapy session?"
]

# Display sample questions if no conversation has started
if len(st.session_state.messages) <= 1:
    st.info("💬 **Quick Start:** Try one of these common questions:")
    
    cols = st.columns(2)
    for i, question in enumerate(sample_questions):
        col = cols[i % 2]
        if col.button(f"❓ {question}", key=f"sample_{i}", use_container_width=True):
            # Add the question to chat
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user", avatar="👤"):
                st.markdown(question)
            
            # Get and display response
            with st.chat_message("assistant", avatar="🤖"):
                with st.spinner("🔍 Searching for information..."):
                    response = get_chatbot_response(question)
                    st.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.chat_count += 1
            st.rerun()

# Main chat input
if prompt := st.chat_input("💬 Ask me about mental healthcare topics...", key="main_chat_input"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🔍 Finding information..."):
            response = get_chatbot_response(prompt)
            st.markdown(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.chat_count += 1

# --- USAGE STATISTICS ---
if st.session_state.chat_count > 0:
    st.markdown(f"""
    <div class="stats-container">
        <h4>📊 Session Statistics</h4>
        <div class="stat-grid">
            <div class="stat-item">
                <div class="stat-number">{st.session_state.chat_count}</div>
                <div class="stat-label">Questions Asked</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{len(st.session_state.messages)}</div>
                <div class="stat-label">Total Messages</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{datetime.now().strftime('%H:%M')}</div>
                <div class="stat-label">Current Time</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CLEAR CHAT BUTTON ---
if len(st.session_state.messages) > 1:
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.messages = st.session_state.messages[:1]  # Keep welcome message
        st.session_state.chat_count = 0
        st.rerun()

# --- FOOTER INFORMATION ---
with st.expander("ℹ️ Important Information & Disclaimers"):
    st.markdown("""
    **🔒 Privacy & Security:**
    - Your conversations are not stored permanently
    - No personal information is collected
    - All interactions are anonymous
    
    **⚠️ Important Disclaimers:**
    - This chatbot provides general information only
    - It is not a substitute for professional medical advice
    - Always consult with qualified healthcare providers for personalized care
    - In emergencies, contact emergency services immediately
    
    **🎯 Best Use Cases:**
    - Learning about mental health concepts
    - Understanding different therapy types
    - Getting guidance on finding providers
    - Insurance and coverage questions
    """)

# --- TECHNICAL INFO (FOR DEVELOPERS) ---
if st.checkbox("🔧 Show Technical Information", value=False):
    st.markdown("**System Status:**")
    st.write(f"- API Status: {'✅ Connected' if api_configured else '❌ Not Connected'}")
    st.write(f"- Session Messages: {len(st.session_state.messages)}")
    st.write(f"- Questions Asked: {st.session_state.chat_count}")
    st.write(f"- Model: Gemini-2.0-Flash")
    st.write(f"- Cache TTL: 1 hour")