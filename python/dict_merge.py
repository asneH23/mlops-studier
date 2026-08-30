# Quest: Dict-detektiven
# Funktion som slår samman två dicts utan att skriva över befintliga nycklar

def merge_dicts(base: dict, extra: dict) -> dict:
    """Mergar extra into base, men skriver INTE över befintliga nycklar."""
    return {**extra, **base}  # base-nycklar vinner

a = {"name": "Alice", "score": 95}
b = {"score": 80, "level": 3}

result = merge_dicts(a, b)
print(result)  # {"name": "Alice", "score": 95, "level": 3}
