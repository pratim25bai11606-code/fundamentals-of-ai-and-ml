# -----------------------------
# Step 1: Dataset
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
# Step 2: Prepare Data
# -----------------------------
X = []
y = []

for r in routes:
    X.append([r[2], r[3]])  # distance, stops
    y.append(r[4])          # time

n = len(X)

# -----------------------------
# Step 3: Initialize Weights
# -----------------------------
w1 = 0.0
w2 = 0.0
b = 0.0

learning_rate = 0.01
epochs = 1000

# -----------------------------
# Step 4: Training (Gradient Descent)
# -----------------------------
for epoch in range(epochs):
    dw1 = 0
    dw2 = 0
    db = 0

    for i in range(n):
        x1, x2 = X[i]
        y_true = y[i]

        # Prediction
        y_pred = w1 * x1 + w2 * x2 + b

        # Error
        error = y_pred - y_true

        # Gradients
        dw1 += error * x1
        dw2 += error * x2
        db += error

    # Update weights
    w1 -= (learning_rate * dw1) / n
    w2 -= (learning_rate * dw2) / n
    b -= (learning_rate * db) / n

# -----------------------------
# Step 5: Show learned values
# -----------------------------
print("Learned Weights:")
print("w1 (distance):", round(w1, 2))
print("w2 (stops):", round(w2, 2))
print("bias:", round(b, 2))

# -----------------------------
# Step 6: User Input
# -----------------------------
print("\n=== Smart Transport Route Finder ===")

source = input("Enter Source: ")
destination = input("Enter Destination: ")

# -----------------------------
# Step 7: Prediction
# -----------------------------
best_route = None
min_time = 999999

for r in routes:
    if r[0] == source and r[1] == destination:
        x1 = r[2]
        x2 = r[3]

        predicted_time = w1 * x1 + w2 * x2 + b

        if predicted_time < min_time:
            min_time = predicted_time
            best_route = r

# -----------------------------
# Step 8: Output
# -----------------------------
if best_route is None:
    print("No route found!")
else:
    print("\nBest Route Found:")
    print("From:", best_route[0])
    print("To:", best_route[1])
    print("Stops:", best_route[3])
    print("Predicted Time:", round(min_time, 2), "minutes")
    
