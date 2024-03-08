from logistics_simulation_app import simulate_transport_costs  # Adjust the import statement according to your script structure

def test_average_rail_transport_cost_sydney_melbourne():
    # Predefined values for the test
    locations = {('Sydney', 'Melbourne', 'rail'): 800}  # Assuming 800 km for the rail route
    transport_costs = {'rail': 0.3}  # Assuming $0.3 per km
    n_simulations = 1000  # Number of simulations for the test

    # Run the simulation
    simulated_costs = simulate_transport_costs(locations, transport_costs, ('Sydney', 'Melbourne', 'rail'), 'rail', n_simulations)
    
    # Calculate the average cost from the simulation
    average_cost = sum(simulated_costs) / len(simulated_costs)
    print(f"Simulated average cost: ${average_cost:.2f}")

    # Define expected range (based on your domain knowledge or previous calculations)
    expected_low = 800 * 0.3 * 0.9  # lower bound (10% less than the nominal)
    expected_high = 800 * 0.3 * 1.1  # upper bound (10% more than the nominal)
    
    # Assert that the average cost falls within the expected range
    assert expected_low <= average_cost <= expected_high, f"Average cost {average_cost} out of expected range ({expected_low}-{expected_high})"


