# Import necessary libraries
from sklearn.metrics.pairwise import cosine_similarity

# Creating a user-item matrix
user_item_matrix = user_data_exploded.pivot_table(index='user_id', columns='preferences', aggfunc='size', fill_value=0)
user_similarity = cosine_similarity(user_item_matrix)

# Recommendation function
def recommend_destinations(user_id, user_data, user_similarity, top_n=5):
    user_idx = user_data[user_data['user_id'] == user_id].index[0]
    similar_users = user_similarity[user_idx]
    similar_users_idx = similar_users.argsort()[-top_n:][::-1]
    
    recommendations = []
    for idx in similar_users_idx:
        similar_user_id = user_data.iloc[idx]['user_id']
        similar_user_data = user_data_exploded[user_data_exploded['user_id'] == similar_user_id]
        recommendations.extend(similar_user_data['preferences'].values)
    
    return recommendations

# Get recommendations for a user
user_id = 1
recommendations = recommend_destinations(user_id, user_data, user_similarity)
print(f"Recommendations for User {user_id}: {recommendations}")
