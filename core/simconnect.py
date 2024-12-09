from pysimconnect import SimConnect, AircraftRequests

class SimConnectManager:
    def __init__(self):
        self.sm = None
        self.aq = None

    def connect(self):
        try:
            self.sm = SimConnect()
            self.aq = AircraftRequests(self.sm, _time=2000)
            print("Connected to Microsoft Flight Simulator.")
        except Exception as e:
            print(f"Error connecting to MSFS: {e}")

    def reposition_aircraft(self, latitude, longitude, altitude, heading, airspeed):
        if not self.aq:
            print("Error: Not connected to MSFS.")
            return

        try:
            self.aq.set("PLANE_LATITUDE", float(latitude))
            self.aq.set("PLANE_LONGITUDE", float(longitude))
            self.aq.set("PLANE_ALTITUDE", float(altitude))
            self.aq.set("PLANE_HEADING_DEGREES_TRUE", float(heading))
            self.aq.set("AIRSPEED_TRUE", float(airspeed))
            print(f"Aircraft repositioned to ({latitude}, {longitude}) at {altitude} feet, heading {heading}°, airspeed {airspeed} knots.")
        except Exception as e:
            print(f"Error repositioning aircraft: {e}")

    def disconnect(self):
        if self.sm:
            self.sm.quit()
            print("Disconnected from Microsoft Flight Simulator.")
