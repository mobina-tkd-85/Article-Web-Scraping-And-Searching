# 🚀 Article-Web-Scraping: The Ultimate Sports News AI Assistant

## 📰 About The Project

Ever wished you could have a personal sports analyst who's read every single article published today? Well, that's exactly what this project delivers!

**The Evolution of a Simple Scraper:**
This project started as a basic Guardian API scraper, but it has evolved into something far more powerful. I've transformed it into an intelligent Q&A system that doesn't just fetch articles—it understands them!

Here's what makes this project special:
- 🔍 **Scrapes** the latest sports and football articles from The Guardian
- 🧩 **Breaks down** articles into intelligent chunks for better processing
- 🧠 **Stores** everything in FAISS (Facebook AI Similarity Search) for lightning-fast retrieval
- 💬 **Answers** your questions using state-of-the-art Hugging Face LLM models
- 🌐 **Showcases** everything through a sleek local Flask server with an intuitive HTML interface

The best part? You can ask questions like "What were the key highlights from yesterday's football matches?" and get instant, accurate answers drawn from dozens of articles!

---

## 🖥️ Interface Preview

![Screenshot 2026-06-21 221345.png](output/Screenshot%202026-06-21%20221345.png)

*The user-friendly HTML interface where you can ask questions and get AI-powered answers instantly!*

---

## 🛠️ Built With

- **Beautiful Soup** - For elegant HTML parsing
- **FAISS** - Facebook's powerful similarity search library
- **Hugging Face Transformers** - State-of-the-art LLM models
- **Flask** - Lightweight web framework for the local server
- **Sentence-Transformers** - For creating embeddings that understand context
- **LangChain** - For seamless LLM integration and document processing

---

## ✨ Key Features

### Data Pipeline
1. **Smart Fetching**: Pulls sports and football articles from Guardian API
2. **Intelligent Chunking**: Breaks down long articles into meaningful, context-rich segments
3. **Vector Storage**: Uses FAISS to create a searchable database of article embeddings
4. **Semantic Search**: Finds the most relevant articles based on your questions

### AI Capabilities
- **Context-Aware Answers**: The LLM doesn't just retrieve articles—it understands them
- **Conversational Interface**: Ask follow-up questions naturally
- **Real-Time Processing**: New articles are processed and available instantly
- **Source Attribution**: Know exactly which articles your answers came from

---
