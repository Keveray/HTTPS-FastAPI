# HTTPS FastAPI

Простой веб-сайт на Python с использованием FastAPI и HTTPS.

На главной странице отображается изображение персонажа Arc Warden из Dota 2 и небольшая подпись.

## Используемые технологии

- Python
- FastAPI
- Uvicorn
- OpenSSL
- HTML

## Структура проекта

```text
HTTPS FastAPI/
├── src/
│   ├── main.py
│   ├── cert.pem
│   └── key.pem
├── venv/
└── README.md
```

## Установка и запуск

### 1. Создание виртуального окружения

```powershell
python -m venv venv
```

Активация в PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Установка зависимостей

```powershell
pip install fastapi uvicorn
```

### 3. Создание SSL-сертификата

Перейдите в папку `src`:

```powershell
cd src
```

Создайте самоподписанный сертификат с помощью OpenSSL:

```powershell
openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365 -subj "/CN=localhost" -config NUL
```

### 4. Запуск сервера

```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8443 --ssl-keyfile key.pem --ssl-certfile cert.pem
```

### 5. Открытие сайта

После запуска перейдите по адресу:

**https://localhost:8443**

При первом открытии браузер может показать предупреждение о безопасности, поскольку используется самоподписанный SSL-сертификат.

## Описание работы

Приложение использует FastAPI для обработки HTTP-запросов.

При обращении к главной странице `/` сервер возвращает HTML-документ, содержащий изображение Arc Warden и текстовую подпись.

HTTPS обеспечивает шифрование соединения с помощью TLS-сертификата.

## Примечание

Проект предназначен для локального запуска и демонстрации работы HTTPS в FastAPI. Изображение загружается из внешнего источника.

Файлы `key.pem`, `cert.pem` и папку `venv` не следует добавлять в Git. Для публичного размещения необходимо использовать доверенный TLS-сертификат.