from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    home = Component(xpath="//span[text()='Главное']")
    monitoring = Button(xpath="//span[text()='Мониторинг']")
    monitoring_lk = Button(xpath="//div[text()='Мониторинг работы ЛК']")


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
