# Flask API

A simple Flask application with a welcome page, a health check, and JSON API routes. Each route includes sample data loaded from `data.json`.

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

- `/` - welcome message and sample data
- `/api` - API message and sample data
- `/health` - application health status and sample data
- `/api/message` - JSON message and sample data

## Run tests

Run the unit tests from the project root:

```bash
python -m unittest discover -s tests
```
