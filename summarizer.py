from langchain.chat_models import ChatOpenAI

def generate_summary(text):
    prompt = f"Summarize the following in less than 150 words:\n{text[:4000]}"
    llm = ChatOpenAI(temperature=0)
    return llm.predict(prompt)
