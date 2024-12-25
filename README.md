
# Chat with Multiple PDFs

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![OpenAI](https://img.shields.io/badge/OpenAI-Integration-success)
![License](https://img.shields.io/badge/License-MIT-green)

📚 **Chat with Multiple PDFs** is a Streamlit-based application that allows users to upload multiple PDF files, process their content, and interact with the information through an AI-powered conversational interface. It uses modern vector-based search and language models to provide intelligent answers to user queries about the uploaded documents.

---

## ✨ Features

- **Multi-PDF Support**: Upload multiple PDFs simultaneously and query their combined content.
- **AI Models**: Choose between OpenAI's GPT models or HuggingFace models for responses.
- **Memory Integration**: Keeps track of the conversation context for coherent, multi-turn interactions.
- **Vector-Based Search**: Efficiently searches through document chunks using FAISS (Facebook AI Similarity Search).
- **Interactive UI**: Clean, modern interface with styled user and bot avatars for an engaging experience.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/zwayth/chat_with_pdfs.git
cd chat_with_pdfs
```

### 2. Set Up the Environment

#### Python Installation
Ensure Python 3.7+ is installed.  
Check version:
```bash
python --version
```

#### Create a Virtual Environment
```bash
python -m venv venv
```
- Activate on Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- Activate on macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
1. Create a `.env` file in the root directory:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here
   ```
2. Replace `your_openai_api_key_here` and `your_huggingface_api_key_here` with your actual keys.

---

## 🛠️ How to Run

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser. It will usually run at `http://localhost:8501`.

---

## 📘 Usage

1. **Upload PDFs**: Drag and drop your PDF files into the sidebar.
2. **Process PDFs**: Click the **Process** button to extract and split text into chunks.
3. **Ask Questions**: Use the input box to ask questions about the uploaded documents.
4. **Toggle Models**: Choose between OpenAI and HuggingFace models via the sidebar settings.

---

## 📂 File Structure

```
chat_with_pdfs/
│
├── app.py                  # Main application logic
├── htmlTemplates.py        # Contains HTML and CSS for UI templates
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not shared publicly)
├── README.md               # Project documentation
├── assets/                 # Contains images for avatars
│   ├── bot_avatar.png      # Bot avatar image
│   ├── user_avatar.png     # User avatar image
```

---

## 💻 Technologies Used

- **Streamlit**: Web framework for the UI.
- **LangChain**: For language model integration and conversation memory.
- **FAISS**: Vector similarity search for efficient document retrieval.
- **PyPDF2**: For reading and processing PDF content.
- **OpenAI API**: GPT models for natural language understanding.
- **HuggingFace Hub**: Alternative LLM models.

---

## 🤝 Contributing

Feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- Inspired by the power of AI to transform document management.
- Special thanks to the LangChain and Streamlit communities for their support and tools.
