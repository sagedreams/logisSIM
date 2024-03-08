import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to simulate transportation costs
def simulate_transport_costs(locations, transport_costs, route, method, n_simulations):
    distance = locations.get(route, 0)
    cost_per_km = transport_costs.get(method, 0)
    simulated_costs = [np.random.uniform(cost_per_km * 0.9, cost_per_km * 1.1) * distance for _ in range(n_simulations)]
    return simulated_costs

# Streamlit app UI
st.title('Logistics Network Simulation')

# Sidebar for user inputs
st.sidebar.header('Setup Parameters')

# User inputs for locations and distances
st.sidebar.subheader('Locations and Distances')
default_locations = 'Sydney-Melbourne,880\nSydney-Brisbane,920\nMelbourne-Brisbane,1650'
user_locations = st.sidebar.text_area("Enter locations and distances (format: 'City1-City2,Distance')", value=default_locations)

# Parse user input into dictionary
locations = {}
for line in user_locations.split('\n'):
    parts = line.split(',')
    if len(parts) == 2:
        route, distance = parts
        locations[tuple(route.split('-'))] = float(distance)

# User inputs for transport costs
st.sidebar.subheader('Transportation Costs')
road_cost = st.sidebar.number_input('Road Cost per Km', min_value=0.0, value=0.5)
rail_cost = st.sidebar.number_input('Rail Cost per Km', min_value=0.0, value=0.3)

transport_costs = {'road': road_cost, 'rail': rail_cost}

# Select route
route = st.selectbox('Select Route', options=list(locations.keys()))
# Select transportation method
method = st.selectbox('Select Transportation Method', options=['road', 'rail'])
# Number of simulations
n_simulations = st.slider('Number of Simulations', min_value=100, max_value=1000, value=500)

# Button to run simulation
if st.button('Simulate Transportation Costs'):
    simulated_costs = simulate_transport_costs(locations, transport_costs, route, method, n_simulations)
    average_cost = sum(simulated_costs) / len(simulated_costs)
    st.write(f"Average {method} transport cost for {'-'.join(route)}: ${average_cost:.2f}")

    # Histogram of simulated costs using matplotlib
    fig, ax = plt.subplots()
    ax.hist(simulated_costs, bins=30, alpha=0.5)
    ax.set_xlabel('Cost')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Simulated Costs')
    st.pyplot(fig)

