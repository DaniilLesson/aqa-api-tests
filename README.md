# AQA API Tests (pytest + httpx + pydantic + allure)

[![Tests](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)

Учебный проект для портфолио AQA на Python: тестирование API-клиента на `httpx`, валидация данных через `pydantic`, отчёты `Allure`, запуск тестов в CI через GitHub Actions.

## What’s inside
- ✅ API client (`httpx.Client`) + context manager (`with ApiClient() as api`)
- ✅ Pydantic-модели для валидации ответов
- ✅ Unit-тесты (MockTransport) — не зависят от сети и всегда стабильны
- ✅ Negative-тесты (404/ошибки) + проверки `raise_for_status()`
- ✅ Allure-results генерация для отчётов
- ✅ CI: GitHub Actions (pytest on push / PR)

## Stack
- Python 3.12
- pytest
- httpx
- pydantic
- allure-pytest
- GitHub Actions

## Project structure
- `src/` — API client + models
  - `src/clients/reqres_client.py`
  - `src/models/user.py`
  - `src/config.py`
- `tests/` — unit/negative tests + fixtures
  - `tests/conftest.py`
  - `tests/test_users_unit.py`
  - `tests/test_users_negative.py`
- `.github/workflows/tests.yml` — CI workflow

## Setup (Windows)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
