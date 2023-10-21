# --------------------------------------------------------------------------
# Member의 testcase를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
import unittest

from fastapi.testclient import TestClient

from helper import override_get_db, get_test_engine

from src import create_app
from src.db.database import get_db, Base
from src.core.settings import AppSettings


class TestMemberCreation(unittest.TestCase):
    def setUp(self):
        app_settings = AppSettings()
        self.app = create_app(app_settings)
        self.app.dependency_overrides[get_db] = override_get_db
        self.engine = get_test_engine()
        Base.metadata.create_all(bind=self.engine)
        self.client = TestClient(self.app)

    def create_member(self, name: str, email: str):
        """Helper function to create a member and return the id"""
        response = self.client.post(
            "api/v1/member/", json={"name": name, "email": email}
        )
        return response.json()["id"]

    def test_create_new_member(self):
        # given

        # when
        response = self.client.post(
            "api/v1/member/", json={"name": "John Doe", "email": "john.doe@example.com"}
        )

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "john.doe@example.com")

    def test_read_member(self):
        # given
        member_id = self.create_member("John Doe", "john.doe@example.com")

        # when
        response = self.client.get(f"api/v1/member/{member_id}")

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "john.doe@example.com")

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
