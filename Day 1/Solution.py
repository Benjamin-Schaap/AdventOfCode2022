import heapq


class Solution:

    def __init__(self):
        self.elfList = []

    def loadInput(self, fileName):
        file = open(fileName)
        elfCalories = 0

        for calories in file.read().split('\n'):

            if calories == '':
                self.elfList.append(elfCalories)
                elfCalories = 0
                pass
            else:
                elfCalories += int(calories)

    def getSingleMostCalories(self):
        print(heapq.nlargest(1, self.elfList)[0])

    def getSumOfTop3Calories(self):

        topThree = heapq.nlargest(3, self.elfList)
        print(sum(topThree))


partOne = Solution()
partOne.loadInput("input.txt")
partOne.getSingleMostCalories()

partTwo = Solution()
partTwo.loadInput("input.txt")
partTwo.getSumOfTop3Calories()
