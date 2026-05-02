# Звіт до роботи

## Тема: AI Агенти з Google ADK

### Мета роботи: Навчитись створювати AI агентів з використанням Google ADK (Python) та Poetry для управління залежностями проекту

### Виконання роботи

---

## 1. Підготовка робочого середовища

Версії встановленого ПО:

```
python --version
Python 3.13.13

poetry --version
Poetry (version 2.2.1)
```

Google API ключ отримано з [Google AI Studio](https://aistudio.google.com/app/apikey). Ключ збережено у файлах `.env` кожного агента та додано до `.gitignore`.

---

## 2. Встановлення Google ADK

```bash
cd works/10_python_agents
poetry init
poetry add google-adk python-dotenv
```

Файл `poetry.lock` — це файл з точно зафіксованими версіями всіх залежностей проекту (включно з транзитивними). Він гарантує, що всі розробники та середовища використовують однакові версії пакетів.

```bash
poetry run adk --version
adk, version 1.31.1
```

Основні команди ADK:

- `adk create <name>` — створює структуру нового проекту агента
- `adk run <name>` — запускає агента в інтерактивному CLI режимі
- `adk web --port 8000` — запускає веб-інтерфейс для тестування агентів

```
poetry run adk --help

Usage: adk [OPTIONS] COMMAND [ARGS]...

  Agent Development Kit CLI tools.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  api_server   Starts a FastAPI server for agents.
  create       Creates a new app in the current folder with prepopulated...
  deploy       Deploys agent to hosted environments.
  eval         Evaluates an agent given the eval sets.
  run          Runs an interactive CLI for a certain agent.
  web          Starts a FastAPI server with Web UI for agents.
```

---

## 3. Перший агент: my_first_agent

Структура проекту:

```
my_first_agent/
    agent.py
    .env
    __init__.py
```

Код агента (`my_first_agent/agent.py`):

```python
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
```

**Пояснення коду:**
- `Agent` — базовий клас ADK для створення агента на основі LLM (Large Language Model)
- Параметр `tools` — список функцій-інструментів, які агент може викликати для виконання завдань
- Функція `get_current_time` — інструмент, який повертає поточний час (mock-реалізація)

Запуск та діалог з агентом:

```
poetry run adk run my_first_agent

Який зараз час у Львові?
> Зараз у Львові 14:32:15.

Який час у Київ?
> У Києві зараз 14:32:18.

А скільки часу у Нью-Йорку?
> У Нью-Йорку зараз 14:32:21.
```

Веб-інтерфейс запущено командою `poetry run adk web --port 8000`, відкрито на http://localhost:8000.

---

## 4. Агент з математичними інструментами: math_agent

```python
import math
from google.adk.agents.llm_agent import Agent


def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height


def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2


def calculate_cube_volume(side: float) -> float:
    return side ** 3


def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height


root_agent = Agent(
    model="gemini-2.5-flash",
    name="math_agent",
    ...
    tools=[calculate_rectangle_area, calculate_circle_area, calculate_cube_volume, calculate_triangle_area],
)
```

Тестування агента через `adk web`:

```
Обчисли площу прямокутника зі сторонами 5 та 10
> Площа прямокутника зі сторонами 5 та 10 дорівнює 50.0 кв. од.

Яка площа кола з радіусом 7?
> Площа кола з радіусом 7 дорівнює приблизно 153.94 кв. од.

Який об'єм куба з ребром 3?
> Об'єм куба з ребром 3 дорівнює 27.0 куб. од.

Яка площа трикутника з основою 6 та висотою 4?
> Площа трикутника з основою 6 та висотою 4 дорівнює 12.0 кв. од.
```

Додатковий інструмент: `calculate_triangle_area` — обчислює площу трикутника за формулою $S = \frac{1}{2} \cdot b \cdot h$.

---

## 5. Агент-помічник для студентів: student_helper

```python
def explain_concept(concept: str, level: str = "beginner") -> dict: ...
def check_syntax(code: str, language: str = "python") -> dict: ...

root_agent = Agent(
    model="gemini-2.5-flash",
    name="student_helper",
    instruction="""
    Ти досвідчений викладач з ООП програмування який допомагає студентам.
    ...
    """,
    tools=[explain_concept, check_syntax],
)
```

Тестування:

```
Поясни що таке декоратори в Python
> Декоратори в Python — це функції, які змінюють поведінку інших функцій або класів.
  Вони використовуються за допомогою символу @. Наприклад:
  
  @my_decorator
  def my_function():
      pass

Як працює list comprehension?
> List comprehension — це стислий спосіб створення списків. Наприклад:
  squares = [x**2 for x in range(10)]

Перевір синтаксис: print('Hello World')
> Синтаксис виглядає коректно! Функція print() правильно використовується для виведення тексту.
```

---

## 6. Агент з конфігурацією: creative_writer

```python
root_agent = Agent(
    model="gemini-2.5-flash",
    name="creative_writer",
    ...
    config=GenerateContentConfig(
        temperature=1.5,
        top_k=40,
        top_p=0.95,
    ),
)
```

**Пояснення параметрів:**
- `temperature=1.5` — висока температура збільшує креативність та різноманітність відповідей (0.0–2.0)
- `top_k=40` — обмежує вибір до 40 найімовірніших токенів
- `top_p=0.95` — використовує токени з сукупною ймовірністю до 95%

Тестування:

```
Напиши коротку історію про подорож у космосі
> У серці зоряного скупчення, де галактики торкаються одна одної крилами туманностей,
  пілот Олена Коваль вела свій корабель крізь шторм темної матерії. Консоль мигала
  тривожним червоним, але в серці Олени горів лише один вогонь — цікавість...
```

---

## 7. Агент з пам'яттю: conversation_agent

```python
from google.adk.tools.tool_context import ToolContext

def save_user_preference(tool_context: ToolContext, preference_type: str, value: str) -> dict:
    existing_state = tool_context.state.get(preference_type, [])
    tool_context.state[preference_type] = existing_state + [value]
    ...

def recall_preference(tool_context: ToolContext, preference_type: str) -> dict:
    preferences = tool_context.state.get(preference_type, [])
    ...
```

Тестування:

```
Мене звати Віктор
> Привіт, Вікторе! Радий познайомитись!

Моє хобі — програмування та музика
> Чудово! Збережу, що ти захоплюєшся програмуванням та музикою.

Як мене звати?
> Тебе звати Віктор.

Яке моє хобі?
> Твоє хобі — програмування та музика.
```

---

## 8. Агент зі збереженням стану між сесіями: stateful_agent

```python
STATE_FILE = Path("stateful_agent/user_state.json")

def remember_fact(key: str, value: str) -> dict:
    state = load_state()
    state[key] = value
    return save_state(state)

def recall_fact(key: str) -> dict:
    state = load_state()
    value = state.get(key)
    ...
```

Перша сесія:
```
Мене звати Віктор і я вчуся в IT-коледжі
> Запам'ятав! Тебе звати Віктор, і ти навчаєшся в IT-коледжі.
```

Файл `user_state.json` після першої сесії:
```json
{
  "ім'я": "Віктор",
  "місце навчання": "IT-коледж"
}
```

Друга сесія (новий запуск):
```
Як мене звати?
> Тебе звати Віктор.

Де я навчаюся?
> Ти навчаєшся в IT-коледжі.
```

---

## 9. Налагодження агентів

Запуск у verbose режимі:

```
poetry run adk run my_first_agent --verbose
```

Verbose режим показує:
- Токени, відправлені до моделі
- Виклики інструментів та їх аргументи
- Відповіді інструментів
- Думки моделі (reasoning)

---

## 10. Структура проекту та спільні інструменти

```
works/10_python_agents/
├── my_first_agent/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── math_agent/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── student_helper/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── creative_writer/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── conversation_agent/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── stateful_agent/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── code_pipeline/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── story_improver/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── research_team/
│   ├── agent.py
│   ├── .env
│   └── __init__.py
├── tools/
│   ├── __init__.py
│   └── common_tools.py
├── pyproject.toml
├── poetry.lock
├── .env.example
├── .gitignore
└── README.md
```

Спільні інструменти у `tools/common_tools.py`:

```python
def format_text(text: str, style: str = "uppercase") -> str:
    if style == "uppercase":
        return text.upper()
    elif style == "lowercase":
        return text.lower()
    elif style == "title":
        return text.title()
    return text


def count_words(text: str) -> dict:
    words = text.split()
    return {
        "total_words": len(words),
        "total_chars": len(text),
        "unique_words": len(set(words)),
    }
```

Використання у агентах:
```python
from tools.common_tools import format_text, count_words
```

---

## 11. Workflow агенти

### Sequential Agent: code_pipeline

`SequentialAgent` виконує підагенти один за одним у строгому порядку.

```python
root_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[code_writer, code_reviewer, code_refactorer],
)
```

Тестування:
```
Створи функцію для обчислення факторіалу числа

[CodeWriterAgent]
```python
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Число має бути невід'ємним")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

[CodeReviewerAgent]
1. Правильність: рекурсія коректна, базовий випадок є
2. Обробка помилок: є перевірка на від'ємне число
3. Відсутня перевірка на цілочисельний тип

[CodeRefactorerAgent]
```python
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Очікується ціле число")
    if n < 0:
        raise ValueError("Число має бути невід'ємним")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
```

**Переваги Sequential агента:** гарантований порядок виконання, кожен наступний агент отримує результати попереднього через `output_key`. Порядок критично важливий — рев'ю не може відбутись до написання коду.

### Loop Agent: story_improver

`LoopAgent` виконує підагенти у циклі до досягнення умови завершення.

```python
improvement_loop = LoopAgent(
    name="ImprovementLoop",
    sub_agents=[critic, improver],
    max_iterations=5,
)

root_agent = SequentialAgent(
    name="StoryImprovementPipeline",
    sub_agents=[initial_writer, improvement_loop],
)
```

Механізм виходу з циклу: функція `exit_loop` встановлює `tool_context.actions.escalate = True`, що сигналізує `LoopAgent` зупинити виконання. Агент-покращувач викликає цю функцію, коли критик підтверджує, що всі критерії виконані.

Тестування:
```
Тема: робот який навчився мріяти

[Ітерація 1]
Початкова: "Робот ОМ-7 раптово почав мріяти."
Критик: Замало деталей, додай сцену та розвиток.

[Ітерація 2]
Покращена: "В тихій лабораторії, серед мерехтливих екранів, робот ОМ-7 вперше
побачив сон — нескінченне поле зі сріблястої трави..."
Критик: Історія готова.
```

### Parallel Agent: research_team

`ParallelAgent` виконує підагенти одночасно (паралельно).

```python
parallel_research = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[python_researcher, ai_researcher, web_researcher],
)

root_agent = SequentialAgent(
    name="ResearchPipeline",
    sub_agents=[parallel_research, synthesizer],
)
```

Тестування:
```
Які останні тренди у технологіях?

## Огляд технологічних тенденцій

### Python
Python 3.13 отримав значні покращення у продуктивності завдяки JIT-компіляції
та новому режиму без GIL. Python 3.14 продовжує цю тенденцію з покращеним
трасуванням помилок.

### Штучний інтелект
Головні тренди — мультимодальні моделі та агентні системи. Google ADK, LangChain
та AutoGen дозволяють будувати складні системи агентів.

### Веб-розробка
React 19 та Next.js 15 домінують у фронтенді. На бекенді зростає популярність
FastAPI та Bun.

### Висновок
Технологічний ландшафт 2026 визначається AI-інтеграцією в усі сфери розробки.
```

**Переваги паралельного виконання:** три дослідження виконуються одночасно замість послідовно, що скорочує час у ~3 рази. Підходить для незалежних завдань, які не залежать одне від одного.

### Порівняння Workflow агентів

| Тип | Коли використовувати | Приклад |
|-----|---------------------|---------|
| Sequential | Завдання потрібно виконати у строгому порядку | Pipeline: код → рев'ю → рефакторинг |
| Loop | Потрібне ітеративне покращення до певної умови | Покращення тексту до досягнення якості |
| Parallel | Незалежні завдання можна виконати одночасно | Дослідження різних тем паралельно |

---

### Висновок

У ході роботи було виконано наступне:

- Встановлено та налаштовано Google ADK 1.31.1 через Poetry з Python 3.13
- Створено 9 агентів у окремих папках: `my_first_agent`, `math_agent`, `student_helper`, `creative_writer`, `conversation_agent`, `stateful_agent`, `code_pipeline`, `story_improver`, `research_team`
- Реалізовано спільні інструменти у модулі `tools/common_tools.py`
- Протестовано всі три типи workflow агентів: `SequentialAgent`, `LoopAgent`, `ParallelAgent`

Мету роботи досягнуто — навчився створювати AI агентів з використанням Google ADK.

Нові знання:
- Клас `Agent` / `LlmAgent` та параметри `model`, `instruction`, `tools`, `config`
- `ToolContext` для збереження стану в межах сесії
- Збереження стану між сесіями через JSON файл
- `SequentialAgent` — послідовне виконання підагентів
- `LoopAgent` з механізмом виходу через `exit_loop`
- `ParallelAgent` — паралельне виконання для незалежних завдань
- `GenerateContentConfig` — налаштування `temperature`, `top_k`, `top_p`

Всі завдання виконано. Складнощів не виникло — документація Google ADK добре структурована. Формат здачі через GitHub зручний та дозволяє зберігати всі артефакти роботи. API ключі надійно захищені через `.env` + `.gitignore`.
