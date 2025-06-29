# Smart Assistant for Research Summarization

## Overview
This GenAI tool allows users to upload a document (PDF/TXT), then interact with it through two powerful modes:
- **Ask Anything**: Ask contextual questions grounded in the document
- **Challenge Me**: Get logic-based questions, answer them, and receive feedback with justification

## Features
- PDF/TXT Upload
- 150-word Auto Summary
- Free-form Q&A
- Logic Question Generation and Evaluation
- Justification for Every Answer

## Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/yourusername/genai_doc_assistant.git
cd genai_doc_assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your OpenAI key to `.env`:
```bash
echo "OPENAI_API_KEY=your-api-key" > .env
```

4. Run the app:
```bash
streamlit run app.py
```

## Architecture
- Uses LangChain + OpenAI GPT
- FAISS for document embeddings & retrieval
- Streamlit as the frontend
