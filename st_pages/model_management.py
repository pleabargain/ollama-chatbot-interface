import streamlit as st
import subprocess

from .ollama_models_db import (get_model_info, 
                               create_models_dataframe, 
                               display_models_library)

def get_available_models():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        models = result.stdout.strip().split('\n')[1:]  # Skip the header
        # Filter out models with "NAME", "failed" or empty models
        models = [model.split()[0] for model in models if "NAME" not in model and "failed"
                  not in model and model.strip()]
        return models
    except Exception as e:
        st.error(f"Error fetching models: {e}")
        return []

def pull_model(model_name):
    try:
        with st.spinner(f"Downloading model {model_name}..."):
            subprocess.run(['ollama', 'pull', model_name], check=True)
        st.success(f"Successfully installed {model_name}")
    except subprocess.CalledProcessError as e:
        st.error(f"Error pulling {model_name}: {e}")

def run():
    # Main title with styling
    st.markdown('''
    <div class="header-container">
        <p class="header-subtitle">🤖 Explore, Download, and Manage State-of-the-Art Language Models</p>
    </div>
    ''', unsafe_allow_html=True)

    # Model Installation Section
    st.markdown("""
    <div class="section-header">
        <h2>Download New Language Models</h2>
        <p>Install models from the Ollama ibrary</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 6])
    with col1:
        new_model = st.text_input("Enter the name of the model you want to download:", 
                                placeholder="e.g., llama2, mistral, gemma... (Press Enter to download)",
                                key="model_input")
        if new_model:  # When Enter is pressed and there's input
            pull_model(new_model)
    with col2:
        pass

    st.markdown('---') 

    # Local Models Section
    st.markdown("""
    <div class="section-header">
        <h2>Downloaded Language Models</h2>
        <p>Manage your local model collection</p>
    </div>
    """, unsafe_allow_html=True)

    available_models = get_available_models()
    if available_models:
        for model in available_models:
            with st.expander(f"📦 {model}"):
                model_info = get_model_info(model)
                if model_info:
                    st.code(model_info, language="yaml")
    else:
        st.info("No models currently installed. Use the Download tab to install models.")

    st.markdown('---') 

    # Apply styling and display
    models_df = create_models_dataframe()
    display_models_library(models_df)
    # Apply styling and display

    # Display hardware requirements
    st.markdown("### Hardware Requirements")
    st.markdown(
    """
    <div style='padding: 1rem; background-color: #374B5D; color: white; border-radius: 0.5rem'>
    <p>
    Minimum RAM requirements by model size:
    <ul>
    <li>1B-7B models: 8GB RAM</li>
    <li>8B-13B models: 16GB RAM</li>
    <li>14B-33B models: 32GB RAM</li>
    <li>34B+ models: 64GB+ RAM</li>
    </ul>
    Note: GPU acceleration (optional) can significantly improve inference speed.
    </p>
    </div>
    """, 
    unsafe_allow_html=True
    )

    st.markdown('---')

    # Tips for using models
    st.subheader("Tips for Using Models")
    st.markdown("""
    - Different models have different capabilities and are suited for various tasks.
    - Larger models generally perform better but require more computational resources.
    - Some models are specialized for certain languages or domains.
    - Be aware of model biases and limitations in your applications.
    - It's advisable to start with smaller models and scale up as needed for your usage.
    """)