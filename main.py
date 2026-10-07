import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from recommender import recommend_movies, movies


# ==============================
# Main Window
# ==============================

root = tk.Tk()

root.title("Movie Recommendation System")
root.geometry("1100x750")
root.configure(bg="#141414")


# ==============================
# Header
# ==============================

header = tk.Frame(root, bg="#141414")
header.pack(fill="x", pady=20)

title = tk.Label(
    header,
    text="🎬 MOVIE RECOMMENDATION SYSTEM",
    font=("Arial", 26, "bold"),
    bg="#141414",
    fg="white"
)
title.pack()

subtitle = tk.Label(
    header,
    text="Find movies you will love",
    font=("Arial", 13),
    bg="#141414",
    fg="#bbbbbb"
)
subtitle.pack(pady=5)


# ==============================
# Search Area
# ==============================

search_frame = tk.Frame(root, bg="#141414")
search_frame.pack(pady=15)

movie_combo = ttk.Combobox(
    search_frame,
    width=35,
    font=("Arial", 14),
    state="readonly"
)

movie_combo["values"] = movies["title"].tolist()
movie_combo.set("Select a movie")

movie_combo.grid(row=0, column=0, padx=5)


# ==============================
# Result Title
# ==============================

result_title = tk.Label(
    root,
    text="Recommended Movies",
    font=("Arial", 20, "bold"),
    bg="#141414",
    fg="white"
)

result_title.pack(pady=15)


# ==============================
# Result Area
# ==============================

result_frame = tk.Frame(
    root,
    bg="#141414"
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=20
)


# Keep images in memory
poster_images = []


# ==============================
# Movie Details Popup
# ==============================

def show_movie_details(movie_name):

    movie_data = movies[
        movies["title"] == movie_name
    ].iloc[0]

    details_window = tk.Toplevel(root)

    details_window.title(movie_name)
    details_window.geometry("650x600")
    details_window.configure(bg="#141414")

    # Poster
    try:

        image = Image.open(
            movie_data["poster"]
        )

        image = image.resize(
            (220, 300)
        )

        photo = ImageTk.PhotoImage(image)

        poster_label = tk.Label(
            details_window,
            image=photo,
            bg="#141414"
        )

        poster_label.image = photo
        poster_label.pack(pady=15)

    except:

        poster_label = tk.Label(
            details_window,
            text="🎬\nPoster Not Found",
            font=("Arial", 20),
            bg="#333333",
            fg="white",
            width=18,
            height=8
        )

        poster_label.pack(pady=15)

    # Title
    title_label = tk.Label(
        details_window,
        text=movie_data["title"],
        font=("Arial", 24, "bold"),
        bg="#141414",
        fg="white"
    )

    title_label.pack(pady=5)

    # Genre
    genre_label = tk.Label(
        details_window,
        text=f"Genre: {movie_data['genre']}",
        font=("Arial", 12),
        bg="#141414",
        fg="#bbbbbb"
    )

    genre_label.pack(pady=5)

    # Rating + Year
    info_label = tk.Label(
        details_window,
        text=f"⭐ Rating: {movie_data['rating']}    📅 Year: {movie_data['year']}",
        font=("Arial", 12, "bold"),
        bg="#141414",
        fg="#ffd700"
    )

    info_label.pack(pady=5)

    # Description
    description_label = tk.Label(
        details_window,
        text=movie_data["description"],
        font=("Arial", 11),
        bg="#141414",
        fg="white",
        wraplength=550,
        justify="center"
    )

    description_label.pack(pady=20)


# ==============================
# Recommendation Function
# ==============================

