# TODO: Failure test case 추가
# --------------------------------------------------------------------------
# Member의 testcase를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
import pytest_asyncio

from httpx import AsyncClient


async def _create_member(app_client: AsyncClient, name: str, email: str):
    """Helper function to create a member and return the id"""
    response = await app_client.post(
        "api/v1/member/", json={"name": name, "email": email}
    )
    return response.json()


class TestMemberAPI:
    @pytest_asyncio.fixture(autouse=True)
    async def setup(self, app_client: AsyncClient):
        self.test_user = await _create_member(
            app_client, "John Doe", "test@example.com"
        )

    async def test_create_member(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.post(
            "api/v1/member/",
            json={"name": "Test User", "email": "newuser@testmail.com"},
        )

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["name"] == "Test User"
        assert data["email"] == "newuser@testmail.com"

    async def test_read_member(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.get(f"api/v1/member/{self.test_user['id']}")

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["name"] == "John Doe"
        assert data["email"] == "test@example.com"

    async def test_read_members(self, app_client: AsyncClient):
        # given
        for i in range(10):
            await _create_member(
                app_client, f"Test User {i}", f"testmail{i}@example.com"
            )

        # when
        response = await app_client.get("api/v1/member/")

        # then
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 11

    async def test_read_members_with_skip_and_limit(self, app_client: AsyncClient):
        # given
        for i in range(10):
            await _create_member(
                app_client, f"Test User {i}", f"testmail{i}@example.com"
            )

        # when
        response = await app_client.get("api/v1/member/?skip=5&limit=5")
        response_2 = await app_client.get("api/v1/member/?limit=5")

        # then
        data = response.json()
        data_2 = response_2.json()
        assert response.status_code == 200
        assert len(data) == 5
        assert response_2.status_code == 200
        assert len(data_2) == 5
        assert data != data_2

    async def test_read_member_by_email(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.get("api/v1/member/email/test@example.com")

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["name"] == "John Doe"
        assert data["email"] == "test@example.com"

    async def test_update_member(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.put(
            f"api/v1/member/{self.test_user['id']}", json={"name": "Updated User Name"}
        )

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["name"] == "Updated User Name"
        assert data["email"] == "test@example.com"

    async def test_delete_member(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.delete(f"api/v1/member/{self.test_user['id']}")

        # then
        data = response.json()
        assert response.status_code == 200
        assert data == self.test_user["id"]
