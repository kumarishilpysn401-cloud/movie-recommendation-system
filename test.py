from recommender import recommend_movies

movie = "Avengers"

recommendations = recommend_movies(movie)

print("Recommendations for:", movie)

for movie in recommendations:
    print("-", movie)