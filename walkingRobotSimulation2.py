# A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".
#
# The robot can be instructed to move for a specific number of steps. For each step, it does the following.
#
# Attempts to move forward one cell in the direction it is facing.
# If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
# After the robot finishes moving the number of steps required, it stops and awaits the next instruction.
#
# Implement the Robot class:
#
# Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
# void step(int num) Instructs the robot to move forward num steps.
# int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
# String getDir() Returns the current direction of the robot, "North", "East", "South", or "West"
#
#
# Input
# ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
# [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
# Output
# [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]
#
# Explanation
# Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
# robot.step(2);  // It moves two steps East to (2, 0), and faces East.
# robot.step(2);  // It moves two steps East to (4, 0), and faces East.
# robot.getPos(); // return [4, 0]
# robot.getDir(); // return "East"
# robot.step(2);  // It moves one step East to (5, 0), and faces East.
#                 // Moving the next step East would be out of bounds, so it turns and faces North.
#                 // Then, it moves one step North to (5, 1), and faces North.
# robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
# robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
#                 // Then, it moves four steps West to (1, 2), and faces West.
# robot.getPos(); // return [1, 2]
# robot.getDir(); // return "West

from typing import List
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # 0 north, 1 west, 2 south, 3 east
        self.direction = 3
        self.delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        self.x = 0
        self.y = 0

    def step(self, num: int) -> None:
        if num == 0:
            return
        # bypass the loops by modding the number of steps of a circle, -4 is to off count the double counted corners
        num = num % (self.width * 2 + self.height * 2 - 4)
        if num == 0:  # if after mode num is 0, still need to go one circle, note you don't know where x, y is atm
            num = self.width * 2 + self.height * 2 - 4
        while num > 0:
            if self.inbounds(self.x + self.delta[self.direction][0], self.y + self.delta[self.direction][1]):
                self.x = self.x + self.delta[self.direction][0]
                self.y = self.y + self.delta[self.direction][1]
                num -= 1
            else:
                self.direction = (self.direction + 1) % 4

    def inbounds(self, x, y) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def getPos(self) -> List[int]:
        return [self.x, self.y]


    def getDir(self) -> str:
        return {0: "North", 1: "West", 2: "South", 3: "East"}[self.direction]


if __name__ == '__main__':
    r = Robot(2, 3)
    print(r.getPos())
    print(r.getDir())
    r.step(24)
    print(r.getDir())
    print(r.getPos())
