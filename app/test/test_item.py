# TODO: pytest로 변경, 비동기 테스트 케이스 configuration 정의 및 테스트케이스 수정
# --------------------------------------------------------------------------
# Item의 testcase를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
import unittest


class TestItemAPI(unittest.TestCase):
    def setUp(self):
        pass

    def create_item(self, name: str, price: int):
        pass

    def test_create_new_item(self):
        pass

    def test_read_item(self):
        pass

    def test_update_item(self):
        pass

    def test_delete_item(self):
        pass

    def tearDown(self):
        pass
