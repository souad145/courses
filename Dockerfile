# 1. Build Stage
FROM python:3.11-slim AS build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 2. Runtime Stage
FROM python:3.11-slim


WORKDIR /app

COPY --from=build /app /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
