# Define the rules for the expert system
rules = [
    {
        "features": {"rock_type": "granite", "mineral_content": "high", "faults": "few"},
        "site": "High potential for drilling"
    },
    {
        "features": {"rock_type": "sandstone", "mineral_content": "moderate", "faults": "moderate"},
        "site": "Moderate potential for drilling"
    },
    {
        "features": {"rock_type": "shale", "mineral_content": "low", "faults": "many"},
        "site": "Low potential for drilling"
    },
    {
        "features": {"rock_type": "limestone", "mineral_content": "high", "faults": "few"},
        "site": "High potential for drilling"
    }
]

# Function to find the drilling potential based on geological features
def find_drilling_potential(rock_type, mineral_content, faults):
    for rule in rules:
        if (rule["features"]["rock_type"] == rock_type and 
            rule["features"]["mineral_content"] == mineral_content and 
            rule["features"]["faults"] == faults):
            return rule["site"]
    return "No potential site found"

# Main function to run the expert system
def main():
    # Example geological features input
    rock_type = input("Enter rock type (granite, sandstone, shale, limestone): ").strip().lower()
    mineral_content = input("Enter mineral content (low, moderate, high): ").strip().lower()
    faults = input("Enter faults (few, moderate, many): ").strip().lower()
    
    # Find the drilling potential based on geological features
    potential = find_drilling_potential(rock_type, mineral_content, faults)
    
    # Display the potential site
    print(f"Drilling Potential: {potential}")

# Run the main function
if __name__ == "__main__":
    main()
