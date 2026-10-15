
import os
from datetime import datetime

import pandas as pd
import streamlit as st

try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="NovaTech Solutions",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# 2. CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b1120;
        color: #f8fafc;
    }

    .hero {
        padding: 38px 24px;
        border-radius: 18px;
        background: linear-gradient(120deg, #312e81, #6d28d9);
        text-align: center;
        margin-bottom: 24px;
    }

    .hero h1 {
        color: white;
        font-size: 40px;
    }

    .hero p {
        color: #e0e7ff;
        font-size: 18px;
    }

    .card {
        background: #172033;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 3. PAGE DATA
# ============================================================

PAGES = [
    "Home",
    "About Us",
    "Services",
    "Portfolio",
    "Contact Us",
    "AI Assistant",
    "Client Dashboard",
    "Admin Dashboard",
]

SERVICES = [
    (
        "AI Application Development",
        "Intelligent applications and machine learning solutions "
        "designed around business requirements.",
    ),
    (
        "AI Agents & Multi-Agent Systems",
        "AI agents that perform multi-step tasks and support "
        "business workflows.",
    ),
    (
        "AI Chatbots",
        "Conversational assistants for customer support and "
        "business communication.",
    ),
    (
        "Website Development",
        "Modern websites designed for businesses and individuals.",
    ),
    (
        "Web Application Development",
        "Interactive applications with useful business features.",
    ),
    (
        "Mobile Application Development",
        "Mobile application solutions for Android and iOS.",
    ),
    (
        "Custom Software Development",
        "Software solutions tailored to specific requirements.",
    ),
    (
        "Workflow Automation",
        "Automation of repetitive tasks and business processes.",
    ),
    (
        "API Integration",
        "Connect applications and third-party services.",
    ),
    (
        "UI/UX Design",
        "User-friendly interfaces and digital experiences.",
    ),
]

DEFAULT_PROJECTS = [
    {
        "title": "MediBot AI Assistant",
        "category": "AI Chatbots",
        "tech": "Python, FastAPI, Gemini API",
        "description": "A demonstration healthcare assistant concept.",
        "link": "",
    },
    {
        "title": "SupplyChain Sync",
        "category": "Web Applications",
        "tech": "React, Node.js, PostgreSQL",
        "description": "A demonstration supply-chain tracking dashboard.",
        "link": "",
    },
]


# ============================================================
# 4. INITIALIZE SESSION STATE
# ============================================================

defaults = {
    "page": "Home",
    "user": None,
    "inquiries": [],
    "projects": [project.copy() for project in DEFAULT_PROJECTS],
    "selected_service": SERVICES[0][0],
    "chat_history": [
        (
            "assistant",
            "Assalam-o-Alaikum! Welcome to NovaTech Solutions. "
            "How can I help you today?",
        )
    ],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

if "page_radio" not in st.session_state:
    st.session_state.page_radio = st.session_state.page


# ============================================================
# 5. NAVIGATION FUNCTIONS
# ============================================================

def navigate(page):
    """Navigate to a page using the radio widget state."""
    if page in PAGES:
        st.session_state.page = page
        st.session_state.page_radio = page


def sync_page_from_radio():
    """Save the page selected from the navigation radio."""
    st.session_state.page = st.session_state.page_radio


def navigate_to_service(service):
    """Select a service and open the contact form."""
    st.session_state.selected_service = service
    navigate("Contact Us")


def sign_out():
    """Sign out and return to Home."""
    st.session_state.user = None
    navigate("Home")


# ============================================================
# 6. SIDEBAR: BRAND AND ACCOUNT
# ============================================================

with st.sidebar:
    st.markdown("## 🚀 NovaTech")
    st.caption("AI & Software Development")
    st.divider()

    st.markdown("### Account")

    if st.session_state.user is None:
        with st.form("login_form"):
            login_email = st.text_input("Email address")
            login_password = st.text_input(
                "Password",
                type="password",
            )

            login_submit = st.form_submit_button(
                "Sign In",
                use_container_width=True,
            )

        if login_submit:
            email = login_email.strip().lower()

            if (
                email == "admin@novatech.com"
                and login_password == "admin123"
            ):
                st.session_state.user = {
                    "email": email,
                    "role": "admin",
                }
                st.success("Demo admin signed in.")
                st.rerun()

            elif (
                email
                and "@" in email
                and "." in email.split("@")[-1]
                and login_password.strip()
            ):
                st.session_state.user = {
                    "email": email,
                    "role": "client",
                }
                st.success("Demo client signed in.")
                st.rerun()

            else:
                st.error("Enter a valid email and password.")

        st.caption("Demo admin login:")
        st.caption("admin@novatech.com")
        st.caption("Password: admin123")

    else:
        st.write(
            f"Signed in: {st.session_state.user['email']}"
        )
        st.write(
            f"Role: {st.session_state.user['role'].title()}"
        )

        st.button(
            "Sign Out",
            use_container_width=True,
            on_click=sign_out,
        )

    st.divider()
    st.markdown("### Quick Navigation")

    for page_name in PAGES:
        st.button(
            page_name,
            key=f"sidebar_{page_name}",
            use_container_width=True,
            on_click=navigate,
            args=(page_name,),
        )

    st.divider()
    st.caption("NovaTech Solutions demo application")


# ============================================================
# 7. MAIN NAVIGATION
# ============================================================

st.markdown("## 🚀 NovaTech Solutions")

st.radio(
    "Navigate to a page",
    PAGES,
    key="page_radio",
    horizontal=True,
    label_visibility="collapsed",
    on_change=sync_page_from_radio,
)

selected_page = st.session_state.page_radio

st.divider()


# ============================================================
# 8. HOME PAGE
# ============================================================

if selected_page == "Home":

    st.markdown(
        """
        <div class="hero">
            <h1>We Build Intelligent Software</h1>
            <p>
                AI applications, smart automation and modern
                digital solutions for a smarter future.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🤖 AI Innovation")
        st.write(
            "Explore AI applications, chatbots and intelligent agents."
        )
        st.button(
            "Explore AI Services",
            key="home_ai",
            use_container_width=True,
            on_click=navigate,
            args=("Services",),
        )

    with col2:
        st.markdown("### 💻 Modern Software")
        st.write(
            "Discover web applications and custom software solutions."
        )
        st.button(
            "View Our Projects",
            key="home_projects",
            use_container_width=True,
            on_click=navigate,
            args=("Portfolio",),
        )

    with col3:
        st.markdown("### 📩 Start a Project")
        st.write(
            "Tell us about your idea using our project inquiry form."
        )
        st.button(
            "Contact Us",
            key="home_contact",
            use_container_width=True,
            on_click=navigate,
            args=("Contact Us",),
        )

    st.divider()
    st.markdown("### Why Choose NovaTech?")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown(
            """
            <div class="card">
                <h3>AI-First</h3>
                <p>Intelligent solutions for real needs.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_b:
        st.markdown(
            """
            <div class="card">
                <h3>Modern Technology</h3>
                <p>Modern tools and practical applications.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c:
        st.markdown(
            """
            <div class="card">
                <h3>Customer Focus</h3>
                <p>Solutions designed around your goals.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.markdown("### Explore More")

    shortcut_cols = st.columns(4)

    for index, page_name in enumerate(
        ["About Us", "Services", "Portfolio", "AI Assistant"]
    ):
        with shortcut_cols[index]:
            st.button(
                page_name,
                key=f"shortcut_{index}",
                use_container_width=True,
                on_click=navigate,
                args=(page_name,),
            )


# ============================================================
# 9. ABOUT US PAGE
# ============================================================

elif selected_page == "About Us":

    st.title("About NovaTech Solutions")

    st.write(
        "NovaTech Solutions is a demonstration company concept "
        "focused on AI development, software engineering and "
        "digital transformation."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>🎯 Our Mission</h3>
                <p>
                    To make useful technology more accessible and
                    help businesses improve their digital workflows.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🔭 Our Vision</h3>
                <p>
                    To build practical, reliable and user-friendly
                    digital solutions for the future.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Our Approach")

    st.write(
        "We understand requirements, plan the solution, develop "
        "useful features and improve the user experience."
    )

    st.subheader("Technology Areas")

    st.markdown(
        "- Python and Streamlit\n"
        "- AI APIs and intelligent agents\n"
        "- Web application development\n"
        "- Database and API integration\n"
        "- UI/UX and workflow automation"
    )

    st.button(
        "Explore Our Services",
        on_click=navigate,
        args=("Services",),
    )


# ============================================================
# 10. SERVICES PAGE
# ============================================================

elif selected_page == "Services":

    st.title("Our Services")

    st.write(
        "Explore the services available in this demonstration app."
    )

    for index, (name, description) in enumerate(SERVICES, start=1):
        with st.container(border=True):
            st.subheader(f"{index}. {name}")
            st.write(description)

            st.button(
                "Enquire About This Service",
                key=f"service_{index}",
                on_click=navigate_to_service,
                args=(name,),
            )


# ============================================================
# 11. PORTFOLIO PAGE
# ============================================================

elif selected_page == "Portfolio":

    st.title("Our Portfolio")

    st.write(
        "These are sample demonstration projects, not verified "
        "client deliveries."
    )

    categories = [
        "All",
        "AI Chatbots",
        "Web Applications",
        "Mobile Apps",
    ]

    category = st.selectbox(
        "Filter projects",
        categories,
        key="portfolio_category",
    )

    visible_projects = [
        project
        for project in st.session_state.projects
        if category == "All"
        or project["category"] == category
    ]

    if not visible_projects:
        st.info("No projects match this category.")

    for index, project in enumerate(visible_projects):
        with st.container(border=True):
            st.subheader(project["title"])
            st.caption(project["category"])
            st.write(f"**Technology:** {project['tech']}")
            st.write(project["description"])

            if project.get("link"):
                st.link_button(
                    "Open Project",
                    project["link"],
                    key=f"project_link_{index}",
                )

    st.button(
        "Discuss a Similar Project",
        on_click=navigate,
        args=("Contact Us",),
    )


# ============================================================
# 12. CONTACT US PAGE
# ============================================================

elif selected_page == "Contact Us":

    st.title("Let's Discuss Your Project")

    st.write(
        "Complete this form to create a project inquiry."
    )

    service_options = [item[0] for item in SERVICES]
    default_service = st.session_state.get(
        "selected_service",
        service_options[0],
    )

    if default_service not in service_options:
        default_service = service_options[0]

    with st.form("contact_form", clear_on_submit=True):

        name = st.text_input("Full name *")
        email = st.text_input("Email address *")
        phone = st.text_input("Phone number (optional)")
        company = st.text_input("Company (optional)")

        service = st.selectbox(
            "Service required",
            service_options,
            index=service_options.index(default_service),
        )

        budget = st.selectbox(
            "Estimated budget",
            [
                "Not specified",
                "Under $5,000",
                "$5,000–$15,000",
                "$15,000–$50,000",
                "$50,000+",
            ],
        )

        description = st.text_area(
            "Describe your project *"
        )

        submitted = st.form_submit_button(
            "Submit Inquiry",
            use_container_width=True,
        )

    if submitted:
        clean_email = email.strip().lower()

        if (
            not name.strip()
            or "@" not in clean_email
            or "." not in clean_email.split("@")[-1]
            or not description.strip()
        ):
            st.error(
                "Enter your name, a valid email address and "
                "your project description."
            )

        else:
            next_id = max(
                [
                    item["id"]
                    for item in st.session_state.inquiries
                ],
                default=0,
            ) + 1

            inquiry = {
                "id": next_id,
                "name": name.strip(),
                "email": clean_email,
                "phone": phone.strip(),
                "company": company.strip(),
                "service": service,
                "budget": budget,
                "description": description.strip(),
                "status": "Inquiry Received",
                "date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M"
                ),
            }

            st.session_state.inquiries.append(inquiry)
            st.session_state.selected_service = service

            st.success(
                "Your inquiry has been recorded in this demo session."
            )
            st.info(
                "You can view the inquiry in the appropriate "
                "dashboard while this session data remains available."
            )


# ============================================================
# 13. AI ASSISTANT PAGE
# ============================================================

elif selected_page == "AI Assistant":

    st.title("💬 NovaTech AI Assistant")

    st.write(
        "Ask me anything about NovaTech Solutions. "
        "I can reply in English, Roman Urdu, or Urdu."
    )

    # Load API key securely from Streamlit Secrets
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "").strip()
    except Exception:
        api_key = ""

    # Display previous messages
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)

    prompt = st.chat_input("Write your question...")

    if prompt:
        st.session_state.chat_history.append(("user", prompt))

        with st.chat_message("user"):
            st.write(prompt)

        if not GEMINI_AVAILABLE:
            answer = (
                "The Gemini SDK is missing. Please add "
                "google-genai to requirements.txt and redeploy."
            )

        elif not api_key:
            answer = (
                "The AI assistant is not configured yet. "
                "Please contact the administrator."
            )

        else:
            try:
                client = genai.Client(api_key=api_key)

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=[
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": (
                                        "You are NovaTech Solutions' "
                                        "friendly AI assistant.\n\n"

                                        "LANGUAGE RULES — MUST FOLLOW:\n"
                                        "1. If the user writes in English, "
                                        "reply entirely in English.\n"
                                        "2. If the user writes in Roman Urdu "
                                        "(Urdu written using English letters), "
                                        "reply in natural Roman Urdu.\n"
                                        "3. If the user writes in Urdu script, "
                                        "reply in Urdu script.\n"
                                        "4. Do not answer in English when "
                                        "the user asks in Roman Urdu or Urdu.\n"
                                        "5. Follow the language of the latest "
                                        "user message.\n\n"

                                        "PERSONALITY AND ACCURACY:\n"
                                        "- Be friendly, clear, and helpful.\n"
                                        "- Keep answers simple and relevant.\n"
                                        "- Greet users with 'Hello!' when "
                                        "a greeting is appropriate.\n"
                                        "- Do not use 'Assalamu-Alaikum' "
                                        "as the default greeting.\n"
                                        "- You help with NovaTech Solutions, "
                                        "AI, software, and general questions.\n"
                                        "- Never invent company achievements "
                                        "or claim unverified facts.\n\n"

                                        f"User's message:\n{prompt}"
                                    )
                                }
                            ]
                        }
                    ],
                )

                answer = (
                    response.text.strip()
                    if response.text
                    else "Sorry, I could not generate a response. "
                         "Please try asking again."
                )

            except Exception as e:
                # Show the error so the administrator can diagnose it.
                st.error(
                    f"Gemini error: {type(e).__name__}: {e}"
                )
                answer = (
                    "Sorry, I could not get a response right now. "
                    "Please try again in a moment."
                )

        st.session_state.chat_history.append(
            ("assistant", answer)
        )

        with st.chat_message("assistant"):
            st.write(answer)

    st.button(
        "Clear Chat",
        key="clear_chat",
        on_click=lambda: st.session_state.update(
            chat_history=[
                (
                    "assistant",
                    "Hello! Welcome to NovaTech Solutions. "
                    "How can I help you today?",
                )
            ]
        ),
    )



