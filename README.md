#  Flight Ticket Booking System — Python CLI

A fully interactive, real-world flight reservation system built using **pure Python (no frameworks)** and **JSON file storage**. Supports global + Indian capital routes, automatic daily flight generation, bold terminal UI, two-way search, ticket booking, PNR generation, and booking management.

---

##  Features

*  Search flights **both directions** (A → B & B → A)
*  Auto-generated flights daily
*  Domestic + international **capital cities**
*  Real-time future travel dates
*  Departure, arrival & **duration calculation**
*  Book up to **3 passengers per ticket**
*  Passenger details stored (name, age, gender)
*  Auto-generated unique **PNR number**
*  Persistent storage using JSON
*  Seat availability updates after booking
*  View all bookings anytime
*  Cancel bookings & restore seats
*  Bold, clean terminal output — no emojis
*  Pure Python data structures — beginner-friendly

---

## 🛠️ Tech Stack

| Component | Technology             |
| --------- | ---------------------- |
| Language  | Python 3.x             |
| Storage   | JSON files             |
| Data      | Lists & Dictionaries   |
| UI        | Command-Line Interface |

---

## 📂 Project Structure

```
Flight Ticket Booking System/
│
├── app.py
├── flights.json
└── bookings.json
```

* `app.py` → main application logic
* `flights.json` → live flight data
* `bookings.json` → confirmed ticket records

---

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/flight-ticket-booking-system.git
cd flight-ticket-booking-system
```

2. Run the program:

```bash
python app.py
```

(Use `python3` if required)

---

##  Menu Options

```
1. Search Flights
2. Book Ticket
3. View Bookings
4. Cancel Booking
5. Exit
```

---

## 🔍 Flight Search Example

```
Enter source city: Delhi
Enter destination city: Mumbai
```

* Shows available flights
* Sorted cheapest first
* Both directions included

Example output:

```
Available flights between Delhi and Mumbai (both ways):

ID: 12 | Vistara | 2025-11-27 09:45 → 14:20 | Seats: 18 | Price: ₹6200 | Duration: 4h 35m
```

---

##  Booking Example

```
Enter flight ID to book: 12
How many passengers? (1-3): 2
```

Result:

```
Booking Confirmed! Booking ID: 7 | PNR: X8PQ9K
```

---

##  JSON Booking Record Example

```json
{
  "booking_id": 7,
  "pnr": "X8PQ9K",
  "flight_id": 12,
  "airline": "Vistara",
  "date": "2025-11-27",
  "passengers": [
    { "name": "Amit", "age": "24", "gender": "M" },
    { "name": "Riya", "age": "22", "gender": "F" }
  ],
  "total_seats": 2,
  "total_price": 12400
}
```

---

## 🌍 Supported Cities

* All Indian state/UT capitals
* Major world capitals — London, Tokyo, Washington DC, Paris, Dubai, etc.
* Random flight generation between any two capitals

---

##  Learning Outcomes

* File handling & JSON storage
* CLI program structuring
* Searching & sorting logic
* Random data generation
* ANSI bold formatting
* Data persistence in Python
* Realistic booking logic

---

##  Ideal For

* Python beginners
*  College mini-project
*  Portfolio showcase
*  Offline flight booking simulation
*  Learning CRUD operations without databases

---

## 🤝 Contributing

Pull requests are welcome — feel free to improve UI, add features, or optimize logic!

---

## 📜 License

Free to use, modify & learn from — educational & personal projects welcome 

---

##  Developed by

**Abdus Sahir Choudhury**
Assam down town University 
*B.Tech CSE | Python | GenAI Developer*

