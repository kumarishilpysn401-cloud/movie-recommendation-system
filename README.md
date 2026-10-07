\# 🎬 Movie Recommendation System



A Python-based Movie Recommendation System with a graphical user interface (GUI).



The system recommends similar movies based on the selected movie using \*\*TF-IDF Vectorization\*\* and \*\*Cosine Similarity\*\*.



\---



\## 📌 Project Overview



The Movie Recommendation System helps users discover movies similar to a movie they already like.



The system analyzes the movie's:



\- Genre

\- Description



and calculates similarity between movies.



The top 5 most similar movies are then displayed in the GUI.



\---



\## ✨ Features



\- 🎬 Movie selection using dropdown

\- 🤖 Content-based movie recommendation

\- 🧠 TF-IDF text vectorization

\- 📊 Cosine Similarity

\- ⭐ Movie ratings

\- 📅 Movie release year

\- 🖼️ Movie posters

\- 📈 Match percentage

\- 🖥️ User-friendly Tkinter GUI

\- 🔄 Reset functionality

\- 📋 Movie details popup



\---



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- Scikit-learn

\- Tkinter

\- Pillow

\- TF-IDF

\- Cosine Similarity



\---



\## 🧠 Recommendation Method



This project uses a \*\*Content-Based Recommendation System\*\*.



\### Step 1: Feature Selection



The system uses:



\- Movie Genre

\- Movie Description



as the main features.



\### Step 2: TF-IDF



TF-IDF converts the text information into numerical vectors.



TF-IDF stands for:



\*\*Term Frequency - Inverse Document Frequency\*\*



\### Step 3: Cosine Similarity



Cosine Similarity compares the movie vectors and calculates how similar two movies are.



\### Step 4: Top Recommendations



Movies are sorted according to their similarity score.



The system displays the \*\*Top 5 similar movies\*\*.



\---



\## 🔄 System Workflow



```text

Select Movie

&#x20;    ↓

Get Genre + Description

&#x20;    ↓

TF-IDF Vectorization

&#x20;    ↓

Calculate Cosine Similarity

&#x20;    ↓

Sort Similarity Scores

&#x20;    ↓

Select Top 5 Movies

&#x20;    ↓

Display Recommendations



movie-recommendation-system/

│

├── main.py

├── recommender.py

├── movie.csv

├── test.py

├── requirements.txt

├── README.md

├── .gitignore

│

└── images/

&#x20;   ├── avengers.jpg

&#x20;   ├── ironman.jpg

&#x20;   ├── captainamerica.jpg

&#x20;   ├── thor.jpg

&#x20;   ├── spiderman.jpg

&#x20;   ├── batman.jpg

&#x20;   ├── superman.jpg

&#x20;   ├── avatar.jpg

&#x20;   ├── interstellar.jpg

&#x20;   ├── inception.jpg

&#x20;   ├── matrix.jpg

&#x20;   ├── titanic.jpg

&#x20;   ├── notebook.jpg

&#x20;   ├── jurassicpark.jpg

&#x20;   └── darkknight.jpg