# ============================================================
# 14. CLIENT DASHBOARD
# ============================================================

elif selected_page == "Client Dashboard":

    st.title("👤 Client Dashboard")

    user = st.session_state.user

    if user is None:
        st.warning(
            "Please sign in using the sidebar to access this page."
        )

    else:
        st.write(f"Welcome, **{user['email']}**")

        if user["role"] == "admin":
            user_inquiries = st.session_state.inquiries
        else:
            user_inquiries = [
                inquiry
                for inquiry in st.session_state.inquiries
                if inquiry["email"] == user["email"]
            ]

        if user_inquiries:
            st.dataframe(
                pd.DataFrame(user_inquiries),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info(
                "No inquiries found. Submit one from Contact Us."
            )

        st.button(
            "Create a New Inquiry",
            on_click=navigate,
            args=("Contact Us",),
        )


# ============================================================
# 15. ADMIN DASHBOARD
# ============================================================

elif selected_page == "Admin Dashboard":

    st.title("🛡️ Admin Dashboard")

    user = st.session_state.user

    if user is None or user["role"] != "admin":
        st.error(
            "Admin access required. Sign in using the demo admin "
            "credentials shown in the sidebar."
        )

    else:
        inquiries = st.session_state.inquiries
        projects = st.session_state.projects

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Inquiries", len(inquiries))
        col2.metric("Portfolio Projects", len(projects))
        col3.metric("Services", len(SERVICES))

        st.divider()
        st.subheader("Manage Inquiries")

        statuses = [
            "Inquiry Received",
            "Under Review",
            "Proposal Sent",
            "In Progress",
            "Completed",
            "Cancelled",
        ]

        if not inquiries:
            st.info("There are no inquiries to manage.")

        for inquiry in inquiries:
            with st.container(border=True):
                st.write(
                    f"**#{inquiry['id']} — {inquiry['name']}**"
                )
                st.write(f"**Email:** {inquiry['email']}")
                st.write(f"**Service:** {inquiry['service']}")
                st.write(f"**Budget:** {inquiry['budget']}")
                st.write(inquiry["description"])

                current_status = inquiry.get(
                    "status",
                    "Inquiry Received",
                )

                if current_status not in statuses:
                    current_status = statuses[0]

                st.selectbox(
                    "Inquiry status",
                    statuses,
                    index=statuses.index(current_status),
                    key=f"status_{inquiry['id']}",
                    on_change=lambda inquiry_id=inquiry["id"]: None,
                )

                inquiry["status"] = st.session_state[
                    f"status_{inquiry['id']}"
                ]

        st.divider()
        st.subheader("Add Portfolio Project")

        with st.form("add_project_form"):

            project_title = st.text_input("Project title")

            project_category = st.selectbox(
                "Category",
                [
                    "AI Chatbots",
                    "Web Applications",
                    "Mobile Apps",
                ],
            )

            project_tech = st.text_input("Technology stack")
            project_description = st.text_area(
                "Project description"
            )
            project_link = st.text_input(
                "Project URL (optional)"
            )

            add_project = st.form_submit_button(
                "Add Project",
                use_container_width=True,
            )

        if add_project:
            clean_link = project_link.strip()

            valid_link = (
                not clean_link
                or clean_link.startswith(("https://", "http://"))
            )

            if not project_title.strip():
                st.error("Enter a project title.")

            elif not valid_link:
                st.error(
                    "Project URL must start with https:// or http://."
                )

            else:
                st.session_state.projects.append(
                    {
                        "title": project_title.strip(),
                        "category": project_category,
                        "tech": project_tech.strip(),
                        "description": project_description.strip(),
                        "link": clean_link,
                    }
                )

                st.success("Project added to the demo portfolio.")
                st.rerun()


# ============================================================
# 16. FOOTER
# ============================================================

st.divider()

st.caption(
    "© NovaTech Solutions | AI & Software Development"
)

st.caption(
    "Demo notice: inquiries, chat history and projects are stored "
    "in session memory, not a permanent database. The demo login "
    "is not production-grade authentication."
)


