from selenium.webdriver.common.by import By

class StartPageLocators():
    LOGIN_BUTTON = (By.ID, "com.ajaxsystems:id/login")
    REGISTER_BUTTON = (By.ID, "com.ajaxsystems:id/registration")

class LoginPageLocators():
    EMAIL_FIELD = (By.ID, "com.ajaxsystems:id/login")
    PASSWORD_FIELD = (By.ID, "com.ajaxsystems:id/password")
    FORGOT_PASSWORD_BUTTOM = (By.ID, "com.ajaxsystems:id/forgot")
    LOGIN_BUTTON = (By.ID, "com.ajaxsystems:id/next")

class MainPageLocators():
    MAIN_DISPLAY = (By.ID, "com.ajaxsystems:id/loading")
    CHECK_LATER_BUTTON = (By.ID, "com.ajaxsystems:id/cancel_button")
    MENU_ICON = (By.ID, "com.ajaxsystems:id/menuDrawer")
    ADD_HUB_ITEM = (By.ID, "com.ajaxsystems:id/addHub")
    HUB_PAGE = (By.ID, "com.ajaxsystems:id/include")
    SETTINGS_ITEM = (By.ID, "com.ajaxsystems:id/settings")
    SETTINGS_PAGE = (By.ID, "com.ajaxsystems:id/items")
    HELP_ITEM = (By.ID, "com.ajaxsystems:id/help")
    HELP_PAGE = (By.ID, "com.ajaxsystems:id/web")
    LOGS_ITEM = (By.ID, "com.ajaxsystems:id/logs")
    LOGS_PAGE = (By.ID, "com.ajaxsystems:id/content")

