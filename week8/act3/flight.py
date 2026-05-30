class GeneralFlight:
    def __init__(self, no):
        self.no = no
        self.src = None
        self.dst = None
        self.depart_time = None
        self.arrival_time = None
        self.status = "Scheduled"

    def set_route(self, src, dst):
        self.src = src
        self.dst = dst
        return self

    def set_schedule(self, departure, arrival):
        self.depart_time = departure
        self.arrival_time = arrival
        return self

    def flight_duration(self):
        try:
            dep_date, dep_time = self.depart_time.split(" ")
            arr_date, arr_time = self.arrival_time.split(" ")
            from datetime import datetime
            fmt = "%Y-%m-%d %H:%M:%S"
            departure_dt = datetime.strptime(self.depart_time, fmt)
            arrival_dt = datetime.strptime(self.arrival_time, fmt)
            duration = arrival_dt - departure_dt
            return str(duration)
        except Exception:
            return "Unknown"
        
    def __str__(self):
        return (
            f"Flight NZ{self.no}: [{self.status}]"
        )

class DomesticFlight(GeneralFlight):
    def __init__(self, no, src, dst, departure, arrival, aircraft="ATR 72", terminal="Domestic"):
        super().__init__(no)
        self.set_route(src, dst)
        self.set_schedule(departure, arrival)

    def is_domestic(self):
        return True

    def summary(self):
        return (
            f"Domestic Flight NZ{self.no}: {self.src}->{self.dst}\n"
            f"Departure: {self.depart_time}\n"
            f"Arrival: {self.arrival_time}\n"
            f"Duration: {self.flight_duration()}"
        )


if __name__ == "__main__":
    flight = DomesticFlight(
        123,
        "Auckland",
        "Wellington",
        "2026-06-03 09:00:05",
        "2026-06-03 10:00:00",
        aircraft="Embraer 190",
    )
    print(flight)
    print(flight.summary())
