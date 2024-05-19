import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def go_page(self, url):
        return self.driver.get(url)

    @allure.step('Ожидание переданного локатора')
    def find_element(self, locator, time=30):
        return WebDriverWait(
            self.driver, time
        ).until(
            expected_conditions.visibility_of_element_located(locator),
            message=f'Element not found'
        )

    @allure.step('Ожидание отсутствия локатора')
    def not_find_element(self, locator, time=30):
        return WebDriverWait(
            self.driver, time
        ).until(
            expected_conditions.none_of(
                expected_conditions.visibility_of_element_located(locator)
            ),
            message=f'Element was found'
        )

    @allure.step('Ожидаем url')
    def get_current_url(self, url, time=30):
        return WebDriverWait(self.driver, time).until(expected_conditions.url_to_be(url))

    @allure.step('Перетаскиваем элемент source в поле target')
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
