import pandas as pd
from scipy.spatial.distance import cosine

# Sample data: User-Item ratings matrix
data = {
    'User': ['User1', 'User1', 'User1', 'User2', 'User2', 'User2', 'User3', 'User3', 'User3', 'User4', 'User4', 'User4'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item4', 'Item1', 'Item3', 'Item4', 'Item2', 'Item3', 'Item4'],
    'Rating': [5, 3, 4, 4, 5, 2, 4, 5, 3, 2, 4, 5]
}

df = pd.DataFrame(data)

# Create the user-item matrix
user_item_matrix = df.pivot_table(index='User', columns='Item', values='Rating').fillna(0)

# Compute user similarity using cosine similarity
def compute_similarity(matrix):
    similarity = pd.DataFrame(index=matrix.index, columns=matrix.index, dtype=float)
    for i in matrix.index:
        for j in matrix.index:
            if i != j:
                similarity.loc[i, j] = 1 - cosine(matrix.loc[i], matrix.loc[j])
            else:
                similarity.loc[i, j] = 1  # self-similarity
    return similarity

user_similarity = compute_similarity(user_item_matrix)

# Recommend items to a user based on user similarity
def recommend_items(user, user_item_matrix, user_similarity, num_recommendations=2):
    similar_users = user_similarity[user].drop(user).nlargest(3).index
    recommended_items = pd.Series(dtype='float64')

    for similar_user in similar_users:
        similar_user_ratings = user_item_matrix.loc[similar_user]
        similar_user_ratings = similar_user_ratings[similar_user_ratings > 0]
        recommended_items = pd.concat([recommended_items, similar_user_ratings])

    recommended_items = recommended_items.groupby(recommended_items.index).mean()
    user_rated_items = user_item_matrix.loc[user]
    recommended_items = recommended_items[~recommended_items.index.isin(user_rated_items[user_rated_items > 0].index)]
    recommended_items = recommended_items.nlargest(num_recommendations)
    return recommended_items

# Example recommendation for User1
user = 'User1'
recommendations = recommend_items(user, user_item_matrix, user_similarity)
print(f"Recommendations for {user}:")
print(recommendations)
