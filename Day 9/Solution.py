class Solution():

    def __init__(self):
        self.moves = []
        self.placesTailHasBeen = {}

        # the algorithm prefers if we can land next to head, not diagonally from it.
        # use the ideal list, then emergency
        self.idealAdjacencyChecks = [[0,1], [0, -1], [1, 0], [-1, 0]]
        self.emergencyAdjacencyChecks = [[1,1], [1, -1], [-1, 1], [-1, -1]]

    def LoadInput(self, filename):
        file = open(filename)

        for move in file.read().split("\n"):

            
            direction, distance = move.split(' ')

            for value in range(int(distance)):
                self.moves.append([direction, 1])


    def isTailAdjacentPreferred(self, headCoord, tailCoord):

        for check in self.idealAdjacencyChecks:

            newCoord = [headCoord[0] + check[0], headCoord[1] + check[1]]

            if tailCoord == newCoord:
                return True
        
        return False

    def isTailAdjecentEmergency(self,headCoord, tailCoord):
        
        for check in self.emergencyAdjacencyChecks:

            newCoord = [headCoord[0] + check[0], headCoord[1] + check[1]]

            if tailCoord == newCoord:
                return True
        return False
    
    def generateNewHeadCoord(self, headCoord, move):

        match move[0]:
            case "U":
                return [headCoord[0] - move[1], headCoord[1]]
            case "D":
                return [headCoord[0] + move[1], headCoord[1]]
            case "L":
                return [headCoord[0], headCoord[1] - move[1]]
            case "R":
                return [headCoord[0], headCoord[1] + move[1]]

    def logTailMovement(self, tailCoord) -> None:

        key = tuple(tailCoord)

        if key in self.placesTailHasBeen:
            pass
        else:
            self.placesTailHasBeen[key] = True

    def findTailsNextLocation(self, headCoord, tailCoord):

        compositChecks = self.idealAdjacencyChecks + self.emergencyAdjacencyChecks

        # there is a way to use head's current location to inform where to look
        # for tail's next position. But out of laziness, I'm just going to check
        # the adjacency lists.
        for check in compositChecks:

            newCoord = [tailCoord[0] + check[0], tailCoord[1] + check[1]].copy()

            if self.isTailAdjacentPreferred(headCoord, newCoord):
                return newCoord

        for check in compositChecks:

            newCoord = [tailCoord[0] + check[0], tailCoord[1] + check[1]].copy()

            if self.isTailAdjecentEmergency(headCoord, newCoord):
                return newCoord
     
    def part1(self):

        headCoord = [0,0]
        tailCoord = [0,0]

        # log starting location
        self.logTailMovement(tailCoord)

        for move in self.moves:

            headCoord = self.generateNewHeadCoord(headCoord, move)

            if tailCoord == headCoord:
                continue

            # see if there's a reason to move the tail
            if self.isTailAdjacentPreferred(headCoord, tailCoord) or self.isTailAdjecentEmergency(headCoord, tailCoord):
                continue

            # otherwise we need to move the tail next to the head
            tailCoord = self.findTailsNextLocation(headCoord, tailCoord)
            self.logTailMovement(tailCoord)

        
        print(len(self.placesTailHasBeen.keys()))
    
    def logLongTailMovement(self, tailCoord) -> None:

        key = 9
        value = tuple(tailCoord)

        if value in self.placesTailHasBeen[key]:
            pass
        else:
            self.placesTailHasBeen[key].append(value)

    def DisplayBoard(self, knotDict):

        board = []

        for i in range(20):
            row = ["."] * 25
            board.append(row)

        for key in knotDict.keys():
            xCoord, yCoord = knotDict[key]

            xCoord = (len(board) // 2) + xCoord
            yCoord = len(board[0]) // 2 + yCoord

            displayLabel = key

            if key == 0:
                displayLabel = "H"

            if board[xCoord][yCoord] == ".":
                board[xCoord][yCoord] = displayLabel

        for row in board:
            print(row)

        print(" * * * * * * * *  *")
    
    def part2(self):

        # key 9 is the tail
        self.placesTailHasBeen = {9: []}

        knotDict = {}
        
        for i in range(0,10):
            knotDict[i] = [0,0]


        # log starting location
        self.logLongTailMovement(knotDict[9])

        for move in self.moves:

            headCoord = self.generateNewHeadCoord(knotDict[0], move)
            knotDict[0] = headCoord.copy()

            for key in knotDict.keys():


                keyCoord = knotDict[key].copy()

                # skip the real head
                if key == 0:
                    continue

                headCoord = knotDict[key - 1].copy()

                # We are exactly where the knot head is, no need to move
                if keyCoord == headCoord:
                    continue

                # see if there's a reason to move the knot
                if self.isTailAdjacentPreferred(headCoord, keyCoord) or self.isTailAdjecentEmergency(headCoord, keyCoord):
                    continue

                # else the knots head moved diagonally, and we need to get a preferred placement.
                knotDict[key] = self.findTailsNextLocation(headCoord, keyCoord)                

                if key == 9:
                    self.logLongTailMovement(knotDict[key])
            
        print(len(self.placesTailHasBeen[9]))


solution = Solution()
solution.LoadInput('input.txt')
solution.part1()
solution.part2()