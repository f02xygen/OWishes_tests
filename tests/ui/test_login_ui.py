import allure


@allure.story("UI")
@allure.title("Заглушка для теста UI")
def test_login(page):
    with allure.step("Открыть веб-страницу"):
        page.goto("http://localhost:3000")
