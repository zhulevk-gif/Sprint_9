# Sprint_9: «Продуктовый помощник».


- Python 3.11
- Pytest
- Selenium WebDriver
- Allure Pytest
- Docker, Docker Compose
- Selenoid Chrome 128.0
- GitHub Actions

## Local run with installed Chrome

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest test --alluredir=allure-results
```

## Docker Compose run with Selenoid

```bash
docker pull selenoid/chrome:128.0
docker compose up --build --abort-on-container-exit --exit-code-from tests
```

## Allure report

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## CI report artifact
GitHub Actions runs the Docker Compose suite, generates `allure-report`, and uploads it as an artifact.
