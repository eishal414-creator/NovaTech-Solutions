
import os
from datetime import datetime

import pandas as pd
import streamlit as st

# Gemini AI SDK
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="NovaTech Solutions - AI & Software Development",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------------------------------------------------------
# CUSTOM STYLING
# -----------------------------------------------------------------------------
st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "inquiries" not in st.session_state:
    st.session_state.inquiries = [
        {
            "id": 1,
            "name": "Ahmed Khan",
            "email": "ahmed@example.com",
            "service": "AI Application Development",
            "status": "In Progress",
            "description": (
                "Sample predictive analytics dashboard for retail inventory."
            ),
            "date": "2026-10-10",
        }
    ]

if "portfolio" not in st.session_state:
    st.session_state.portfolio = [
        {
            "title": "MediBot AI Assistant",
            "category": "AI Chatbots",
            "tech": "Python, FastAPI, Next.js, Gemini API",
            "desc": (
                "Demo healthcare assistant and appointment booking chatbot."
            ),
            "demo": "https://github.com",
        },
        {
            "title": "SupplyChain Sync",
            "category": "Web Applications",
            "tech": "React, Node.js, PostgreSQL, Tailwind",
            "desc": (
                "Demo supply-chain tracking and workflow dashboard."
            ),
            "demo": "https://github.com",
        },
    ]

if "services_list" not in st.session_state:
    st.session_state.services_list = [
        (
            "AI Application Development",
            "Build intelligent AI applications and machine learning solutions.",
        ),
        (
            "AI Agents and Multi-Agent Systems",
            "Create AI agents for multi-step tasks and business workflows.",
        ),
        (
            "AI Chatbots and Customer Support Automation",
            "Build conversational assistants in English and Roman Urdu.",
        ),
        (
            "Website Development",
            "Create modern, responsive websites for businesses.",
        ),
        (
            "Web Application Development",
            "Build secure and scalable web applications.",
        ),
        (
            "Mobile Application Development",
            "Create applications for Android and iOS.",
        ),
        (
            "Custom Software Development",
            "Develop software tailored to business requirements.",
        ),
        (
            "Workflow Automation",
            "Automate repetitive tasks and business processes.",
        ),
        (
            "API Integration",
            "Connect third-party APIs and business services.",
        ),
        (
            "UI/UX Design",
            "Design user-friendly interfaces and digital experiences.",
        ),
    ]


# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 🚀 NovaTech Solutions")
st.sidebar.markdown("*We Build Intelligent Software for a Smarter Future.*")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "About Us",
        "Services",
        "Portfolio",
        "Contact Us",
        "AI Assistant",
        "Client Dashboard",
        "Admin Dashboard",
    ],
)


# -----------------------------------------------------------------------------
# DEMO AUTHENTICATION
# -----------------------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Authentication")

if st.session_state.user is None:
    auth_mode = st.sidebar.selectbox(
        "Action",
        ["Sign In", "Sign Up"],
    )

    email_input = st.sidebar.text_input("Email")
    pass_input = st.sidebar.text_input(
        "Password",
        type="password",
    )

    if auth_mode == "Sign In":
        if st.sidebar.button("Login"):
            email = email_input.strip().lower()

            if (
                email == "admin@novatech.com"
                and pass_input == "admin123"
            ):
                st.session_state.user = {
                    "email": email,
                    "role": "admin",
                }
                st.rerun()

            elif email and "@" in email:
                st.session_state.user = {
                    "email": email,
                    "role": "client",
                }
                st.rerun()

            else:
                st.sidebar.error("Please enter a valid email.")

    else:
        if st.sidebar.button("Register"):
            email = email_input.strip().lower()

            if email and "@" in email:
                st.session_state.user = {
                    "email": email,
                    "role": "client",
                }
                st.rerun()

            else:
                st.sidebar.error("Please enter a valid email.")

