from fastapi import Header, APIRouter, HTTPException
from typing import List
from models import Movie, db, PyObjectId


movies = APIRouter(prefix="/movie")


@movies.get('/', status_code=200)
async def index_movie():
    movies = []
    for movie in db.movies.find():
        movies.append(Movie(**movie))
    return {'movies': movies}


@movies.post('/', status_code=201)
async def add_movie(movie: Movie):
    if hasattr(movie, 'id'):
        delattr(movie, 'id')
    ret = db.movies.insert_one(movie.dict(by_alias=True))
    movie.id = ret.inserted_id
    return {'movie': movie}


@movies.delete('/{id}')
async def delete_movie(id: PyObjectId):
    if db.movies.count_documents({'_id': id}, limit=1):
        result = db.movies.delete_one({'_id': id})
        return {'message': f"Movie with id {id} was sucessfully deleted"}
    raise HTTPException(status_code=404, detail="Movie with given id not found")