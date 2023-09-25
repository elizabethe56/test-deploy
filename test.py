import streamlit as st
import pandas as pd
import numpy as np

# if 's' not in st.session_state:
#         st.session_state.s = False
# st.write(st.session_state)
write_text = 'A'
if 'write_text' not in st.session_state:
    st.session_state.write_text = 0
def test():
    # if st.session_state.s:
    #     st.session_state.s = False
    # else:
    #     st.session_state.s = True
    st.session_state.write_text += 1
    return

st.button('AHHH', on_click=test())

# if not st.session_state.s:
st.write(''.join([write_text, st.session_state.write_text * 'HHH']))