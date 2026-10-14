
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
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="NovaTech Solutions",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# STYLING
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b1120;
        color: #f8fafc;
    }

    .hero {
        padding: 40px 25px;
        border-radius: 18px;
        background: linear-gradient(120deg, #312e81, #6d28d9);
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white;
        font-size: 42px;
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
        margin: 10px 0;
    }

    .muted {
        color: #cbd5e1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INITIAL DATA
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
        "description": (
            "A demonstration healthcare assistant concept."
        ),
        "link": "",
    },
    {
        "title": "SupplyChain Sync",
        "category": "Web Applications",
        "tech": "React, Node.js, PostgreSQL",
        "description": (
            "A demonstration supply-chain tracking dashboard."
        ),
        "link": "",
    },
]


if "page" not in st.session_state:
    st.session_state.page = "Home"
    
if "page_radio" not in st.session_state:
    st.session_state.page_radio = st.session_state.page


if "user" not in st.session_state:
    st.session_state.user = None

if "inquiries" not in st.session_state:
    st.session_state.inquiries = []

if "projects" not in st.session_state:
    st.session_state.projects = DEFAULT_PROJECTS.copy()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        (
            "assistant",
            "Assalam-o-Alaikum! Welcome to NovaTech Solutions. "
            "How can I help you today?",
        )
    ]



def navigate(page):
    st.session_state.page = page
    st.session_state.page_radio = page
    
def navigate_to_service(service):
    st.session_state.selected_service = service
    navigate("Contact Us")




# ============================================================
# SIDEBAR: BRAND AND LOGIN
# ============================================================

with st.sidebar:
    st.markdown("## 🚀 NovaTech")
    st.caption("AI & Software Development")
    st.divider()

    st.markdown("### Account")

    if st.session_state.user is None:
        login_email = st.text_input(
            "Email address",
            key="login_email",
        )
        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password",
        )

        if st.button("Sign In", use_container_width=True):
            email = login_email.strip().lower()

            if (
                email == "admin@novatech.com"
                and login_password == "admin123"
            ):
                st.session_state.user = {
                    "email": email,
                    "role": "admin",
                }
                st.success("Admin signed in.")
                st.rerun()

            elif email and "@" in email and login_password:
                st.session_state.user = {
                    "email": email,
                    "role": "client",
                }
                st.success("Demo client signed in.")
                st.rerun()

            else:
                st.error(
                    "Enter a valid email and a password."
                )

        st.caption(
            "Demo admin: admin@novatech.com / admin123"
        )

    else:
        st.write(
            f"Signed in: {st.session_state.user['email']}"
        )
        st.write(
            f"Role: {st.session_state.user['role'].title()}"
        )

        
if st.button("Sign Out", use_container_width=True):
    st.session_state.user = None
    st.session_state.page = "Home"
    st.session_state.page_radio = "Home"
    st.rerun()


    st.divider()
    st.caption("Demo application")


# ============================================================
# MAIN NAVIGATION
# ============================================================

st.markdown("## 🚀 NovaTech Solutions")

selected_page = st.radio(
    "Navigate to a page",
    PAGES,
    key="page_radio",
    horizontal=True,
    label_visibility="collapsed",
)

st.divider()


