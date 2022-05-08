import streamlit as st

import Team_A as a1
import Team_B as a2
import Team_C as a3

from text import TEXT

st.sidebar.title("Linear Regression")

page_option = st.sidebar.radio("Options",
                               ["Intro", "Team - 1", "Team - 2", "Team - 3"],
                               )

if page_option == "Intro":
    st.title("Introduction")
    st.image('img.jpg')
    st.write(TEXT)
'''
elif page_option == "Team - 1":
    A = a1.A()
    A.main()

elif page_option == "Team - 2":
    B = a2.Team()
    B.main()

elif page_option == "Team - 3":
    C = a3.team4()
    C.main()
'''