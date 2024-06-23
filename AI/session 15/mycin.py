# Define the rules for the expert system
rules = [
    {
        "if": {"symptoms": ["fever", "cough", "sore throat"]},
        "then": {"disease": "Streptococcal Pharyngitis", "antibiotic": "Penicillin"}
    },
    {
        "if": {"symptoms": ["fever", "cough", "shortness of breath"]},
        "then": {"disease": "Pneumonia", "antibiotic": "Amoxicillin"}
    },
    {
        "if": {"symptoms": ["nausea", "vomiting", "diarrhea"]},
        "then": {"disease": "Gastroenteritis", "antibiotic": "Metronidazole"}
    },
    {
        "if": {"symptoms": ["headache", "stiff neck", "fever"]},
        "then": {"disease": "Meningitis", "antibiotic": "Ceftriaxone"}
    },
]

# Function to match symptoms with rules
def diagnose(symptoms):
    for rule in rules:
        if set(rule["if"]["symptoms"]).issubset(set(symptoms)):
            return rule["then"]["disease"], rule["then"]["antibiotic"]
    return "Unknown", "No recommendation"

# Main function to run the expert system
def main():
    # Example symptoms input
    symptoms = input("Enter the symptoms separated by commas: ").split(", ")
    
    # Diagnose based on symptoms
    disease, antibiotic = diagnose(symptoms)
    
    # Display the diagnosis and recommendation
    print(f"Diagnosis: {disease}")
    print(f"Recommended Antibiotic: {antibiotic}")

# Run the main function
if __name__ == "__main__":
    main()
