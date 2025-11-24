import streamlit as st
from src.converter import JLDialectConverter
from src.rule_loader import load_rules
from src.analyzer import DialectAnalyzer

# Load everything
converter = JLDialectConverter()
rules = load_rules()
analyzer = DialectAnalyzer(rules["JEOLLA_TO_STD"])

# Streamlit UI
st.title("🟢 JLDialect: Jeolla Dialect ↔ Standard Korean Converter")
st.write("Convert between Jeolla dialect (전라도 사투리) and Standard Korean with one click.")

mode = st.radio(
    "Choose conversion direction:",
    ("Jeolla → Standard", "Standard → Jeolla")
)

text_input = st.text_area("Enter your sentence here:", height=120)

if st.button("Convert"):
    if text_input.strip() == "":
        st.warning("Please enter a sentence first.")
    else:
        # Convert
        mode_key = "j2s" if mode == "Jeolla → Standard" else "s2j"
        result = converter.convert(text_input, mode=mode_key)

        st.subheader("🔄 Converted Result")
        st.success(result)

        # Dialect analysis (only for Jeolla → Standard)
        if mode_key == "j2s":
            analysis = analyzer.analyze(text_input)
            st.subheader("📊 Dialect Analysis")
            st.write(f"**Matched dialect words:** {analysis['matched_tokens']}")
            st.write(f"**Dialect intensity:** {analysis['dialect_intensity']}")