class Indenter:
    def __init__(self):
        self.indent_multiplier = 0

    def __enter__(self):
        self.indent_multiplier += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_multiplier -= 1

    def print(self, text: str) -> None:
        print(f'{" "*self.indent_multiplier}{text}')


if __name__ == '__main__':
    with Indenter() as ind:
        ind.print("It's indent level 1")
        with ind:
            ind.print("It's indent level 2")
            with ind:
                ind.print("It's indent level 3")
            ind.print("It's indent level 2 again")
        ind.print("It's indent level 1 again")
