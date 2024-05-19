from selenium.webdriver.common.by import By


class RestorePageLocators:

    RESTORE_PASS_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    RESTORE_MAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    RESTORE_MAIL_FIELD_ACTIVE = (By.XPATH, ".//input[contains(@class,'text input') and @type='text']")
    SHOW_SIGN = (By.XPATH, ".//div[contains(@class,'input__icon')]")
