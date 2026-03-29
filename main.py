import pandas as pd
from sklearn.linear_model import LinearRegression

# -----------------------------
# Step 1: Dataset (inside Python)
# -----------------------------
data = [
    {"source": "Kolar", "destination": "MP Nagar", "distance": 8, "stops": 6, "time": 25},
    {"source": "Kolar", "destination": "New Market", "distance": 10, "stops": 8, "time": 30},
    {"source": "Bairagarh", "destination": "New Market", "distance": 6, "stops": 5, "time": 20},
    {"source": "Bairagarh", "destination": "MP Nagar", "distance": 9, "stops": 7, "time": 28},
    {"source": "Habibganj", "destination": "MP Nagar", "distance": 4, "stops": 3, "time": 12},
    {"source": "Habibganj", "destination": "New Market", "distance": 5, "stops": 4, "time": 15}
]

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Train ML Model
# -----------------------------
X = df[["distance", "stops"]]
y = df["time"]

model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Step 3: Program Start
# -----------------------------
print("=== Smart Transport Route Finder ===")

source = input("Enter Source: ")
destination = input("Enter Destination: ")

# -----------------------------
# Step 4: Filter Routes
# -----------------------------
routes = df[(df["source"] == source) & (df["destination"] == destination)]

# -----------------------------
# Step 5: Output Result
# -----------------------------
if routes.empty:
    print("No route found!")
else:
    best_route = None
    min_time = float("inf")

    for _, row in routes.iterrows():
        predicted_time = model.predict([[row["distance"], row["stops"]]])[0]

        if predicted_time < min_time:
            min_time = predicted_time
            best_route = row

    print("\nBest Route Found:")
    print("From:", best_route["source"])
    print("To:", best_route["destination"])
    print("Stops:", best_route["stops"])
    print("Predicted Time:", round(min_time, 2), "minutes")
