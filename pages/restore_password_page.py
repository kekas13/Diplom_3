import allure
from pages.base_page import BasePage
from locators.restore_page_locators import RestorePageLocators


class RestorePasswordPage(BasePage):

    @allure.step('Нажимаем кнопку Восстановить пароль')
    def click_restore_password(self):
        return self.find_element(RestorePageLocators.RESTORE_PASS_LINK).click()

    @allure.step('Нажимаем кнопку Восстановить')
    def click_restore_button(self):
        return self.find_element(RestorePageLocators.RESTORE_BUTTON).click()

    @allure.step('Нажимаем кнопку показать/скрыть пароль')
    def click_password_show_sign(self):
        return self.find_element(RestorePageLocators.SHOW_SIGN).click()

    @allure.step('Заполняем поле Email')
    def set_email(self, email):
        return self.find_element(RestorePageLocators.RESTORE_MAIL_FIELD).send_keys(email)
