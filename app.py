import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from htmlTemplates import css, bot_template, user_template
import os

# Load API keys
load_dotenv()

# Functions for PDF processing
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks, use_openai):
    if use_openai:
        embeddings = OpenAIEmbeddings()
    else:
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore, use_openai):
    if use_openai:
        llm = ChatOpenAI()
    else:
        llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512})

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

# Streamlit Page Configuration
st.set_page_config(page_title="PDF Chatbot", page_icon=":books:")
st.write(css, unsafe_allow_html=True)

# App Initialization
st.sidebar.title("PDF Chatbot 🤖")
st.header("Chat with your PDFs 📚")

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

# Sidebar Inputs
st.sidebar.subheader("Upload PDFs")
pdf_docs = st.sidebar.file_uploader("Upload PDF files", accept_multiple_files=True)
use_openai = st.sidebar.radio("Choose Model", ["OpenAI", "HuggingFace"], index=0) == "OpenAI"

if st.sidebar.button("Process PDFs"):
    with st.spinner("Processing PDFs..."):
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks, use_openai)
        st.session_state.conversation = get_conversation_chain(vectorstore, use_openai)
        st.success("PDFs Processed Successfully!")

# Display uploaded files
if pdf_docs:
    st.sidebar.subheader("Uploaded Files")
    for doc in pdf_docs:
        st.sidebar.write(f"📄 {doc.name}")

# Chat Input and Output
user_question = st.text_input("Ask a question about your PDFs:")
if user_question:
    handle_userinput(user_question)

# Clear Chat Button
if st.button("Clear Chat"):
    st.session_state.chat_history = None
    st.session_state.conversation = None
    st.experimental_rerun()