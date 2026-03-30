# -----------------------------
# Step 1: Dataset (hardcoded)
# -----------------------------
routes = [
    ["Kolar", "MP Nagar", 8, 6, 25],
    ["Kolar", "New Market", 10, 8, 30],
    ["Bairagarh", "New Market", 6, 5, 20],
    ["Bairagarh", "MP Nagar", 9, 7, 28],
    ["Habibganj", "MP Nagar", 4, 3, 12],
    ["Habibganj", "New Market", 5, 4, 15]
]

# -----------------------------
# Step 2: Simple "ML-like" model
# -----------------------------
# We simulate Linear Regression using a formula
# time ≈ (distance × weight1) + (stops × weight2)

weight_distance = 2.0
weight_stops = 1.5

# -----------------------------
# Step 3: User Input
# -----------------------------
print("=== Smart Transport Route Finder ===")

source = input("Enter Source: ")
destination = input("Enter Destination: ")

# -----------------------------
# Step 4: Find Best Route
# -----------------------------
best_route = None
min_time = 999999

for route in routes:
    if route[0] == source and route[1] == destination:
        distance = route[2]
        stops = route[3]

        # Prediction using formula
        predicted_time = (distance * weight_distance) + (stops * weight_stops)

        if predicted_time < min_time:
            min_time = predicted_time
            best_route = route

# -----------------------------
# Step 5: Output
# -----------------------------
if best_route is None:
    print("No route found!")
else:
    print("\nBest Route Found:")
    print("From:", best_route[0])
    print("To:", best_route[1])
    print("Stops:", best_route[3])
    print("Predicted Time:", round(min_time, 2), "minutes")
