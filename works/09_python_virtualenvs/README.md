# Віртуальні середовища Python

## Тема
Віртуальні середовища Python (venv, pipenv, poetry).

## Мета роботи
Навчитися працювати зі сторонніми бібліотеками, створювати та використовувати віртуальні середовища (venv, pipenv, poetry), управляти залежностями та змінними середовища.

---

## Виконання роботи

### 1. Основи роботи з сторонніми бібліотеками

Перевірено версію `pip` на комп'ютері:

```
$ pip3 -V
pip 21.2.4 from /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
```

Переглянуто доступні команди `pip`:

```
$ pip3 --help
Commands:
  install       Install packages.
  download      Download packages.
  uninstall     Uninstall packages.
  freeze        Output installed packages in requirements format.
  list          List installed packages.
  show          Show information about installed packages.
  check         Verify installed packages have compatible dependencies.
  config        Manage local and global configuration.
  search        Search PyPI for packages.
  cache         Inspect and manage pip's wheel cache.
  index         Inspect information available from package indexes.
  wheel         Build wheels from your requirements.
  hash          Compute hashes of package archives.
  completion    A helper command used for command completion.
  debug         Show information useful for debugging.
  help          Show help for commands.
```

Перевірено встановлені бібліотеки:

```
$ pip3 list
Package            Version
------------------ ------------
altgraph           0.17.2
appnope            0.1.4
certifi            2026.2.25
charset-normalizer 3.4.5
comm               0.2.3
debugpy            1.8.20
exceptiongroup     1.3.1
filelock           3.19.1
idna               3.11
ipykernel          6.31.0
ipython            8.18.1
jedi               0.19.2
jupyter_client     8.6.3
jupyter_core       5.8.1
numpy              2.0.2
openpyxl           3.1.5
packaging          26.0
pandas             2.3.3
parso              0.8.6
pexpect            4.9.0
pillow             11.3.0
pip                21.2.4
pipenv             2025.0.4
platformdirs       4.4.0
playwrighty        1.58.0
poetry             2.2.1
prompt_toolkit     3.0.52
psutil             7.2.2
Pygments           2.19.2
python-dateutil    2.9.0.post0
pytz               2025.2
requests           2.32.5
setuptools         82.0.1
six                1.15.0
tornado            6.5.4
traitlets          5.14.3
typing_extensions  4.15.0
urllib3            2.6.3
virtualenv         21.2.0
wheel              0.37.0
zipp               3.23.0
```

---

### 2. Робота з бібліотекою requests

Встановлено бібліотеку `requests` та перевірено її роботу:

```
$ python3 -c "import requests; print(requests.__version__)"
2.32.5

$ python3 -c "import requests; r = requests.get('https://google.com'); print(r.status_code)"
200
```

Результат виконання команд демонструє, що бібліотека `requests` успішно працює — отримано відповідь зі статусом 200 від Google.

Додаткові методи бібліотеки requests: `requests.post()`, `requests.put()`, `requests.delete()`, `requests.head()`, `requests.patch()` — дозволяють виконувати різні HTTP-запити.

Перевірка інформації про бібліотеку та зміна версій:

```
$ pip3 show requests
Name: requests
Version: 2.32.5
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Location: /Users/viktortsvyk/Library/Python/3.9/lib/python/site-packages
Requires: urllib3, charset_normalizer, idna, certifi
```

---

### 3. Робота з Jikanpy (Anime API)

Встановлено бібліотеки `jikanpy-v4` та `Flask`. Створено файл `anime.py` який отримує дані про епізоди аніме серіалу:

```python
from flask import Flask
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

j = jikan.anime(54595, extension='episodes')

@app.route('/')
def home():
    a = str()
    for episode in j["data"]:
        a += (
            f"<p>Епізод {episode['mal_id']} "
            f"з назвою: {episode['title']} "
            f"має оцінку {episode['score']}<p>"
        )
    return a
```

Результат виконання програми:

```
$ pipenv run python -c "from jikanpy import Jikan; ..."
Епізод 1 з назвою: The Lawless City має оцінку 4.49
Епізод 2 з назвою: The Haven має оцінку 4.48
Епізод 3 з назвою: The Hour of Awakening має оцінку 4.53
Епізод 4 з назвою: Mask of Falsehood має оцінку 4.34
Епізод 5 з назвою: He Who Pulls The Strings має оцінку 4.36
Епізод 6 з назвою: John Smith має оцінку 4.46
Епізод 7 з назвою: Something Precious має оцінку 4.54
Епізод 8 з назвою: Tears of the Dragon має оцінку 3.89
Епізод 9 з назвою: Key має оцінку 4.36
Епізод 10 з назвою: The Caged Bird має оцінку 4.4
Епізод 11 з назвою: Decision має оцінку 4.64
Епізод 12 з назвою: Highest має оцінку 4.52
```

