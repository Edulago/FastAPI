# Uvicorn
# rodar a api: uvicorn main:app -- reload
# rodar a api em outra porta: uvicorn main:app --host 127.0.0.1 --port 8080 --reload
# routes - rodas da minha ap "/api"
# RestAPI
# verificar a documentação - /docs
# raise - lançar exceções de forma manual e interrompe a execução do código.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = {
    1: {"Name": "The Avengers", "Genre": "Action/Adventure", "Duration": "2h 23min", "Release Year": "2012"},
    2: {"Name": "Inception", "Genre": "Sci-Fi/Thriller", "Duration": "2h 28min", "Release Year": "2010"},
    3: {"Name": "Interstellar", "Genre": "Sci-Fi/Drama", "Duration": "2h 49min", "Release Year": "2014"},
    4: {"Name": "The Dark Knight", "Genre": "Action/Crime", "Duration": "2h 32min", "Release Year": "2008"},
    5: {"Name": "Pulp Fiction", "Genre": "Crime/Drama", "Duration": "2h 34min", "Release Year": "1994"}
}

class Movie(BaseModel):
    Name: str
    Genre: str
    Duration: str
    Release_Year: str

@app.get("/")
def home():
    return {"Movies": movies}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if movie_id in movies:
        return movies[movie_id]

    raise HTTPException(status_code=404, detail="Movie ID not found")

@app.post("/movies/")
def create_movie(movie: Movie):
    new_id = max(movies.keys(), default=0) + 1
    movies[new_id] = dict(movie)
    return {"msg" : "Movie Created", "id": new_id, "movie": movie}