# Very simple first-order logic evaluator

# Define a simple interpretation
interpretation = {
    ('John', 'father', 'Alice'),
    ('Mary', 'mother', 'Alice'),
    ('John', 'father', 'Bob'),
    ('Mary', 'mother', 'Bob')
}

# Define a function to evaluate the statement
def evaluate_statement(subject, relation, object):
    return (subject, relation, object) in interpretation

# Example first-order logic statement: John is the father of Alice
statement = evaluate_statement('John', 'father', 'Alice')

print(f"The statement is {statement}")