Аніме серіали поточного сезону (Winter 2026):

```
$ pipenv run python -c "from jikanpy import Jikan; jikan=Jikan(); ..."
Аніме поточного сезону (Winter 2026):
  Sousou no Frieren 2nd Season - оцінка: 9.15
  Jujutsu Kaisen: Shimetsu Kaiyuu - Zenpen - оцінка: 8.58
  Jigokuraku 2nd Season - оцінка: 8.24
  Yuusha-kei ni Shosu: Choubatsu Yuusha 9004-tai Keimu Kiroku - оцінка: 8.17
  [Oshi no Ko] 3rd Season - оцінка: 8.59
  Enen no Shouboutai: San no Shou Part 2 - оцінка: 8.05
  Fate/strange Fake - оцінка: 8.51
  Seihantai na Kimi to Boku - оцінка: 8.21
  Mato Seihei no Slave 2 - оцінка: 7.46
  Yuusha Party wo Oidasareta Kiyoubinbou - оцінка: 6.66
```

---

### 4. Робота у віртуальному середовищі (venv)

Створено віртуальне середовище за допомогою `venv`:

```
$ python3 -m venv ./my_env
$ source my_env/bin/activate
$ pip install requests
Successfully installed certifi-2026.2.25 charset-normalizer-3.4.5 idna-3.11 requests-2.32.5 urllib3-2.6.3
$ deactivate
```

Після `deactivate` команда `pip show requests` показує глобально встановлену бібліотеку, а не ту що була встановлена у `venv`. Це демонструє ізоляцію віртуального середовища — бібліотеки встановлені в `venv` доступні лише всередині нього.

Для `VENV` середовища потрібно ігнорувати наступні папки у `.gitignore`:

```
my_env/
.venv/
__pycache__/
*.pyc
```

Створено файл `.gitignore` з відповідними правилами.

---

### 5. Робота з Pipenv

Перевірено доступні команди `pipenv`:

```
$ pipenv --help
Commands:
  check         Checks for PyUp Safety security vulnerabilities
  clean         Uninstalls all packages not specified in Pipfile.lock
  graph         Displays currently-installed dependency graph information
  install       Installs provided packages and adds them to Pipfile
  lock          Generates Pipfile.lock
  open          View a given module in your editor
  requirements  Generate a requirements.txt from Pipfile.lock
  run           Spawns a command installed into the virtualenv
  scripts       Lists scripts in current environment config
  shell         Spawns a shell within the virtualenv
  sync          Installs all packages specified in Pipfile.lock
  uninstall     Uninstalls a provided package and removes it from Pipfile
  update        Runs lock, then sync
  upgrade       Resolves provided packages and adds them to Pipfile
  verify        Verify the hash in Pipfile.lock is up-to-date
```

Створено середовище та встановлено бібліотеки:

```
$ pipenv --python 3.9
Creating a virtualenv for this project...
Virtualenv location: /Users/viktortsvyk/.local/share/virtualenvs/09_python_virtualenvs-LzUQ4qE6

$ pipenv --venv
/Users/viktortsvyk/.local/share/virtualenvs/09_python_virtualenvs-LzUQ4qE6

$ pipenv run python -V
Python 3.9.6

$ pipenv install requests
Installing requests...
✔ Installation Succeeded
Installing dependencies from Pipfile.lock...
All dependencies are now up-to-date!

$ pipenv install jikanpy-v4 Flask
Installing jikanpy-v4...
✔ Installation Succeeded
Installing Flask...
✔ Installation Succeeded
All dependencies are now up-to-date!
```

Перевірено список встановлених бібліотек у pipenv середовищі:

```
$ pipenv run pip list
Package           Version
----------------- ---------
aiohappyeyeballs  2.6.1
aiohttp           3.13.3
aiosignal         1.4.0
attrs             25.4.0
async-timeout     5.0.1
blinker           1.9.0
certifi           2026.2.25
charset-normalizer 3.4.5
click             8.1.8
flake8            7.3.0
Flask             3.1.3
frozenlist        1.8.0
idna              3.11
itsdangerous      2.2.0
jikanpy-v4        1.0.2
Jinja2            3.1.6
mccabe            0.7.0
MarkupSafe        3.0.3
multidict         6.7.1
pip               26.0.1
propcache         0.4.1
pycodestyle       2.14.0
pyflakes          3.4.0
requests          2.32.5
simplejson        3.20.2
urllib3           2.6.3
Werkzeug          3.1.6
yarl              1.22.0
zipp              3.23.0
```

