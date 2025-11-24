from src.rule_loader import load_rules
import re

class JLDialectConverter:
    def __init__(self):
        rules = load_rules()
        self.j2s = rules["JEOLLA_TO_STD"]
        self.s2j = rules["STD_TO_JEOLLA"]

    def convert(self, text, mode="j2s"):
        rules = self.j2s if mode == "j2s" else self.s2j
        output = text

        for key in sorted(rules.keys(), key=lambda x: len(x), reverse=True):
            pattern = re.compile(re.escape(key))
            output = pattern.sub(rules[key], output)

        return output