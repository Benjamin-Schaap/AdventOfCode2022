class Solution():

    def __init__(self):
        self.commands = []
        self.valuesWeCareAbout = []
        self.image = []
        self.currentRow = []

    def LoadInput(self, filename):

        file = open(filename)

        for line in file.read().split('\n'):
            
            parts = line.split(' ')

            if parts[0] == 'noop':

                self.commands.append('noop')
            else:

                self.commands.append(int(parts[1]))

    def handleCyclesOfInterest(self, cycle, x):

        match cycle:
                case 20:
                    self.valuesWeCareAbout.append(20 * x)
                case 60:
                    self.valuesWeCareAbout.append(60 * x)
                case 100:
                    self.valuesWeCareAbout.append(100 * x)
                case 140:
                    self.valuesWeCareAbout.append(140 * x)
                case 180:
                    self.valuesWeCareAbout.append(180 * x)
                case 220:
                    self.valuesWeCareAbout.append(220 * x)


    def part1(self):

        cycle = 1
        x = 1

        for command in self.commands:

            if command == 'noop':
                self.handleCyclesOfInterest(cycle, x)
                cycle += 1
                continue
            
            # the first cycle of an addx command, do nothing. We increment cycle up to get to the second part of the addx command.
            # but before that, check to make sure we capture a cycle of interest
            self.handleCyclesOfInterest(cycle, x)
            cycle += 1

            self.handleCyclesOfInterest(cycle, x)
            
            x += command
            cycle += 1

        print(sum(self.valuesWeCareAbout))

    def draw(self, x):

        index = len(self.currentRow)

        if index == x or index + 1 == x or index - 1 == x:
            self.currentRow.append('#')
        else:
            self.currentRow.append('.')

        if len(self.currentRow) == 40:
            self.image.append(self.currentRow)
            self.currentRow = []
        

    
    def part2(self):

        cycle = 1
        x = 1

        for command in self.commands:

            if command == 'noop':
                self.draw(x)
                cycle += 1
                continue
            
            # always draw before the cycle ends, and before x changes.
            self.draw(x)
            cycle += 1

            self.draw(x)
            x += command
            cycle += 1
        
        for row in self.image:
            print(''.join(row))

solution = Solution()
solution.LoadInput("input.txt")
solution.part1()
solution.part2()