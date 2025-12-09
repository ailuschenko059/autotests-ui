from _pytest.fixtures import SubRequest

import pytest




@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0
    print(f'number: {number}')

@pytest.mark.parametrize('number, expected', [(1,1), (2,4), (3,9)])
def test_seceral_numbers_1(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit card', 'Debit Card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'user_with_operations:{user}')


    def test_user_without_operations(self, user: str):
        print(f'user_without_operations:{user}')


users = {
    '+78928282822': 'User with money on banl account',
    '+89382928782': 'User withouy money on banl account',
    '+99382928782': 'User with operations on banl account'
}

@pytest.mark.parametrize('phone_number', users.keys(), ids=lambda phone_number: f'{phone_number}: {users[phone_number]}')
def test_identifires(phone_number: str):
    ...

@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [4, 5])
def test_multiplication(x, y):
    assert x * y