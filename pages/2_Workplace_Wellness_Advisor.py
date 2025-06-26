# =======================================================================================
# ENHANCED PROFESSIONAL WORKPLACE WELLNESS ADVISOR
# =======================================================================================

import streamlit as st
import pandas as pd
import pickle
import os
import google.generativeai as genai
import shap
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from fpdf import FPDF
import base64
from datetime import datetime
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Workplace Wellness Advisor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .insight-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }
    
    .recommendation-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1.5rem 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .sidebar-content {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .feature-highlight {
        border: 2px solid #667eea;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background: rgba(102, 126, 234, 0.05);
    }
    
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-high { background-color: #ff4757; }
    .status-medium { background-color: #ffa502; }
    .status-low { background-color: #2ed573; }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
<div class="main-header">
    <h1>🧠 AI Workplace Wellness Advisor</h1>
    <p style="font-size: 1.2em; margin-top: 1rem; opacity: 0.9;">
        Advanced predictive analytics for workplace mental health assessment
    </p>
    <p style="font-size: 1em; margin-top: 0.5rem; opacity: 0.8;">
        Powered by Machine Learning • SHAP Explainability • Gemini AI
    </p>
</div>
""", unsafe_allow_html=True)

# --- CONFIGURATION AND LOADING ---
@st.cache_data
def load_config():
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        return True
    except Exception:
        st.error("⚠️ Gemini API Key not configured. Please check your secrets.toml file.")
        return False

@st.cache_resource
def load_ml_assets():
    """Load all ML models and preprocessing assets"""
    required_files = ['best_model.pkl', 'scaler.pkl', 'shap_explainer.pkl']
    
    if not all(os.path.exists(file) for file in required_files):
        st.error("❌ Required ML model files not found. Please run the training script first.")
        return None, None, None
    
    try:
        with open('best_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        with open('shap_explainer.pkl', 'rb') as f:
            explainer = pickle.load(f)
        
        st.success("✅ ML models loaded successfully")
        return model, scaler, explainer
    except Exception as e:
        st.error(f"❌ Error loading ML assets: {str(e)}")
        return None, None, None

# --- ENHANCED HELPER FUNCTIONS ---
def calculate_wellness_scores(inputs):
    """Calculate comprehensive wellness scores"""
    
    # Support Infrastructure Score
    support_components = {
        'benefits': 4 if inputs['benefits'] == 'Yes' else 1 if inputs['benefits'] == "Don't know" else 0,
        'anonymity': 3 if inputs['anonymity'] == 'Yes' else 1 if inputs['anonymity'] == "Don't know" else 0,
        'leave_ease': 3 if inputs['leave'] in ['Very easy', 'Somewhat easy'] else 1 if inputs['leave'] == "Don't know" else 0,
        'care_awareness': 2 if inputs['care_options'] == 'Yes' else 1 if inputs['care_options'] == 'Not sure' else 0
    }
    
    # Cultural Openness Score  
    culture_components = {
        'no_consequences': 4 if inputs['mental_health_consequence'] == 'No' else 2 if inputs['mental_health_consequence'] == 'Maybe' else 0,
        'supervisor_comfort': 3 if inputs['supervisor'] == 'Yes' else 2 if inputs['supervisor'] == 'Some of them' else 0,
        'peer_comfort': 2 if inputs['coworkers'] == 'Yes' else 1 if inputs['coworkers'] == 'Some of them' else 0,
        'equality': 2 if inputs['mental_vs_physical'] == 'Yes' else 1 if inputs['mental_vs_physical'] == "Don't know" else 0
    }
    
    support_score = sum(support_components.values()) / 12 * 100
    culture_score = sum(culture_components.values()) / 11 * 100
    
    return support_score, culture_score, support_components, culture_components

def create_wellness_dashboard(support_score, culture_score, support_components, culture_components):
    """Create interactive wellness dashboard"""
    
    # Overall scores gauge chart
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{'type': 'indicator'}, {'type': 'indicator'}]],
        subplot_titles=("Support Infrastructure", "Cultural Openness")
    )
    
    # Support score gauge
    fig.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = support_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Support Score"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "yellow"},
                {'range': [80, 100], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ), row=1, col=1)
    
    # Culture score gauge
    fig.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = culture_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Culture Score"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkgreen"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "yellow"},
                {'range': [80, 100], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ), row=1, col=2)
    
    fig.update_layout(height=400, showlegend=False)
    return fig

def create_risk_assessment_viz(prediction_proba, prediction):
    """Create risk assessment visualization"""
    
    risk_level = "High Risk" if prediction == 1 else "Low Risk"
    risk_color = "#ff4757" if prediction == 1 else "#2ed573"
    confidence = max(prediction_proba) * 100
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence,
        title = {'text': f"Risk Assessment: {risk_level}"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': risk_color},
            'steps': [
                {'range': [0, 30], 'color': "#2ed573"},
                {'range': [30, 70], 'color': "#ffa502"},
                {'range': [70, 100], 'color': "#ff4757"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 85
            }
        }
    ))
    
    fig.update_layout(height=300)
    return fig

@st.cache_data
def generate_ai_insights(prediction_text, confidence, support_score, culture_score):
    """Generate AI-powered insights using Gemini"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        As an expert workplace wellness consultant, analyze this workplace assessment:
        
        - Risk Level: {prediction_text} (Confidence: {confidence:.1f}%)
        - Support Infrastructure Score: {support_score:.1f}/100
        - Cultural Openness Score: {culture_score:.1f}/100
        
        Provide a comprehensive analysis with:
        1. **Executive Summary** (2-3 sentences)
        2. **Key Strengths** (bullet points)
        3. **Areas for Improvement** (bullet points)
        4. **Strategic Recommendations** (3-4 actionable items)
        5. **Implementation Timeline** (short-term vs long-term priorities)
        
        Keep the tone professional yet accessible. Focus on actionable insights.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Unable to generate AI insights at this time. Error: {str(e)}"

def create_enhanced_pdf_report(results_data):
    """Create a professional PDF report"""
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(102, 126, 234)
    pdf.cell(0, 15, 'AI Workplace Wellness Assessment Report', 0, 1, 'C')
    
    # Timestamp
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 10, f'Generated on: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}', 0, 1, 'C')
    pdf.ln(10)
    
    # Content sections
    for section_title, content in results_data.items():
        pdf.set_font("Arial", 'B', 14)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 10, section_title, 0, 1, 'L')
        pdf.ln(2)
        
        if isinstance(content, str):
            pdf.set_font("Arial", '', 11)
            # Handle encoding issues
            content_clean = content.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 6, content_clean)
        pdf.ln(5)
    
    return bytes(pdf.output(dest='S'))

# --- MAIN APPLICATION ---
def main():
    # Load configuration and assets
    if not load_config():
        st.stop()
    
    model, scaler, explainer = load_ml_assets()
    if not all([model, scaler, explainer]):
        st.stop()
    
    # Sidebar for input parameters
    with st.sidebar:
        st.markdown("### 📊 Assessment Parameters")
        
        with st.expander("👥 Company Profile", expanded=True):
            age = st.slider('Average Employee Age', 18, 80, 32, help="Average age of employees")
            gender = st.selectbox('Predominant Gender', ['Female', 'Male', 'Other'])
            no_employees = st.selectbox('Company Size', [
                '1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'
            ])
            tech_company = st.radio('Tech Company?', ['Yes', 'No'], horizontal=True)
            remote_work = st.radio('Remote Work Common?', ['Yes', 'No'], horizontal=True)
            family_history = st.radio('Family History Common?', ['Yes', 'No'], horizontal=True)
        
        with st.expander("🏢 Support & Benefits", expanded=True):
            benefits = st.selectbox('Mental Health Benefits?', ["Yes", "No", "Don't know"])
            care_options = st.selectbox('Care Options Awareness?', ["Yes", "No", "Not sure"])
            wellness_program = st.selectbox('Wellness Program Discusses MH?', ["Yes", "No", "Don't know"])
            seek_help = st.selectbox('Resources to Seek Help?', ["Yes", "No", "Don't know"])
            anonymity = st.selectbox('Anonymity Protected?', ["Yes", "No", "Don't know"])
            leave = st.selectbox('Ease of Mental Health Leave?', [
                'Very easy', 'Somewhat easy', "Don't know", 'Somewhat difficult', 'Very difficult'
            ])
        
        with st.expander("🤝 Culture & Communication", expanded=True):
            mental_vs_physical = st.selectbox('MH/Physical Health Treated Equally?', ["Yes", "No", "Don't know"])
            mental_health_consequence = st.selectbox('Negative Consequences for MH Discussion?', ['No', 'Maybe', 'Yes'])
            phys_health_consequence = st.selectbox('Negative Consequences for Physical Health Discussion?', ['No', 'Maybe', 'Yes'])
            coworkers = st.selectbox('Would Discuss with Coworkers?', ['Yes', 'Some of them', 'No'])
            supervisor = st.selectbox('Would Discuss with Supervisor?', ['Yes', 'Some of them', 'No'])
    
    # Main content area
    st.markdown("### 🎯 Ready to Analyze Your Workplace?")
    st.markdown("Complete the assessment parameters in the sidebar, then click the button below to generate your comprehensive wellness report.")
    
    if st.button('🚀 **Generate Comprehensive Analysis**', type="primary", use_container_width=True):
        with st.spinner('🔄 Processing your workplace assessment...'):
            
            # Data preprocessing
            encoding_maps = {
                'no_employees': {'1-5': 0, '6-25': 1, '26-100': 2, '100-500': 3, '500-1000': 4, 'More than 1000': 5},
                'benefits': {'Yes': 1, 'No': 0, "Don't know": -1},
                'care_options': {'Yes': 1, 'No': 0, "Not sure": -1},
                'wellness_program': {'Yes': 1, 'No': 0, "Don't know": -1},
                'seek_help': {'Yes': 1, 'No': 0, "Don't know": -1},
                'anonymity': {'Yes': 1, 'No': 0, "Don't know": -1},
                'tech_company': {'Yes': 1, 'No': 0},
                'remote_work': {'Yes': 1, 'No': 0},
                'family_history': {'Yes': 1, 'No': 0},
                'leave': {'Very difficult': -2, 'Somewhat difficult': -1, "Don't know": 0, 'Somewhat easy': 1, 'Very easy': 2},
                'mental_health_consequence': {'No': 2, 'Maybe': 1, 'Yes': 0},
                'phys_health_consequence': {'No': 2, 'Maybe': 1, 'Yes': 0},
                'coworkers': {'Yes': 2, 'Some of them': 1, 'No': 0},
                'supervisor': {'Yes': 2, 'Some of them': 1, 'No': 0},
                'mental_vs_physical': {'Yes': 1, 'No': 0, "Don't know": -1}
            }
            
            # Create input data
            input_data = {
                'Age': age,
                'no_employees': encoding_maps['no_employees'][no_employees],
                'tech_company': encoding_maps['tech_company'][tech_company],
                'remote_work': encoding_maps['remote_work'][remote_work],
                'family_history': encoding_maps['family_history'][family_history],
                'benefits': encoding_maps['benefits'][benefits],
                'care_options': encoding_maps['care_options'][care_options],
                'wellness_program': encoding_maps['wellness_program'][wellness_program],
                'seek_help': encoding_maps['seek_help'][seek_help],
                'anonymity': encoding_maps['anonymity'][anonymity],
                'leave': encoding_maps['leave'][leave],
                'mental_health_consequence': encoding_maps['mental_health_consequence'][mental_health_consequence],
                'phys_health_consequence': encoding_maps['phys_health_consequence'][phys_health_consequence],
                'coworkers': encoding_maps['coworkers'][coworkers],
                'supervisor': encoding_maps['supervisor'][supervisor],
                'mental_vs_physical': encoding_maps['mental_vs_physical'][mental_vs_physical],
                'Gender_male': 1 if gender == 'Male' else 0,
                'Gender_other': 1 if gender == 'Other' else 0
            }
            
            # Prepare data for prediction
            input_df = pd.DataFrame([input_data])[scaler.feature_names_in_]
            input_df_scaled = scaler.transform(input_df)
            
            # Make predictions
            prediction = model.predict(input_df_scaled)[0]
            prediction_proba = model.predict_proba(input_df_scaled)[0]
            
            # Calculate wellness scores
            current_inputs = locals()
            support_score, culture_score, support_components, culture_components = calculate_wellness_scores(current_inputs)
            
        # Display results
        st.markdown("---")
        st.markdown("## 📈 **Analysis Results**")
        
        # 1. Risk Assessment
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 🎯 Model Probability")
            risk_fig = create_risk_assessment_viz(prediction_proba, prediction)
            st.plotly_chart(risk_fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Quick Stats")
            confidence = max(prediction_proba) * 100
            risk_level = "High Possible" if prediction == 1 else "Low Possible"
            
            if prediction == 1:
                st.markdown(f"""
                <div class="metric-container">
                    <h4>🔴 Model Probability Detected</h4>
                    <p><strong>Confidence:</strong> {confidence:.1f}%</p>
                    <p><strong>Status:</strong> Requires attention</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="metric-container">
                    <h4>🟢 Low Risk Environment</h4>
                    <p><strong>Confidence:</strong> {confidence:.1f}%</p>
                    <p><strong>Status:</strong> Good workplace wellness foundation</p>
                </div>
                """, unsafe_allow_html=True)
        
        # 2. Wellness Dashboard
        st.markdown("### 🏥 Wellness Infrastructure Analysis")
        wellness_fig = create_wellness_dashboard(support_score, culture_score, support_components, culture_components)
        st.plotly_chart(wellness_fig, use_container_width=True)
        
        # 3. Detailed Breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🛠️ Support Infrastructure Components")
            for component, score in support_components.items():
                max_score = {'benefits': 4, 'anonymity': 3, 'leave_ease': 3, 'care_awareness': 2}[component]
                percentage = (score / max_score) * 100
                st.progress(percentage / 100)
                st.write(f"**{component.replace('_', ' ').title()}:** {score}/{max_score}")
        
        with col2:
            st.markdown("#### 🤝 Cultural Openness Components")
            for component, score in culture_components.items():
                max_score = {'no_consequences': 4, 'supervisor_comfort': 3, 'peer_comfort': 2, 'equality': 2}[component]
                percentage = (score / max_score) * 100
                st.progress(percentage / 100)
                st.write(f"**{component.replace('_', ' ').title()}:** {score}/{max_score}")
        
        # 4. SHAP Analysis
        st.markdown("### 🔍 Feature Impact Analysis")
        with st.spinner("Generating SHAP analysis..."):
            shap_values = explainer(input_df_scaled)
            
            # Create SHAP force plot
            force_plot_fig = shap.force_plot(
                explainer.expected_value[1], 
                shap_values.values[..., 1], 
                input_df, 
                matplotlib=True, 
                show=False
            )
            st.pyplot(force_plot_fig, bbox_inches='tight', use_container_width=True)
        
        # 5. AI Insights
        st.markdown("### 🤖 AI-Generated Insights & Recommendations")
        with st.spinner("Generating personalized insights..."):
            ai_insights = generate_ai_insights(risk_level, confidence, support_score, culture_score)
            
            st.markdown(f"""
            <div class="recommendation-box">
                {ai_insights}
            </div>

            """, unsafe_allow_html=True)
        
        # 6. Action Items
        st.markdown("### 🎯 Actionable Resources")
        
        tab1, tab2, tab3 = st.tabs(["📧 Communication Tools", "📋 Meeting Resources", "📊 Tracking Templates"])
        
        with tab1:
            if st.button("Generate Team Communication Email"):
                with st.spinner("Crafting personalized email..."):
                    email_prompt = f"""
                    Create a professional, empathetic email template for a manager to send to their team about workplace wellness.
                    Context: Risk level is {risk_level} with {confidence:.1f}% confidence.
                    Support score: {support_score:.1f}/100, Culture score: {culture_score:.1f}/100.
                    Make it encouraging and solution-focused.
                    """
                    email_content = generate_ai_insights(email_prompt, confidence, support_score, culture_score)
                    st.text_area("📧 Team Communication Email:", email_content, height=300)
        
        with tab2:
            if st.button("Create Leadership Meeting Agenda"):
                with st.spinner("Preparing meeting agenda..."):
                    agenda_prompt = f"""
                    Create a structured meeting agenda for leadership to discuss workplace wellness improvements.
                    Focus on the key findings: {risk_level} environment with specific focus on support infrastructure ({support_score:.1f}/100) 
                    and cultural openness ({culture_score:.1f}/100).
                    """
                    agenda_content = generate_ai_insights(agenda_prompt, confidence, support_score, culture_score)
                    st.text_area("📋 Leadership Meeting Agenda:", agenda_content, height=300)
        
        with tab3:
            st.markdown("#### 📊 Progress Tracking Metrics")
            st.markdown("""
            **Monthly Tracking Suggested Metrics:**
            - Employee Assistance Program (EAP) utilization rates
            - Mental health benefit enrollment
            - Anonymous feedback survey scores
            - Manager training completion rates
            - Workplace flexibility adoption
            
            **Quarterly Review Items:**
            - Support infrastructure improvements
            - Cultural openness initiatives
            - Policy updates and communications
            - Budget allocation for wellness programs
            """)
        
        # 7. Download Report
        st.markdown("### 📄 Export Your Analysis")
        
        # Prepare report data
        report_data = {
            "Executive Summary": f"Risk Assessment: {risk_level} ({confidence:.1f}% confidence)",
            "Wellness Scores": f"Support Infrastructure: {support_score:.1f}/100, Cultural Openness: {culture_score:.1f}/100",
            "AI Insights": ai_insights,
            "Generated On": datetime.now().strftime("%B %d, %Y at %I:%M %p")
        }
        
        pdf_report = create_enhanced_pdf_report(report_data)
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📄 Download Full PDF Report",
                data=pdf_report,
                file_name=f"Workplace_Wellness_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        
        with col2:
            # Create CSV export of key metrics
            metrics_df = pd.DataFrame({
                'Metric': ['Risk Level', 'Confidence', 'Support Score', 'Culture Score'] + list(support_components.keys()) + list(culture_components.keys()),
                'Value': [risk_level, f"{confidence:.1f}%", f"{support_score:.1f}/100", f"{culture_score:.1f}/100"] + list(support_components.values()) + list(culture_components.values())
            })
            
            csv_data = metrics_df.to_csv(index=False)
            st.download_button(
                label="📊 Download Metrics CSV",
                data=csv_data,
                file_name=f"Wellness_Metrics_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv",
                use_container_width=True
            )

if __name__ == "__main__":
    main()