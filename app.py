# save this as app.py and run using: streamlit run app.py 

# This is just for having the idea how GUI works from an ameture's point of view with the help of chatGPT

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Function Plotter")

# Function selector
func_name = st.selectbox(
    "Choose a function to plot:",
    ("sin(x)", "cos(x)", "exp(x)", "tan(x)", "log(x)")
)

# Range inputs
x_min = st.number_input("x min", value=-10.0)
x_max = st.number_input("x max", value=10.0)

# Ensure valid range
if x_min >= x_max:
    st.error("x min must be less than x max.")
else:
    x = np.linspace(x_min, x_max, 1000)

    # Map selected function to actual NumPy function
    if func_name == "sin(x)":
        y = np.sin(x)
    elif func_name == "cos(x)":
        y = np.cos(x)
    elif func_name == "exp(x)":
        y = np.exp(x)
    elif func_name == "tan(x)":
        y = np.tan(x)
        y[np.abs(y) > 10] = np.nan  # clip large tan(x) values
    elif func_name == "log(x)":
        x = np.linspace(max(x_min, 0.01), x_max, 1000)
        y = np.log(x)

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"{func_name}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    st.pyplot(fig)
