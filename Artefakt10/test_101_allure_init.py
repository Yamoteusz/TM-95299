import allure
import pytest

@allure.epic("Blok 10")
@allure.feature("10.1: Inicjalizacja Allure")
def test_pass_example():
    with allure.step("Uruchomienie kroku PASS"):
        assert 1 == 1

@allure.epic("Blok 10")
@allure.feature("10.1: Inicjalizacja Allure")
def test_fail_example():
    with allure.step("Uruchomienie kroku FAIL"):
        assert 1 == 2, "To jest celowy fail do raportu Allure"