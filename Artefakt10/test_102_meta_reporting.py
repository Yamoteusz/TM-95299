import allure

@allure.epic("Epic: Platforma Edukacyjna Mobilna")
@allure.feature("Feature: Moduł Logiki")
@allure.story("Story: Przeglądanie listy lekcji")
def test_browse_lessons():
    allure.attach("Log: użytkownik otworzył listę lekcji", name="UI_Log", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Wejście do listy lekcji"):
        assert True

@allure.epic("Epic: Platforma Edukacyjna Mobilna")
@allure.feature("Feature: Moduł Kursów")
@allure.story("Story: Zakup kursu online")
def test_buy_course():
    allure.attach("Log: użytkownik przeszedł do zakupu kursu", name="Purchase_Log", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Otwarcie ekranu zakupu"):
        assert True