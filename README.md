#  BusNetwork

A web application for booking bus routes, built with Django and HTML/CSS.

---

## Features

- Browse all available bus routes
- View station details including departing and arriving routes
- Book routes as a registered user
- User authentication (register, login, logout)

---

##  Bonus Features

### My Routes Page
Logged-in users can view a personalized page listing all the routes they have booked, making it easy to track their travel history.

### Station Detail Page
Each station has a dedicated detail page that lists all routes departing from and arriving at that station, giving users a full picture of available connections.

### Search & Filter
Users can search and filter routes by origin or destination, making it quick and easy to find the right route without scrolling through the full list.

### Passenger Count
The route index page displays the current passenger count next to each route, so users can see how popular or full a route is at a glance.

### Polished UI with Bootstrap
The app is styled with Bootstrap, providing a clean, responsive, and professional look across all pages and screen sizes.

---

## Known Limitations

- No real-time seat availability — passenger counts reflect bookings in the database but are not updated live.
- No payment integration — bookings are confirmed without any payment processing.
- No email notifications — users do not receive confirmation emails after booking a route.
- Admin management is handled through Django's default admin panel, with no custom admin dashboard.
- The app is not optimized for very large datasets; performance may degrade with a high number of routes or users.

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django database)

---



