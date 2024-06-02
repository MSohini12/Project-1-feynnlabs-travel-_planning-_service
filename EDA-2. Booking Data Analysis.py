# Booking Data Analysis
print("\nBooking Data Summary:")
print(booking_data.describe())

# Visualize bookings over time
booking_data['date'] = pd.to_datetime(booking_data['date'])
booking_data.set_index('date', inplace=True)
booking_data['bookings'].plot(figsize=(12, 6))
plt.title('Bookings Over Time')
plt.show()
