import re

def detect_pii(text: str):
    patterns = {
        "email": r"\S+@\S+\.\S+",
        "phone": r"\b\d{10}\b",
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b"
    }

    detected = []

    for key, pattern in patterns.items():
        if re.search(pattern, text):
            detected.append(key)

    return detected


def mask_pii(text: str):
    # Mask SSN
    text = re.sub(r"\b\d{3}-\d{2}-(\d{4})\b", r"***-**-\1", text)

    # Mask phone
    text = re.sub(r"\b\d{6}(\d{4})\b", r"******\1", text)

    # Mask email
    text = re.sub(r"(\S)[^\s@]*(@\S+)", r"\1***\2", text)

    return text