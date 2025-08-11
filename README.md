# ML Churn Prediction API Demo

This repository demonstrates how to deploy a machine learning model as a web API endpoint for churn prediction, using a modern Python stack:

- **FastAPI** for building the API
- **Pydantic** for data validation
- **UV** for dependency management and reproducible builds

The project is inspired by and follows the [mlzoomcamp-flask-uv workshop](https://github.com/alexeygrigorev/workshops/tree/main/mlzoomcamp-flask-uv) by [Alexey Grigorev](https://github.com/alexeygrigorev) from [DataTalks.Club](https://datatalks.club/). Many thanks to Alexey and the DataTalks.Club community for their excellent educational resources!

## Features

- **Churn prediction**: Exposes a `/predict` endpoint that accepts customer data and returns the probability of churn.
- **Modern Python stack**: Uses FastAPI and Pydantic for robust, type-safe APIs.
- **Reproducible builds**: Uses [UV](https://github.com/astral-sh/uv) for fast, reliable dependency management.
- **Dockerized**: Easily build and run the service in a container.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed

### Build and Run

1. **Build the Docker image:**
   ```sh
   docker build -t churn-api .
   ```

2. **Run the container:**
   ```sh
   docker run -p 9696:9696 churn-api
   ```

3. **Test the API:**
   Send a POST request to `http://localhost:9696/predict` with a JSON payload representing customer data.  
   Example using `curl`:
   ```sh
   curl -X POST "http://localhost:9696/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "gender": "male",
       "seniorcitizen": 0,
       "partner": "no",
       "dependents": "yes",
       "phoneservice": "no",
       "multiplelines": "no_phone_service",
       "internetservice": "dsl",
       "onlinesecurity": "no",
       "onlinebackup": "yes",
       "deviceprotection": "no",
       "techsupport": "no",
       "streamingtv": "no",
       "streamingmovies": "no",
       "contract": "month-to-month",
       "paperlessbilling": "yes",
       "paymentmethod": "electronic_check",
       "tenure": 6,
       "monthlycharges": 29.85,
       "totalcharges": 129.85
     }'
   ```

   You should receive a response like:
   ```json
   {
     "churn_probability": 0.54,
     "churn": true
   }
   ```

## Credits

- Workshop: [mlzoomcamp-flask-uv](https://github.com/alexeygrigorev/workshops/tree/main/mlzoomcamp-flask-uv)
- Author: [Alexey Grigorev](https://github.com/alexeygrigorev)
- Community: [DataTalks.Club](https://datatalks.club/)

---

This project is for educational and demonstration purposes only. It is not intended for production use. Please review the code and adapt it to your needs if you plan to use it in a real application.