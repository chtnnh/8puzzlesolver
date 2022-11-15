"""
a_star.py

Contains class definition for A*
"""

from puzzle import Puzzle

class AStar(Puzzle):

    """
    A*
    """

    def solver(self):

        """
        A* Solver
        """

        if self.check_state(-1):
            self.print_state(-1)
            return

        index = 0

        while True:

            self.state = self.states[index]
            distances = []
            count = 0

            if self.shift([-1, 0]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                count += 1

            if self.shift([0, -1]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                count += 1

            if self.shift([1, 0]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                count += 1

            if self.shift([0, 1]):
                if self.check_state(-1):
                    print(f"Count: {self.count}")
                    break
                count += 1

            for i in range(count):
                distances.append([self.manhattan_distance(-1-i), i])
                distances.sort(key=lambda x: x[0])

            if count > 1:
                append = self.states[-count:]
                for i in range(int(count / 2)):
                    append[distances[i][1]], append[i] = append[i], append[distances[i][1]]
                self.states[-count:] = append

            index += 1
            print("Depth: ", index)

        return


if __name__ == "__main__":
    a_star = AStar()
    a_star.solver()
