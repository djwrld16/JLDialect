class DialectAnalyzer:
    def __init__(self, rules):
        self.rules = rules

    def analyze(self, text):
        tokens = text.split()
        matched = [t for t in tokens if t in self.rules.keys()]
        score = len(matched) / len(tokens)

        return {
            "matched_tokens": matched,
            "dialect_intensity": round(score, 2)
        }