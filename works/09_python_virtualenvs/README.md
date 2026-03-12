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

⭐ Переглянуто доступні команди `pip`:

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

⭐ Перевірено встановлені бібліотеки:

```
$ pip3 list
Package            Version
------------------ -----------
certifi            2026.2.25
charset-normalizer 3.4.5
idna               3.11
ipykernel          6.31.0
ipython            8.18.1
numpy              2.0.2
openpyxl           3.1.5
pandas             2.3.3
pillow             11.3.0
pip                21.2.4
pipenv             2025.0.4
requests           2.32.5
setuptools         82.0.1
...
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

⭐ Результат виконання команд демонструє, що бібліотека `requests` успішно працює — отримано відповідь зі статусом 200 від Google.

⭐ Додаткові методи бібліотеки requests: `requests.post()`, `requests.put()`, `requests.delete()`, `requests.head()`, `requests.patch()` — дозволяють виконувати різні HTTP-запити.

⭐ Перевірка інформації про бібліотеку та зміна версій:

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

⭐ Результат виконання програми:

```
Епізод 1 з назвою: The Lawless City має оцінку 4.49
Епізод 2 з назвою: The Haven має оцінку 4.48
Епізод 3 з назвою: The Hour of Awakening має оцінку 4.53
Епізод 4 з назвою: Mask of Falsehood має оцінку 4.34
Епізод 5 з назвою: He Who Pulls The Strings має оцінку 4.36
```

⭐ Аніме серіали поточного сезону (Winter 2026):

```
Sousou no Frieren 2nd Season - оцінка: 9.15
Jujutsu Kaisen: Shimetsu Kaiyuu - Zenpen - оцінка: 8.58
Jigokuraku 2nd Season - оцінка: 8.24
Yuusha-kei ni Shosu - оцінка: 8.17
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

⭐ Після `deactivate` команда `pip show requests` показує глобально встановлену бібліотеку, а не ту що була встановлена у `venv`. Це демонструє ізоляцію віртуального середовища — бібліотеки встановлені в `venv` доступні лише всередині нього.

⭐ Для `VENV` середовища потрібно ігнорувати наступні папки у `.gitignore`:

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
$ pipenv --venv
/Users/viktortsvyk/.local/share/virtualenvs/09_python_virtualenvs-LzUQ4qE6

$ pipenv run python -V
Python 3.9.6

$ pipenv install requests
```

⭐ Файл `Pipfile` містить опис залежностей проекту:

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

⭐ Дерево залежностей (`pipenv graph`):

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

⭐ Результат запуску через `pipenv run`:

```
$ pipenv run python requests_test.py
b'<!DOCTYPE html>'
b'<html lang="en">'
b'<head>'
b'    <meta charset="UTF-8">'
b'    <title>httpbin.org</title>'
...
```

Програма успішно виконується у віртуальному середовищі pipenv.

---

### 7. Перевірка коду за допомогою flake8

Встановлено `flake8` як dev-залежність:

```
$ pipenv install --dev flake8
```

⭐ Результат виконання `flake8`:

```
$ pipenv run flake8 --exclude=my_env .
(порожній вивід - помилок не знайдено)
```

Код написаний відповідно до стандартів PEP 8, тому `flake8` не знайшов жодних помилок.

---

### 8. Перевірка безпеки залежностей

⭐ Результат перевірки безпеки:

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

⭐ Результат запуску через `pipenv run`:

```
$ pipenv run python env_test.py
Loading .env environment variables...
Значення змінної IT_TEST = HelloWorld
```

⭐ Якщо виконати скрипт без активації віртуального середовища:

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
$ poetry new myproject
Created package myproject in myproject

$ cd myproject
$ poetry add requests
Installing requests (2.32.5)
```

⭐ Файл `pyproject.toml`:

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

⭐ Дерево залежностей poetry:

```
$ poetry show --tree
requests 2.32.5 Python HTTP for Humans.
├── certifi >=2017.4.17
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.21.1,<3
```

⭐ Інформація про середовище:

```
$ poetry env info
Virtualenv
Python:         3.9.6
Implementation: CPython
Path:           /Users/viktortsvyk/Library/Caches/pypoetry/virtualenvs/myproject-o1Fx34Hx-py3.9
Valid:          True
```

⭐ Створено та запущено програму `main.py` у Poetry середовищі:

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
Installing flake8 (7.3.0)
Installing pytest (8.4.2)
```

---

### 11. Допомога ChatGPT

За допомогою АІ створено Flask веб-додаток (`anime.py`) який використовує бібліотеку `jikanpy` для отримання даних про аніме та відображення їх на веб-сторінці. Додаток запускається через `pipenv run python anime.py` та доступний за адресою `http://127.0.0.1:5000/`.

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
