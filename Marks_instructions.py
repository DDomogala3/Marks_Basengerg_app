import streamlit as st
import numpy as np
#Hello This is Mark's first app

st.write("Hello this is Mark's first application.")

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

st.chat_input("Say something")
