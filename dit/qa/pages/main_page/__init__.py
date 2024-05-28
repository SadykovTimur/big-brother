from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.component.header import Header
from dit.qa.pages.main_page.component.menu import Menu
from dit.qa.pages.main_page.component.page import Pages

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(id="captionbar")
    menu = Menu(id="themesCell")
    page = Pages(id="pages")
    exit = Button(css='[class*="pressDefault"]')
    log_btn = Button(id="LogoutCloseButton")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible

                assert self.menu.home.visible

                return self.menu.monitoring.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_monitoring(self) -> None:
        def condition() -> bool:
            try:
                assert self.page.command.visible
                assert self.page.monitoring_lk.visible
                assert self.page.app_hour.visible
                assert self.page.app_bgu.visible
                assert self.page.app_zkgu.visible
                assert self.page.app_lot.visible
                assert self.page.checkbox_hour.visible
                assert self.page.image_hour.visible
                assert self.page.checkbox_bgu.visible
                assert self.page.image_bgu.visible
                assert self.page.checkbox_zkgu.visible
                assert self.page.image_zkgu.visible
                assert self.page.checkbox_regist.visible

                return self.page.image_regist.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
