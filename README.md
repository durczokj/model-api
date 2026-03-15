# Iris Model API

A simple REST API that predicts iris species based on sepal and petal length.

## Usage

**Get API info:**
```
GET /
```

**Make a prediction:**
```
GET /predict?sepal_length=5.1&petal_length=1.4
```

## Run locally

```bash
docker-compose up -d
```

API available at `http://localhost:3000`

## Deployment

Pushing to `main` automatically builds and deploys to the server via GitHub Actions.

Live at: `http://durczok.ovh/model_api/`
