# Define symptoms and possible causes
symptoms = {
    "engine_wont_start": {
        "cause1": "dead_battery",
        "question1": "Are the headlights dim or off?"
    },
    "car_makes_noise": {
        "cause1": "loose_belt",
        "question1": "Is there a squealing sound coming from the engine?"
    },
    "car_overheats": {
        "cause1": "low_coolant",
        "question1": "Is the coolant level low?"
    }
}

# Function to diagnose the problem
def diagnose(symptoms_list):
  for symptom in symptoms_list:
    cause = symptoms[symptom]["cause1"]  # Assuming single cause for simplicity
    question = symptoms[symptom]["question1"]
    answer = input(question + " (yes/no): ")
    if answer.lower() == "yes":
      return cause
  return "Unknown problem. Consult a mechanic."

# Get user input for symptoms
user_symptoms = []
print("Select symptoms from the list (enter 'done' when finished):")
for symptom in symptoms.keys():
  print(symptom)
while True:
  user_input = input("Enter symptom: ")
  if user_input.lower() == "done":
    break
  elif user_input in symptoms.keys():
    user_symptoms.append(user_input)
  else:
    print("Invalid symptom. Please choose from the list.")

# Diagnose the problem
diagnosis = diagnose(user_symptoms)

# Print the diagnosis
print("Your car problem might be caused by:", diagnosis)

