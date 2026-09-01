# 🤖 Local LLM Chat Assistant

A simple and interactive **Streamlit web application** for chatting with a locally hosted Large Language Model using **Ollama** and **Llama 3.2**.

This project was developed as **Task 1 of the Generative AI Internship at Arch Technologies**.

---

## 📌 Project Overview

Large Language Models can be run locally using tools such as Ollama, allowing users to interact with AI models without depending on cloud-based APIs.

This project provides a user-friendly Streamlit interface that communicates with a locally hosted **Llama 3.2** model through the **Ollama REST API**.

The application supports interactive conversations, conversation history, and resetting the chat session.

---

## 🎯 Objectives

* Build a Streamlit-based chatbot interface.
* Run a Large Language Model locally using Ollama.
* Connect Streamlit with Ollama using API calls.
* Display AI-generated responses.
* Maintain conversation history.
* Provide a reset conversation feature.
* Understand the basic workflow of local LLM inference.

---

## ✨ Features

* 💬 Interactive chat interface
* 🤖 Local Llama 3.2 LLM
* 🏠 Local inference using Ollama
* 🔄 Conversation history
* 🧠 Conversation context/memory
* 🗑️ Reset conversation button
* ⚙️ Model and backend information
* 🔌 Ollama REST API integration
* ❌ Basic error handling
* 🚀 Streamlit web interface

---

## 🛠️ Technologies Used

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Application development                    |
| Streamlit  | Web interface                              |
| Ollama     | Local LLM runtime                          |
| Llama 3.2  | Large Language Model                       |
| Requests   | API communication                          |
| REST API   | Communication between Streamlit and Ollama |

---

## 🏗️ System Architecture

```text
             👤 User
                │
                ▼
      ┌────────────────────┐
      │   Streamlit UI     │
      │                    │
      │  Chat Input        │
      │  Chat History      │
      │  Reset Button      │
      └─────────┬──────────┘
                │
                │ HTTP POST
                ▼
      ┌────────────────────┐
      │    Ollama API      │
      │ localhost:11434    │
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │     Llama 3.2      │
      │    Local LLM       │
      └─────────┬──────────┘
                │
                │ Generated Response
                ▼
      ┌────────────────────┐
      │   Streamlit UI     │
      └────────────────────┘
```

---

## 📂 Project Structure

```text
Local-LLM-Streamlit/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

> The `venv` directory is excluded from GitHub using `.gitignore`.

---

## ⚙️ Prerequisites

Before running the project, install:

* Python 3.x
* Ollama
* Llama 3.2
* Git

---

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sindhunelluri/Local-LLM-Streamlit.git
```

Navigate into the project:

```bash
cd Local-LLM-Streamlit
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

If PowerShell blocks activation, the application can also be run directly using the Python executable inside the virtual environment.

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
streamlit
requests
```

---

## 🦙 Ollama Setup

Install Ollama on your computer and verify the installation:

```bash
ollama --version
```

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Check installed models:

```bash
ollama list
```

You should see:

```text
llama3.2:latest
```

Test the model:

```bash
ollama run llama3.2
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

If port 8501 is already in use, Streamlit may automatically select another available port such as 8502.

---

## 🔌 Ollama API

The Streamlit application communicates with Ollama using the following local endpoint:

```text
http://localhost:11434/api/chat
```

The application sends the selected model and conversation messages to Ollama.

Example request structure:

```python
payload = {
    "model": "llama3.2",
    "messages": messages,
    "stream": False
}
```

Ollama returns the generated response, which is then displayed in the Streamlit interface.

---

## 💬 Example Interaction

### User

```text
What is Generative AI?
```

### Llama 3.2

```text
Generative AI is a branch of artificial intelligence
that can create new content such as text, images,
audio, video, and code based on patterns learned
from training data.
```

Users can continue asking questions while the current conversation context is maintained.

---

## 🧠 Conversation Memory

The application uses Streamlit session state to maintain the current conversation.

Messages are stored as:

```python
st.session_state.messages
```

Both user messages and assistant responses are added to the conversation history and sent to the Ollama chat endpoint.

This allows the model to use previous messages as context during the current session.

---

## 🗑️ Reset Conversation

The application provides a **Reset Conversation** button in the sidebar.

When clicked:

```python
st.session_state.messages = []
```

The conversation history is cleared and a new chat session can begin.

---

## 🛡️ Error Handling

The application handles common problems such as:

* Ollama not running
* Connection errors
* Request timeouts
* API errors
* Unexpected API responses

For example, if Ollama is unavailable, the application displays an appropriate error message instead of crashing.

---

## 📸 Screenshots

### Streamlit Interface

Add your project screenshot here:

```text
screenshots/streamlit-interface.png
```

### Conversation History

Add your conversation screenshot here:

```text
screenshots/conversation-history.png
```

### Ollama Model

Add your Ollama terminal screenshot here:

```text
screenshots/ollama-model.png
```

> Create a `screenshots` folder in the repository and upload your screenshots there.

---

## 🌐 Live Demo

A Streamlit deployment of the interface is available at:

**https://local-llm-app.streamlit.app/**

### Important Note

The deployed Streamlit interface runs on a remote server, while the Ollama model used for this project runs locally on the developer's computer.

Therefore, the live deployment demonstrates the Streamlit interface, while full Llama 3.2 inference is performed through the local Ollama setup.

---

## 🔗 Repository

GitHub:

**https://github.com/sindhunelluri/Local-LLM-Streamlit**

---

## 🎓 Internship Information

**Internship Domain:** Generative AI

**Organization:** Arch Technologies

**Task:** Task 1 - Build a Streamlit Interface for Inference of a Locally Hosted LLM

---

## 📚 Learning Outcomes

Through this project, I learned:

* Basics of Large Language Models
* Running LLMs locally with Ollama
* Using the Ollama REST API
* Building interactive applications with Streamlit
* Managing conversation state
* Connecting frontend applications with AI backends
* Handling API errors and timeouts
* Deploying Streamlit applications
* Managing and documenting a project using GitHub

---

## 🔮 Future Improvements

Possible future enhancements include:

* Support for multiple Ollama models
* Streaming token-by-token responses
* Temperature and model parameter controls
* Chat export functionality
* Dark/light theme customization
* Improved UI design
* Persistent chat history
* Authentication
* Remote LLM/API integration for cloud deployment

---

## 👩‍💻 Author

**Sindhu Nelluri**


---

⭐ If you find this project useful, consider giving the repository a star.
