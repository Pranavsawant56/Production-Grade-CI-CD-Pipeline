# Flask API

A simple Flask application with a welcome page, a health check, and a JSON API route.

## Install dependencies

Make sure Python and pip are installed, then run:

```bash
python -m pip install -r requirements.txt
```

## Run locally

```bash
python app.py
```

The application runs at <http://127.0.0.1:5000>.

Available routes:

- `/` - welcome message
- `/health` - application health status
- `/api/message` - JSON message
