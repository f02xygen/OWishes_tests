import allure


@allure.title("Заглушка для теста UI")
def test_login(page):
    with allure.step("Открыть веб-страницу"):
        page.goto("http://localhost:3000")
