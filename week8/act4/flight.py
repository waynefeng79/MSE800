from datetime import datetime, timedelta

# ==================== BASE CLASSES ====================

class Flight:
    """Base class for all flights - Single Inheritance foundation"""
    
    def __init__(self, flight_id: str, departure_city: str, arrival_city: str, 
                 departure_time: str):
        self.flight_id = flight_id
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.status = "Scheduled"

    def get_flight_info(self) -> dict:
        """Get flight information"""
        return {
            "flight_id": self.flight_id,
            "departure": self.departure_city,
            "arrival": self.arrival_city,
            "departure_time": self.departure_time,
            "status": self.status
        }
    
    def update_status(self, new_status: str) -> None:
        """Update flight status"""
        valid_statuses = ["Scheduled", "Boarding", "Departed", "In-Flight", "Landed", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Flight {self.flight_id} status updated to: {new_status}")
        else:
            print(f"Invalid status: {new_status}")

class Crew:
    """Base class for flight crew - Mixin for Multiple Inheritance"""
    
    def __init__(self, crew_name: str, crew_size: int):
        self.crew_name = crew_name
        self.crew_size = crew_size
        self.crew_members = []
    
    def add_crew_member(self, member_name: str, position: str) -> None:
        """Add a crew member to the flight"""
        if len(self.crew_members) < self.crew_size:
            self.crew_members.append({"name": member_name, "position": position})
            print(f"Crew member {member_name} added as {position}")
        else:
            print(f"Crew is full. Cannot add more members.")
    
    def get_crew_info(self) -> dict:
        """Get crew information"""
        return {
            "crew_name": self.crew_name,
            "total_size": self.crew_size,
            "members": len(self.crew_members),
            "crew_members": self.crew_members
        }
    
    def check_crew_ready(self) -> bool:
        """Check if crew is ready for flight"""
        return len(self.crew_members) >= self.crew_size


# ==================== SINGLE INHERITANCE ====================

class DomesticFlight(Flight):
    """Domestic flight class - Single Inheritance from Flight"""
    
    def __init__(self, flight_id: str, departure_city: str, arrival_city: str, 
                 departure_time: str, meal_service: bool):
        super().__init__(flight_id, departure_city, arrival_city, departure_time)
        self.meal_service = meal_service
        self.baggage_allowance = 20  # kg
        self.flight_type = "Domestic"
    
    def calculate_fare(self, base_price: float) -> float:
        """Calculate domestic flight fare"""
        return base_price  # No additional taxes for domestic

    def add_baggage_allowance(self, weight_kg: int) -> bool:
        """Add baggage allowance for domestic flight"""
        if weight_kg <= self.baggage_allowance:
            print(f"Baggage of {weight_kg}kg allowed for domestic flight")
            return True
        else:
            print(f"Excess baggage. Additional charges apply.")
            return False
    
    def get_domestic_info(self) -> dict:
        """Get domestic flight specific information"""
        info = self.get_flight_info()
        info.update({
            "flight_type": self.flight_type,
            "meal_service": self.meal_service,
            "baggage_allowance": f"{self.baggage_allowance}kg"
        })
        return info


class InternationalFlight(Flight):
    """International flight class - Single Inheritance from Flight"""
    
    def __init__(self, flight_id: str, departure_city: str, arrival_city: str, 
                 departure_time: str, destination_country: str):
        super().__init__(flight_id, departure_city, arrival_city, departure_time)
        self.destination_country = destination_country
        self.baggage_allowance = 30  # kg
        self.flight_type = "International"
        self.visa_requirements = True
        self.customs_info = []

    def calculate_fare(self, base_price: float, tax_rate: float = 0.15) -> float:
        """Calculate international flight fare with taxes"""
        return base_price + (base_price * tax_rate)

    def add_customs_info(self, item: str, declaration_value: float) -> None:
        """Add customs declaration for international flight"""
        self.customs_info.append({"item": item, "value": declaration_value})
        print(f"Customs declaration added: {item} - ${declaration_value}")

    def get_international_info(self) -> dict:
        """Get international flight specific information"""
        info = self.get_flight_info()
        info.update({
            "flight_type": self.flight_type,
            "destination_country": self.destination_country,
            "baggage_allowance": f"{self.baggage_allowance}kg",
            "visa_required": self.visa_requirements,
            "customs_declarations": len(self.customs_info)
        })
        return info

# ==================== HYBRID INHERITANCE (MULTIPLE & MULTILEVEL) ====================

class ScheduledDomesticFlight(DomesticFlight, Crew):
    """Scheduled Domestic Flight - Multiple Inheritance (DomesticFlight + Crew)
    and Multilevel Inheritance (Flight -> DomesticFlight -> ScheduledDomesticFlight)
    This demonstrates HYBRID INHERITANCE"""
    
    def __init__(self, flight_id: str, departure_city: str, arrival_city: str, 
                 departure_time: str, meal_service: bool,
                 crew_name: str, crew_size: int, schedule_frequency: str):
        DomesticFlight.__init__(self, flight_id, departure_city, arrival_city, 
                                departure_time, meal_service)
        Crew.__init__(self, crew_name, crew_size)
        self.schedule_frequency = schedule_frequency
        self.scheduled_dates = []
    
    def schedule_flights(self, start_date: str, end_date: str) -> list:
        """Schedule recurring domestic flights"""
        scheduled = []
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        current = start
        while current <= end:
            scheduled.append(current.strftime("%Y-%m-%d"))
            if self.schedule_frequency == "Daily":
                current += timedelta(days=1)
            elif self.schedule_frequency == "Weekly":
                current += timedelta(days=7)
        
        self.scheduled_dates = scheduled
        return scheduled
    
    def get_combined_flight_details(self) -> dict:
        """Get combined flight and crew details - Hybrid approach"""
        details = {
            "flight_info": self.get_domestic_info(),
            "crew_info": self.get_crew_info(),
            "schedule_frequency": self.schedule_frequency,
            "total_scheduled": len(self.scheduled_dates)
        }
        return details
    
    def validate_flight_readiness(self) -> bool:
        """Validate if flight is ready for operation"""
        crew_ready = self.check_crew_ready()
        return crew_ready


class ScheduledInternationalFlight(InternationalFlight, Crew):
    """Scheduled International Flight - Multiple Inheritance (InternationalFlight + Crew)
    and Multilevel Inheritance (Flight -> InternationalFlight -> ScheduledInternationalFlight)
    This demonstrates HYBRID INHERITANCE"""
    
    def __init__(self, flight_id: str, departure_city: str, arrival_city: str, 
                 departure_time: str, destination_country: str,
                 crew_name: str, crew_size: int, flight_route: str):
        InternationalFlight.__init__(self, flight_id, departure_city, arrival_city, 
                                     departure_time, destination_country)
        Crew.__init__(self, crew_name, crew_size)
        self.flight_route = flight_route
        self.international_regulations = []

    def add_international_regulation(self, regulation: str) -> None:
        """Add international aviation regulation for this flight"""
        self.international_regulations.append(regulation)
        print(f"Regulation added: {regulation}")
    
    def get_combined_international_details(self) -> dict:
        """Get combined international flight and crew details"""
        details = {
            "flight_info": self.get_international_info(),
            "crew_info": self.get_crew_info(),
            "flight_route": self.flight_route,
            "regulations": self.international_regulations
        }
        return details
    
    def check_international_compliance(self) -> bool:
        """Check international flight compliance"""
        crew_ready = self.check_crew_ready()
        regulations_met = len(self.international_regulations) > 0
        return crew_ready and regulations_met

# ==================== MAIN EXECUTION ====================

def main():
    """Main function to demonstrate the flight management system"""

    # ========== DOMESTIC FLIGHTS ==========
    print("\n[1] Creating Domestic Flights...")
    domestic_flight1 = DomesticFlight(
        flight_id="DF001",
        departure_city="Auckland",
        arrival_city="Wellington",
        departure_time="10:00 AM",
        meal_service=True
    )
    
    # Test baggage allowance
    print("\nTesting baggage allowance:")
    domestic_flight1.add_baggage_allowance(15)

    # Calculate fare
    domestic_fare = domestic_flight1.calculate_fare(150.00)
    print(f"\nDomestic Flight Fare: ${domestic_fare}")

    # ========== INTERNATIONAL FLIGHTS ==========
    print("\n[2] Creating International Flights...")
    international_flight1 = InternationalFlight(
        flight_id="IF001",
        departure_city="Auckland",
        arrival_city="Sydney",
        departure_time="02:00 PM",
        destination_country="Australia"
    )
    
    # Add customs info
    international_flight1.add_customs_info("Laptop", 1500.00)
    international_flight1.add_customs_info("Jewelry", 500.00)

    # Calculate fare with tax
    international_fare = international_flight1.calculate_fare(300.00, 0.12)
    print(f"International Flight Fare (with 12% tax): ${international_fare}")
    
    # ========== HYBRID INHERITANCE - SCHEDULED DOMESTIC FLIGHT ==========
    print("\n[3] Creating Scheduled Domestic Flight (Hybrid Inheritance)...")
    scheduled_domestic = ScheduledDomesticFlight(
        flight_id="SDF001",
        departure_city="Christchurch",
        arrival_city="Dunedin",
        departure_time="09:00 AM",
        meal_service=True,
        crew_name="Crew A",
        crew_size=6,
        schedule_frequency="Daily"
    )
    
    # Add crew members
    scheduled_domestic.add_crew_member("Captain Sarah", "Pilot")
    scheduled_domestic.add_crew_member("First Officer Tom", "Co-Pilot")
    scheduled_domestic.add_crew_member("Emma Brown", "Flight Attendant")
    
    # Schedule flights
    scheduled_flights = scheduled_domestic.schedule_flights("2026-06-01", "2026-06-07")
    print(f"Scheduled flights for 7 days: {len(scheduled_flights)} flights")
    
    # Validate readiness
    is_ready = scheduled_domestic.validate_flight_readiness()
    print(f"Flight readiness: {is_ready}")
    
    # ========== HYBRID INHERITANCE - SCHEDULED INTERNATIONAL FLIGHT ==========
    print("\n[4] Creating Scheduled International Flight (Hybrid Inheritance)...")
    scheduled_international = ScheduledInternationalFlight(
        flight_id="SIF001",
        departure_city="Auckland",
        arrival_city="Los Angeles",
        departure_time="11:00 PM",
        destination_country="United States",
        crew_name="Crew International",
        crew_size=12,
        flight_route="South Pacific Route"
    )
    
    # Add crew members
    for i, pos in enumerate(["Pilot", "Co-Pilot", "Flight Attendant", "Flight Attendant", 
                             "Flight Attendant", "Flight Attendant", "Flight Attendant",
                             "Flight Attendant", "Purser", "Senior Flight Attendant", 
                             "Cargo Handler", "Communications Officer"], 1):
        scheduled_international.add_crew_member(f"Crew Member {i}", pos)

    # Add international regulations
    scheduled_international.add_international_regulation("ICAO Annex 6 - Operation of Aircraft")
    scheduled_international.add_international_regulation("Chicago Convention on Civil Aviation")
    scheduled_international.add_international_regulation("FAA International Flight Rules")
    
    # Add customs
    scheduled_international.add_customs_info("Camera Equipment", 2000.00)

    # Check compliance
    compliance = scheduled_international.check_international_compliance()
    print(f"International flight compliance: {compliance}")
    
    # ========== DETAILED INFORMATION ==========
    print("\n[6] Detailed Flight Information...")
    
    print("\n--- Domestic Flight Details ---")
    print(f"Flight Info: {domestic_flight1.get_domestic_info()}")
    
    print("\n--- International Flight Details ---")
    print(f"Flight Info: {international_flight1.get_international_info()}")
    
    print("\n--- Scheduled Domestic Flight (Hybrid) Details ---")
    hybrid_domestic_details = scheduled_domestic.get_combined_flight_details()
    for key, value in hybrid_domestic_details.items():
        print(f"{key}: {value}")
    
    print("\n--- Scheduled International Flight (Hybrid) Details ---")
    hybrid_international_details = scheduled_international.get_combined_international_details()
    for key, value in hybrid_international_details.items():
        print(f"{key}: {value}")
    
if __name__ == "__main__":
    main()
