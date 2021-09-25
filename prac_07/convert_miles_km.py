from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        result = self.convert_to_number() * MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def convert_to_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0

    def handle_increment(self, increment_size):
        result = self.convert_to_number() + increment_size
        self.root.ids.input_number.text = str(result)


ConvertMilesApp().run()
