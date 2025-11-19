from fastapi import FastAPI
from app.router import sms_routes, transaction_routes, prediction_routes

app = FastAPI()

# Include your routers
app.include_router(sms_routes.router)
app.include_router(transaction_routes.router)
app.include_router(prediction_routes.router)

# Root route
@app.get("/")
def root():
    return {"message": "API is running!"}