else:
    st.sidebar.write(
        f"Logged in as: **{st.session_state.user['email']}**"
    )
    st.sidebar.write(
        f"Role: `{st.session_state.user['role'].upper()}`"
    )

    if st.sidebar.button("Sign Out"):
        st.session_state.user = None
        st.rerun()


# -----------------------------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------------------------
if menu == "Home":
    st.markdown(
        '<p class="main-header">'
        "We Build Intelligent Software for a Smarter Future."
        "</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="sub-tagline">'
        "NovaTech Solutions combines Artificial Intelligence "
        "with software development to support business growth."
        "</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "🚀 Explore Our Services",
            use_container_width=True,
        ):
            st.info("Select Services from the sidebar.")

    with col2:
        if st.button(
            "💬 Start Your Project",
            use_container_width=True,
        ):
            st.info("Select Contact Us from the sidebar.")

    st.markdown("### 🌟 Why Partner With NovaTech?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card">
                <h4>🤖 AI-First Engineering</h4>
                <p>AI applications, intelligent agents, and
                automated workflows.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="card">
                <h4>⚡ Modern Development</h4>
                <p>Responsive websites and web applications
                built with modern technologies.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="card">
                <h4>🔒 Scalable Solutions</h4>
                <p>Software designed around business needs
                and future growth.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 📊 Company Metrics")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Sample Active Projects", "12+")
    m2.metric("Client Satisfaction", "Demo")
    m3.metric("AI Solutions", "25+")
    m4.metric("Uptime", "Demo")

    st.caption(
        "These are demonstration figures, not verified company statistics."
    )


