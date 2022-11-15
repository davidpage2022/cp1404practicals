"""Exercise for creating dynamic GUI labels."""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App to create dynamic GUI labels."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob", "Jane", "John", "Doe", "Larry", "Andy", "Mo"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Dynamically generates labels based on list of names given on construction."""
        for name in self.names:
            label = Label(text=name)
            # self.root.add_widget(label)  # For adding directly to root widget.
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()