Файл `Pipfile` містить опис залежностей проекту:

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"
jikanpy-v4 = "*"
flask = "*"

[dev-packages]
flake8 = "*"

[requires]
python_version = "3.9"
python_full_version = "3.9.6"
```

`Pipfile.lock` містить точні версії всіх залежностей та їх хеші для забезпечення відтворюваності середовища.

Дерево залежностей (`pipenv graph`):

```
flake8==7.3.0
├── mccabe
├── pycodestyle
└── pyflakes
Flask==3.1.3
├── blinker
├── click
├── importlib_metadata
│   └── zipp
├── itsdangerous
├── Jinja2
│   └── MarkupSafe
├── MarkupSafe
└── Werkzeug
    └── MarkupSafe
jikanpy-v4==1.0.2
├── aiohttp
│   ├── aiohappyeyeballs
│   ├── aiosignal
│   ├── async-timeout
│   ├── attrs
│   ├── frozenlist
│   ├── multidict
│   ├── propcache
│   └── yarl
├── requests
│   ├── certifi
│   ├── charset-normalizer
│   ├── idna
│   └── urllib3
└── simplejson
```

---

### 6. Запуск програми через pipenv

Створено файл `requests_test.py`:

```python
import requests

response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)
```

Результат запуску через `pipenv run`:

```
$ pipenv run python requests_test.py
b'<!DOCTYPE html>'
b'<html lang="en">'
b''
b'<head>'
b'    <meta charset="UTF-8">'
b'    <title>httpbin.org</title>'
b'    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"'
b'        rel="stylesheet">'
b'    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">'
b'    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />'
b'    <style>'
b'        html {'
b'            box-sizing: border-box;'
b'            overflow: -moz-scrollbars-vertical;'
b'            overflow-y: scroll;'
b'        }'
...
```

Програма успішно виконується у віртуальному середовищі pipenv.

---

### 7. Перевірка коду за допомогою flake8

Встановлено `flake8` як dev-залежність:

```
$ pipenv install --dev flake8
Installing flake8...
✔ Installation Succeeded
Installing dependencies from Pipfile.lock...
All dependencies are now up-to-date!
```

Результат виконання `flake8`:

```
$ pipenv run flake8 --exclude=my_env .
(порожній вивід — помилок не знайдено)
```

Код написаний відповідно до стандартів PEP 8, тому `flake8` не знайшов жодних помилок у файлах `anime.py`, `env_test.py`, `requests_test.py`.

---

### 8. Перевірка безпеки залежностей

Результат перевірки безпеки:

```
$ pipenv check
Checking PEP 508 requirements... Passed!
Checking Pipfile.lock packages for vulnerabilities...
Found and scanned 26 packages
0 vulnerabilities reported
0 vulnerabilities ignored
No known security vulnerabilities reported.
```

Вразливостей у залежностях не знайдено.

---

### 9. Робота зі змінними середовища

Створено файл `.env`:

```
IT_TEST=HelloWorld
```

Створено файл `env_test.py`:

```python
import os

print(f"Значення змінної IT_TEST = {os.environ['IT_TEST']}")
```

Результат запуску через `pipenv run`:

```
$ pipenv run python env_test.py
Loading .env environment variables...
Значення змінної IT_TEST = HelloWorld
```

Якщо виконати скрипт без активації віртуального середовища:

```
$ python3 env_test.py
Traceback (most recent call last):
  File "env_test.py", line 3, in <module>
    print(f"Значення змінної IT_TEST = {os.environ['IT_TEST']}")
KeyError: 'IT_TEST'
```

Без `pipenv` файл `.env` не завантажується автоматично, тому змінна `IT_TEST` не доступна і виникає помилка `KeyError`.

---

### 10. Робота з Poetry

Встановлено `poetry` та створено новий проект:

```
$ pip3 install --user poetry
Successfully installed poetry-2.2.1

$ poetry --version
Poetry (version 2.2.1)

$ poetry new myproject
Created package myproject in myproject

$ cd myproject
$ poetry add requests
Creating virtualenv myproject-o1Fx34Hx-py3.9
Using version ^2.32.5 for requests
Resolving dependencies... (0.7s)
  - Installing certifi (2026.2.25)
  - Installing charset-normalizer (3.4.5)
  - Installing idna (3.11)
  - Installing urllib3 (2.6.3)
  - Installing requests (2.32.5)
