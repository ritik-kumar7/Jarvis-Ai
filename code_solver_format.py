import streamlit as st
from utils.code_solver import CodeSolver  # Adjust path if needed

solver = CodeSolver()

user_input = st.text_input("Ask Jarvis for code:")

if user_input:
    response = solver.handle(user_input)

    # Safe way to display code
    if response.startswith("```"):
        # Extract lang and code
        lang = response.split("\n")[0].replace("```", "")
        code = "\n".join(response.split("\n")[1:-1])
        st.code(code, language=lang)
    else:
        st.markdown(response)
