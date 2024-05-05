import itertools

# Function to calculate full joint distribution
def calculate_full_joint_distribution(variables, probabilities):
    full_joint_distribution = {}

    # Generate all possible combinations of variable values
    variable_combinations = list(itertools.product(*variables))

    # Assign probabilities to each combination
    for i, combination in enumerate(variable_combinations):
        full_joint_distribution[combination] = probabilities[i]

    return full_joint_distribution

# Example usage
if __name__ == "__main__":
    # Define variables and their possible values
    temperature_values = ["Hot", "Cold"]
    humidity_values = ["High", "Low"]

    # Specify probabilities for each combination
    probabilities = [0.3, 0.2, 0.1, 0.4]

    # Calculate full joint distribution
    variables = [temperature_values, humidity_values]
    full_joint_distribution = calculate_full_joint_distribution(variables, probabilities)

    # Display the full joint distribution
    print("Full Joint Distribution:")
    for combination, probability in full_joint_distribution.items():
        print(f"P({combination}) = {probability}")
