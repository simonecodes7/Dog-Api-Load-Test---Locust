# Dog-Api-Load-Test---Locust



Dog Breeds API Load Testing

This project uses Locust to load test a Dog Breeds API. The tests are defined in a Python script and cover the following endpoints:

    Random Dog Image: GET /api/breeds/image/random
    List All Breeds: GET /api/breeds/list/all
    Random Image by Breed: GET /api/breed/{breed}/images/random (e.g., retriever/golden)
    Sub-breed List: GET /api/breed/{breed}/list (e.g., hound)

Setup

    Clone the repository:

    bash

git clone <repository-url>
cd <repository-directory>

Install Locust:

bash

    pip install locust

Running Tests

Start Locust with:

bash

locust -f <path-to-your-locustfile.py>

Navigate to http://localhost:8089 in your browser to configure and start the tests.
License
