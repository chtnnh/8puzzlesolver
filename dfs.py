"""
dfs.py

Contains class definition for Dfs
"""

from puzzle import Puzzle

class Dfs(Puzzle):

    """
    Dfs
    """

    def solver(self):

        """
        DFS Solver
        """

        if self.check_state(-1):
            self.print_state(-1)
            return

        index = 0

        while True:

            self.state = self.states[index]

            if self.shift([-1, 0]) and self.check_state(-1):
                print(f"Count: {self.count}")
                break
            if self.shift([0, -1]) and self.check_state(-1):
                print(f"Count: {self.count}")
                break
            if self.shift([1, 0]) and self.check_state(-1):
                print(f"Count: {self.count}")
                break
            if self.shift([0, 1]) and self.check_state(-1):
                print(f"Count: {self.count}")
                break

            index += 1
            print("Depth: ", index)

        return


if __name__ == "__main__":
    dfs = Dfs()
    dfs.solver()
