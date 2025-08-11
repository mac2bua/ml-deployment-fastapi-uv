import requests

url = 'http://localhost:9696/predict'

customer = {
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
}

response = requests.post(url, json=customer)
churn = response.json()

print(f"response: {churn}")

if churn['churn_probability'] >= 0.5:
    print("send an email promo")
else:
    print("don't do anything")

# curl -X 'POST' \
#   'https://cuddly-invention-97g9wxqprhx449-9696.app.github.dev/predict' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "gender": "male",
#     "seniorcitizen": 0,
#     "partner": "no",
#     "dependents": "yes",
#     "phoneservice": "no",
#     "multiplelines": "no_phone_service",
#     "internetservice": "dsl",
#     "onlinesecurity": "no",
#     "onlinebackup": "yes",
#     "deviceprotection": "no",
#     "techsupport": "no",
#     "streamingtv": "no",
#     "streamingmovies": "no",
#     "contract": "month-to-month",
#     "paperlessbilling": "yes",
#     "paymentmethod": "electronic_check",
#     "tenure": 6,
#     "monthlycharges": 29.85,
#     "totalcharges": 129.85
# }'