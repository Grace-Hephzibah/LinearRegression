import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.metrics import mean_squared_error
import plotly.express as px


class A:
    def __init__(self):
        self.count = 0

    def teamA(self):
        st.set_option('deprecation.showPyplotGlobalUse', False)
        df = pd.read_csv("Team1//DAA_DATA.csv")
        st.title("Placement Score Predictor")
        st.image("Team1//pic.png")

        # st.header("Team Name: Team A ")
        st.header("Team Members:\n 1)A P Aishwarya Lakshmi \n \n 2)Prawin R P")
        st.header(
            "About:\n ~ In this project, we are going to discuss how to predict the placement score of a student "
            "based on their using Linear regression algorithm.\n \n ~ This study focuses on a system, that predicts "
            "if a student would be placed or not based on their CGPA. \n \n  ~ This predictor uses a machine-learning "
            "algorithm to give the result.\n \n ~ The algorithm used is Linear regression.\n \n ***Linear "
            "Regression:*** \n \n ~ Linear regression uses the relationship between the data-points to draw a "
            "straight line through all them. \n \n ~ This line can be used to predict future values.")

        st.header("Choose a graph to visualize the data")

        graph = st.selectbox(" ", ["Interactive", "Non-Interactive"], key=self.count)
        self.count += 1

        val = st.slider("Filter Team1 using CGPA", 0.00, 10.00)
        df = df.loc[df["cgpa"] >= val]
        if graph == "Non-Interactive":
            plt.figure(figsize=(10, 5))
            plt.scatter(df["cgpa"], df["placement_score"])
            plt.ylim(0)
            plt.xlabel("CGPA")
            plt.ylabel("Placement Score")
            plt.tight_layout()
            st.pyplot()
        if graph == "Interactive":
            fig = px.scatter(df, x="cgpa", y="placement_score", size_max=200, range_x=[0, 10], range_y=[0, 100])
            fig.update_layout(width=700)
            st.write(fig)

        st.header("Predict Your Placement Score")
        INPUT = st.number_input("Enter your CGPA", 0.00, 10.00)

        x = df.drop('placement_score', axis='columns')
        y = df.drop('cgpa', axis='columns')
        reg = LinearRegression()
        reg.fit(df[['cgpa']], df[['placement_score']])
        predi = reg.predict([[INPUT]])
        if st.button("Predict"):
            st.success(f"Your predicted Placement Score is {predi}")

    def main(self):
        self.teamA()


obj = A()
obj.teamA()
