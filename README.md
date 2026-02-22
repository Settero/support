# Support Telemetry Demo

Простой проект из 3 сервисов:
- `backend` (FastAPI, порт `5000`)
- `sensor` (эмулятор, отправляет телеметрию в backend)
- `frontend` (Nginx + HTML, порт `8080`)

## 1. Требования

На Windows:
- Docker Desktop

На Linux:
- Docker Engine
- Docker Compose plugin (`docker compose`)

Проверка:

```bash
docker --version
docker compose version
```

## 2. Запуск проекта

Перейдите в корень проекта (где лежит `docker-compose.yml`) и выполните:

```bash
docker compose up --build
```

Для запуска в фоне:

```bash
docker compose up --build -d
```

## 3. Доступ к приложению

С этого же устройства:
- Frontend: `http://localhost:8080`
- Backend API: `http://localhost:5000/api/latest`

С другого устройства в той же сети:
- `http://<IP_хоста>:8080`

Пример: `http://192.168.1.25:8080`

## 4. Полезные команды

Логи всех сервисов:

```bash
docker compose logs -f
```

Логи конкретного сервиса:

```bash
docker compose logs -f backend
docker compose logs -f sensor
docker compose logs -f frontend
```

Остановка:

```bash
docker compose down
```

Остановка с удалением томов/сети проекта:

```bash
docker compose down -v
```

## 5. Структура проекта

```text
backend/            # FastAPI приложение
emulator/           # эмулятор датчика
frontend/           # статический frontend (Nginx)
docker-compose.yml  # оркестрация сервисов
```

## 6. Разработка
1. Backend:
Перейдите в папку backend:
```bash
cd backend
```
Установите вирт. окружение (Windows):
```bash
python -m venv venv
```
Активируйте его и установите зависимости:
```bash
source venv/scripts/activate
pip install -r requirements.txt
```
2. Emulator:
Перейдите в папку emulator:
```bash
cd emulator
```
Установите вирт. окружение (Windows):
```bash
python -m venv venv
```
Активируйте его и установите зависимости:
```bash
source venv/scripts/activate
pip install -r requirements.txt
```
