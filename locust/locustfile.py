import time
from locust import FastHttpUser, task, between


class MyUser(FastHttpUser):
    wait_time = between(0.001, 0.002)

    @task
    def hello_world(self):
        self.client.get(url='/')

    @task
    def post_image(self):
        with open("sunny.png", "rb") as f:
            headers = {'content-type': 'image/png'}
            files = {'file': f}
            self.client.post(url='/predict', files=files)