def show_recommendations():

    global poster_images

    selected_movie = movie_combo.get()

    if selected_movie == "Select a movie":

        messagebox.showwarning(
            "Warning",
            "Please select a movie first!"
        )

        return

    recommendations = recommend_movies(
        selected_movie,
        5
    )

    # Clear previous cards
    for widget in result_frame.winfo_children():
        widget.destroy()

    poster_images = []

    # Create movie cards
    for i, recommendation in enumerate(recommendations):

        movie_name = recommendation["title"]
        match_score = recommendation["score"]

        movie_data = movies[
            movies["title"] == movie_name
        ].iloc[0]

        # ==============================
        # Card
        # ==============================

        card = tk.Frame(
            result_frame,
            bg="#222222",
            width=190,
            height=420,
            cursor="hand2"
        )

        card.grid(
            row=0,
            column=i,
            padx=10,
            pady=10
        )

        card.grid_propagate(False)

        # Make card clickable
        card.bind(
            "<Button-1>",
            lambda event, name=movie_name:
            show_movie_details(name)
        )

        # ==============================
        # Poster
        # ==============================

        try:

            image = Image.open(
                movie_data["poster"]
            )

            image = image.resize(
                (160, 220)
            )

            photo = ImageTk.PhotoImage(image)

            poster_images.append(photo)

            poster_label = tk.Label(
                card,
                image=photo,
                bg="#222222",
                cursor="hand2"
            )

            poster_label.pack(pady=8)

            poster_label.bind(
                "<Button-1>",
                lambda event, name=movie_name:
                show_movie_details(name)
            )

        except:

            poster_label = tk.Label(
                card,
                text="🎬\nPoster\nNot Found",
                font=("Arial", 15),
                bg="#333333",
                fg="white",
                width=14,
                height=9
            )

            poster_label.pack(pady=8)

        # ==============================
        # Movie Name
        # ==============================

        name_label = tk.Label(
            card,
            text=movie_name,
            font=("Arial", 13, "bold"),
            bg="#222222",
            fg="white",
            wraplength=160,
            cursor="hand2"
        )

        name_label.pack(pady=4)

        name_label.bind(
            "<Button-1>",
            lambda event, name=movie_name:
            show_movie_details(name)
        )

        # ==============================
        # Genre
        # ==============================

        genre_label = tk.Label(
            card,
            text=movie_data["genre"],
            font=("Arial", 10),
            bg="#222222",
            fg="#bbbbbb",
            wraplength=160
        )

        genre_label.pack(pady=3)

        # ==============================
        # Match Score
        # ==============================

        match_label = tk.Label(
            card,
            text=f"🎯 Match: {match_score}%",
            font=("Arial", 10, "bold"),
            bg="#222222",
            fg="#00ff88"
        )

        match_label.pack(pady=3)

        # ==============================
        # Rating
        # ==============================

        rating_label = tk.Label(
            card,
            text=f"⭐ Rating: {movie_data['rating']}",
            font=("Arial", 10, "bold"),
            bg="#222222",
            fg="#ffd700"
        )

        rating_label.pack(pady=3)

        # ==============================
        # Year
        # ==============================

        year_label = tk.Label(
            card,
            text=f"📅 {movie_data['year']}",
            font=("Arial", 10),
            bg="#222222",
            fg="#bbbbbb"
        )

        year_label.pack(pady=3)


# ==============================
# Reset Function
# ==============================

def reset_app():

    movie_combo.set("Select a movie")

    for widget in result_frame.winfo_children():
        widget.destroy()

    result_title.config(
        text="Recommended Movies"
    )


# ==============================
# Recommend Button
# ==============================

recommend_button = tk.Button(
    search_frame,
    text="🔍 Recommend",
    font=("Arial", 12, "bold"),
    bg="#e50914",
    fg="white",
    padx=15,
    pady=8,
    cursor="hand2",
    command=show_recommendations
)

recommend_button.grid(
    row=0,
    column=1,
    padx=5
)


# ==============================
# Reset Button
# ==============================

reset_button = tk.Button(
    search_frame,
    text="🔄 Reset",
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="white",
    padx=15,
    pady=8,
    cursor="hand2",
    command=reset_app
)

reset_button.grid(
    row=0,
    column=2,
    padx=5
)


# ==============================
# Footer
# ==============================

footer = tk.Label(
    root,
    text="Powered by TF-IDF & Cosine Similarity",
    font=("Arial", 10),
    bg="#141414",
    fg="#777777"
)

footer.pack(pady=10)


# ==============================
# Start Application
# ==============================

root.mainloop()