Writing lock file
```

Файл `pyproject.toml`:

```toml
[project]
name = "myproject"
version = "0.1.0"
description = ""
authors = [{name = "Viktor Tsvyk"}]
requires-python = ">=3.9"
dependencies = ["requests (>=2.32.5,<3.0.0)"]

[dependency-groups]
dev = ["pytest (<9)", "flake8 (>=7.3.0,<8.0.0)"]
```

Дерево залежностей poetry:

```
$ poetry show --tree
requests 2.32.5 Python HTTP for Humans.
├── certifi >=2017.4.17
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.21.1,<3
```

Інформація про середовище:

```
$ poetry env info
Virtualenv
Python:         3.9.6
Implementation: CPython
Path:           /Users/viktortsvyk/Library/Caches/pypoetry/virtualenvs/myproject-o1Fx34Hx-py3.9
Valid:          True
```

Створено та запущено програму `main.py` у Poetry середовищі:

```python
import requests


def main():
    response = requests.get('https://httpbin.org/json')
    data = response.json()
    print(f"Status: {response.status_code}")
    print(f"Slideshow title: {data['slideshow']['title']}")
    for slide in data['slideshow']['slides']:
        print(f"  - {slide['title']}: {slide.get('items', ['No items'])[0]}")


if __name__ == '__main__':
    main()
```

```
$ poetry run python main.py
Status: 200
Slideshow title: Sample Slide Show
  - Wake up to WonderWidgets!: No items
  - Overview: Why <em>WonderWidgets</em> are great
```

Додано dev-залежності:

```
$ poetry add --group dev pytest flake8
Using version ^7.3.0 for flake8
Resolving dependencies... (2.0s)
  - Installing mccabe (0.7.0)
  - Installing pycodestyle (2.14.0)
  - Installing pyflakes (3.4.0)
  - Installing flake8 (7.3.0)
  - Installing pytest (8.4.2)
Writing lock file
```

Перевірено список залежностей та середовище:

```
$ poetry show
certifi            2026.2.25  Python package for providing Mozilla's CA Bundle.
charset-normalizer 3.4.5      The Real First Universal Charset Detector.
idna               3.11       Internationalized Domain Names in Applications
requests           2.32.5     Python HTTP for Humans.
urllib3            2.6.3      HTTP library with thread-safe connection pooling.

$ poetry env list
myproject-o1Fx34Hx-py3.9 (Activated)
```

---

### 11. Допомога ChatGPT

За допомогою АІ створено Flask веб-додаток (`anime.py`) який використовує бібліотеку `jikanpy` для отримання даних про аніме та відображення їх на веб-сторінці. Додаток запускається через `pipenv run python anime.py` та доступний за адресою `http://127.0.0.1:5000/`.

---

---

## Структура файлів

```
works/09_python_virtualenvs/
├── README.md                # Цей файл — звіт
├── Pipfile                  # Опис залежностей pipenv
├── Pipfile.lock             # Зафіксовані версії залежностей
├── .env                     # Змінні середовища (IT_TEST=HelloWorld)
├── .gitignore               # Ігнорування my_env/, __pycache__/ тощо
├── anime.py                 # Flask + Jikanpy веб-додаток
├── env_test.py              # Тест змінних середовища
├── requests_test.py         # Тест бібліотеки requests
├── my_env/                  # VENV середовище (ігнорується git)
├── assets/                  # Папка для скріншотів
└── myproject/               # Poetry проект
    ├── pyproject.toml       # Конфігурація poetry
    ├── poetry.lock          # Зафіксовані версії poetry
    ├── main.py              # Програма для poetry середовища
    └── src/myproject/       # Пакет проекту
```

---

## Висновок

У цій роботі було:
- Вивчено основи роботи з `pip` — встановлення, видалення та перегляд бібліотек Python;
- Навчились створювати ізольовані віртуальні середовища за допомогою `venv`, `pipenv` та `poetry`;
- Ознайомились з бібліотеками `requests`, `jikanpy`, `Flask` та навчились їх використовувати;
- Створено `.gitignore` для ігнорування файлів віртуальних середовищ;
- Перевірено код за допомогою лінтера `flake8` — помилок не знайдено;
- Проведено перевірку безпеки залежностей за допомогою `pipenv check` — вразливостей не виявлено;
- Навчились працювати зі змінними середовища через файл `.env` та `pipenv`;
- Засвоєно використання `poetry` як альтернативного інструменту для управління Python-проектами;
- Мета роботи досягнута — вдалось створити, налаштувати та використати різні віртуальні середовища для ізоляції Python-проектів.
