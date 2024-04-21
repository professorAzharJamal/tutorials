class Predicate:
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __str__(self):
        return f"{self.name}/{self.arity}"


class Term:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Atom:
    def __init__(self, predicate, terms):
        self.predicate = predicate
        self.terms = terms

    def __str__(self):
        return f"{self.predicate}({', '.join(str(term) for term in self.terms)})"


class Interpretation:
    def __init__(self, domain, predicates):
        self.domain = domain
        self.predicates = predicates

    def evaluate_atom(self, atom):
        if atom.predicate.name in self.predicates:
            return atom.predicate.name in self.predicates and len(atom.terms) == atom.predicate.arity
        else:
            return False


def main():
    # Define domain and predicates
    domain = {'John', 'Mary', 'Alice', 'Bob'}
    predicates = {'Father': 2, 'Mother': 2, 'Parent': 2}

    # Create interpretation
    interpretation = Interpretation(domain, predicates)

    # Define terms
    john = Term('John')
    mary = Term('Mary')
    alice = Term('Alice')
    bob = Term('Bob')

    # Define predicates
    father_predicate = Predicate('Father', 2)
    mother_predicate = Predicate('Mother', 2)
    parent_predicate = Predicate('Parent', 2)

    # Define atoms
    father_john_alice = Atom(father_predicate, [john, alice])
    mother_mary_bob = Atom(mother_predicate, [mary, bob])
    parent_john_alice = Atom(parent_predicate, [john, alice])

    # Evaluate atoms
    print(f"Is '{father_john_alice}' true? {interpretation.evaluate_atom(father_john_alice)}")
    print(f"Is '{mother_mary_bob}' true? {interpretation.evaluate_atom(mother_mary_bob)}")
    print(f"Is '{parent_john_alice}' true? {interpretation.evaluate_atom(parent_john_alice)}")


if __name__ == "__main__":
    main()
