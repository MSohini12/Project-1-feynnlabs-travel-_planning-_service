import pandas as pd

# Create user data

user_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'name': ['Rahul', 'Priya', 'Anil', 'Sunita', 'Rajesh'],
    'age': [34, 28, 40, 25, 45],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'preferences': ['beach, adventure, hiking', 'cultural, historical, beach', 'wildlife, adventure, trekking', 'shopping, cultural, nightlife', 'religious, historical, beach'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai']
})

print("\nUser Data\n",user_data)

booking_data = pd.DataFrame({
    'booking_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'user_id': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'date': ['2024-01-15', '2024-02-10', '2024-03-05', '2024-04-20', '2024-05-15', '2024-06-18', '2024-07-22', '2024-08-30', '2024-09-25', '2024-10-15'],
    'destination': ['Goa', 'Jaipur', 'Jim Corbett', 'Varanasi', 'Rameswaram', 'Manali', 'Agra', 'Bandipur', 'Kolkata', 'Mahabalipuram'],
    'bookings': [3, 2, 4, 1, 5, 2, 3, 4, 2, 1]
})

print( "\nBooking Data\n",booking_data)

# Create social media data
social_media_data = pd.DataFrame({
    'post_id': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'user_id': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'date': ['2024-01-05', '2024-02-01', '2024-03-01', '2024-04-10', '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-15', '2024-09-10', '2024-10-01'],
    'platform': ['Twitter', 'Facebook', 'Twitter', 'Instagram', 'Facebook', 'Instagram', 'Twitter', 'Instagram', 'Facebook', 'Twitter'],
    'content': ['Excited for my trip!','Just booked a cultural tour!','waiting for a new journey',"Can't wait to explore",'Planning a religious trip','Manali, here I come!','trip planned next month','Adventure awaits','Excited to visit again','the city of temples'],
    'likes': [150, 200, 250, 300, 100, 180, 220, 270, 160, 130],
    'comments': [20, 30, 40, 50, 10, 25, 35, 45, 18, 15]
})

print( "\nSocial Media Data\n",social_media_data)
