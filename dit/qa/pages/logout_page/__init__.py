from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

__all__ = ['LogoutPage']


class LogoutPage(Page):
    title = Component(xpath="//div[text()='До новых встреч!']")
    exit_title = Component(id="exitConfTitle")
    come = Component(css='[class*="exitPress"]')
    logo = Component(class_name="exitImg")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.exit_title.visible
                assert self.come.visible

                return self.logo.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
