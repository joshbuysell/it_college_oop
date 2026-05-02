import datetime
from google.adk.agents.llm_agent import Agent


def get_current_time(city: str) -> dict:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return {
        "status": "success",
        "city": city,
        "time": current_time,
    }


root_agent = Agent(
    model="gemini-2.5-flash",
    name="time_agent",
    description="Повідомляє поточний час у вказаному місті.",
    instruction=(
        "Ти корисний асистент, який повідомляє поточний час у містах. "
        "Використовуй функцію 'get_current_time' для цього. "
        "Відповідай українською мовою та використовуй формат дати/часу HH:MM:SS."
    ),
    tools=[get_current_time],
)
