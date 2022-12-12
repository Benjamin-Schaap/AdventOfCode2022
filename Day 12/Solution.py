class Solution():

    def __init__(self):
        self.grid = []
        self.endingCoord = None
        self.directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

    def LoadInput(self, filename):
        file = open(filename)

        for line in file.read().split('\n'):

            row = []

            for cell in list(line):
                
                if cell == 'E':
                    self.endingCoord = (len(self.grid), len(row))

                row.append(cell)

            self.grid.append(row)

    def isValidToAddToStack(self, newRow, newCol, currentHeight):
        
        # don't add to stack if out of bounds
        if newRow < 0 or newRow >= len(self.grid) or newCol < 0 or newCol >= len(self.grid[0]):
            return False

        # if it's an int, we already processed it
        if type(self.grid[newRow][newCol]) == int:
            return False

        futureHeight = self.grid[newRow][newCol]

        if futureHeight == 'S':
            futureHeight = 'a'

        heightDifference = ord(currentHeight) - ord(futureHeight)

        if heightDifference < 2:

            return True
        
        return False


    def getAnswer(self, target):

        row = self.endingCoord[0]
        col = self.endingCoord[1]

        visited = {}

        self.grid[row][col] = 0

        visited[(row, col)] = True

        bfsStack = []

        for direction in self.directions:

            newRow = row + direction[0]
            newCol = col + direction[1]
            
            if self.isValidToAddToStack(newRow, newCol, 'z'):
                bfsStack.append((newRow, newCol, 0))

        while len(bfsStack) > 0:

            cell = bfsStack.pop(0)
            row, col, priorDistance = cell

            visited[(row, col)] = True

            currentHeight = self.grid[row][col]

            # we found our answer
            if currentHeight == target:
                print('ANSWER', priorDistance + 1)
                return
            else:
                self.grid[row][col] = priorDistance + 1

                # add new directions for the bfs stack
                for direction in self.directions:

                    newRow = row + direction[0]
                    newCol = col + direction[1]
                    
                    if self.isValidToAddToStack(newRow, newCol, currentHeight):

                        if (newRow, newCol) in visited.keys() or (newRow, newCol, priorDistance + 1) in bfsStack:
                            continue
                        else:
                            bfsStack.append((newRow, newCol, priorDistance + 1)) 


solution = Solution()
solution.LoadInput('input.txt')
solution.getAnswer('S')
solution.LoadInput('input.txt')
solution.getAnswer('a')

