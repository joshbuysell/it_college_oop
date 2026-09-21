from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext


def save_user_preference(
    tool_context: ToolContext, preference_type: str, value: str
) -> dict:
    existing_state = tool_context.state.get(preference_type, [])
    tool_context.state[preference_type] = existing_state + [value]
    print(f"[Added to {preference_type}] {value}")
    return {
        "status": "success",
        "message": f"Збережено: {preference_type} = {value}",
    }


def recall_preference(tool_context: ToolContext, preference_type: str) -> dict:
    preferences = tool_context.state.get(preference_type, [])
    if preferences:
        return {
            "status": "success",
            "message": f"Згадано: {preference_type} = {', '.join(preferences)}",
        }
    return {
        "status": "error",
        "message": f"Не знайдено вподобань типу: {preference_type}",
    }


root_agent = Agent(
    model="gemini-2.5-flash",
    name="conversation_agent",
    description="Розмовний агент який пам'ятає користувача.",
    instruction="""
    Ти дружелюбний асистент який веде розмову з користувачем.

    Важливо:
    - Пам'ятай що користувач розповідає про себе та зберігай цю інформацію як
      вподобання за допомогою інструменту save_user_preference
    - Використовуй цю інформацію у подальшій розмові за допомогою інструменту
      recall_preference
    - Стався уважно до деталей, які користувач розповідає про себе
    - Будь ввічливим та цікавим співрозмовником
    - Звертайся до користувача по імені, якщо він його назве

    Відповідай українською мовою.
    """,
    tools=[save_user_preference, recall_preference],
)
