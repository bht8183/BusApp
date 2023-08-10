from kivy.garden.mapview import MapView

class AppMapView(MapView):
    def build(self):
        mapView = MapView(
            lat = 33.5,
            lon = 84.4,
            zoom = 19
            )
        mapView.zoom = 10
        return mapView

