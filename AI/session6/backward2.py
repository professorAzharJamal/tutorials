class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = {}

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, goal, conditions):
        self.rules[goal] = conditions

    def query(self, goal):
        return self.backward_chain(goal, set())

    def backward_chain(self, goal, visited):
        if goal in visited:
            return False

        visited.add(goal)

        if goal in self.facts:
            return True

        if goal in self.rules:
            conditions = self.rules[goal]
            for condition in conditions:
                if not self.backward_chain(condition, visited):
                    return False
            return True

        return False


def main():
    kb = KnowledgeBase()

    # Populate the knowledge base with facts
    kb.add_fact("Applicant has good credit score")
    kb.add_fact("Applicant has stable income")

    # Define rules
    kb.add_rule("Loan Approved", ["Applicant has good credit score", "Applicant has stable income"])
    kb.add_rule("Applicant has good credit score", ["Applicant has no history of defaults"])
    kb.add_rule("Applicant has stable income", ["Applicant is employed"])

    # Query the knowledge base
    print("Loan Approval Decision:", kb.query("Loan Approved"))


if __name__ == "__main__":
    main()
