# Define the rules for the expert system
rules = [
    {
        "requirements": {"cpu": "i7", "ram": "16GB", "storage": "1TB"},
        "configuration": "High-Performance Configuration"
    },
    {
        "requirements": {"cpu": "i5", "ram": "8GB", "storage": "512GB"},
        "configuration": "Mid-Range Configuration"
    },
    {
        "requirements": {"cpu": "i3", "ram": "4GB", "storage": "256GB"},
        "configuration": "Basic Configuration"
    },
    {
        "requirements": {"cpu": "i7", "ram": "32GB", "storage": "2TB"},
        "configuration": "Ultra High-Performance Configuration"
    }
]

# Function to find the configuration based on requirements
def find_configuration(cpu, ram, storage):
    for rule in rules:
        if (rule["requirements"]["cpu"] == cpu and 
            rule["requirements"]["ram"] == ram and 
            rule["requirements"]["storage"] == storage):
            return rule["configuration"]
    return "No matching configuration found"

# Main function to run the expert system
def main():
    # Example requirements input
    cpu = input("Enter CPU (i3, i5, i7): ").strip()
    ram = input("Enter RAM (4GB, 8GB, 16GB, 32GB): ").strip()
    storage = input("Enter Storage (256GB, 512GB, 1TB, 2TB): ").strip()
    
    # Find the configuration based on requirements
    configuration = find_configuration(cpu, ram, storage)
    
    # Display the configuration
    print(f"Configuration: {configuration}")

# Run the main function
if __name__ == "__main__":
    main()
