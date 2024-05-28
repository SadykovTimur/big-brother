from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Pages']


class PagesWrapper(ComponentWrapper):
    command = Component(xpath="//span[text()='Обновить показатели']")
    monitoring_lk = Component(css='[class="toplineBox"]')
    app_hour = Component(xpath="//label[text()='Нет заявок за последний час:']")
    app_bgu = Component(xpath="//label[text()='Нет заявок за последний час БГУ:']")
    app_zkgu = Component(xpath="//label[text()='Нет заявок за последний час ЗКГУ:']")
    app_lot = Component(xpath="//label[text()='Много заявок на регистрации:']")
    checkbox_hour = Component(css='[id*="НетЗаявокЗаПоследнийЧас_div"] [class="checkbox zoomI"]')
    image_hour = Component(css='[id*="ДекорацияНетЗаявокЗаПоследнийЧас_div"] img')
    checkbox_bgu = Component(css='[id*="НетЗаявокЗаПоследнийЧасБГУ_div"] [class="checkbox zoomI focus"]')
    image_bgu = Component(css='[id*="ДекорацияНетЗаявокЗаПоследнийЧасБГУ_div"] img')
    checkbox_zkgu = Component(css='[id*="НетЗаявокЗаПоследнийЧасЗКГУ_div"] [class="checkbox zoomI"]')
    image_zkgu = Component(css='[id*="ДекорацияНетЗаявокЗаПоследнийЧасЗКГУ_div"] img')
    checkbox_regist = Component(css='[id*="МногоЗаявокНаРегистрации_div"] [class="checkbox zoomI"]')
    image_regist = Component(css='[id*="ДекорацияМногоЗаявокНаРегистрации_div"] img')


class Pages(Component):
    def __get__(self, instance, owner) -> PagesWrapper:
        return PagesWrapper(instance.app, self.find(instance), self._locator)
