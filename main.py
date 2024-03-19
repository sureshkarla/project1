import time

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen


class MainWindow(MDScreen):
    pass


class RegisterPage(MDScreen):
    def open_menu(self, item):
        menu_list = [
            {
                "text": "Farmer",
                "on_release": lambda x="Farmer": self.farmeritem(x)
            },
            {
                "text": "Vendor",
                "on_release": lambda x="Vendor": self.vendoritem(x)
            },
        ]
        MDDropdownMenu(caller=item, items=menu_list).open()

    def farmeritem(self, text_item):
        self.ids.drop_text.text = text_item
        print(text_item)

    def vendoritem(self, text_item):
        self.ids.drop_text.text = text_item
        print(text_item)


class FarmerLoginPage(MDScreen):
    pass


class VendorLoginPage(MDScreen):
    pass


class WindowManage(MDScreenManager):
    pass


class FarmerApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Brown"
        # self.theme_cls.accent_palette = "Green"
        return Builder.load_file('C:\\Data\\Farmer\\main.kv')


if __name__ == '__main__':
    FarmerApp().run()
