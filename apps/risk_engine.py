from apps.pii_detector import detect_pii

def classify_risk(text: str):
    pii_found = detect_pii(text)

    if "ssn" in pii_found:
        return "HIGH"
    elif "email" in pii_found or "phone" in pii_found:
        return "MEDIUM"
    else:
        return "LOW"