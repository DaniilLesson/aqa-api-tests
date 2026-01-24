# AQA API Tests — портфолио автотестера

[![Tests](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)


Коротко: небольшой, но аккуратный проект, который показывает подход к тестированию REST API.  
Основной фокус — структура клиента, тестовая матрица (позитив/негатив), контрактная валидация и стабильные unit-тесты без сети.
 
> Тестовые сценарии, проверки и логика тестов (MockTransport, негативные кейсы, валидация схемы) — выбраны и реализованы мной.


## Что здесь демонстрируется
- API-клиент на `httpx` с управлением таймаутом и контекстным менеджером
- Валидация контракта ответа через Pydantic (модели совпадают с `reqres.in`)
- Unit-тесты через `MockTransport` — без интернета, быстро и стабильно
- Негативные кейсы: 404 и некорректная схема данных
- Генерация Allure-результатов
- CI: запуск `pytest` на push/PR

## Стек
- Python 3.12
- pytest
- httpx
- pydantic
- allure-pytest
- GitHub Actions

## Структура проекта
- `src/` — API-клиент + модели
  - `src/clients/reqres_client.py`
  - `src/models/user.py`
  - `src/config.py`
- `tests/` — unit/negative тесты + фикстуры
  - `tests/conftest.py`
  - `tests/test_users_unit.py`
  - `tests/test_users_negative.py`
- `.github/workflows/tests.yml` — CI workflow

## Быстрый старт (Windows)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pytest -q
```

## Быстрый старт (macOS/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pytest -q
```

## Allure отчёты
```bash
pytest --alluredir=allure-results
allure serve allure-results
```