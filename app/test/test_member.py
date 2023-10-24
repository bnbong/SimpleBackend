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


class TestMemberAPI(unittest.TestCase):
    def setUp(self):
        app_settings = AppSettings()
        self.app = create_app(app_settings)
        self.app.dependency_overrides[get_db] = override_get_db
        self.engine = get_test_engine()
        Base.metadata.create_all(bind=self.engine)
        self.client = TestClient(self.app)

        self.test_member = self.create_member("John Doe", "john.doe@example.com")

    def create_member(self, name: str, email: str):
        """Helper function to create a member and return the id"""
        response = self.client.post(
            "api/v1/member/", json={"name": name, "email": email}
        )
        return response.json()

    def test_create_new_member(self):
        # given

        # when
        response = self.client.post(
            "api/v1/member/", json={"name": "Test User", "email": "testmail@example.com"}
        )

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Test User")
        self.assertEqual(data["email"], "testmail@example.com")

    def test_read_member(self):
        # given
        test_member_id = self.test_member["id"]

        # when
        response = self.client.get(f"api/v1/member/{test_member_id}")

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "john.doe@example.com")

    def test_read_member_by_email(self):
        # given
        test_member_email = self.test_member["email"]

        # when
        response = self.client.get(f"api/v1/member/email/{test_member_email}")

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "john.doe@example.com")

    def test_read_members(self):
        # given
        self.create_member("Test User 1", "test1@testmail.com")
        self.create_member("Test User 2", "test2@testmail.com")

        # when
        response = self.client.get("api/v1/member/")

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 3)

    def test_read_members_with_skip_and_limit(self):
        # given
        for i in range(10):
            self.create_member(f"Test User {i}", f"test{i}@testmail.com")

        # when
        response = self.client.get("api/v1/member/?skip=5&limit=5")
        response_2 = self.client.get("api/v1/member/?limit=5")

        # then
        data = response.json()
        data_2 = response_2.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(len(data_2), 5)

    def test_update_existing_member(self):
        # given
        test_member_id = self.test_member["id"]

        # when
        response = self.client.put(
            f"api/v1/member/{test_member_id}", json={"name": "Updated User Name"})

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Updated User Name")
        self.assertEqual(data["email"], "john.doe@example.com")

    def test_delete_member(self):
        # given
        test_member_id = self.test_member["id"]

        # when
        response = self.client.delete(f"api/v1/member/{test_member_id}")

        # then
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, test_member_id)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
