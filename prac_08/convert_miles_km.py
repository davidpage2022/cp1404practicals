"""GUI program to convert from miles to km."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmConverter(App):
    """Kivy App for converting miles to kilometres."""
    output_km_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Handle request for conversion.
        Takes input from miles input field and outputs to km label."""
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.output_km_text = f"{km:.3f}"

    def handle_increment(self, amount):
        """Handle request for miles input field to be increment/decremented by amount.
        Updates conversion to match the new value."""
        miles = self.get_valid_miles()
        miles += amount
        self.root.ids.input_miles.text = str(miles)

        # Update conversion.
        self.handle_convert()

    def get_valid_miles(self):
        """Get miles (as a decimal value) from user input field.
        If the value is invalid returns zero."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesToKmConverter().run()
