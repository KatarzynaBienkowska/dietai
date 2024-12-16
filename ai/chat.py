from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.messages import SystemMessage
from prompts import system

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def generate_response(user_prompt, chat_history=None):
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content=system.CHAT_SYSTEM_PROMPT),
        MessagesPlaceholder("history"),
        ("human", "{prompt}")
    ])

    chain = prompt_template | llm | StrOutputParser()

    return chain.invoke(
        {
            "history": chat_history or [],
            "prompt": user_prompt
        }
    )