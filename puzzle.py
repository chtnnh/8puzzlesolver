"""
puzzle.py

Contains class definition for Puzzle state
"""

from copy import deepcopy

class Puzzle:

    """
    class: Puzzle
    Contains the state of the board and helper methods for
    various solvers.

    state: list[list: str]
    states: list[list[list: str]]

    print_state()
    __find_x()
    __check_shift()
    shift()
    check_state()
    """

    def __init__(self):

        # Prompt user to to input matrix
        length = int(input("Enter number of rows: "))
        num = length * length - 1

        print(f"Enter numbers from 1 to {num} and an x for the blank spot as shown below")
        print("Example:")
        print("2 3 x\n1 4 5\n7 8 6")

        rows = []
        for i in range(length):
            rows += [input(f"Row {i + 1}: ").strip().split()]

        # Assert matrix is as expected
        for i in range(length):
            assert len(rows[i]) == length, f"Row {i + 1}: {rows[i]} must contain {length} numbers"

        flattened = sum(rows, [])

        for i in range(1, num + 1, 1):
            assert str(i) in flattened, f"Missing digit: {i}"

        assert "x" in flattened, f'Missing blank slot: "x"'

        self.state = rows
        self.states = [self.state]

        self.goal_state = [str(x) for x in range(1, num + 1, 1)]
        self.goal_state = [self.goal_state[i:i+length] for i in range(0, num + 1, length)]
        self.goal_state[-1].append("x")
        self.count = 0

    def print_state(self, index):
        for row in self.states[index]:
            print_row = ""
            for num in row:
                print_row += num + " "
            print(print_row)
        print()

    def find_x(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == "x":
                    return [i, j]
        return [i, j]

    @staticmethod
    def __check_shift(x_coordinates, change):
        x_pos = x_coordinates[0] + change[0]
        y_pos = x_coordinates[1] + change[1]
        if x_pos >= 0 and x_pos <= 2 and y_pos >= 0 and y_pos <= 2:
            return True
        return False

    def shift(self, change):
        x = self.find_x()
        temp_state = deepcopy(self.state)
        if self.__check_shift(x, change):
            temp_state[x[0] + change[0]][x[1] + change[1]], temp_state[x[0]][x[1]] = temp_state[x[0]][x[1]], temp_state[x[0] + change[0]][x[1] + change[1]]
            self.states.append(temp_state)
            self.print_state(-1)
            return True
        return False

    def check_state(self, index):
        self.count += 1
        return self.states[index] == self.goal_state


if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.print_state(-1)
