# Social Media Data Analysis
print("\nSocial Media Data Summary:")
print(social_media_data['platform'].value_counts())

# Visualize social media platform distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='platform', data=social_media_data)
plt.title('Social Media Platform Distribution')
plt.show()
