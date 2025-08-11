# ML Churn Prediction API Demo

This repository demonstrates how to deploy a machine learning model as a web API endpoint for churn prediction, using a modern Python stack:

- **FastAPI** for building the API
- **Pydantic** for data validation and error handling
- **UV** for dependency management and reproducible builds
- **Docker** for containerization with optimized multi-stage builds
- **Fly.io** for cloud deployment with CI/CD

The project is inspired by and follows the [mlzoomcamp-flask-uv workshop](https://github.com/alexeygrigorev/workshops/tree/main/mlzoomcamp-flask-uv) by [Alexey Grigorev](https://github.com/alexeygrigorev) from [DataTalks.Club](https://datatalks.club/). Many thanks to Alexey and the DataTalks.Club community for their excellent educational resources!

## Features

- **Churn prediction**: Exposes a `/predict` endpoint that accepts customer data and returns the probability of churn.
- **Modern Python stack**: Uses FastAPI and Pydantic for robust, type-safe APIs with proper error handling.
- **Reproducible builds**: Uses [UV](https://github.com/astral-sh/uv) for fast, reliable dependency management.
- **Optimized Docker**: Multi-stage Docker build with proper layer caching and security best practices.
- **Cloud deployment**: Ready for deployment on Fly.io with automated CI/CD via GitHub Actions.
- **Production-ready**: Includes proper error handling, dependency locking, and containerization.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed
- (Optional) [UV](https://github.com/astral-sh/uv) for local development
- (Optional) [Fly CLI](https://fly.io/docs/flyctl/) for cloud deployment

### Local Development

#### Option 1: Using Docker (Recommended)

1. **Build the Docker image:**
   ```sh
   docker build -t churn-api .
   ```

2. **Run the container:**
   ```sh
   docker run -p 9696:9696 churn-api
   ```

#### Option 2: Using UV (for development)

1. **Install dependencies:**
   ```sh
   uv sync
   ```

2. **Run the application:**
   ```sh
   uv run uvicorn predict:app --host 0.0.0.0 --port 9696
   ```

### Testing the API

Once the service is running, test the `/predict` endpoint by sending a POST request with customer data:

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

### Cloud Deployment

The project includes configuration for deployment on [Fly.io](https://fly.io/) with automated CI/CD:

1. **Set up Fly.io** (one-time setup):
   ```sh
   fly auth signup  # or fly auth login if you have an account
   fly apps create  # creates a new app
   ```

2. **Deploy manually**:
   ```sh
   fly deploy
   ```

3. **Automated deployment**: 
   The GitHub Actions workflow in `.github/workflows/fly-deploy.yml` automatically deploys the app when you push to the `main` branch. You'll need to set the `FLY_API_TOKEN` secret in your GitHub repository settings.

## Architecture

- **Application code**: `predict.py` contains the FastAPI application with Pydantic models for request/response validation
- **Model**: `model.bin` contains the trained scikit-learn model
- **Dependencies**: `pyproject.toml` and `uv.lock` define and lock dependencies for reproducibility
- **Containerization**: `Dockerfile` uses UV for efficient dependency installation and includes proper error handling
- **Deployment**: `fly.toml` configures the Fly.io deployment with appropriate resource allocation

## Credits

- Workshop: [mlzoomcamp-flask-uv](https://github.com/alexeygrigorev/workshops/tree/main/mlzoomcamp-flask-uv)
- Author: [Alexey Grigorev](https://github.com/alexeygrigorev)
- Community: [DataTalks.Club](https://datatalks.club/)

---

This project is for educational and demonstration purposes only. It is not intended for production use. Please review the code and adapt it to your needs if you plan to use it in a real application.