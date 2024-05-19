import allure
from pages.personal_area_page import PersonalAreaPage


class TestPersonalArea:

    @allure.title('Проверяем переход по клику в личный кабинет')
    @allure.description('Открываем страницу логина, логинимся, нажимаем кнопку "Войти", нажимаем кнопку "личный кабинет", '
                        'проверяем, что попали в личный кабинет')
    def test_transfer_to_personal_area_by_click(self, login):
        login_page = PersonalAreaPage(login)
        login_page.click_personal_area_button()
        assert login_page.find_profile(), 'нет перехода в профиль'

    @allure.title('Проверяем переход в раздел История заказов')
    @allure.description('Открываем страницу логина, логинимся, нажимаем кнопку Войти, нажимаем кнопку "личный кабинет", '
                        'нажимаем кнопку "история заказов", проверяем, что открывается окно истории заказов')
    def test_transfer_to_order_history(self, login):
        login_page = PersonalAreaPage(login)
        login_page.click_personal_area_button()
        login_page.click_order_history_button()
        assert login_page.find_order_history(), 'не открывается окно истории заказов'

    @allure.title('Проверяем выход из аккаунта')
    @allure.description('Открываем страницу логина, логинимся, нажимаем кнопку Войти, нажимаем кнопку "личный кабинет", '
                        'нажимаем кнопку "выход", проверяем, что вышли из аккаунта, появляется кнопка "Войти')
    def test_exit_button(self, login):
        login_page = PersonalAreaPage(login)
        login_page.click_personal_area_button()
        login_page.click_exit_button()
        assert login_page.find_enter_button(), 'не появляется кнопка "Войти"'

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    @allure.description('Открываем страницу логина, логинимся, ожидаем, '
                        'что на главной странице есть кнопка "Оформить заказ"')
    def test_login_user_can_make_order(self, login):
        login_page = PersonalAreaPage(login)
        assert login_page.find_make_order_button(), 'не найдена кнопка "Оформить заказ"'
