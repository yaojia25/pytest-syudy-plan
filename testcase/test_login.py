import pytest


class Testlogin():
    @pytest.mark.smoke
    def test_01_baili(self):
        print("百里守约")


if __name__ == '__main__':
    pytest.main()
