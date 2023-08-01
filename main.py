from kivy.app import App
from kivy.uix.label import Label

class BasicApp(App):
    def build(self):
        label = Label(text="my app")
        return label
    

app = BasicApp()
app.run()