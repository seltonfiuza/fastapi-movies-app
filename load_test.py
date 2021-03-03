import time
import secrets
from locust import HttpUser, task, between
import json

fake_movie = {
    "title": "The return of those who never went",
    "overview": "The return of those who never went",
    "genres": ["Comedy"]
}


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    movies_list = []


    @task
    def hello_world(self):
        self.client.get('/')

    
    @task
    def list_movies(self):
        get_movies_list = self.client.get('/movie/').text
        self.movies_list = json.loads(get_movies_list)

    @task
    def create_movie(self):
        if len(self.movies_list) > 0:
            data = json.dumps(fake_movie)
            new_movie = json.loads(self.client.post('/movie/', data=data).text)
            self.movies_list['movies'].append(new_movie)
    
    
    @task
    def delete_movie(self):
        if 'movies' in self.movies_list:
            if len(self.movies_list['movies']) > 1:
                movie_to_delete = secrets.choice(self.movies_list['movies'])
                self.client.delete('/movie/'+movie_to_delete['_id'])
                for movie in self.movies_list['movies']:
                    if '_id' in movie and '_id' in movie_to_delete:
                        if movie['_id'] == movie_to_delete['_id']:
                            del movie
