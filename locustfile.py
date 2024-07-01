from locust import HttpUser, task, between

class DogApiUser(HttpUser):
    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds between tasks

    @task
    def get_random_dog_image(self):
        self.client.get("/api/breeds/image/random")

    @task
    def get_list_all_breeds(self):
        self.client.get("/api/breeds/list/all")

    @task
    def get_random_image_by_breed(self):
        breed = "retriever/golden"
        self.client.get(f"/api/breed/{breed}/images/random")

    @task
    def get_sub_breed_list(self):
        breed = "hound"
        self.client.get(f"/api/breed/{breed}/list")




 # terminal command: locust -f locustfile.py --host https://dog.ceo
        
# url:   https://dog.ceo/dog-api/

