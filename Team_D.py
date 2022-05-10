import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
#import statsmodels.api as sm
#statsmodels==0.13.2

class team4:
    def prediction(self, x1):
        return 9.7758 * x1 + 2.4837

    def main(self):
        # st.title("DAA PROJECT ")
        # st.header("TEAM WHISTLEPODU")
        st.header("Predicting the Exam Scores when its hours are provided ")
        st.markdown("Team members :  \n"
                    "Nikhil  \n"
                    "John Moses  \n")

        # st.image("mesh-gradient.png")

        st.header("ABOUT ")
        st.write("Project based on Linear regression. ")
        st.markdown("Given the number of hrs of study - prediction of exam score   \n   \n"
                    "Enter the hours and our ML model will predict the scores obtained in the exam")

        st.header("PREDICTION")
        '''
        data = pd.read_csv('Team4//data.csv') #('Vechiko.csv')
        # data
        # Dependent Variable
        y = data['Hours']
        # Independent Variable
        x1 = data['Scores']
        plt.scatter(x1, y)
        plt.xlabel('Hours')
        plt.ylabel('Scores')
        plt.show()
        # Regression Equation
        # yhat = b0 + b1*x1

        x = sm.add_constant(x1)
        results = sm.OLS(y, x).fit()
        results.summary()
        plt.scatter(x1, y)
        # y = mx + c
        # const - c - 0.2750
        # mx - m = 0.0017
        yhat = 9.7758 * x1 + 2.4837
        fig = plt.plot(x1, yhat)  # c = "orange"

        plt.xlabel('Hours')
        plt.ylabel('Scores')
        plt.show()
        '''
        num1 = st.number_input('Enter hours', step=0.5, min_value=0.0)
        st.write('Score = ', self.prediction(num1))


a = team4()
a.main()
