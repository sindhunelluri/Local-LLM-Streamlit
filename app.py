import streamlit as st
import requests

st.set_page_config(
    page_title="Local LLM Chat",
    page_icon="🤖",
    layout="wide"
)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2"

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state.messages = []


def generate_response(messages):
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "❌ Could not connect to Ollama. Please make sure Ollama is running."

    except requests.exceptions.Timeout:
        return "⏱️ The request timed out. Please try again."

    except requests.exceptions.RequestException as e:
        return f"❌ Error communicating with Ollama: {e}"

    except KeyError:
        return "❌ Unexpected response received from Ollama."


# -------------------------------
# Main UI
# -------------------------------

st.title("🤖 Local LLM Chat Assistant")

st.write(
    "Chat with a locally hosted Large Language Model "
    "using Ollama and Streamlit."
)


# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    st.write("**Model**")
    st.code(MODEL_NAME)

    st.write("**Backend**")
    st.code("Ollama")

    st.write("**API Endpoint**")
    st.code(OLLAMA_URL)

    st.divider()

    st.subheader("💬 Conversation")

    st.write(
        f"Messages: {len(st.session_state.messages)}"
    )

    if st.button(
        "🗑️ Reset Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# -------------------------------
# Display chat history
# -------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -------------------------------
# User input
# -------------------------------

prompt = st.chat_input(
    "Ask something to your local LLM..."
)


if prompt:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("🤔 Thinking..."):

            answer = generate_response(
                st.session_state.messages
            )

        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )