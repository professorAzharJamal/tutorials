from collections import defaultdict

# Define probability distribution function (PDF) for a single variable
def pdf(variable, value):
    # Replace this with your actual probability distribution function
    # This is a placeholder for demonstration purposes
    return 1 / len(variable.values)

# Define the joint probability distribution (JPD)
def joint_pdf(variables, values):
    # Initialize the joint probability
    joint_prob = 1.0

    # Iterate over each variable and its value
    for variable, value in values.items():
        joint_prob *= pdf(variable, value)

    return joint_prob

# Example: Simple weather and sprinkler model
variables = {
    "Weather": {"Sunny": 0.6, "Rainy": 0.4},
    "Sprinkler": {"On": 0.2, "Off": 0.8},
}

# Example evidence: Sprinkler is On
evidence = {"Sprinkler": "On"}

# This program doesn't perform inference yet, but demonstrates the basic structure

# Print the variables and their possible values
print("Variables:")
for variable, values in variables.items():
    print(f"\t{variable}: {', '.join(values.keys())}")

# Print the evidence (if any)
if evidence:
    print("Evidence:")
    for variable, value in evidence.items():
        print(f"\t{variable}: {value}")

