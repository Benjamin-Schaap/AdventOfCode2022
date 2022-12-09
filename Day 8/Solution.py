# Not proud of this solution. Got into a time crunch today and decided to brute force it.
# Definitely could have done better.
class Solution():

    def __init__(self):
        self.matrix = []

    def LoadInput(self, filename):
        file = open(filename)

        for row in file.read().split('\n'):

            self.matrix.append(list(row))

    def isVisibleFromTop(self, rowIndex, colIndex, originalValue):

        for index in range(1, len(self.matrix)):

            if rowIndex - index < 0:
                break

            if self.matrix[rowIndex - index][colIndex] >= originalValue:
                return False
        
        return True

    def isVisibleFromBottom(self, rowIndex, colIndex, originalValue):

        for index in range(1, len(self.matrix) - rowIndex):

            if index + rowIndex == len(self.matrix):
                break

            if self.matrix[rowIndex + index][colIndex] >= originalValue:
                return False
        
        return True

    def isVisibleFromLeft(self, rowIndex, colIndex, originalValue):

        for index in range(1, len(self.matrix[0])):

            if colIndex - index < 0:
                break

            if self.matrix[rowIndex][colIndex - index] >= originalValue:
                return False
        
        return True

    def isVisibleFromRight(self, rowIndex, colIndex, originalValue):

        for index in range(1, len(self.matrix[0])):

            if index + colIndex == len(self.matrix[0]):
                break

            if self.matrix[rowIndex][colIndex + index] >= originalValue:
                return False
        
        return True

    def checkNodeVisibility(self, rowIndex, colIndex):

        # return true if we are out of bounds. As far as the algorithm is concerned,
        # and out of bounds values is not taller than the target value.
        if rowIndex < 0 or rowIndex == len(self.matrix):
            return True

        if colIndex < 0 or colIndex == len(self.matrix[0]):
            return True

        originalValue = self.matrix[rowIndex][colIndex]

        # check directions to see if a tree is visible at all
        leftResult = self.isVisibleFromLeft(rowIndex, colIndex, originalValue)
        rightResult = self.isVisibleFromRight(rowIndex, colIndex, originalValue)
        topResult = self.isVisibleFromTop(rowIndex, colIndex, originalValue)
        bottomResult = self.isVisibleFromBottom(rowIndex, colIndex, originalValue)



        # if any direction results in an visible node,  return True
        if leftResult or rightResult or topResult or bottomResult:
            return True
        
        return False

    def part1(self):

        # count the perimiter, since we know all those trees are visible
        visibleTrees = len(self.matrix) * 2
        visibleTrees += (len(self.matrix[0]) - 2) * 2

        rowIndex = 1
        colIndex = 1

        while rowIndex < len(self.matrix) - 1:

            # if the column is about to go out of bounds, reset and move down a row
            if colIndex == len(self.matrix[0]) - 1:
                colIndex = 1
                rowIndex += 1
                continue

            if self.checkNodeVisibility(rowIndex, colIndex):
                # print('Value deemed visible at: ', "row: ", rowIndex, "column", colIndex)
                visibleTrees += 1

            colIndex += 1

        print(visibleTrees)

    def getScenicScoreFromLeft(self, rowIndex, colIndex, originalValue):
        
        score = 0

        for index in range(1, len(self.matrix[0])):

            if colIndex - index < 0:
                break
                
            score += 1

            if self.matrix[rowIndex][colIndex - index] >= originalValue:
                return score
        
        return score

    def getScenicScoreFromRight(self, rowIndex, colIndex, originalValue):

        score = 0

        for index in range(1, len(self.matrix[0])):

            if index + colIndex == len(self.matrix[0]):
                break

            score += 1

            if self.matrix[rowIndex][colIndex + index] >= originalValue:
                return score
        
        return score

    def getScenicScoreFromTop(self, rowIndex, colIndex, originalValue):

        score = 0

        for index in range(1, len(self.matrix)):

            if rowIndex - index < 0:
                break

            score += 1

            if self.matrix[rowIndex - index][colIndex] >= originalValue:
                return score
        
        return score

    def getScenicScoreFromBottom(self, rowIndex, colIndex, originalValue):

        score = 0

        for index in range(1, len(self.matrix) - rowIndex):

            if index + rowIndex == len(self.matrix):
                break

            score += 1

            if self.matrix[rowIndex + index][colIndex] >= originalValue:
                return score
        
        return score

    def checkNodeScenicScore(self, rowIndex, colIndex):
        # return 0 if we are out of bounds. As far as the algorithm is concerned,
        if rowIndex < 0 or rowIndex == len(self.matrix):
            return 0

        if colIndex < 0 or colIndex == len(self.matrix[0]):
            return 0

        originalValue = self.matrix[rowIndex][colIndex]

        scenicTop = 1
        scenicBottom = 1
        scenicRight = 1
        scenicLeft = 1

        # get scores for each direction
        scenicLeft = max(self.getScenicScoreFromLeft(rowIndex, colIndex, originalValue), scenicLeft)
        scenicRight = max(self.getScenicScoreFromRight(rowIndex, colIndex, originalValue), scenicRight)
        scenicTop = max(self.getScenicScoreFromTop(rowIndex, colIndex, originalValue), scenicTop)
        scenicBottom = max(scenicBottom, self.getScenicScoreFromBottom(rowIndex, colIndex, originalValue))

        return scenicLeft * scenicBottom * scenicRight * scenicTop

    def part2(self):

        scenicScore = 0

        rowIndex = 1
        colIndex = 1

        while rowIndex < len(self.matrix):

            # if the column is about to go out of bounds, reset and move down a row
            if colIndex == len(self.matrix[0]):
                colIndex = 1
                rowIndex += 1
                continue

            scenicScore = max(self.checkNodeScenicScore(rowIndex, colIndex), scenicScore)

            colIndex += 1
        
        print(scenicScore)        


solution = Solution()
solution.LoadInput('input.txt')
solution.part1()
solution.part2()