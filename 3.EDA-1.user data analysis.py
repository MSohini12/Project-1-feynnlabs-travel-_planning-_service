# User Data Analysis
print("\nUser Data Summary:")
print(user_data.describe())

# Visualize user preferences distribution
import matplotlib.pyplot as plt
import seaborn as sns

user_data['preferences'] = user_data['preferences'].apply(lambda x: x.split(','))
user_data_exploded = user_data.explode('preferences')

plt.figure(figsize=(10, 6))
sns.countplot(y='preferences', data=user_data_exploded)
plt.title('User Preferences Distribution')
plt.show()
