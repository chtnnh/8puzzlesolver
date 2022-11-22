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

        """
        Initializes class through user input

        Performs basic input validation
        """

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

        assert "x" in flattened, 'Missing blank slot: "x"'

        self.state = rows
        self.states = [self.state]
        self.states_check = {self.flatten(self.state): True}

        self.goal_state = [str(x) for x in range(1, num + 1, 1)]
        self.goal_state = [self.goal_state[i:i+length] for i in range(0, num + 1, length)]
        self.goal_state[-1].append("x")
        self.count = 0

    def print_state(self, index):

        """
        Prints state at self.states[index]
        """

        for row in self.states[index]:
            print_row = ""
            for num in row:
                print_row += num + " "
            print(print_row)
        print()

    @staticmethod
    def __find_x(digit, state):

        """
        Finds and returns position of digit in provided state
        """

        for i in range(3):
            for j in range(3):
                if state[i][j] == digit:
                    return [i, j]
        return [i, j]

    @staticmethod
    def __check_shift(x_coordinates, change):

        """
        Checks if shift is legal
        """

        x_pos = x_coordinates[0] + change[0]
        y_pos = x_coordinates[1] + change[1]

        x_flag = x_pos >= 0 and x_pos <= 2
        y_flag = y_pos >= 0 and y_pos <= 2

        if x_flag and y_flag:
            return True

        return False

    @staticmethod
    def flatten(state):

        """
        Returns identifier string for state_check
        """

        state_identifier = ""
        for row in state:
            state_identifier += "".join(row)
        return state_identifier

    def shift(self, change):

        """
        Perform shift of blank slot with provided change

        Returns True after appending new state to self.states
        if shift is possible and state is new, else returns False
        """

        x_pos = self.__find_x("x", self.state)
        temp_state = deepcopy(self.state)

        if self.__check_shift(x_pos, change):
            temp = temp_state[x_pos[0]][x_pos[1]]
            temp_state[x_pos[0]][x_pos[1]] = temp_state[x_pos[0] + change[0]][x_pos[1] + change[1]]
            temp_state[x_pos[0] + change[0]][x_pos[1] + change[1]] = temp

            temp_state_check = self.flatten(temp_state)

            if temp_state_check not in self.states_check:
                self.states.append(temp_state)
                self.states_check[temp_state_check] = True
                self.print_state(-1)
            else:
                return False

            return True

        return False

    def check_state(self, index):

        """
        Check if provided state is goal state
        """

        self.count += 1
        return self.states[index] == self.goal_state

    def manhattan_distance(self, index):

        """
        Calculate manhattan distance between
        current and goal state
        """

        dist = 0
        for i, row in enumerate(self.states[index]):
            for j, digit in enumerate(row):
                goal_position = self.__find_x(digit, self.goal_state)
                dist += abs(i - goal_position[0]) + abs(j - goal_position[1])

        return dist


if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.print_state(-1)
