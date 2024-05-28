from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Component(id="captionbarTitle")
    logo = Component(id="captionbarLogo")
    menu = Component(id="captionbarFunction")
    title1c = Component(id="captionbar1C")
    field = Component(id="captionbarField")
    notification = Component(id="captionbarNotifications")
    history = Component(id="captionbarHistory")
    favorite = Component(id="captionbarFavorite")
    logout = Button(id="LogoutButton")
    more_menu = Component(id="captionbarMore")

    @property
    def is_visible(self) -> bool:
        assert self.title.visible
        assert self.logo.visible
        assert self.menu.visible
        assert self.title1c.visible
        assert self.field.visible
        assert self.notification.visible
        assert self.history.visible
        assert self.favorite.visible
        assert self.more_menu.visible

        return self.logout.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
