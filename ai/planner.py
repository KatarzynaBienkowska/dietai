from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.messages import SystemMessage, HumanMessage
from prompts import system
from tools import fatsecret

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm_with_tools = llm.bind_tools(tools=[fatsecret.get_recipes])

def generate_response(calories: int, user_preferences: str):
    messages = [
        SystemMessage(system.MEAL_PLANNER_SYSTEM_PROMPT),
        HumanMessage(f"Generate a meal plan with:\nCalories: {calories}\nUser preferences: {user_preferences}")
    ]

    tools_response = llm_with_tools.invoke(messages)
    messages.append(tools_response)

    selected_tool = {"get_recipes": fatsecret.get_recipes}[tools_response.tool_calls[0]["name"]]
    tool_msg = selected_tool.invoke(tools_response.tool_calls[0])
    messages.append(tool_msg)

    response = llm_with_tools.invoke(messages)
    messages.append(response)

    for message in messages:
        print(message.pretty_print())

    return response.content