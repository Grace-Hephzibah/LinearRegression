import streamlit as st


class team4:

    def SourceCode(self):
        st.title("DAA PROJECT ")
        st.header("TEAM D")
        st.subheader("Predicting the cost of an apartment when its dimensions are provided ")
        st.markdown("Team members :  \n"
                    "Kanishk  \n"
                    "Varun  \n")

        # st.image("mesh-gradient.png")

        st.header("ABOUT ")
        st.write("Project based on Linear regression. ")
        st.markdown("Given the size of the apartment(length and the width) - predicting the cost of the given "
                    "apartment.   \n   \n "
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                    "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                    "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
                    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
                    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

        st.header("PREDICTION")

        txt = st.text_input("Type something to get displayed below : ")
        st.write(txt)
        num1, num2 = st.columns(2)
        num1 = num1.number_input('Enter length', step=0.5)
        num2 = num2.number_input('Enter breadth ', step=0.5)
        res = num1 * num2
        st.write('The area = ', res)

    def main(self):
        self.SourceCode()