# ============================================================
# HOME PAGE
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

    a, b, c = st.columns(3)

    with a:
        st.markdown(
            '<div class="card"><h3>AI-First</h3>'
            '<p class="muted">Intelligent solutions for real needs.</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    with b:
        st.markdown(
            '<div class="card"><h3>Modern Technology</h3>'
            '<p class="muted">Modern tools and practical applications.</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    with c:
        st.markdown(
            '<div class="card"><h3>Customer Focus</h3>'
            '<p class="muted">Solutions designed around your goals.</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.divider()
    st.markdown("### Explore More")

    shortcuts = st.columns(4)

    for i, page_name in enumerate(
        ["About Us", "Services", "Portfolio", "AI Assistant"]
    ):
       
for i, page_name in enumerate(
    ["About Us", "Services", "Portfolio", "AI Assistant"]
):
    with shortcuts[i]:
        st.button(
            page_name,
            key=f"shortcut_{i}",
            use_container_width=True,
            on_click=navigate,
            args=(page_name,),
        )



# ============================================================
# ABOUT US PAGE
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

    st.markdown("### Our Approach")

    st.write(
        "We focus on understanding requirements, planning the "
        "solution, developing useful features and improving the "
        "user experience."
    )

    st.markdown("### Technology Areas")

    st.write(
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
# SERVICES PAGE
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
# PORTFOLIO PAGE
# ============================================================

elif selected_page == "Portfolio":

    st.title("Our Portfolio")

    st.write(
        "The following are sample demonstration projects, "
        "not verified client deliveries."
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
    )

    visible_projects = [
        project
        for project in st.session_state.projects
        if category == "All"
        or project["category"] == category
    ]

    if not visible_projects:
        st.info("No projects match this category.")

    for project in visible_projects:
        with st.container(border=True):
            st.subheader(project["title"])
            st.caption(project["category"])
            st.write("**Technology:**", project["tech"])
            st.write(project["description"])

            if project.get("link"):
                st.link_button(
                    "Open Project",
                    project["link"],
                )

   
st.button(
    "Discuss a Similar Project",
    on_click=navigate,
    args=("Contact Us",),
)


# ============================================================
# CONTACT US PAGE
# ============================================================

elif selected_page == "Contact Us":

    st.title("Let's Discuss Your Project")

    st.write(
        "Complete the form below to create a project inquiry."
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
        if (
            not name.strip()
            or "@" not in email
            or not description.strip()
        ):
            st.error(
                "Please enter your name, a valid email "
                "and your project description."
            )

        else:
            inquiry = {
                "id": len(st.session_state.inquiries) + 1,
                "name": name.strip(),
                "email": email.strip().lower(),
                "phone": phone.strip(),
                "company": company.strip(),
                "service": service,
                "budget": budget,
                "description": description.strip(),
                "status": "Inquiry Received",
                "date": str(datetime.now().date()),
            }

            st.session_state.inquiries.append(inquiry)

            st.success(
                "Your inquiry has been recorded in this demo session."
            )

            st.session_state.selected_service = service


# ============================================================
# AI ASSISTANT PAGE
# ============================================================

elif selected_page == "AI Assistant":

    st.title("💬 NovaTech AI Assistant")

    st.write(
        "Ask questions about our services in English or Roman Urdu."
    )

    api_key = st.text_input(
        "Gemini API key",
        type="password",
        value=os.environ.get("GEMINI_API_KEY", ""),
        help="Your API key is used for AI responses. Keep it private.",
    )

    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)

    prompt = st.chat_input("Write your question...")

    if prompt:
        st.session_state.chat_history.append(("user", prompt))

        with st.chat_message("user"):
            st.write(prompt)

        answer = ""

        if not GEMINI_AVAILABLE:
            answer = (
                "The Gemini SDK is not installed. Run "
                "`python -m pip install google-genai` "
                "in your terminal."
            )

        elif not api_key.strip():
            answer = (
                "Enter your Gemini API key to enable live AI responses."
            )

        else:
            try:
                client = genai.Client(api_key=api_key.strip())

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=(
                        "You are the helpful assistant for NovaTech "
                        "Solutions, a demo AI and software company. "
                        "Respond in the language used by the user. "
                        "Do not invent company achievements. "
                        f"\n\nUser question: {prompt}"
                    ),
                )

                answer = (
                    response.text
                    or "The AI did not return a text response."
                )

            except Exception as error:
                answer = (
                    "Could not get an AI response. Check the API key, "
                    "internet connection, model access and API quota. "
                    f"Technical details: {error}"
                )

        st.session_state.chat_history.append(
            ("assistant", answer)
        )

        with st.chat_message("assistant"):
            st.write(answer)

    if st.button("Clear Chat"):
        st.session_state.chat_history = [
            (
                "assistant",
                "Assalam-o-Alaikum! Welcome to NovaTech Solutions. "
                "How can I help you today?",
            )
        ]
        st.rerun()


# ============================================================
# CLIENT DASHBOARD
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
# ADMIN DASHBOARD
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

        a, b, c = st.columns(3)

        a.metric("Total Inquiries", len(inquiries))
        b.metric("Portfolio Projects", len(projects))
        c.metric("Services", len(SERVICES))

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
                st.write(inquiry["email"])
                st.write(inquiry["service"])
                st.write(inquiry["description"])

                current_status = inquiry.get(
                    "status",
                    "Inquiry Received",
                )

                if current_status not in statuses:
                    current_status = statuses[0]

                new_status = st.selectbox(
                    "Inquiry status",
                    statuses,
                    index=statuses.index(current_status),
                    key=f"status_{inquiry['id']}",
                )

                inquiry["status"] = new_status

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
            valid_link = (
                not project_link.strip()
                or project_link.strip().startswith(
                    ("https://", "http://")
                )
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
                        "link": project_link.strip(),
                    }
                )

                st.success("Project added to the demo portfolio.")
                st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "© NovaTech Solutions | AI & Software Development"
)

st.caption(
    "Demo notice: this version stores data in session memory. "
    "It does not yet have permanent database storage or production "
    "grade authentication."
)
