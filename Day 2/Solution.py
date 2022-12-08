class Solution:

    # A - rock, B - Paper, C - Scissors
    # X - rock, Y - paper, Z Scissors

    def __init__(self):
        self.matches = []
        self.winningMatchups = {
        "A": "Z",
        "B": "X",
        "C": "Y",
        "Y": "A",
        "X": "C",
        "Z": "B"}

        self.bonusDict = {
        "X": 1,
        "Y": 2,
        "Z": 3
        }

        self.strategyGuideMeaning = {
            "X": "lose",
            "Y": "draw",
            "Z": "win"
        }

    def loadInput(self, fileName):
        file = open(fileName)

        for match in file.read().split('\n'):

            self.matches.append(match)


    def part1(self):
        
        score = 0

        for match in self.matches:

            opponent, guideChoice = match.split(' ')

            if self.winningMatchups[guideChoice] == opponent:

                score += 6 + self.bonusDict[guideChoice]
            elif self.winningMatchups[opponent] == guideChoice:

                score += self.bonusDict[guideChoice]
            else:
                score += 3 + self.bonusDict[guideChoice]

        print(score)
    
    def part2(self):
        score = 0

        for match in self.matches:

            opponent, guideChoice = match.split(' ')

            if self.strategyGuideMeaning[guideChoice] == "win":

                winningChoice = "0"

                if self.winningMatchups["X"] == opponent:
                    winningChoice = "X"
                elif self.winningMatchups["Y"] == opponent:
                    winningChoice = "Y"
                else:
                    winningChoice = "Z"

                score += 6 + self.bonusDict[winningChoice]
            elif self.strategyGuideMeaning[guideChoice] == "lose":

                losingChoice = self.winningMatchups[opponent]

                score += self.bonusDict[losingChoice]
            else:
                score += 3

                match opponent:
                    case "A":
                        score += 1
                    case "B": 
                        score += 2
                    case "C":
                        score += 3

        print(score)

scoreCalculator = Solution()
scoreCalculator.loadInput("input.txt")
scoreCalculator.part2()
