import streamlit as st
from components import document_handler, summarizer, qa_handler, logic_challenge

st.title("📄 Smart Research Assistant")

file = st.file_uploader("Upload PDF or TXT file", type=['pdf', 'txt'])

if file:
    with open(file.name, "wb") as f:
        f.write(file.read())

    docs = document_handler.load_and_split(file.name)
    text = " ".join([doc.page_content for doc in docs])

    st.subheader("📌 Summary")
    st.write(summarizer.generate_summary(text))

    mode = st.radio("Choose Mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        qa_chain = qa_handler.build_qa_chain(docs)
        question = st.text_input("Ask a question based on the document:")
        if question:
            result = qa_chain({"query": question})
            st.write("Answer:", result['result'])
            if result.get("source_documents"):
                st.caption("Supported by:")
                for src in result['source_documents']:
                    st.markdown(f"> {src.page_content[:300]}...")

    elif mode == "Challenge Me":
        questions = logic_challenge.generate_logic_questions(text)
        st.markdown("### 🧠 Try answering:")
        for i, q in enumerate(questions.split('\n')):
            if q.strip():
                user_ans = st.text_area(f"Q{i+1}: {q}", key=f"q{i}")
                if user_ans:
                    feedback = logic_challenge.evaluate_answer(q, user_ans, text)
                    st.markdown(f"✅ Feedback: {feedback}")
