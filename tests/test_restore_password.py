import allure
from pages.restore_password_page import RestorePasswordPage
from locators.restore_page_locators import RestorePageLocators
from data import Data
from urls import Urls


class TestRestorePassword:

    @allure.title('Проверяем, что клик по кнопке «Восстановить пароль» переводит на страницу запроса восстановления пароля')
    @allure.description('Открываем страницу логина, кликаем на кнопку «Восстановить пароль», '
                        'ожидаем переход на страницу восстановления пароля')
    def test_transfer_from_restore_button_to_restore_page(self, driver):
        restore_page = RestorePasswordPage(driver)
        restore_page.go_page(Urls.LOGIN_PAGE)
        restore_page.click_restore_password()
        assert restore_page.get_current_url(Urls.PASSWORD_RESTORE_PAGE), 'нет перехода на страницу восстановления пароля'

    @allure.title('Проверяем, что ввод почты и клик по кнопке «Восстановить» переводит на страницу восстановления пароля')
    @allure.description('На странице восстановления пароля вводим почту в окно Email и нажимаем кнопку «Восстановить», '
                        'ожидаем переход на страницу сброса пароля')
    def test_input_email_click_restore_button(self, driver):
        restore_page = RestorePasswordPage(driver)
        restore_page.go_page(Urls.PASSWORD_RESTORE_PAGE)
        restore_page.set_email(Data.EMAIL)
        restore_page.click_restore_button()
        assert restore_page.get_current_url(Urls.RESET_PASSWORD_PAGE), 'нет перехода на страницу сброса пароля'

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    @allure.description('На странице восстановления пароля вводим почту в окно Email и нажимаем кнопку «Восстановить», '
                        'переходим на страницу сброса пароля, нажимаем на кнопку показать пароль,'
                        'ожидаем, что поле пароль становится активным')
    def test_show_hide_password_on_restore_page(self, driver):
        restore_page = RestorePasswordPage(driver)
        restore_page.go_page(Urls.PASSWORD_RESTORE_PAGE)
        restore_page.set_email(Data.EMAIL)
        restore_page.click_restore_button()
        restore_page.get_current_url(Urls.RESET_PASSWORD_PAGE)
        restore_page.click_password_show_sign()
        assert restore_page.find_element(
            RestorePageLocators.RESTORE_MAIL_FIELD_ACTIVE), 'поле пароль не становится активным'
