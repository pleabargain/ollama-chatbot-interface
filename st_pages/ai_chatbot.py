import streamlit as st
import requests
import subprocess
import json

def is_ollama_running():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        return response.status_code == 200
    except requests.RequestException:
        return False

def start_ollama():
    try:
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        st.success("Ollama started successfully!")
    except FileNotFoundError:
        st.error("Ollama is not installed or not in the system PATH.")

def get_available_models():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json()
            return [model['name'] for model in models['models'] if 'failed' not in model['name'].lower()]
        return []
    except requests.RequestException:
        return []

def chat_with_llama(prompt, model_name):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model_name,
        "prompt": prompt
    }
    try:
        response = requests.post(url, json=data, stream=True)
        response.raise_for_status()
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_line = json.loads(line)
                    if 'response' in json_line:
                        full_response += json_line['response']
                except json.JSONDecodeError as e:
                    st.error(f"Error decoding JSON: {e}")
                    st.text(f"Problematic line: {line}")
        
        return full_response
    except requests.RequestException as e:
        st.error(f"Error communicating with Ollama: {e}")
        return None

def on_model_change():
    current_model = st.session_state.model_selectbox
    
    # Clear messages whenever the model changes
    if 'previous_model' in st.session_state and st.session_state.previous_model != current_model:
        st.session_state.messages = []
    
    # Update the previous model
    st.session_state.previous_model = current_model


def run():
    # Main title with styling
    st.markdown('''
    <div class="header-container">
        <p class="header-subtitle">🤖 Chat with State-of-the-Art Language Models</p>
    </div>
    ''', unsafe_allow_html=True)

    # Initialize session state variables
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'previous_model' not in st.session_state:
        st.session_state.previous_model = None

    # Main chat interface
    if not is_ollama_running():
        st.warning("Ollama is not running. Click the button below to start it.")
        if st.button("Start Ollama"):
            start_ollama()
        return

    # Model selection with callback
    st.subheader("Select a Language Model:")
    col1, col2 = st.columns([3, 6])
    with col1:
        model_name = st.selectbox(
            label="Language Model Selection",
            options=get_available_models(),
            format_func=lambda x: f'🔮 {x}',
            key="model_selectbox",
            on_change=on_model_change,
            label_visibility="collapsed"
        )
    with col2:
        pass

    st.markdown('---')

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input(
        f"What would you like to ask {model_name}?",
        key="chat_input",
    )

    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response
        with st.chat_message("assistant"):
            response = chat_with_llama(prompt, model_name)
            if response:
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error(f"Failed to get a response from {model_name}. Please check if Ollama is running correctly and the model is available.")