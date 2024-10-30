import pandas as pd
from pandas.io.formats.style import Styler
import streamlit as st
import subprocess


def create_models_dataframe():
    # Get the names list from the original data
    names = [
        'llama3.2', 'llama3.1', 'gemma2', 'qwen2.5', 'phi3.5', 
            'nemotron-mini', 'mistral-small', 'mistral-nemo', 
            'deepseek-coder-v2', 'mistral', 'mixtral', 'codegemma',
            'command-r', 'command-r-plus', 'llava', 'llama3', 'gemma',
            'qwen', 'qwen2', 'phi3', 'llama2', 'codellama',
            'nomic-embed-text', 'mxbai-embed-large', 'dolphin-mixtral',
            'starcoder2', 'phi', 'deepseek-coder', 'llama2-uncensored',
            'dolphin-mistral', 'qwen2.5-coder', 'yi', 'dolphin-llama3',
            'orca-mini', 'zephyr', 'llava-llama3', 'snowflake-arctic-embed',
            'tinyllama', 'mistral-openorca', 'starcoder', 'codestral',
            'vicuna', 'granite-code', 'llama2-chinese', 'wizard-vicuna-uncensored',
            'wizardlm2', 'codegeex4', 'all-minilm', 'nous-hermes2',
            'openchat', 'aya', 'codeqwen', 'tinydolphin', 'wizardcoder',
            'stable-code', 'openhermes', 'mistral-large', 'qwen2-math',
            'reflection','bakllava', 'stablelm2', 'llama3-gradient', 
            'deepseek-llm', 'wizard-math', 'glm4', 'neural-chat', 'moondream',
            'llama3-chatqa', 'xwinlm', 'smollm', 'nous-hermes', 'sqlcoder',
            'phind-codellama', 'yarn-llama2', 'dolphincoder', 'wizardlm',
            'deepseek-v2', 'starling-lm', 'samantha-mistral', 'falcon',
            'solar', 'orca2', 'stable-beluga', 'yi-coder', 'hermes3',
            'internlm2', 'dolphin-phi', 'llava-phi3', 'wizardlm-uncensored',
            'yarn-mistral', 'llama-pro', 'medllama2', 'meditron',
            'nexusraven', 'nous-hermes2-mixtral', 'llama3-groq-tool-use',
            'codeup', 'minicpm-v', 'everythinglm', 'magicoder',
            'stablelm-zephyr', 'codebooga', 'wizard-vicuna', 'mistrallite',
            'falcon2', 'bge-m3', 'duckdb-nsql', 'megadolphin', 'notux',
            'open-orca-platypus2', 'goliath', 'notus', 'mathstral',
            'nemotron', 'solar-pro', 'dbrx', 'nuextract', 'reader-lm',
            'firefunction-v2', 'alfred', 'bge-large', 'deepseek-v2.5',
            'bespoke-minicheck', 'granite3-dense', 'paraphrase-multilingual',
            'granite3-moe', 'shieldgemma', 'llama-guard3', 'aya-expanse'
    ]

        
    # Create lists for each column that correspond to the names order
    descriptions_lists = []
    parameter_sizes = []
    total_pulls = []
    
    descriptions_dict = {
        'llama3.2': "Meta's Llama 3.2 goes small with 1B and 3B models.",
        'llama3.1': "Llama 3.1 is a new state-of-the-art model from Meta available in 8B, 70B and 405B parameter sizes.",
        'gemma2': "Google Gemma 2 is a high-performing and efficient model available in three sizes: 2B, 9B, and 27B.",
        'qwen2.5': "Qwen2.5 models are pretrained on Alibaba's latest large-scale dataset with up to 128K tokens support.",
        'phi3.5': "A lightweight AI model with 3.8 billion parameters with performance overtaking similarly and larger sized models.",
        'nemotron-mini': "A commercial-friendly small language model by NVIDIA optimized for roleplay, RAG QA, and function calling.",
        'mistral-small': "Mistral Small is a lightweight model designed for cost-effective use in tasks like translation and summarization.",
        'mistral-nemo': "A state-of-the-art 12B model with 128k context length, built by Mistral AI in collaboration with NVIDIA.",
        'deepseek-coder-v2': "An open-source Mixture-of-Experts code language model comparable to GPT4-Turbo in code-specific tasks.",
        'mistral': "The 7B model released by Mistral AI, updated to version 0.3.",
        'mixtral': "A set of Mixture of Experts (MoE) model with open weights by Mistral AI.",
        'codegemma': "Collection of powerful, lightweight models for coding tasks and math reasoning.",
        'command-r': "LLM optimized for conversational interaction and long context tasks.",
        'command-r-plus': "Powerful, scalable LLM for enterprise use cases.",
        'llava': "🌋 Multimodal model combining vision encoder and Vicuna for visual and language understanding.",
        'llama3': "Meta Llama 3: The most capable openly available LLM to date",
        'gemma': "Family of lightweight, state-of-the-art open models by Google DeepMind.",
        'qwen': "Series of LLMs by Alibaba Cloud spanning from 0.5B to 110B parameters",
        'qwen2': "New series of large language models from Alibaba group",
        'phi3': "Family of lightweight 3B (Mini) and 14B (Medium) state-of-the-art open models by Microsoft.",
        'llama2': "Collection of foundation language models ranging from 7B to 70B parameters.",
        'codellama': "Code-specialized language model for text-to-code generation and discussion.",
        'nomic-embed-text': "High-performing open embedding model with large token context window.",
        'mxbai-embed-large': "State-of-the-art large embedding model from mixedbread.ai",
        'dolphin-mixtral': "Uncensored Mixtral-based models excelling at coding tasks.",
        'starcoder2': "Next generation of transparently trained open code LLMs.",
        'phi': "2.7B language model with outstanding reasoning capabilities.",
        'deepseek-coder': "Capable coding model trained on two trillion tokens.",
        'llama2-uncensored': "Uncensored Llama 2 model variant.",
        'dolphin-mistral': "Uncensored Dolphin model based on Mistral, excelling at coding.",
        'qwen2.5-coder': "Code-Specific Qwen models for code generation and reasoning.",
        'yi': "High-performing, bilingual language model.",
        'dolphin-llama3': "Dolphin 2.9 based on Llama 3 with various skills.",
        'orca-mini': "General-purpose model suitable for entry-level hardware.",
        'zephyr': "Fine-tuned versions of Mistral and Mixtral models.",
        'llava-llama3': "LLaVA model fine-tuned from Llama 3 Instruct.",
        'snowflake-arctic-embed': "Text embedding models suite by Snowflake.",
        'tinyllama': "Compact 1.1B Llama model trained on 3 trillion tokens.",
        'mistral-openorca': "7B parameter model fine-tuned on OpenOrca dataset.",
        'starcoder': "Code generation model trained on 80+ programming languages.",
        'codestral': "Mistral AI's first code model for code generation.",
        'vicuna': "General use chat model based on Llama and Llama 2.",
        'granite-code': "Family of open foundation models by IBM for Code Intelligence",
        'llama2-chinese': "Llama 2 model fine-tuned for Chinese dialogue.",
        'wizard-vicuna-uncensored': "Uncensored Llama 2-based model series.",
        'wizardlm2': "Microsoft AI LLM for complex chat and reasoning.",
        'codegeex4': "Versatile model for AI software development.",
        'all-minilm': "Embedding models for sentence-level datasets.",
        'nous-hermes2': "Nous Research models for scientific discussion and coding.",
        'openchat': "Open-source models surpassing ChatGPT on various benchmarks.",
        'aya': "Cohere's multilingual models supporting 23 languages.",
        'codeqwen': "LLM pretrained on large amount of code data.",
        'tinydolphin': "1.1B parameter model based on TinyLlama.",
        'wizardcoder': "State-of-the-art code generation model",
        'stable-code': "3B coding model competing with larger models.",
        'openhermes': "7B model fine-tuned on Mistral with open datasets.",
        'mistral-large': "Mistral's flagship model with 128k context window.",
        'qwen2-math': "Specialized math models outperforming many others.",
        'reflection': "Model trained with Reflection-tuning for self-correction.",
        'bakllava': "BakLLaVA is a multimodal model with Mistral 7B base and LLaVA architecture",
        'stablelm2': "Multilingual model trained in 7 European languages",
        'llama3-gradient': "Extended LLama-3 with 1M token context",
        'deepseek-llm': "Advanced bilingual model with 2T tokens",
        'wizard-math': "Specialized for math and logic problems",
        'glm4': "Strong multi-lingual general language model",
        'neural-chat': "Mistral-based model with good domain coverage",
        'moondream': "Small vision language model for edge devices",
        'llama3-chatqa': "NVIDIA's Llama 3 model for QA and RAG",
        'xwinlm': "Competitive conversational model based on Llama 2",
        'smollm': "Family of small models from 135M to 1.7B parameters",
        'nous-hermes': "General purpose models from Nous Research",
        'sqlcoder': "SQL completion model based on StarCoder",
        'phind-codellama': "Code generation model based on Code Llama",
        'yarn-llama2': "Extended Llama 2 with 128k context",
        'dolphincoder': "Uncensored StarCoder2-based coding model",
        'wizardlm': "General purpose Llama 2 model",
        'deepseek-v2': "Strong and efficient MoE language model",
        'starling-lm': "RL-trained model for improved chatbot helpfulness",
        'samantha-mistral': "Companion assistant with psychology focus",
        'falcon': "TII's model for text tasks and chatbots",
        'solar': "Compact 10.7B model for single-turn chat",
        'orca2': "Microsoft's reasoning-focused Llama 2 variant",
        'stable-beluga': "Orca-style dataset fine-tuned model",
        'yi-coder': "State-of-the-art code model under 10B parameters",
        'hermes3': "Latest Hermes model by Nous Research",
        'internlm2': "Practical model with strong reasoning",
        'dolphin-phi': "Uncensored Phi-based Dolphin model",
        'llava-phi3': "Small LLaVA model from Phi 3 Mini",
        'wizardlm-uncensored': "Uncensored Wizard LM variant",
        'yarn-mistral': "Extended Mistral with 128K context",
        'llama-pro': "Specialized Llama 2 with domain knowledge",
        'medllama2': "Medical-focused Llama 2 model",
        'meditron': "Medical domain-adapted Llama 2",
        'nexusraven': "Function calling specialized model",
        'nous-hermes2-mixtral': "Nous Hermes 2 on Mixtral architecture",
        'llama3-groq-tool-use': "Advanced models for tool use/function calling",
        'codeup': "Llama2-based code generation model",
        'minicpm-v': "Vision-language understanding model",
        'everythinglm': "Uncensored Llama2 with 16K context",
        'magicoder': "Family of 7B code-focused models",
        'stablelm-zephyr': "Lightweight responsive chat model",
        'codebooga': "Merged high-performance code model",
        'wizard-vicuna': "Llama 2 based chat model",
        'mistrallite': "Extended context Mistral variant",
        'falcon2': "11B parameter model by TII",
        'bge-m3': "Versatile embedding model from BAAI",
        'duckdb-nsql': "Specialized SQL generation model",
        'megadolphin': "Enhanced large Dolphin variant",
        'notux': "High-quality MoE model",
        'open-orca-platypus2': "Merged chat and code generation model",
        'goliath': "Combined Llama 2 70B model",
        'notus': "High-quality Zephyr-based chat model",
        'mathstral': "Specialized math reasoning model",
        'nemotron': "NVIDIA's customized Llama 3.1 variant",
        'solar-pro': "Advanced 22B single-GPU model",
        'dbrx': "Databricks' general-purpose LLM",
        'nuextract': "Information extraction model based on Phi-3",
        'reader-lm': "HTML to Markdown conversion model",
        'firefunction-v2': "Advanced function calling model",
        'alfred': "Robust conversational model",
        'bge-large': "BAAI's text embedding model",
        'deepseek-v2.5': "Upgraded DeepSeek with combined abilities",
        'bespoke-minicheck': "Specialized fact-checking model",
        'granite3-dense': "IBM's tool-optimized model",
        'paraphrase-multilingual': "Multilingual sentence embedding model",
        'granite3-moe': "IBM's first MoE model series",
        'shieldgemma': "Safety-focused instruction model",
        'llama-guard3': "Content safety classification model",
        'aya-expanse': "Multilingual performance model"
    }

    # Use the original dictionaries to fill the lists in the correct order
    param_dict = {
            'llama3.2': "1B, 3B",
            'llama3.1': "8B, 70B, 405B",
            'gemma2': "2B, 9B, 27B",
            'qwen2.5': "0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B",
            'phi3.5': "3.8B",
            'nemotron-mini': "4B",
            'mistral-small': "22B",
            'mistral-nemo': "12B",
            'deepseek-coder-v2': "16B, 236B",
            'mistral': "7B",
            'mixtral': "8x7B, 8x22B",
            'codegemma': "2B, 7B",
            'command-r': "35B",
            'command-r-plus': "104B",
            'llava': "7B, 13B, 34B",
            'llama3': "8B, 70B",
            'gemma': "2B, 7B",
            'qwen': "0.5B, 1.8B, 4B, 7B, 14B, 32B, 72B, 110B",
            'qwen2': "0.5B, 1.5B, 7B, 72B",
            'phi3': "3.8B, 14B",
            'llama2': "7B, 13B, 70B",
            'codellama': "7B, 13B, 34B, 70B",
            'nomic-embed-text': "Embedding",
            'mxbai-embed-large': "335M",
            'dolphin-mixtral': "8x7B, 8x22B",
            'starcoder2': "3B, 7B, 15B",
            'phi': "2.7B",
            'deepseek-coder': "1.3B, 6.7B, 33B",
            'llama2-uncensored': "7B, 70B",
            'dolphin-mistral': "7B",
            'qwen2.5-coder': "1.5B, 7B",
            'yi': "6B, 9B, 34B",
            'dolphin-llama3': "8B, 70B",
            'orca-mini': "3B, 7B, 13B, 70B",
            'zephyr': "7B, 141B",
            'llava-llama3': "8B",
            'snowflake-arctic-embed': "22M, 33M, 110M, 137M, 335M",
            'tinyllama': "1.1B",
            'mistral-openorca': "7B",
            'starcoder': "1B, 3B, 7B, 15B",
            'codestral': "22B",
            'vicuna': "7B, 13B, 33B",
            'granite-code': "3B, 8B, 20B, 34B",
            'llama2-chinese': "7B, 13B",
            'wizard-vicuna-uncensored': "7B, 13B, 30B",
            'wizardlm2': "7B, 8x22B",
            'codegeex4': "9B",
            'all-minilm': "22M, 33M",
            'nous-hermes2': "10.7B, 34B",
            'openchat': "7B",
            'aya': "8B, 35B",
            'codeqwen': "7B",
            'tinydolphin': "1.1B",
            'wizardcoder': "33B",
            'stable-code': "3B",
            'openhermes': "7B",
            'mistral-large': "123B",
            'qwen2-math': "1.5B, 7B, 72B",
            'reflection': "70B",
            'bakllava': "7B",
            'stablelm2': "1.6B, 12B",
            'llama3-gradient': "8B, 70B",
            'deepseek-llm': "7B, 67B",
            'wizard-math': "7B, 13B, 70B",
            'glm4': "9B",
            'neural-chat': "7B",
            'moondream': "1.8B",
            'llama3-chatqa': "8B, 70B",
            'xwinlm': "7B, 13B",
            'smollm': "135M, 360M, 1.7B",
            'nous-hermes': "7B, 13B",
            'sqlcoder': "7B, 15B",
            'phind-codellama': "34B",
            'yarn-llama2': "7B, 13B",
            'dolphincoder': "7B, 15B",
            'wizardlm': "7B",
            'deepseek-v2': "16B, 236B",
            'starling-lm': "7B",
            'samantha-mistral': "7B",
            'falcon': "7B, 40B, 180B",
            'solar': "10.7B",
            'orca2': "7B, 13B",
            'stable-beluga': "7B, 13B, 70B",
            'yi-coder': "1.5B, 9B",
            'hermes3': "8B, 70B, 405B",
            'internlm2': "1M, 1.8B, 7B, 20B",
            'dolphin-phi': "2.7B",
            'llava-phi3': "3.8B",
            'wizardlm-uncensored': "13B",
            'yarn-mistral': "7B",
            'llama-pro': "N/A",
            'medllama2': "7B",
            'meditron': "7B, 70B",
            'nexusraven': "13B",
            'nous-hermes2-mixtral': "8x7B",
            'llama3-groq-tool-use': "8B, 70B",
            'codeup': "13B",
            'minicpm-v': "8B",
            'everythinglm': "13B",
            'magicoder': "7B",
            'stablelm-zephyr': "3B",
            'codebooga': "34B",
            'wizard-vicuna': "13B",
            'mistrallite': "7B",
            'falcon2': "11B",
            'bge-m3': "567M",
            'duckdb-nsql': "7B",
            'megadolphin': "120B",
            'notux': "8x7B",
            'open-orca-platypus2': "13B",
            'goliath': "N/A",
            'notus': "7B",
            'mathstral': "7B",
            'nemotron': "70B",
            'solar-pro': "22B",
            'dbrx': "132B",
            'nuextract': "3.8B",
            'reader-lm': "0.5B, 1.5B",
            'firefunction-v2': "70B",
            'alfred': "40B",
            'bge-large': "335M",
            'deepseek-v2.5': "236B",
            'bespoke-minicheck': "7B",
            'granite3-dense': "2B, 8B",
            'paraphrase-multilingual': "278M",
            'granite3-moe': "1B, 3B",
            'shieldgemma': "2B, 9B, 27B",
            'llama-guard3': "1B, 8B",
            'aya-expanse': "8B, 32B"
        }
        
    # Fill the lists maintaining order
    for name in names:
        descriptions_lists.append(descriptions_dict.get(name, "N/A"))
        parameter_sizes.append(param_dict.get(name, "N/A"))
    
    # Create DataFrame with aligned columns
    df = pd.DataFrame({
        'Model Name': names,
        'Description': descriptions_lists,
        'Parameter Sizes': parameter_sizes,
    })
    
    return df

