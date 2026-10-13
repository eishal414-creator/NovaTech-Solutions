import os
import streamlit as st
import pandas as pd
from datetime import datetime

# Optional import for Gemini
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="NovaTech Solutions — AI & Software Development",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Dark/Light Navy Theme & Gradients
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-tagline {
        font-size: 1.2rem;
        color: #94a3b8;
        margin-bottom: 20px;
    }
    .card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #4f46e5;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# INITIALIZE SESSION STATE DATA
# -----------------------------------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None  # None, {"email": "...", "role": "client"/"admin"}

if "inquiries" not in st.session_state:
    st.session_state.inquiries = [
        {
            "id": 1,
            "name": "Ahmed Khan",
            "email": "ahmed@example.com",
            "service": "AI Application Development",
            "status": "In Progress",
            "description": "Custom predictive analytics dashboard for retail inventory.",
            "date": "2026-10-10"
        }
    ]

if "portfolio" not in st.session_state:
    st.session_state.portfolio = [
        {
            "title": "MediBot AI Assistant",
            "category": "AI Chatbots",
            "tech": "Python, FastAPI, Next.js, Gemini API",
            "desc": "Automated patient triage and appointment booking chatbot with 95% accuracy.",
            "demo": "https://github.com"
        },
        {
            "title": "SupplyChain Sync",
            "category": "Web Applications",
            "tech": "React, Node.js, PostgreSQL, Tailwind",
            "desc": "Real-time enterprise supply chain tracking and automated workflow dashboard.",
            "demo": "https://github.com"
        }
    ]

