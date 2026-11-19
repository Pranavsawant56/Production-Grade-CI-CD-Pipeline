import json
import unittest
from pathlib import Path

from app import app


class FlaskApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_file = Path(__file__).resolve().parents[1] / "data.json"
        with data_file.open(encoding="utf-8") as file:
            cls.expected_data = json.load(file)

    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_welcome_message_and_data(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertEqual(
            response.get_json(),
            {
                "message": "Welcome to the Flask API!",
                "data": self.expected_data,
            },
        )

    def test_health_returns_status_and_data(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertEqual(
            response.get_json(),
            {"status": "healthy", "data": self.expected_data},
        )

    def test_message_returns_json_message_and_data(self):
        response = self.client.get("/api/message")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertEqual(
            response.get_json(),
            {
                "message": "Hello from the Flask API!",
                "data": self.expected_data,
            },
        )


if __name__ == "__main__":
    unittest.main()
