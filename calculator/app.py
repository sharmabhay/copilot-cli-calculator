"""Streamlit web UI for the calculator."""

import streamlit as st
from calculator.parser import evaluate, UNARY_FUNCTIONS

st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("🧮 Calculator")

tab_basic, tab_advanced, tab_expression = st.tabs(["Basic", "Advanced", "Expression"])

with tab_basic:
    col1, col2 = st.columns(2)
    a = col1.number_input("Left operand", value=0.0, key="basic_a")
    b = col2.number_input("Right operand", value=0.0, key="basic_b")
    op = st.selectbox("Operator", ["+", "-", "*", "/", "**", "%", "//"])
    if st.button("Calculate", key="basic_calc"):
        try:
            result = evaluate(f"{a} {op} {b}")
            st.success(f"= {result}")
        except ValueError as e:
            st.error(str(e))

with tab_advanced:
    func = st.selectbox("Function", list(UNARY_FUNCTIONS.keys()))
    x = st.number_input("Value", value=0.0, key="adv_x")
    if st.button("Calculate", key="adv_calc"):
        try:
            result = evaluate(f"{func}({x})")
            st.success(f"= {result}")
        except ValueError as e:
            st.error(str(e))

with tab_expression:
    expr = st.text_input("Expression", placeholder="e.g. 2 ** 10 or sqrt(16)")
    if st.button("Evaluate", key="expr_calc"):
        if expr:
            try:
                result = evaluate(expr)
                st.success(f"= {result}")
            except ValueError as e:
                st.error(str(e))