if "services_list" not in st.session_state:
    st.session_state.services_list = [
        ("AI Application Development", "Build intelligent, scalable AI models and machine learning pipelines tailored to your business data."),
        ("AI Agents and Multi-Agent Systems", "Deploy autonomous agent swarms capable of complex multi-step reasoning and automated execution."),
        ("AI Chatbots and Customer Support Automation", "24/7 intelligent conversational agents trained on your documentation in English & Roman Urdu."),
        ("Website Development", "High-converting, lightning-fast modern websites built with cutting-edge frameworks."),
        ("Web Application Development", "Robust, secure, and scalable cloud-native web applications with intuitive UX."),
        ("Mobile Application Development", "Cross-platform iOS and Android apps delivering seamless native performance."),
        ("Custom Software Development", "Enterprise-grade bespoke software solutions designed to eliminate operational bottlenecks."),
        ("Workflow Automation", "Automate repetitive business processes using custom scripts, webhooks, and AI pipelines."),
        ("API Integration", "Seamlessly connect third-party services, payment gateways, and CRM systems."),
        ("UI/UX Design", "User-centric wireframing, prototyping, and modern design systems optimized for conversion.")
    ]

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & AUTH
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 🚀 NovaTech Solutions")
st.sidebar.markdown("*We Build Intelligent Software for a Smarter Future.*")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation", 
    ["Home", "About Us", "Services", "Portfolio", "Contact Us", "AI Assistant", "Client Dashboard", "Admin Dashboard"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Authentication")
if st.session_state.user is None:
    auth_mode = st.sidebar.selectbox("Action", ["Sign In", "Sign Up"])
    email_input = st.sidebar.text_input("Email")
    pass_input = st.sidebar.text_input("Password", type="password")
    
    if auth_mode == "Sign In":
        if st.sidebar.button("Login"):
            if email_input == "admin@novatech.com" and pass_input == "admin123":
                st.session_state.user = {"email": email_input, "role": "admin"}
                st.sidebar.success("Logged in as Admin!")
                st.rerun()
            elif email_input:
                st.session_state.user = {"email": email_input, "role": "client"}
                st.sidebar.success("Logged in successfully!")
                st.rerun()
            else:
                st.sidebar.error("Please enter a valid email.")
    else:
        if st.sidebar.button("Register"):
            if email_input:
                st.session_state.user = {"email": email_input, "role": "client"}
                st.sidebar.success("Account created & logged in!")
                st.rerun()
            else:
                st.sidebar.error("Please enter an email.")
else:
    st.sidebar.write(f"Logged in as: **{st.session_state.user['email']}**")
    st.sidebar.write(f"Role: `{st.session_state.user['role'].upper()}`")
    if st.sidebar.button("Sign Out"):
        st.session_state.user = None
        st.rerun()

# -----------------------------------------------------------------------------
# 1. HOME PAGE
# -----------------------------------------------------------------------------
if menu == "Home":
    st.markdown('<p class="main-header">We Build Intelligent Software for a Smarter Future.</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">NovaTech Solutions combines advanced Artificial Intelligence with expert Full-Stack Engineering to accelerate your digital growth.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Explore Our Services", use_container_width=True):
            st.info("Navigate to the Services tab using the sidebar.")
    with col2:
        if st.button("💬 Start Your Project", use_container_width=True):
            st.info("Navigate to the Contact Us tab to submit your project inquiry.")

    st.markdown("### 🌟 Why Partner With NovaTech?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><h4>🤖 AI-First Engineering</h4><p>Custom LLM integrations, intelligent agents, and automated workflows built right into your core product.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h4>⚡ High Performance</h4><p>Lightning-fast web and mobile apps engineered with Next.js, TypeScript, and modern cloud infrastructure.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><h4>🔒 Secure & Scalable</h4><p>Enterprise-grade security with role-based access control, robust database design, and clean codebases.</p></div>', unsafe_allow_html=True)

    st.markdown("### 📊 Company Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Projects", "12+")
    m2.metric("Client Satisfaction", "99%")
    m3.metric("AI Models Deployed", "25+")
    m4.metric("Uptime Guarantee", "99.9%")

# -----------------------------------------------------------------------------
# 2. ABOUT PAGE
# -----------------------------------------------------------------------------
elif menu == "About Us":
    st.markdown("## About NovaTech Solutions")
    st.write("NovaTech Solutions is a next-generation software development and artificial intelligence company. We bridge the gap between complex machine learning research and practical, high-impact enterprise software.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>🎯 Our Mission</h3><p>To empower businesses worldwide by delivering intelligent, scalable, and intuitive software solutions that drive exponential growth and efficiency.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>🔭 Our Vision</h3><p>To be the global benchmark for AI-driven software development, recognized for technical excellence, transparency, and innovation.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Our Core Technology Stack")
    st.write("We prioritize modern, robust, and cost-effective technologies:")
    st.code("Frontend: Next.js, React, TypeScript, Tailwind CSS\nBackend: Node.js, Python FastAPI, Serverless APIs\nDatabase & Auth: PostgreSQL, Supabase, Row Level Security\nAI & ML: Google Gemini API, LangChain, PyTorch", language="text")

# -----------------------------------------------------------------------------
# 3. SERVICES PAGE
# -----------------------------------------------------------------------------
elif menu == "Services":
    st.markdown("## Our Professional Services")
    st.write("Explore our comprehensive suite of AI and software development capabilities.")
    
    for idx, (title, desc) in enumerate(st.session_state.services_list, 1):
        st.markdown(f"""
        <div class="card">
            <h3>{idx}. {title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. PORTFOLIO PAGE
# -----------------------------------------------------------------------------
elif menu == "Portfolio":
    st.markdown("## Project Portfolio")
    st.write("Browse our demonstration projects and sample implementations.")
    
    selected_cat = st.selectbox("Filter by Category", ["All", "AI Chatbots", "Web Applications"])
    
    for proj in st.session_state.portfolio:
        if selected_cat == "All" or proj["category"] == selected_cat:
            st.markdown(f"""
            <div class="card">
                <h3>{proj['title']} <span style="font-size:0.8rem; background:#4f46e5; padding:2px 8px; border-radius:4px;">{proj['category']}</span></h3>
                <p><b>Tech Stack:</b> {proj['tech']}</p>
                <p>{proj['desc']}</p>
                <p><i>[Demo Project / Sample Implementation]</i></p>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. CONTACT PAGE
# -----------------------------------------------------------------------------
elif menu == "Contact Us":
    st.markdown("## Start Your Project Inquiry")
    st.write("Fill out the form below and our team will get back to you within 24 hours.")
    
    with st.form("contact_form"):
        c_name = st.text_input("Full Name *")
        c_email = st.text_input("Email *")
        c_phone = st.text_input("Phone (Optional)")
        c_company = st.text_input("Company Name (Optional)")
        c_service = st.selectbox("Required Service", [s[0] for s in st.session_state.services_list])
        c_budget = st.selectbox("Estimated Budget", ["< $5,000", "$5,000 - $15,000", "$15,000 - $50,000", "$50,000+"])
        c_desc = st.text_area("Project Description *")
        
        submitted = st.form_submit_button("Submit Inquiry")
        if submitted:
            if c_name and c_email and c_desc:
                new_inquiry = {
                    "id": len(st.session_state.inquiries) + 1,
                    "name": c_name,
                    "email": c_email,
                    "service": c_service,
                    "status": "Inquiry Received",
                    "description": c_desc,
                    "date": str(datetime.now().date())
                }
                st.session_state.inquiries.append(new_inquiry)
                st.success("✅ Inquiry submitted successfully! Our team will review your requirements shortly.")
            else:
                st.error("❌ Please fill out all required fields (Name, Email, Description).")

# -----------------------------------------------------------------------------
# 6. AI ASSISTANT CHATBOT (GEMINI API INTEGRATION)
# -----------------------------------------------------------------------------
elif menu == "AI Assistant":
    st.markdown("## 💬 NovaTech AI Assistant")
    st.write("Ask questions about our services, get recommendations, or discuss your project requirements in English or Roman Urdu.")
    
    api_key_input = st.text_input("Enter Gemini API Key (or set GEMINI_API_KEY environment variable):", type="password", value=os.environ.get("GEMINI_API_KEY", ""))
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            ("assistant", "Assalam-o-Alaikum! Main NovaTech Solutions ka AI assistant hoon. Main aapki kya madad kar sakta hoon?")
        ]

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)

    user_prompt = st.chat_input("Type your message here (e.g., 'What AI services do you offer?' or 'Mujhe website banwani hai')...")
    
    if user_prompt:
        st.session_state.chat_history.append(("user", user_prompt))
        with st.chat_message("user"):
            st.write(user_prompt)
            
        bot_response = ""
        if not GEMINI_AVAILABLE:
            bot_response = "Error: `google-generativeai` module is not installed or available."
        elif not api_key_input:
            bot_response = "⚠️ Please provide a valid Gemini API key above to enable live AI responses, or use our Contact Form."
        else:
            try:
                genai.configure(api_key=api_key_input)
                model = genai.GenerativeModel("gemini-1.5-flash")
                chat_context = "You are an AI assistant for NovaTech Solutions, an AI and software development company. Respond politely in English or Roman Urdu based on the user's input, explain our services, and guide them to our Contact Us page for project inquiries."
                response = model.generate_content(f"{chat_context}\nUser: {user_prompt}")
                bot_response = response.text
            except Exception as e:
                bot_response = f"⚠️ Error communicating with Gemini API: {str(e)}. Please check your API key or quota."
                
        st.session_state.chat_history.append(("assistant", bot_response))
        with st.chat_message("assistant"):
            st.write(bot_response)

# -----------------------------------------------------------------------------
# 7. CLIENT DASHBOARD
# -----------------------------------------------------------------------------
elif menu == "Client Dashboard":
    st.markdown("## 👤 Client Dashboard")
    if st.session_state.user is None:
        st.warning("Please sign in from the sidebar to access your dashboard.")
    else:
        st.write(f"Welcome back, **{st.session_state.user['email']}**")
        st.markdown("### Your Project Inquiries & Status")
        
        user_inquiries = [i for i in st.session_state.inquiries if i['email'] == st.session_state.user['email'] or st.session_state.user['role'] == 'admin']
        if not user_inquiries:
            st.info("No inquiries found. Submit a project inquiry via the Contact Us page.")
        else:
            df = pd.DataFrame(user_inquiries)
            st.dataframe(df, use_container_width=True)

# -----------------------------------------------------------------------------
# 8. ADMIN DASHBOARD
# -----------------------------------------------------------------------------
elif menu == "Admin Dashboard":
    st.markdown("## 🛡️ Admin Control Panel")
    if st.session_state.user is None or st.session_state.user['role'] != 'admin':
        st.error("⛔ Unauthorized access. Please log in as admin (`admin@novatech.com` / `admin123`).")
    else:
        st.success("Authenticated as Administrator")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Inquiries", len(st.session_state.inquiries))
        col2.metric("Portfolio Projects", len(st.session_state.portfolio))
        col3.metric("Services Offered", len(st.session_state.services_list))
        
        st.markdown("### Manage Inquiries Status")
        for inquiry in st.session_state.inquiries:
            st.write(f"**ID:** {inquiry['id']} | **Name:** {inquiry['name']} | **Service:** {inquiry['service']}")
            new_status = st.selectbox(
                f"Update status for Inquiry #{inquiry['id']}",
                ["Inquiry Received", "Under Review", "Proposal Sent", "In Progress", "Completed", "Cancelled"],
                index=["Inquiry Received", "Under Review", "Proposal Sent", "In Progress", "Completed", "Cancelled"].index(inquiry['status']),
                key=f"status_{inquiry['id']}"
            )
            if new_status != inquiry['status']:
                inquiry['status'] = new_status
                st.success(f"Status updated for #{inquiry['id']} to {new_status}")
            st.markdown("---")

        st.markdown("### Add Portfolio Project")
        with st.form("add_portfolio_form"):
            p_title = st.text_input("Project Title")
            p_cat = st.selectbox("Category", ["AI Chatbots", "Web Applications", "Mobile Apps"])
            p_tech = st.text_input("Technologies Used")
            p_desc = st.text_area("Description")
            p_submit = st.form_submit_button("Add Project")
            if p_submit and p_title:
                st.session_state.portfolio.append({
                    "title": p_title,
                    "category": p_cat,
                    "tech": p_tech,
                    "desc": p_desc,
                    "demo": "https://github.com"
                })
                st.success("Project added successfully!")
