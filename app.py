#!/usr/bin/env python3

import json
import os
import random
import string
from datetime import datetime, timedelta

FLIGHTS_FILE = "flights.json"
BOOKINGS_FILE = "bookings.json"


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def generate_pnr():
    """Generate a 6-character alphanumeric PNR."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def calculate_duration(departure, arrival):
    dep_hour, dep_min = map(int, departure.split(":"))
    arr_hour, arr_min = map(int, arrival.split(":"))
    dep_total = dep_hour * 60 + dep_min
    arr_total = arr_hour * 60 + arr_min

    if arr_total < dep_total:
        arr_total += 24 * 60

    duration = arr_total - dep_total
    return f"{duration // 60}h {duration % 60}m"



flights = load_data(FLIGHTS_FILE)
bookings = load_data(BOOKINGS_FILE)


last_search = []


if not flights:
    today = datetime.today().date()
    flights = [
        {
            "id": 1,
            "airline": "IndiGo",
            "source": "New Delhi",
            "destination": "London",
            "date": str(today + timedelta(days=2)),
            "departure_time": "09:00",
            "arrival_time": "13:00",
            "seats": 12,
            "price": 55000
        },
        {
            "id": 2,
            "airline": "Emirates",
            "source": "Abu Dhabi",
            "destination": "Sydney",
            "date": str(today + timedelta(days=5)),
            "departure_time": "09:00",
            "arrival_time": "13:00",
            "seats": 8,
            "price": 72000
        },
        {
            "id": 3,
            "airline": "Qatar Airways",
            "source": "Doha",
            "destination": "Tokyo",
            "date": str(today + timedelta(days=3)),
            "departure_time": "09:00",
            "arrival_time": "13:00",
            "seats": 15,
            "price": 68000
        },
        {
            "id": 4,
            "airline": "Air India",
            "source": "Delhi",
            "destination": "Toronto",
            "date": str(today + timedelta(days=7)),
            "departure_time": "09:00",
            "arrival_time": "13:00",
            "seats": 10,
            "price": 64000
        },
        {
            "id": 5,
            "airline": "Vistara",
            "source": "Delhi",
            "destination": "Mumbai",
            "date": str(today + timedelta(days=4)),
            "departure_time": "09:00",
            "arrival_time": "13:00",
            "seats": 20,
            "price": 4800
        }
    ]
    cities_list = [
        "New Delhi", "Mumbai", "Chennai", "Bengaluru", "Hyderabad", "Kolkata",
        "Jaipur", "Lucknow", "Bhopal", "Patna", "Ranchi", "Raipur",
        "Bhubaneswar", "Thiruvananthapuram", "Panaji", "Chandigarh",
        "Shimla", "Dehradun", "Srinagar", "Guwahati", "Shillong",
        "Itanagar", "Imphal", "Kohima", "Aizawl", "Gangtok", "Agartala",
        "Port Blair",
        "Washington D.C.", "London", "Tokyo", "Beijing", "Paris", "Moscow",
        "Berlin", "Ottawa", "Canberra", "Abu Dhabi", "Riyadh", "Rome",
        "Madrid", "Buenos Aires", "Brasilia", "Cairo", "Kathmandu",
        "Islamabad", "Colombo", "Dhaka", "Kabul", "Bangkok", "Singapore",
        "Wellington", "Jakarta", "Seoul", "Hanoi", "Kuala Lumpur", "Manila",
        "Tehran", "Cape Town", "Nairobi"
    ]
    save_data(FLIGHTS_FILE, flights)

today = datetime.today().date()
flights = [f for f in flights if datetime.strptime(f["date"], "%Y-%m-%d").date() >= today]

airlines_list = ["IndiGo", "Emirates", "Qatar Airways", "Air India", "Vistara", "Lufthansa", "United Airlines", "American Airlines"]
cities_list = [
    "New Delhi", "Mumbai", "Chennai", "Bengaluru", "Hyderabad", "Kolkata",
    "Jaipur", "Lucknow", "Bhopal", "Patna", "Ranchi", "Raipur",
    "Bhubaneswar", "Thiruvananthapuram", "Panaji", "Chandigarh",
    "Shimla", "Dehradun", "Srinagar", "Guwahati", "Shillong",
    "Itanagar", "Imphal", "Kohima", "Aizawl", "Gangtok", "Agartala",
    "Port Blair",
    "Washington D.C.", "London", "Tokyo", "Beijing", "Paris", "Moscow",
    "Berlin", "Ottawa", "Canberra", "Abu Dhabi", "Riyadh", "Rome",
    "Madrid", "Buenos Aires", "Brasilia", "Cairo", "Kathmandu",
    "Islamabad", "Colombo", "Dhaka", "Kabul", "Bangkok", "Singapore",
    "Wellington", "Jakarta", "Seoul", "Hanoi", "Kuala Lumpur", "Manila",
    "Tehran", "Cape Town", "Nairobi"
]

max_id = max([f["id"] for f in flights], default=0)

for i in range(3):
    source = random.choice(cities_list)
    destination = random.choice([c for c in cities_list if c != source])
    date = str(today + timedelta(days=random.randint(1, 7)))

    dep_hour = random.randint(5, 20)
    arr_hour = dep_hour + random.randint(2, 10)
    if arr_hour >= 24:
        arr_hour -= 24

    departure_time = f"{dep_hour:02d}:{random.randint(0, 59):02d}"
    arrival_time = f"{arr_hour:02d}:{random.randint(0, 59):02d}"

    flights.append({
        "id": max_id + i + 1,
        "airline": random.choice(airlines_list),
        "source": source,
        "destination": destination,
        "date": date,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "seats": random.randint(5, 30),
        "price": random.randint(4000, 90000)
    })

save_data(FLIGHTS_FILE, flights)

booking_id = max([b.get("booking_id", 0) for b in bookings], default=0) + 1


def search_flights():
    source = input("Enter source city: ").strip().title()
    destination = input("Enter destination city: ").strip().title()
  
    result = [
        f for f in flights
        if (f["source"] == source and f["destination"] == destination)
        or (f["source"] == destination and f["destination"] == source)
    ]


    if not result:
        print("\n\033[1mNo flights available for this route!\033[0m\n")
        return

    result = sorted(result, key=lambda x: x["price"])

    global last_search
    last_search = result

    print(f"\n\033[1mAvailable flights between {source} and {destination} (both ways):\033[0m\n")
    for f in result:
        print(
            f"ID: {f['id']} | {f['airline']} | {f['date']} {f['departure_time']} → {f['arrival_time']} | "
            f"Seats: {f['seats']} | Price: ₹{f['price']} | Duration: {calculate_duration(f['departure_time'], f['arrival_time'])}"
        )
    print()



def book_ticket():
    global booking_id
    global last_search
    if not last_search:
        print("\n\033[1mPlease search flights first before booking!\033[0m\n")
        return

    try:
        flight_id = int(input("Enter flight ID to book: "))
        num_passengers = int(input("How many passengers? (1-3): "))
    except ValueError:
        print("\033[1mInvalid input!\033[0m")
        return

    if num_passengers < 1 or num_passengers > 3:
        print("\033[1mOnly 1 to 3 passengers allowed!\033[0m")
        return

    selected_flight = next((f for f in last_search if f["id"] == flight_id), None)

    if not selected_flight:
        print("\n\033[1mInvalid Flight ID! Select from last search results.\033[0m\n")
        return

    if num_passengers > selected_flight["seats"]:
        print("\n\033[1mNot enough seats available!\033[0m\n")
        return

    passengers = []
    for i in range(num_passengers):
        print(f"\nPassenger {i + 1}:")
        name = input("Enter name: ").title()
        age = input("Enter age: ")
        gender = input("Enter gender (M/F/O): ").upper()

        if gender not in ["M", "F", "O"]:
            print("\033[1mInvalid gender! Use M, F, or O\033[0m")
            return

        passengers.append({
            "name": name,
            "age": age,
            "gender": gender
        })

    selected_flight["seats"] -= num_passengers

    booking = {
        "booking_id": booking_id,
        "pnr": generate_pnr(),
        "flight_id": selected_flight["id"],
        "airline": selected_flight["airline"],
        "date": selected_flight["date"],
        "passengers": passengers,
        "total_seats": num_passengers,
        "total_price": num_passengers * selected_flight["price"]
    }

    bookings.append(booking)

    save_data(BOOKINGS_FILE, bookings)
    save_data(FLIGHTS_FILE, flights)

    print(f"\n\033[1mBooking Confirmed! Booking ID: {booking_id} | PNR: {booking['pnr']}\033[0m\n")
    booking_id += 1

    last_search = []



def view_bookings():
    if not bookings:
        print("\n\033[1mNo bookings yet!\033[0m\n")
        return

    print("\n\033[1mYour Bookings:\033[0m\n")
    for b in bookings:
        print(
            f"Booking ID: {b['booking_id']} | PNR: {b['pnr']} | "
            f"{b['airline']} | {b['date']} | "
            f"Seats: {b['total_seats']} | Total: ₹{b['total_price']}"
        )
        flight = next((fl for fl in flights if fl["id"] == b["flight_id"]), None)
        if flight:
            print(f"Departure: {flight['date']} {flight['departure_time']} → Arrival: {flight['arrival_time']} | Duration: {calculate_duration(flight['departure_time'], flight['arrival_time'])}")
        print("Passengers:")
        for p in b["passengers"]:
            gender_full = {"M": "Male", "F": "Female", "O": "Other"}.get(p["gender"], "Unknown")
            print(f" - {p['name']} ({p['age']} yrs, {gender_full})")
        print()


def cancel_booking():
    try:
        cancel_id = int(input("Enter booking ID to cancel: "))
    except ValueError:
        print("\033[1mInvalid input!\033[0m")
        return

    for b in bookings:
        if b["booking_id"] == cancel_id:
            for f in flights:
                if f["id"] == b["flight_id"]:
                    f["seats"] += b["total_seats"]

            bookings.remove(b)

            save_data(BOOKINGS_FILE, bookings)
            save_data(FLIGHTS_FILE, flights)

            print("\n\033[1mBooking Cancelled!\033[0m\n")
            return

    print("\n\033[1mBooking ID not found!\033[0m\n")


def main():
    while True:
        print("")
        print("\033[1mFLIGHT TICKET BOOKING SYSTEM ✈️\033[0m")
        print("")
        print("1. Search Flights")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            search_flights()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("\n \033[1mThank you for using our system\033[0m!\n")
            break
        else:
            print("\nERROR: Invalid choice!\n")


if __name__ == "__main__":
    main()
