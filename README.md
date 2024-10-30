[![LinkedIn][linkedin-shield]][linkedin-url]
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/luísfssantos/
[contributors-shield]: https://img.shields.io/github/contributors/TsLu1s/SegmentAE.svg?style=for-the-badge&logo=github&logoColor=white
[contributors-url]: https://github.com/TsLu1s/SegmentAE/graphs/contributors
[license-shield]: https://img.shields.io/github/license/TsLu1s/SegmentAE.svg?style=for-the-badge&logo=opensource&logoColor=white
[license-url]: https://github.com/TsLu1s/SegmentAE/blob/main/LICENSE

# Streamlit Ollama Chatbot Multi-Model Interface

An advanced and interactive Streamlit chatbot application that integrates multiple language models through the Ollama API, featuring a sophisticated multi language model management system with an intuitive user interface.

## 🌟 Key Features

- **Multi-Model Support**: Seamlessly interact with various state-of-the-art Ollama language models including Llama, Mistral, Gemma, and 120+ more.
- **Model Management Interface**: Easy-to-use interface for downloading, managing, and switching between different language models.
- **Real-time Chat Interface**:  Clean interface with model-specific chat history and streamed responses.
- **Responsive Design**: Modern, responsive UI with animated components and intuitive navigation.

## 👏 Acknowledgments

* [Ollama](https://ollama.com/)
* [Streamlit](https://streamlit.io/)  

## 📋 Prerequisites

- Python 3.10 or higher
- Ollama API (latest version)
- Streamlit
- 8GB+ RAM (varies based on model size)

## STREAMLIT DEMO APP

**Important Note:** Demo Version is not able to run Ollama API, run the app locally for full feature usability.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ollama-chatbot-interface.streamlit.app/)

## ⚙️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/TsLu1s/ollama-chatbot-interface.git
cd ollama-chatbot-interface
```

2. **Set Up Conda Environment**

First, ensure you have Conda installed. Then create and activate a new environment with Python 3.10:

```bash
# Create new environment
conda create -n ollama_env python=3.10

# Activate the environment
conda activate ollama_env
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Ollama**
   
Visit Ollama API and follow the installation instructions for your operating system. **[Possible Restart PC needed]**


<div align="left">
   
[![Download Ollama](https://img.shields.io/badge/DOWNLOAD-OLLAMA-grey?style=for-the-badge&labelColor=black)](https://ollama.com/download)

</div>

5. **Start the Application**
```bash
streamlit run navegation.py
```

## 💻 Usage & Architecture

### Home Page
- Explore the Ollama model ecosystem with detailed model cards
- View comprehensive information about model capabilities and specializations:
  - Language Models, Specialized Models, Task-Specific Models, Domain-Specific Models...
- Access quick reference for hardware requirements
- Find links to essential documentation and resources

<details>
<summary>📸 View Home Page Template</summary>

![Home Page](https://github.com/TsLu1s/ollama-chatbot-interface/blob/main/imgs/home_page.jpg)
</details>

### Model Management
1. Navigate to the "Language Models Management" section
2. Select and download desired models from the available list
3. Monitor installation progress and system requirements
4. Manage installed models through the interface

<details>
<summary>📸 View Model Management Template</summary>

![Model Management](https://github.com/TsLu1s/ollama-chatbot-interface/blob/main/imgs/models_page.jpg)
</details>

### Chat Interface
1. Select a model from the dropdown menu
2. Enter your message in the chat input
3. View real-time responses in the chat window
4. Switch between models as needed

<details>
<summary>📸 View Chat Interface Template</summary>

![Chat Interface](https://github.com/TsLu1s/ollama-chatbot-interface/blob/main/imgs/chat_page.jpg)
</details>

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See [LICENSE](https://github.com/TsLu1s/SegmentAE/blob/main/LICENSE) for more information.

## 🔗 Contact 
 
Luis Santos - [LinkedIn](https://www.linkedin.com/in/lu%C3%ADsfssantos/)
