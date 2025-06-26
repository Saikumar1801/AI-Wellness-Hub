# 🏆 The AI Wellness Hub

### A Dual-AI Platform for Proactive Workplace Mental Health
**Submission for the AITHON: 14 Days of AI for Social Good**

The AI Wellness Hub is a comprehensive, multi-page application designed to foster mentally healthy workplaces. It combines a powerful predictive analytics tool for managers with a safe, informational chatbot for all employees, creating a complete ecosystem for mental wellness support.

**Demo:** https://youtu.be/l9HKwWM9s_0

**Screenshot:**
![1Capture](https://github.com/user-attachments/assets/c0bd21d1-fe09-471f-96a8-644cb87b2f34)

---

## 💡 The Problem: Moving from Intention to Action

Many companies genuinely want to support their employees' mental health, but they often lack the data-driven tools to understand their unique environment. This leads to generic, one-size-fits-all solutions that are often ineffective. The key challenge is bridging the gap between the *desire* to help and the *ability* to provide targeted, impactful support.

## ✨ Our Solution: The AI Wellness Hub

Our Hub tackles this problem with a two-pronged, AI-powered approach:

### 1. 📈 The Workplace Wellness Advisor
A sophisticated diagnostic tool designed for managers and HR leaders. It provides a multi-faceted analysis of the workplace environment, turning raw data into clear, actionable strategy.

**Key Features:**
*   **Predictive Analysis:** Forecasts the likelihood of employees seeking mental health treatment using a fine-tuned XGBoost model.
*   **Wellness Report Card:** Scores the workplace on the crucial dimensions of "Support Structures" and "Open Culture."
*   **AI Explainability (SHAP):** Moves beyond a "black box" AI by using SHAP to reveal the exact factors driving the prediction, building trust and providing deep insights.
*   **Generative AI Companion (Gemini):** A Google Gemini-powered advisor provides a detailed, empathetic interpretation of the results with actionable recommendations.
*   **AI Action Kit:** Instantly generates draft emails and meeting agendas to help managers implement the AI's advice.
*   **Downloadable PDF Report:** Creates a professional, shareable PDF summary of the complete analysis for stakeholder meetings.

### 2. 💬 The Mental Healthcare Chatbot
A safe and anonymous informational resource for everyone. This chatbot uses Google Gemini to provide reliable, general information about mental healthcare topics. It is strictly programmed with safety protocols to **not** give medical advice and to **immediately provide crisis hotline numbers** if a user appears to be in distress.

---

## 🚀 The Development Journey & Technical Deep Dive

Our process was a real-world journey of iterative development and intelligent problem-solving.

1.  **Initial Model (V1):** We began by training several models on the [OSMI Mental Health in Tech Survey dataset](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey).
2.  **The Critical Insight (V2):** We built a prototype and discovered a critical flaw—the model was "lazy," relying on non-actionable features like `Age` and `family_history`. While statistically accurate, it was not practically useful as an advisor.
3.  **The Strategic Pivot (V3):** We re-engineered our entire approach, creating a focused "Advisor Model" by intentionally removing non-actionable features. This forced the AI to learn the more subtle patterns within workplace policies, making the tool genuinely responsive.
4.  **Advanced Data Techniques (V4):** To enhance our focused model, we implemented `IterativeImputer` to intelligently handle missing data and `SMOTE` to synthetically augment our training set, leading to a more robust final model.
5.  **The Complete Application (V5):** We built the final multi-page application, integrating all advanced features like SHAP, Gemini AI, PDF reports, and the informational chatbot.

### Tech Stack
*   **Programming Language:** Python
*   **Web Framework:** Streamlit
*   **Machine Learning:** Scikit-learn, XGBoost, Pandas, NumPy
*   **AI Explainability:** SHAP
*   **Generative AI:** Google Gemini API
*   **Data Augmentation:** Imbalanced-learn (for SMOTE)
*   **PDF Generation:** FPDF2
*   **Data Visualization:** Matplotlib

---

## 🛠️ How to Run the Project Locally

This project is fully reproducible. Follow these steps to run it on your local machine.

### Prerequisites
*   Python 3.9+
*   An API key for the Google Gemini API.

### 1. Clone the Repository
```bash
git clone https://github.com/Saikumar1801/AI-Wellness-Hub.git
cd AI-Wellness-Hub
```
### 2. Set Up the Environment
Create and activate a Python virtual environment:
``` bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
Install all required libraries from the requirements.txt file:
```bash
pip install -r requirements.txt
```
### 4. Add Your API Key
Create a folder named .streamlit in the main project directory. Inside it, create a file named secrets.toml and add your API key:
``` toml
# .streamlit/secrets.toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```
### 5. Run the Application
The project is now ready. Launch the app with:
``` bash
streamlit run Home.py
```
A new tab will open in your browser with the AI Wellness Hub. Enjoy!
## 🌟 What We Learned
This project was a powerful lesson in building AI that is not just accurate but useful and ethical. The journey from a simple predictive model to a transparent, feature-rich advisor taught us the importance of critical thinking, iterative development, and designing for real-world impact. We are incredibly proud of the final result—a tool that has the genuine potential to help create healthier workplaces.
``` code
Make sure to replace the placeholder links and image with your actual ones. This README will serve as a fantastic guide for anyone looking at your project.
```
