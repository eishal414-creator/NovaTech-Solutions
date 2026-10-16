# NovaTech Solutions

**A portfolio demonstration project for an AI and software development
company.**

🔗 **Live App:** [Open NovaTech
Solutions](https://novatech-solutions-pbrklhk4m6fvv62jkpzmlv.streamlit.app/)

## Overview

NovaTech Solutions is a Streamlit web application built to demonstrate a
modern AI and software development company website. It presents sample
services and projects, lets visitors submit project inquiries, and
includes an AI assistant powered by the Google Gemini API.

> **Demo notice:** Inquiries, chat history, and projects are stored in
> Streamlit session memory, not a permanent database. Data may not
> persist after the session resets. The demo login is not
> production-grade authentication. Do not use real or sensitive
> information.

## Features

-   **Home** --- introduction to the NovaTech Solutions concept.
-   **About Us** --- mission, vision, and technology areas.
-   **Services** --- overview of sample AI and software development
    services.
-   **Portfolio** --- demonstration projects and sample implementations.
-   **Contact Us** --- form for submitting project inquiries.
-   **AI Assistant** --- chatbot for questions about services and
    project requirements, with English and Roman Urdu support.
-   **Client Dashboard** --- demo client area.
-   **Admin Dashboard** --- demo administrative view restricted by the
    app's role check.
-   **Authentication demo** --- separate admin and client roles for
    demonstrating navigation and access control.

## Technology Stack

-   **Language:** Python
-   **Web app framework:** Streamlit
-   **Data handling:** pandas
-   **AI integration:** Google Gemini API (Google Gen AI SDK; check the
    current app configuration for the exact package version)

## Run Locally

1.  Clone or download this repository.

2.  Open a terminal in the project folder.

3.  Install the dependencies:

    ``` bash
    python -m pip install -r requirements.txt
    ```

4.  Configure the required secrets or environment variables locally. For
    Gemini features, provide a valid Gemini API key using the method
    supported by the current app configuration.

5.  Start the app:

    ``` bash
    streamlit run app.py
    ```

## Security and Data Limitations

This project is intended for portfolio demonstration and learning. It
does not currently use a permanent database for inquiries, chat history,
or project data. Session data can be lost when the session resets.

The demo authentication is not suitable for protecting real customer
data. Before using this app with real users, implement production-grade
authentication, server-side authorization, secure secret management, and
persistent database storage. Never commit API keys or
`.streamlit/secrets.toml` to GitHub.

## Project Status

**Portfolio demo / sample implementation.** Features and sample metrics
shown in the app should not be interpreted as verified business
statistics or real client results.

## Author

Created as an AI and software development portfolio project.
