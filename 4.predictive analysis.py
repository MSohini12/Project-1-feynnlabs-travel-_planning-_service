# Import necessary libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Feature Engineering for booking data
booking_data['day_of_week'] = booking_data.index.dayofweek
booking_data['month'] = booking_data.index.month

# Model Training
X = booking_data[['day_of_week', 'month']]
y = booking_data['bookings']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Prediction and evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"\nMean Absolute Error: {mae}")

# Forecasting future demand
future_data = pd.DataFrame({
    'day_of_week': [0, 1, 2],  # Example: Monday, Tuesday, Wednesday
    'month': [6, 6, 6]        # Example: June
})
future_demand = model.predict(future_data)
print(f"Future Demand: {future_demand}")
