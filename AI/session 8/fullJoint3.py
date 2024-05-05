# Define the full joint distribution as a dictionary
# Key: tuple representing the assignment of variables (A, B, C)
# Value: probability of that assignment
full_joint_distribution = {
    (True, True, True): 0.1,
    (True, True, False): 0.05,
    (True, False, True): 0.05,
    (True, False, False): 0.1,
    (False, True, True): 0.2,
    (False, True, False): 0.1,
    (False, False, True): 0.2,
    (False, False, False): 0.2
}

# Function to compute the marginal probability of a variable
def marginal_probability(variable_index, value, joint_distribution):
    marginal_prob = 0
    for assignment, probability in joint_distribution.items():
        if assignment[variable_index] == value:
            marginal_prob += probability
    return marginal_prob

def main():
    # Compute the marginal probability of variable C being true
    marginal_prob_C_true = marginal_probability(2, True, full_joint_distribution)
    print("Marginal probability of variable C being true:", marginal_prob_C_true)

    # Compute the conditional probability of variable A being true given that B is true
    conditional_prob_A_true_given_B_true = 0
    total_prob_B_true = marginal_probability(1, True, full_joint_distribution)
    for assignment, probability in full_joint_distribution.items():
        if assignment[1] == True:  # B is true
            if assignment[0] == True:  # A is true
                conditional_prob_A_true_given_B_true += probability
    conditional_prob_A_true_given_B_true /= total_prob_B_true
    print("Conditional probability of variable A being true given B is true:", conditional_prob_A_true_given_B_true)

if __name__ == "__main__":
    main()
