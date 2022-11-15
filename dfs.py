"""
dfs.py

Contains class definition for Dfs
"""

from puzzle import Puzzle

class Dfs(Puzzle):

    """
    Dfs
    """

    def __init__(self):

        """
        Initializes class through user input

        Performs basic input validation
        """

        super().__init__()
        self.index = 0
        self.parent_indices = [0]

    def update(self):

        """
        Updates state variables for solver
        """

        self.index += 1
        self.parent_indices.append(self.index)
        self.state = self.states[self.index]

    def solver(self):

        """
        DFS Solver
        """

        if self.check_state(-1):
            self.print_state(-1)
            return

        while True:

            if self.shift([-1, 0]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                self.update()
                continue

            if self.shift([0, -1]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                self.update()
                continue

            if self.shift([1, 0]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                self.update()
                continue

            if self.shift([0, 1]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                self.update()
                continue

            self.state = self.states[self.parent_indices.pop()]
            print("Depth: ", self.index)

        return


if __name__ == "__main__":
    dfs = Dfs()
    dfs.solver()
