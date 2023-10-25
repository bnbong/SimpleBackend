# --------------------------------------------------------------------------
# TimeTable의 testcase를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
import pytest_asyncio

from httpx import AsyncClient

from test.test_member import _create_member


async def _create_timetable(
    app_client: AsyncClient, index: str, owner_id: int, start_date: str, end_date: str
):
    """Helper function to create a timetable and return the id"""
    response = await app_client.post(
        "api/v1/timetable/",
        json={
            "index": index,
            "owner_id": owner_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )
    return response.json()


class TestTimeTableAPI:
    @pytest_asyncio.fixture(autouse=True)
    async def setup(self, app_client: AsyncClient):
        self.test_user = await _create_member(
            app_client, "John Doe", "test@testmail.com"
        )
        self.test_timetable = await _create_timetable(
            app_client,
            "Test Timetable",
            self.test_user["id"],
            "2021-01-01",
            "2021-01-31",
        )

    async def test_create_timetable(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.post(
            "api/v1/timetable/",
            json={
                "index": "Test Timetable",
                "owner_id": self.test_user["id"],
                "start_date": "2021-01-01",
                "end_date": "2021-01-31",
            },
        )

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["index"] == "Test Timetable"
        assert data["owner_id"] == self.test_user["id"]
        assert data["start_date"] == "2021-01-01"
        assert data["end_date"] == "2021-01-31"

    async def test_read_timetable(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.get(f"api/v1/timetable/{self.test_timetable['id']}")

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["index"] == "Test Timetable"
        assert data["owner_id"] == self.test_user["id"]
        assert data["start_date"] == "2021-01-01"
        assert data["end_date"] == "2021-01-31"

    async def test_read_timetables(self, app_client: AsyncClient):
        # given
        for i in range(10):
            await _create_timetable(
                app_client,
                f"Test Timetable {i}",
                self.test_user["id"],
                "2023-02-10",
                "2023-02-11",
            )

        # when
        response = await app_client.get(f"api/v1/timetable/")

        # then
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 11

    async def test_update_timetable(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.put(
            f"api/v1/timetable/{self.test_timetable['id']}",
            json={
                "index": "Modified Timetable",
                "start_date": "2021-01-01",
                "end_date": "2021-02-10",
            },
        )

        # then
        data = response.json()
        assert response.status_code == 200
        assert data["index"] == "Modified Timetable"
        assert data["owner_id"] == self.test_user["id"]
        assert data["start_date"] == "2021-01-01"
        assert data["end_date"] == "2021-02-10"

    async def test_delete_timetable(self, app_client: AsyncClient):
        # given

        # when
        response = await app_client.delete(
            f"api/v1/timetable/{self.test_timetable['id']}"
        )

        # then
        data = response.json()
        assert response.status_code == 200
        assert data == self.test_timetable["id"]
