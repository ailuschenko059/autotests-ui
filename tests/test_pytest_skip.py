import pytest








@pytest.mark.skip(reason='Фича в Разработке')
def test_feature_in_development():
    ...

class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_developmen_2(self):
        ...