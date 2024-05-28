import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.logout_page import LogoutPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'open_tab_monitoring',
    'check_checkbox_app_hour',
    'logout',
    'check_checkbox_app_hour_bgu',
    'check_checkbox_app_hour_zkgu',
    'check_checkbox_app_lot_registration',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def open_tab_monitoring(app: Application) -> None:
    with allure.step('Opening Tab monitoring page'):
        try:
            page = MainPage(app)
            page.menu.monitoring.click()
            page.menu.monitoring_lk.click()

            page.wait_for_loading_monitoring()

            screenshot_attach(app, 'tab_monitoring_page')
        except Exception as e:
            screenshot_attach(app, 'tab_monitoring_page_error')

            raise TimeoutError('Tab monitoring page was not loaded') from e


def check_checkbox_app_hour(app: Application) -> None:
    with allure.step('Checking Checkbox app hour'):
        try:
            page = MainPage(app).page

            assert "select" not in page.checkbox_hour.webelement.get_attribute("class")
            assert "0_85998f14-805b-4e2b-ba19-9d79b0464042" in page.image_hour.webelement.get_attribute("src")

            screenshot_attach(app, 'checkbox_app_hour')
        except Exception as e:
            screenshot_attach(app, 'checkbox_app_hour_error')

            raise AssertionError('Checkbox app hour is selected') from e


def check_checkbox_app_hour_bgu(app: Application) -> None:
    with allure.step('Checking Checkbox app hour bgu'):
        try:
            page = MainPage(app).page

            assert "select" not in page.checkbox_bgu.webelement.get_attribute("class")
            assert "0_85998f14-805b-4e2b-ba19-9d79b0464042" in page.image_bgu.webelement.get_attribute("src")

            screenshot_attach(app, 'checkbox_app_hour_bgu')
        except Exception as e:
            screenshot_attach(app, 'checkbox_app_hour_bgu_error')

            raise AssertionError('Checkbox app hour bgu is selected') from e


def check_checkbox_app_hour_zkgu(app: Application) -> None:
    with allure.step('Checking Checkbox app hour zkgu'):
        try:
            page = MainPage(app).page

            assert "select" not in page.checkbox_zkgu.webelement.get_attribute("class")
            assert "0_85998f14-805b-4e2b-ba19-9d79b0464042" in page.image_zkgu.webelement.get_attribute("src")

            screenshot_attach(app, 'checkbox_app_hour_zkgu')
        except Exception as e:
            screenshot_attach(app, 'checkbox_app_hour_zkgu_error')

            raise AssertionError('Checkbox app hour zkgu is selected') from e


def check_checkbox_app_lot_registration(app: Application) -> None:
    with allure.step('Checking Checkbox app lot registration'):
        try:
            page = MainPage(app).page

            assert "select" not in page.checkbox_regist.webelement.get_attribute("class")
            assert "0_85998f14-805b-4e2b-ba19-9d79b0464042" in page.image_regist.webelement.get_attribute("src")

            screenshot_attach(app, 'checkbox_app_lot_registration')
        except Exception as e:
            screenshot_attach(app, 'checkbox_app_hour_lot_registration')

            raise AssertionError('Checkbox app lot registration is selected') from e


def logout(app: Application) -> None:
    with allure.step('Logout page'):
        try:
            main_page = MainPage(app)
            main_page.header.logout.click()
            main_page.log_btn.click()
            main_page.exit.click()

            LogoutPage(app).wait_for_loading()

            screenshot_attach(app, 'logout_page')
        except Exception as e:
            screenshot_attach(app, 'logout_page_error')

            raise TimeoutError('Logout was not loaded') from e
