"""GUI program to convert from miles to km."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmConverter(App):
    output_km_text = StringProperty()

    def build(self):
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        miles = float(self.root.ids.input_miles.text)
        km = miles * MILES_TO_KM
        self.output_km_text = f"{km:.3f}"


if __name__ == '__main__':
    MilesToKmConverter().run()
