class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def query(self, statement):
        if statement in self.facts:
            return True
        for rule in self.rules:
            if rule[0] == statement and all(fact in self.facts for fact in rule[1]):
                return True
        return False


def main():
    kb = KnowledgeBase()

    # Populate the knowledge base with facts
    kb.add_fact("John is a human")
    kb.add_fact("Mary is a human")
    kb.add_fact("John is a parent")
    kb.add_fact("Mary is a parent")
    kb.add_fact("Alice is a child")
    kb.add_fact("Bob is a child")

    # Define rules
    kb.add_rule(("John is a parent", ["John is a human"]))
    kb.add_rule(("Mary is a parent", ["Mary is a human"]))
    kb.add_rule(("Alice is a child", ["John is a parent"]))
    kb.add_rule(("Bob is a child", ["Mary is a parent"]))

    # Query the knowledge base
    print("Is John a parent?", kb.query("John is a parent"))
    print("Is Alice a parent?", kb.query("Alice is a parent"))
    print("Is Bob a child?", kb.query("Bob is a child"))
    print("Is Mary a human?", kb.query("Mary is a human"))
    print("Is Jane a child?", kb.query("Jane is a child"))


if __name__ == "__main__":
    main()
