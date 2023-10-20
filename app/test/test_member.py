import unittest

from fastapi.testclient import TestClient
from src import create_app
from src.db.database import Base, engine
from src.core.settings import AppSettings


class TestMemberCreation(unittest.TestCase):

    def setUp(self):
        app_settings = AppSettings()
        self.app = create_app(app_settings)
        self.client = TestClient(self.app)

        Base.metadata.create_all(bind=engine)

    def test_create_new_member(self):
        response = self.client.post("api/v1/member/", json={"name": "John Doe", "email": "john.doe@example.com"})

        data = response.json()
        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")
        self.assertEqual(data["name"], "John Doe", f"Expected name 'John Doe' but got {data['name']}")
        self.assertEqual(data["email"], "john.doe@example.com",
                         f"Expected email 'john.doe@example.com' but got {data['email']}")

    # def test_read_member(self):
    #     # Assuming that the created member from the previous test has an ID of 1
    #     response = self.client.get("api/v1/member/1")
    #
    #     data = response.json()
    #     self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")
    #     self.assertEqual(data["name"], "John Doe", f"Expected name 'John Doe' but got {data['name']}")
    #     self.assertEqual(data["email"], "john.doe@example.com",
    #                      f"Expected email 'john.doe@example.com' but got {data['email']}")

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)