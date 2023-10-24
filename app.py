import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_trajectory():
    # Define the initial conditions
    x0 = 0  # initial position in x-direction
    y0 = 0.07336  # initial position in y-direction
    x_velocity0 = -1.8 * np.sin(np.deg2rad(10))  # initial velocity in x-direction
    y_velocity0 = -1.8 * np.cos(np.deg2rad(10))  # initial velocity in y-direction

    # Define the time range and step size
    t = np.arange(0, 5, 5/120)

    # Calculate the position x as a function of time t
    x_acceleration = (-430 / 505) * (x_velocity0 + 3 * np.cos(np.pi / 36)) + 9.8 * np.sin(np.pi / 18)
    x = x0 + x_velocity0 * t + (1/2) * x_acceleration * t**2

    # Calculate the position y as a function of time t
    y_acceleration = (-9089 / 505) * y_velocity0 - (430 / 505) * (y_velocity0 + 3 * np.sin(np.pi / 36)) + 9.8 * np.cos(np.pi / 18)
    y = y0 + y_velocity0 * t + (1/2) * y_acceleration * t**2

    # Plot x, y, x_velocity, and y_velocity against time
    st.figure(figsize=(10, 8))

    st.subplot(2, 2, 1)
    st.plot(t, x)
    st.xlabel('Time')
    st.ylabel('Position x')
    st.title('Position x vs Time')
    st.grid(True)

    st.subplot(2, 2, 2)
    st.plot(t, y)
    st.xlabel('Time')
    st.ylabel('Position y')
    st.title('Position y vs Time')
    st.grid(True)

    st.subplot(2, 2, 3)
    st.plot(t, x_velocity0 + x_acceleration * t)
    st.xlabel('Time')
    st.ylabel('Velocity x')
    st.title('Velocity x vs Time')
    st.grid(True)

    st.subplot(2, 2, 4)
    st.plot(t, y_velocity0 + y_acceleration * t)
    st.xlabel('Time')
    st.ylabel('Velocity y')
    st.title('Velocity y vs Time')
    st.grid(True)

    st.tight_layout()
    st.show()

@st.cache
def main():
    plot_trajectory()

if __name__ == '__main__':
    main()
