# Звіт до роботи

## Тема: Автоматизація тестування за допомогою GitHub Actions

### Мета роботи

Навчитися створювати workflow-файли GitHub Actions, запускати Python-тести
автоматично та вручну, використовувати розклад, параметри й умови виконання
кроків, а також додавати статусні badges до README.

### Виконання роботи

Роботу виконано за матеріалами:

- [Завдання про GitHub Actions](https://github.com/BobasB/it_college/tree/main/notes/08_github_actions)
- [Зразок оформлення звітів](https://github.com/BobasB/it_college/tree/main/reports)

У репозиторії створено два workflow:

| Workflow | Призначення |
|---|---|
| `Python Tests` | запускається під час push, pull request і вручну; виконує всі попередні роботи з тестування |
| `Manual Python Check` | запускається вручну або щосуботи о 09:00 UTC; перевіряє інтеграційні тести й створює coverage XML |

Файл `python-tests.yml` виконує такі кроки:

1. отримує код через `actions/checkout`;
2. налаштовує Python 3.11;
3. встановлює `pytest`, `Flask`, `coverage` та `pytest-cov`;
4. запускає `unittest`, pytest, coverage та інтеграційні тести;
5. перевіряє мінімальне покриття 90%.

Файл `manual-check.yml` демонструє:

- `workflow_dispatch` з параметром `name`;
- `schedule` з cron-виразом;
- умову `if`, яка пропускає або виконує крок привітання;
- створення `coverage.xml`.

У кореневий README додано badges для обох workflow. Вони ведуть на сторінку
Actions відповідного workflow та показують його останній статус.

### Локальна перевірка

Workflow-файли перевірено за структурою YAML і відповідністю синтаксису
GitHub Actions. Команди, які повторюють основні кроки CI локально:

```bash
python -m pip install pytest flask coverage pytest-cov
cd testing/11_general_unittest
python -m unittest -v
cd ../12_pytest
python -m pytest -v
cd ../13_coverage
python -m pytest --cov=app --cov-fail-under=90 -v
cd ../14_integration_testing
python -m pytest -v
```

Результат локальної перевірки:

```text
unittest: 14 passed
pytest: 13 passed
coverage: 7 passed, 100% coverage
integration: 9 passed
```

Фактичний запуск workflow відбувається на GitHub після push у гілку `main`,
створення pull request або ручного запуску у вкладці Actions. Для ручного
запуску `Manual Python Check` можна передати власне ім'я; якщо залишити
значення `Executer`, крок привітання буде пропущено.

### Висновок

У роботі створено два GitHub Actions workflow з автоматичним, ручним і плановим
запусками. Налаштовано встановлення залежностей, запуск усіх попередніх
Python-тестів, перевірку coverage, параметр workflow, умову `if` та status
badges. Мету роботи досягнуто, усі вимоги виконано, а локальні тести успішно
проходять.

### Посилання на виконану роботу

[GitHub Actions та звіт](https://github.com/joshbuysell/it_college_oop/tree/main/testing/15_github_actions)