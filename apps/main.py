from fastapi import FastAPI
from apps.risk_engine import classify_risk
from apps.audit_logger import log_interaction

app = FastAPI()

@app.post("/chat")
def chat(input_text: str):
    risk = classify_risk(input_text)
    log_interaction(input_text, risk)

    return {
        "message": "Input received",
        "risk_level": risk
    }