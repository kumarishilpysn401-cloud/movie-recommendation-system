import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("movie.csv")


movies["features"] = (
    movies["genre"].fillna("") + " " +
    movies["description"].fillna("")
)


vectorizer = TfidfVectorizer(
    stop_words="english"
)

feature_matrix = vectorizer.fit_transform(
    movies["features"]
)


similarity_matrix = cosine_similarity(
    feature_matrix
)


def recommend_movies(movie_title, number_of_movies=5):

    movie_index = movies[
        movies["title"].str.lower() == movie_title.lower()
    ].index

    if len(movie_index) == 0:
        return []

    movie_index = movie_index[0]

    similarity_scores = list(
        enumerate(
            similarity_matrix[movie_index]
        )
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores[
        1:number_of_movies + 1
    ]:

        recommendations.append({
            "title": movies.iloc[index]["title"],
            "score": round(score * 100, 1)
        })

    return recommendations
