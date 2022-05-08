import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


class Team:

    def teamdp(self):
        st.title("Salary Predictor")

        st.image("Team2//salary.jpg", width=700)

        st.header("Team Members")

        st.markdown('''
           - David Raj
           - Prakash
           ''')
        st.header("What is salary predictor")

        st.write(
            "The graphical representation of predicting salary is a process that aims for developing computerized "
            "system to maintain all the daily work of salary growth graph in any field and can predict salary after a "
            "certain time period.")
        st.write(
            "The purpose of this project is to use Team1 transformation and machine learning to create a model that "
            "will predict a salary when given years of experience,This model can be used as a guide when determining "
            "salaries since it shows reasonable predictions when given information on years of experience.")
        st.header("Methods Used")

        st.markdown('''
    - Data Visualization
    - Linear Regression

    ''')

        st.header("Technologies/Libraries Used")

        st.markdown('''
    - Streamlit
    - Python 3
    - Pandas
    - NumPy 
    ''')

        st.header("Information Used To Predict Salaries")

        st.write(
            "Years Experience: How many years of experience is taken as input and the expected output will be the "
            "salary.")

        st.header("Let's Predict Your Salary")

        val = st.number_input("Enter your experience", 0.00, 20.00, step=0.25)
        # ml model
        df = pd.read_csv("Team2//data.csv")
        x = df.drop('Salary', axis='columns')
        y = df.drop('YearsExperience', axis='columns')
        reg = LinearRegression()
        reg.fit(df[['YearsExperience']], df.Salary)  # training model
        predict = reg.predict([[val]])

        if st.button("Predict Salary"):
            st.success(f"Your predicted salary is {predict}")

    def main(self):
        self.teamdp()
