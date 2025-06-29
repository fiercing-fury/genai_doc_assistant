from langchain.chat_models import ChatOpenAI

def generate_logic_questions(text, n=3):
    llm = ChatOpenAI()
    prompt = f"Generate {n} logical/comprehension questions from this text:\n{text[:4000]}"
    return llm.predict(prompt)

def evaluate_answer(question, user_answer, source_text):
    llm = ChatOpenAI()
    prompt = f"""
    Question: {question}
    User's Answer: {user_answer}
    Source Content: {source_text}
    Evaluate if the answer is correct. Justify with a reference to the text.
    """
    return llm.predict(prompt)
