def medical_diagnosis(symptoms):
    # Dictionary mapping symptoms to possible medical conditions
    condition_map = {
        'fever': ['flu', 'common cold', 'pneumonia'],
        'cough': ['flu', 'common cold', 'bronchitis'],
        'headache': ['migraine', 'tension headache', 'sinusitis'],
        'fatigue': ['anemia', 'chronic fatigue syndrome', 'hypothyroidism'],
        'chest pain': ['heart attack', 'angina', 'pericarditis']
    }

    # List to store possible conditions based on symptoms
    possible_conditions = []

    # Check each symptom and find possible conditions
    for symptom in symptoms:
        if symptom in condition_map:
            possible_conditions.extend(condition_map[symptom])

    # Remove duplicate conditions
    possible_conditions = list(set(possible_conditions))

    return possible_conditions

def main():
    print("Welcome to Medical Diagnosis System")
    print("Please enter your symptoms (separated by commas):")
    user_input = input("> ").lower()
    symptoms = [symptom.strip() for symptom in user_input.split(',')]

    possible_conditions = medical_diagnosis(symptoms)

    if possible_conditions:
        print("\nPossible medical conditions based on your symptoms:")
        for condition in possible_conditions:
            print("- " + condition)
    else:
        print("\nNo specific medical conditions found based on your symptoms.")

if __name__ == "__main__":
    main()
