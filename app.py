from src.converter import JLDialectConverter
from src.rule_loader import load_rules
from src.analyzer import DialectAnalyzer
from src.utils import print_result

converter = JLDialectConverter()
rules = load_rules()
analyzer = DialectAnalyzer(rules["JEOLLA_TO_STD"])

print("=== JLDialect: 전라도 사투리 ↔ 표준어 변환기 ===")
print("1) 전라도 → 표준어")
print("2) 표준어 → 전라도")

mode_input = input("모드 선택 (1/2): ")
mode = "j2s" if mode_input == "1" else "s2j"

text = input("문장을 입력하세요: ")

output = converter.convert(text, mode=mode)

analysis = analyzer.analyze(text) if mode == "j2s" else None

print_result(text, output, mode)

if analysis:
    print("\n[사투리 분석 결과]")
    print(f"사용된 사투리: {analysis['matched_tokens']}")
    print(f"사투리 강도: {analysis['dialect_intensity']}")