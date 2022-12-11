class Monkey():

    def __init__(self):
        self.items = []
        self.operation = None
        self.divisibleTest = None
        self.cases = []

class Solution():

    def __init__(self):
        self.monkeyList = {}

    def LoadInput(self, filename):
        file = open(filename)

        currentMonkey = 0

        for line in file.read().split('\n'):

            parts = line.split(' ')

            # use list compression to remove empty strings
            parts = [ part for part in parts if part != '']

            # if parts was a blank line in the input file, skip
            if parts == []:
                continue

            match parts[0]:
                case 'Monkey':
                    self.monkeyList[int(parts[1][0])] = Monkey()
                    currentMonkey = int(parts[1][0])

                case'Starting':

                    # cycle through each item, after the first two items 
                    for i in range (2, len(parts)):

                        itemNumber = parts[i]

                        # if the number has a comma in the input text, remove it
                        if ',' in parts[i]:
                            itemNumber = parts[i].replace(',', '')

                        self.monkeyList[currentMonkey].items.append(int(itemNumber))
                case 'Operation:':

                    # we start on parts index 3 because the first parts are 'operation:', 'new', '=', and 'old'
                    # which is not useful information for us because it occurs for every monkey.
                    self.monkeyList[currentMonkey].operation = parts[4:]
                case 'Test:':
                    self.monkeyList[currentMonkey].divisibleTest = int(parts[3])
                case 'If':
                    self.monkeyList[currentMonkey].cases.append(int(parts[5]))

    def printMonkeys(self):

        for key in self.monkeyList.keys():

            monkey = self.monkeyList[key]

            print("Monkey", key)
            print("Starting Items", monkey.items)
            print("Operation", monkey.operation)
            print("Test", monkey.divisibleTest)
            print("Cases", monkey.cases)
            print('- - - - - - - -')

    def calculateOperation(self, operation, item, relief):

        modifier = 0

        # setup the modifier for the operation
        if operation[1] == 'old':
            modifier = item
        else:
            modifier = int(operation[1])
        
        # because monkeys always get bored, divide any value by 3
        match operation[0]:

            case '*':
                return (item * modifier) // relief
            case '-':
                return (item - modifier) // relief
            case '+':
                return (item + modifier) // relief
            case '/':
                return (item // modifier) // relief
                
    def determineNewOwner(self, item, monkey):

        # if the test passes, return the success case
        if item % monkey.divisibleTest == 0:
            return monkey.cases[0]
        
        return monkey.cases[1]
        
    def getSolution(self, rounds, relief):

        monkeyInspections = {}

        for key in self.monkeyList.keys():

            monkeyInspections[key] = 0
        
        # simulate X rounds
        for i in range(rounds):
            print('round', i)

            for key in self.monkeyList.keys():

                monkey = self.monkeyList[key]

                monkeyInspections[key] += len(monkey.items)

                for i in range(len(monkey.items)):

                    item = monkey.items.pop(0)

                    item = self.calculateOperation(monkey.operation, item, relief)

                    newOwnerKey = self.determineNewOwner(item, monkey)

                    self.monkeyList[newOwnerKey].items.append(item)
        
        values = sorted(monkeyInspections.values())
        print(values)

        print(values[-1] * values[-2])



solution = Solution()
solution.LoadInput('input.txt')
solution.getSolution(20, 3)
solution.getSolution(10000, 1)