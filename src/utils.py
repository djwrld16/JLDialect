def print_result(input_text, output_text, mode):
    direction = "전라도 → 표준어" if mode == "j2s" else "표준어 → 전라도"
    print("\n=== JLDialect Converter ===")
    print(f"변환 방향: {direction}")
    print(f"입력: {input_text}")
    print(f"결과: {output_text}")