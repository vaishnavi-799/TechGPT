
# 🤖 ML Technical FAQ Chatbot (AI + ML + DL + NLP)

An intelligent AI-powered Technical FAQ Chatbot built using Flask and Sentence-BERT that understands the semantic meaning of user queries and returns the most relevant technical answer from a FAQ dataset.

---

# 🚀 Project Overview

This project is a Deep Learning-based NLP chatbot designed to answer technical questions related to Artificial Intelligence, Machine Learning, NLP, Flask, APIs, Databases, and other computer science topics.

The chatbot uses Sentence-BERT embeddings and cosine similarity to understand user questions based on meaning instead of exact keyword matching.

---

## 🤖 AI Techniques

* Intelligent chatbot system
* Automated response generation

---

## 📊 ML Techniques

* Cosine similarity
* Semantic similarity matching

---

## 🧠 DL Techniques

* Sentence-BERT (Transformer model)
* Embedding generation
* Semantic understanding

---

## 🗣️ NLP Techniques

* Sentence processing
* Semantic search
* Question answering system

---

# 🛠 Technologies Used

| Layer         | Technology                   |
| ------------- | ---------------------------- |
| Backend       | Flask (Python)               |
| Deep Learning | Sentence-BERT (Transformers) |
| NLP           | Sentence Transformers        |
| ML Concept    | Cosine Similarity            |
| Frontend      | HTML, CSS, JavaScript        |
| Dataset       | JSON                         |

---

# 📌 Project Workflow

User Question
↓
Sentence-BERT Model (Deep Learning)
↓
Convert Sentence → Embeddings (Vectors)
↓
Cosine Similarity (ML technique)
↓
Find Best Matching FAQ
↓
Return Answer

---

# 📂 Project Structure

```bash
technical-faq-chatbot/
│
├── app.py
├── faq.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── utils/
    └── preprocess.py
```
## ⚙️ How to Run This Project (Step-by-Step)

```bash
# 1. Clone the repository
        git clone https://github.com/your-username/technical-faq-chatbot.git

# 2. Move into project folder
        cd TechGPT

# 3. Create virtual environment 
        python -m venv venv

# 4. Activate virtual environment
        # Windows:
        venv\Scripts\activate
        
        # Mac/Linux:
        source venv/bin/activate

# 5. Install required dependencies
        pip install -r requirements.txt

# 6. Run Flask application
        python app.py

# 7. Open browser and go to:
        http://127.0.0.1:5000/