def style_dataframe(df: pd.DataFrame) -> Styler:
    """Apply sophisticated styling to the DataFrame with wider cells"""
    
    styles = [
        # Table-wide styles
        {'selector': 'table', 
         'props': [
             ('border-collapse', 'separate'),
             ('border-spacing', '0 4px'),
             ('margin', '25px 0'),
             ('width', '100%'),
             ('border-radius', '8px'),
             ('overflow', 'hidden'),
             ('table-layout', 'fixed'),  # Added for better column width control
             ('box-shadow', '0 4px 6px rgba(0, 0, 0, 0.1)')
         ]},
        
        # Header styles
        {'selector': 'thead th', 
         'props': [
             ('background-color', '#374B5D'),
             ('color', '#FFFAE5'),
             ('padding', '18px 20px'),
             ('font-weight', '800'),
             ('text-transform', 'uppercase'),
             ('letter-spacing', '0.5px'),
             ('font-size', '20px'),
             ('border-bottom', '3px solid #56382D'),
             ('position', 'sticky'),
             ('top', '0')
         ]},
        
        # Index styling
        {'selector': 'tbody th', 
         'props': [
             ('background-color', '#935F4C'),
             ('color', '#FFFAE5'),
             ('padding', '12px 15px'),
             ('font-weight', '600'),
             ('text-align', 'center'),
             ('border-bottom', '1px solid rgba(255, 250, 229, 0.1)'),
             ('font-size', '17px'),
             ('width', '50px')  # Fixed width for index
         ]},
        
        # Cell styles
        {'selector': 'td', 
         'props': [
             ('padding', '12px 15px'),
             ('background-color', '#FFFAE5'),
             ('border-bottom', '1px solid rgba(55, 75, 93, 0.1)'),
             ('font-size', '17px'),
             ('transition', 'all 0.2s ease'),
             ('line-height', '1.6')  # Improved line height for readability
         ]},
        
        # Row hover effect
        {'selector': 'tbody tr:hover td', 
         'props': [
             ('background-color', '#F1E2AD'),
             ('transform', 'scale(1.01)'),
             ('box-shadow', '0 2px 4px rgba(0, 0, 0, 0.05)')
         ]},
        
        # Row hover effect for index
        {'selector': 'tbody tr:hover th', 
         'props': [
             ('transform', 'scale(1.01)'),
             ('box-shadow', '0 2px 4px rgba(0, 0, 0, 0.05)')
         ]},
        
        # Model name column
        {'selector': 'td:first-child', 
         'props': [
             ('font-weight', '600'),
             ('color', '#374B5D'),
             ('width', '100px')  # Fixed width for model name
         ]},
        
        # Description column
        {'selector': 'td:nth-child(2)', 
         'props': [
             ('text-align', 'left'),
             ('line-height', '1.6'),
             ('width', '250px'),  # Increased width for description
             ('white-space', 'normal'),
             ('padding-right', '20px')
         ]},
        
        # Parameter Sizes column
        {'selector': 'td:nth-child(3)', 
         'props': [
             ('width', '1000px'),  # Increased width for parameter sizes
             ('text-align', 'left'),
             ('white-space', 'normal')
         ]},
        
        {'selector': 'td:nth-child(5)', 
         'props': [
             ('width', '200px'),
             ('text-align', 'center')
         ]}

    ]

    return (df.style
            .set_table_styles(styles)
            .set_properties(**{
                'overflow': 'hidden',
                'text-overflow': 'ellipsis'
            })
            .set_table_attributes('class="dataframe hover-effect"'))