# -----------------------------------------------------------------------------
# ABOUT US PAGE
# -----------------------------------------------------------------------------
elif menu == "About Us":
    st.markdown("## About NovaTech Solutions")

    st.write(
        "NovaTech Solutions is a demonstration AI and software "
        "development company concept. It focuses on building "
        "useful digital products and intelligent software solutions."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>🎯 Our Mission</h3>
                <p>To help businesses use technology to improve
                their services and workflows.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🔭 Our Vision</h3>
                <p>To create practical, accessible, and
                user-friendly digital solutions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### ⚙️ Our Core Technology Stack")

    st.code(
        "Frontend: HTML, CSS, JavaScript, React, Next.js\n"
        "Backend: Python, FastAPI, Node.js\n"
        "Database: PostgreSQL, Supabase\n"
        "AI: Google Gemini API\n"
        "Current Website: Python and Streamlit",
        language="text",
    )


# -----------------------------------------------------------------------------
# SERVICES PAGE
# -----------------------------------------------------------------------------
elif menu == "Services":
    st.markdown("## Our Professional Services")

    st.write(
        "Explore our AI and software development services."
    )

    for idx, (title, desc) in enumerate(
        st.session_state.services_list,
        start=1,
    ):
        st.markdown(
            f"""
            <div class="card">
                <h3>{idx}. {title}</h3>
                <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------------------------
# PORTFOLIO PAGE
# -----------------------------------------------------------------------------
elif menu == "Portfolio":
    st.markdown("## Project Portfolio")

    st.write(
        "These are sample projects for demonstration purposes."
    )

    selected_cat = st.selectbox(
        "Filter by Category",
        [
            "All",
            "AI Chatbots",
            "Web Applications",
            "Mobile Apps",
        ],
    )

    for proj in st.session_state.portfolio:
        if (
            selected_cat == "All"
            or proj["category"] == selected_cat
        ):
            st.markdown(
                f"""
                <div class="card">
                    <h3>{proj['title']}</h3>
                    <p><b>Category:</b> {proj['category']}</p>
                    <p><b>Tech Stack:</b> {proj['tech']}</p>
                    <p>{proj['desc']}</p>
                    <p><i>Demo Project / Sample Implementation</i></p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# -----------------------------------------------------------------------------
# CONTACT PAGE
# -----------------------------------------------------------------------------
elif menu == "Contact Us":
    st.markdown("## Start Your Project Inquiry")

    st.write(
        "Complete the form to record a project inquiry in this demo."
    )

    with st.form("contact_form"):
        c_name = st.text_input("Full Name *")
        c_email = st.text_input("Email *")
        c_phone = st.text_input("Phone (Optional)")
        c_company = st.text_input("Company Name (Optional)")

        c_service = st.selectbox(
            "Required Service",
            [service[0] for service in st.session_state.services_list],
        )

        c_budget = st.selectbox(
            "Estimated Budget",
            [
                "Not specified",
                "Under $5,000",
                "$5,000 - $15,000",
                "$15,000 - $50,000",
                "$50,000+",
            ],
        )

        c_desc = st.text_area("Project Description *")

        submitted = st.form_submit_button("Submit Inquiry")

        if submitted:
            email = c_email.strip().lower()

            if (
                c_name.strip()
                and email
                and "@" in email
                and c_desc.strip()
            ):
                new_inquiry = {
                    "id": len(st.session_state.inquiries) + 1,
                    "name": c_name.strip(),
                    "email": email,
                    "phone": c_phone.strip(),
                    "company": c_company.strip(),
                    "service": c_service,
                    "budget": c_budget,
                    "status": "Inquiry Received",
                    "description": c_desc.strip(),
                    "date": str(datetime.now().date()),
                }

                st.session_state.inquiries.append(new_inquiry)

                st.success(
                    "Inquiry recorded successfully in this demo session."
                )

            else:
                st.error(
                    "Please enter your name, a valid email, "
                    "and your project description."
                )


# -----------------------------------------------------------------------------
# AI ASSISTANT
# -----------------------------------------------------------------------------
elif menu == "AI Assistant":
    st.markdown("## 💬 NovaTech AI Assistant")

    st.write(
        "Ask about our services or discuss your project in English "
        "or Roman Urdu."
    )

    api_key_input = st.text_input(
        "Gemini API Key",
        type="password",
        value=os.environ.get("GEMINI_API_KEY", ""),
        help=(
            "Get an API key from Google AI Studio. "
            "Do not share your API key publicly."
        ),
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            (
                "assistant",
                "Assalam-o-Alaikum! Main NovaTech Solutions ka "
                "AI assistant hoon. Main aapki kya madad kar sakta hoon?",
            )
        ]

    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)

    user_prompt = st.chat_input(
        "Type your message here..."
    )

    if user_prompt:
        st.session_state.chat_history.append(
            ("user", user_prompt)
        )

        with st.chat_message("user"):
            st.write(user_prompt)

        bot_response = ""

        if not GEMINI_AVAILABLE:
            bot_response = (
                "Gemini SDK install nahi hai. Terminal mein "
                "`python -m pip install -r requirements.txt` "
                "run karo."
            )

        elif not api_key_input.strip():
            bot_response = (
                "AI responses use karne ke liye apni Gemini API key "
                "enter karo."
            )

        else:
            try:
                client = genai.Client(
                    api_key=api_key_input.strip()
                )

                chat_context = (
                    "You are NovaTech Solutions' helpful AI assistant. "
                    "The company concept offers AI development, AI agents, "
                    "chatbots, websites, web apps, mobile apps, custom "
                    "software, workflow automation, API integration, "
                    "and UI/UX design. Respond politely in English or "
                    "Roman Urdu according to the user's language. "
                    "Do not invent company achievements or make "
                    "unsupported promises. Guide users to the Contact "
                    "Us page for project inquiries."
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=(
                        f"{chat_context}\n\n"
                        f"User: {user_prompt}"
                    ),
                )

                bot_response = (
                    response.text
                    or "Sorry, AI ne is waqt text response nahi diya."
                )

            except Exception as error:
                bot_response = (
                    "Gemini API se response lene mein masla hua. "
                    "API key, internet connection, model availability, "
                    "aur API quota check karo.\n\n"
                    f"Technical details: {error}"
                )

        st.session_state.chat_history.append(
            ("assistant", bot_response)
        )

        with st.chat_message("assistant"):
            st.write(bot_response)

    if st.button("Clear Chat"):
        st.session_state.chat_history = [
            (
                "assistant",
                "Assalam-o-Alaikum! Main NovaTech Solutions ka "
                "AI assistant hoon. Main aapki kya madad kar sakta hoon?",
            )
        ]
        st.rerun()


# -----------------------------------------------------------------------------
# CLIENT DASHBOARD
# -----------------------------------------------------------------------------
elif menu == "Client Dashboard":
    st.markdown("## 👤 Client Dashboard")

    if st.session_state.user is None:
        st.warning(
            "Please sign in from the sidebar to access your dashboard."
        )

    else:
        user_email = st.session_state.user["email"]
        user_role = st.session_state.user["role"]

        st.write(f"Welcome back, **{user_email}**")
        st.markdown("### Your Project Inquiries & Status")

        user_inquiries = [
            inquiry
            for inquiry in st.session_state.inquiries
            if (
                inquiry["email"] == user_email
                or user_role == "admin"
            )
        ]

        if not user_inquiries:
            st.info(
                "No inquiries found. Submit an inquiry through Contact Us."
            )

        else:
            df = pd.DataFrame(user_inquiries)
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
            )


