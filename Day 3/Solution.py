class Solution:

    def __init__(self):
        self.items = []
        self.badgeGroups = []

    def loadInput(self, fileName):
        file = open(fileName)

        badgeGroup = []

        for rucksack in file.read().split('\n'):

            # this code is for finding the badge groups
            badgeGroup.append(rucksack)

            if len(badgeGroup) == 3:
                self.badgeGroups.append(badgeGroup.copy())
                badgeGroup = []

            
            # this code is for finding the items in a rucksack
            splitPoint = len(rucksack) // 2

            itemOne = rucksack[0:splitPoint]
            itemTwo = rucksack[splitPoint:]

            self.items.append(self.findCommonChar(itemOne, itemTwo))

    def findCommonChar(self, itemOne, itemTwo):

        charDict = {}

        for char in itemOne:
            charDict[char] = True
        
        for char in itemTwo:
            if char in charDict:
                # since there is always one match, we know it's safe to return now
                return char
    
    def findAllCommonChars(self, group):

        charDict = {}
        
        rucksackOne, rucksackTwo, rucksackThree = group

        for char in rucksackOne:
            charDict[char] = 1
        

        for char in rucksackTwo:
            if char in charDict:
                charDict[char] = 2
        
        for char in rucksackThree:

            # we found a match with 2 values already existing. 
            if char in charDict and charDict[char] == 2:
                return char


    def calculatePriority(self, list):

        value = 0

        lowercaseBaseValue = ord('a') - 1
        uppercaseBaseValue = ord("A") - 27


        for item in list:
            
            if item.isupper() == True:
                value += ord(item) - uppercaseBaseValue
            else:
                value += ord(item) - lowercaseBaseValue

        return value
    
    def part1(self):
        print("Part 1 value: ", self.calculatePriority(self.items))

    def part2(self):

        badges = []

        for group in self.badgeGroups:
            badges.append(self.findAllCommonChars(group))
        
        print("Part 1 value: ", self.calculatePriority(badges))


solution = Solution()
solution.loadInput("input.txt")
solution.part1()
solution.part2()
                
