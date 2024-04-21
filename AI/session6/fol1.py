# Simple first-order logic evaluator

class Interpretation:
    def __init__(self):
        self.domain = {'John', 'Mary', 'Alice', 'Bob'}

    def is_father_of(self, x, y):
        return (x, y) in {('John', 'Alice'), ('John', 'Bob')}

    def is_mother_of(self, x, y):
        return (x, y) in {('Mary', 'Alice'), ('Mary', 'Bob')}


def main():
    interpretation = Interpretation()

    # Example first-order logic statement: John is the father of Alice
    statement = interpretation.is_father_of('John', 'Alice')
    statement2 = interpretation.is_father_of('John', 'Mary')

    print(f"The statement is {statement}")
    print(f"The statement is {statement2}")


if __name__ == "__main__":
    main()
