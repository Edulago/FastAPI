# Uvicorn - Servidor ASGI para aplicações FastAPI
# Comandos úteis para execução da API:

# Iniciar a API com recarregamento automático ao modificar o código:
# uvicorn main:app --reload

# Iniciar a API em uma porta específica:
# uvicorn main:app --host 127.0.0.1 --port 8080 --reload

# Rotas (endpoints) da API:
# As rotas da aplicação estão definidas sob o prefixo "/api".

# Documentação da API:
# A documentação interativa pode ser acessada através do endpoint "/docs".

# Tratamento de exceções:
# O comando 'raise' é utilizado para lançar exceções manualmente,
# interrompendo a execução do código quando necessário.

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