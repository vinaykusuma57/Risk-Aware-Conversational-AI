import json
from datetime import datetime
from apps.pii_detector import mask_pii

LOG_FILE = "logs/interactions.json"

def log_interaction(user_input: str, risk_level: str):
    masked_input = mask_pii(user_input)

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": masked_input,
        "risk_level": risk_level
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")