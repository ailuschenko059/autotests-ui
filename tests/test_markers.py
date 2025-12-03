import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_resr(self):
        ...

    def test__logout(self):
        ...


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...


@pytest.mark.ui
class TestUserInterface():
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_buttnon(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_sgnup_form(self):
        pass