# Usage in Streamlit
def display_models_library(df: pd.DataFrame):

    st.markdown("""
        <div class="section-header">
            <h2>Ollama Models Library</h2>
            <p>Browse and explore available language models</p>
        </div>
    """, unsafe_allow_html=True)

    # Apply styling and display
    styled_df = style_dataframe(df)
    st.markdown(styled_df.to_html(escape=False), unsafe_allow_html=True)

def get_model_info(model_name):
    try:
        result = subprocess.run(['ollama', 'show', model_name], capture_output=True, text=True)
        raw_info = result.stdout.strip()
        
        def get_value(key):
            try:
                return raw_info.split(key)[1].split('\n')[0].strip()
            except:
                return 'N/A'
                
        def get_section(start_key, end_key='Parameters'):
            try:
                return raw_info.split(start_key)[1].split(end_key)[0].strip()
            except:
                return 'N/A'

        # Build the display text piece by piece
        display_text = [
            "",
            "📱 Model Architecture",
            "-------------------",
            f"• Architecture: {get_value('architecture')}",
            f"• Parameters: {get_value('parameters')}",
            f"• Quantization: {get_value('quantization')}",
            "",
            "🔄 Context Settings",
            "----------------",
            f"• Context Length: {get_value('context length')}",
            f"• Embedding Length: {get_value('embedding length')}",
            "",
            "⚙️ System Configuration",
            "--------------------",
            get_section('System'),
            "",
        ]
        
        return "\n".join(display_text)
        
    except Exception as e:
        st.error(f"Error fetching model info: {e}")
        return None


