import json

def load_rules(path="data/dialect_rules.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)