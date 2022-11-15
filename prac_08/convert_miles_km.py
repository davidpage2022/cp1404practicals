"""GUI program to convert between miles and km."""

from kivy.app import App
from kivy.lang import Builder


class MilesToKmConverter(App):
    def build(self):
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


if __name__ == '__main__':
    MilesToKmConverter().run()
