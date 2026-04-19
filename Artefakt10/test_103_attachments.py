import allure
import pytest

@allure.epic("Blok 10")
@allure.feature("10.3: Failure Attachments")
@allure.story("Test z załącznikami przy błędzie")
def test_failure_with_attachments():
    with allure.step("Przygotowanie symulowanego screenshotu"):
        fake_png = b"\x89PNG\r\n\x1a\nFAKEPNGDATA"
        allure.attach(
            fake_png,
            name="Screenshot_Error_01",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Dołączenie odpowiedzi API"):
        fake_api_response = '{"status":500,"message":"Internal Server Error"}'
        allure.attach(
            fake_api_response,
            name="API_Response",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Celowe wywołanie błędu"):
        assert False, "Symulowany błąd testu dla raportu Allure"