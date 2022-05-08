import streamlit as st


class team4:
    def prediction(self, x1):
        return 223.1787 * x1 + 1.019e+05

    def main(self):
        # st.title("DAA PROJECT ")
        # st.header("TEAM D")
        st.header("Predicting the cost of an apartment when its dimensions are provided ")
        st.markdown("Team members :  \n"
                    "Kanishk  \n"
                    "Varun  \n")

        # st.image("mesh-gradient.png")

        st.header("ABOUT ")
        st.write("Project based on Linear regression. ")
        st.markdown("Given the size of the apartment(area) - predicting the cost of the given apartment.   \n   \n"
                    "Enter the area and our ML model will predict the cost of the apartment")

        st.header("PREDICTION")

        num1 = st.number_input('Enter area', step=0.5, min_value=300.0)
        st.write('The price = ', self.prediction(num1))

        # st.table(new_data)


a = team4()
a.main()
