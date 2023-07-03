# Movie Genre API

This repository contains code for a Movie Genre API that predicts the genre of a movie based on its description. It uses a pre-trained model stored in the `model-new.pt` file.

## Prerequisites

Before running the API, make sure that the `model-new.pt` file is present in the project directory. If it is not available, you can build the model by running the `model_building.ipynb` notebook or simply download from the below google drive link
[Link for built model](https://drive.google.com/file/d/1lMMBOpV00Bgb5dNPv6YNXV1raqq-6e19/view?usp=sharing)

## Docker Setup

To create a Docker container for the API, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the Dockerfile.
3. Build the Docker image using the following command:

   ```
   docker build -t movie_genre-api .
   ```

## Running the API Server

To run the API server inside a Docker container, use the following command:

```
docker run -p 8000:8000 movie_genre-api
```

The API server will start and listen on port 8000.

## Making API Requests

You can use the following `curl` command to get the genre of a movie by providing its description:

```
curl -d "description=A movie about 5 comedians who are on a trip to las vegas" -X POST http://127.0.0.1:8000/analyze
```

Make sure to replace `127.0.0.1:8000` with the appropriate address if running the API server on a different machine.

The response will contain the predicted genre of the movie.
