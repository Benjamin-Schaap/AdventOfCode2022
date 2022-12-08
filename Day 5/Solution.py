class Solution():

    def __init__(self):
        self.crateColumns = {}
        self.craneCommands = []

    def LoadInput(self, filename):
        file = open(filename)

        lines = file.read().split('\n')
        lineIndex = 0

        while True:

            # manage where we are in the file ourselves. The reason for this is because after the 
            # crate visualization has been parsed, new parsing needs to take place on the crane operator
            # commands. We will break out of this loop when the visualization ends.
            stackLevel = lines[lineIndex]
            lineIndex += 1

            stackLevel = stackLevel.split(' ')
            
            # this is where the crate visualization ends and the column labels begin
            if stackLevel[1] == '1':
                break

            # the column a particular crate is on.
            column = 0

            # every 4 empty strings makes up the space of one 'column'. Thus, if we encounter
            # 4 empty strings, we know there wasn't a crate at that level, for that column
            emptyStringCount = 0

            for value in stackLevel:

                if value == '':
                    emptyStringCount += 1

                    if emptyStringCount == 4:
                        column += 1
                        emptyStringCount = 0
                elif value.isnumeric():
                    break
                elif value[1].isalpha():
                    emptyStringCount = 0

                    # we found a new crate, index which column it belongs to
                    column += 1

                    if column in self.crateColumns:
                        self.crateColumns[column].append(value[1])
                    else:
                        self.crateColumns[column] = [value[1]]
        
        # now that the input is loaded, reverse the lists for each level so that they are ordered properly
        for key in self.crateColumns.keys():
            self.crateColumns[key].reverse()

        # clear past the empty whitespace line
        lineIndex += 1

        while lineIndex < len(lines):

            line = lines[lineIndex]
            lineIndex += 1

            self.parseCommands(line)
            
    # takes a line and parses out the numeric values. Creates a list of three values that represent (in order):
    #   * the number of crates to move
    #   * the crate column we're moving from
    #   * the crate column we're moving to
    #
    # The list is then added to self.craneCommands to be reused.
    def parseCommands(self, line):
        values = line.split(' ')

        commandList = []

        for value in values:

            if value.isnumeric():
                commandList.append(int(value))

        self.craneCommands.append(commandList)

    def part1(self):
        
        # rearrange the crates
        for commands in self.craneCommands:

            numberOfCratesToMove = commands[0]
            startingColumn = commands[1]
            destinationColumn = commands[2]

            for i in range(numberOfCratesToMove):

                crate = self.crateColumns[startingColumn].pop()
                self.crateColumns[destinationColumn].append(crate)
        
        # get the top crate from each column
        topCrateString = ''

        for i in range(1, 10):

            topCrateString = topCrateString + self.crateColumns[i][-1]

        print(topCrateString)

    def part2(self):
        
        # rearrange the crates
        for commands in self.craneCommands:

            # making the number of crates to move negative makes indexing easier
            numberOfCratesToMove = commands[0] * -1
            startingColumn = commands[1]
            destinationColumn = commands[2]
                
            crates = self.crateColumns[startingColumn][numberOfCratesToMove:].copy()
            self.crateColumns[destinationColumn].extend(crates)
            del self.crateColumns[startingColumn][numberOfCratesToMove:]

        
        # get the top crate from each column
        topCrateString = ''

        for i in range(1, 10):

            topCrateString = topCrateString + self.crateColumns[i][-1]

        print(topCrateString)



solution = Solution()
solution.LoadInput('input.txt')
solution.part1()

solution2 = Solution()
solution2.LoadInput('input.txt')
solution2.part2()