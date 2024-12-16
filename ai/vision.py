from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.messages import SystemMessage
from prompts import system

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def generate_response(image_data):
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content=system.VISION_SYSTEM_PROMPT),
        ("human", [
            {
                "type": "text",
                "text": "Please provide me with information about this food."
            },
            {
                "type": "image_url",
                "image_url": {"url": "data:image/jpeg;base64,{image_data}"}
            }
        ])
    ])

    chain = prompt_template | llm | StrOutputParser()

    return chain.invoke(
        {
            "image_data": image_data
        }
    )