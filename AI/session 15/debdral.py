# Define the rules for the expert system
rules = [
    {
        "fragments": ["CH4"],
        "mass": 16,
        "structure": "Methane"
    },
    {
        "fragments": ["C2H6"],
        "mass": 30,
        "structure": "Ethane"
    },
    {
        "fragments": ["C3H8"],
        "mass": 44,
        "structure": "Propane"
    },
    {
        "fragments": ["C4H10"],
        "mass": 58,
        "structure": "Butane"
    },
    {
        "fragments": ["C2H5OH"],
        "mass": 46,
        "structure": "Ethanol"
    },
]

# Function to infer the structure from mass
def infer_structure(mass):
    for rule in rules:
        if rule["mass"] == mass:
            return rule["structure"]
    return "Unknown structure"

# Main function to run the expert system
def main():
    try:
        # Example mass input
        mass = int(input("Enter the mass of the molecule: "))
        
        # Infer the structure based on mass
        structure = infer_structure(mass)
        
        # Display the inferred structure
        print(f"Inferred Structure: {structure}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the main function
if __name__ == "__main__":
    main()
