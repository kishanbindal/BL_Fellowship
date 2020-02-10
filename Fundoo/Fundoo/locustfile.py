from locust import HttpLocust, TaskSet, between, task
# from services import TokenService
import jwt
import random


class UserInteractions(TaskSet):

    @task(4)
    def login(self):
        self.client.post("/fun/api/login", {"email": "asd@gmail.com", "password": "123"})

    @task(2)
    def post_note(self):
        token = jwt.encode({"id": 15}, 'secretkey', algorithm='HS256')
        self.client.get("/notes/api/notes", headers={'token': token})


class WebsiteUser(HttpLocust):

    task_set = UserInteractions
    wait_time = between(5.0, 9.0)
