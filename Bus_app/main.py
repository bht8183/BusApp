from kivy.uix.label import Label
from kivymd.app import MDApp
from AppMapView import AppMapView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.button import Button


class MainApp(MDApp):
    def build(self):
        theGrid = GridLayout(
            cols = 2,
            rows = 1
        )
        map = MapView(
            lat = 10,
            lon = 10,
            zoom = 5
        )
        m1 = MapMarker(lat=10, lon=10, source = 'imag.JPG')

        map.add_marker(m1)

        button1 = Button( text = 'hi' )

        theGrid.add_widget(map)
        theGrid.add_widget(button1)


        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return theGrid
    

MainApp().run()