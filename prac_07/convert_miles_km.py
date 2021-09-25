from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        result = self.get_miles() * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesKmApp().run()