# -----------------------------------------------------------------------------
# ADMIN DASHBOARD
# -----------------------------------------------------------------------------
elif menu == "Admin Dashboard":
    st.markdown("## 🛡️ Admin Control Panel")

    if (
        st.session_state.user is None
        or st.session_state.user["role"] != "admin"
    ):
        st.error(
            "Unauthorized access. For this demo only, the admin "
            "login is admin@novatech.com with password admin123."
        )

    else:
        st.success("Authenticated as Administrator")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Inquiries",
            len(st.session_state.inquiries),
        )
        col2.metric(
            "Portfolio Projects",
            len(st.session_state.portfolio),
        )
        col3.metric(
            "Services Offered",
            len(st.session_state.services_list),
        )

        st.markdown("### Manage Inquiry Status")

        statuses = [
            "Inquiry Received",
            "Under Review",
            "Proposal Sent",
            "In Progress",
            "Completed",
            "Cancelled",
        ]

        for inquiry in st.session_state.inquiries:
            st.write(
                f"**ID:** {inquiry['id']} | "
                f"**Name:** {inquiry['name']} | "
                f"**Service:** {inquiry['service']}"
            )

            current_status = inquiry.get(
                "status",
                "Inquiry Received",
            )

            if current_status not in statuses:
                current_status = "Inquiry Received"

            new_status = st.selectbox(
                f"Status for Inquiry #{inquiry['id']}",
                statuses,
                index=statuses.index(current_status),
                key=f"status_{inquiry['id']}",
            )

            if new_status != inquiry.get("status"):
                inquiry["status"] = new_status
                st.success(
                    f"Inquiry #{inquiry['id']} status updated."
                )

            st.markdown("---")

        st.markdown("### Add Portfolio Project")

        with st.form("add_portfolio_form"):
            p_title = st.text_input("Project Title")

            p_cat = st.selectbox(
                "Category",
                [
                    "AI Chatbots",
                    "Web Applications",
                    "Mobile Apps",
                ],
            )

            p_tech = st.text_input("Technologies Used")
            p_desc = st.text_area("Description")

            p_submit = st.form_submit_button("Add Project")

            if p_submit:
                if p_title.strip():
                    st.session_state.portfolio.append(
                        {
                            "title": p_title.strip(),
                            "category": p_cat,
                            "tech": p_tech.strip(),
                            "desc": p_desc.strip(),
                            "demo": "https://github.com",
                        }
                    )

                    st.success("Sample project added successfully.")

                else:
                    st.error("Please enter a project title.")


# -----------------------------------------------------------------------------
# IMPORTANT DEMO LIMITATIONS
# -----------------------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.caption(
    "Demo version: accounts, inquiries, and projects are stored "
    "in session memory and are not permanently saved."
)

