class TreeNode():

    def __init__(self):
        self.name = ''
        self.parent = None
        self.directories = {}
        self.files = {}
        self.totalDirSize = 0

class Solution():

    def __init__(self):
        self.root = None
        self.commands = []

    def LoadInput(self, filename):
        file = open(filename)

        for consoleLog in file.read().split('\n'):

            self.commands.append(consoleLog)

    def constructTree(self):

        currentNode = TreeNode()

        for command in self.commands:

            components = command.split(' ')

            if components[0] == '$':
                
                if components[1] == "ls":
                    pass
                elif components[1] == 'cd':
                    
                    if components[2] == '/':
                        self.root = TreeNode()
                        currentNode = self.root
                        self.root.name = 'root'
                    elif components[2] == '..':
                        
                        if currentNode.parent != None:
                            currentNode = currentNode.parent
                        else:
                            parentNode = TreeNode()
                            parentNode.directories[currentNode.name] = currentNode
                            currentNode = parentNode
                    else:
                        currentNode = currentNode.directories[components[2]]

            elif components[0].isnumeric():
                
                fileSize, fileName = components

                if fileName in currentNode.files:
                    pass
                else:
                    currentNode.files[fileName] = fileSize
            elif components[0] == 'dir':
                
                directoryName = components[1]

                if directoryName in currentNode.directories:
                    pass
                else:
                    newDirectory = TreeNode()
                    newDirectory.name = directoryName
                    newDirectory.parent = currentNode
                    currentNode.directories[directoryName] = newDirectory

    def calculateDirectorySizes(self, node: TreeNode):

        for child in node.directories.keys():

            node.totalDirSize += self.calculateDirectorySizes(node.directories[child])

        for file in node.files.keys():

            node.totalDirSize += int(node.files[file])

        return node.totalDirSize

    def part1(self):

        
        if self.root.totalDirSize <= 100000:
            print(self.root.totalDirSize)

        validSum = 0

        bfsStack = []

        for child in self.root.directories.keys():
            bfsStack.append(self.root.directories[child])

        while len(bfsStack) > 0:

            currentNode = bfsStack.pop()


            for child in currentNode.directories.keys():
                bfsStack.append(currentNode.directories[child])

            if currentNode.totalDirSize <= 100000:
                validSum += currentNode.totalDirSize
            
        print(validSum)

    def part2(self):

        totalSpace = 70000000
        required = 30000000
        available = 70000000 - self.root.totalDirSize

        # we are looking for a directory as close to this number as we can get
        target = required - available

        # the size of the directory to achieve target
        smallestDirTo30Mil = self.root.totalDirSize

        bfsStack = []

        for child in self.root.directories.keys():
            bfsStack.append(self.root.directories[child])

        while len(bfsStack) > 0:

            currentNode = bfsStack.pop()

            for child in currentNode.directories.keys():
                bfsStack.append(currentNode.directories[child])

            if currentNode.totalDirSize >= target:
                smallestDirTo30Mil = min(currentNode.totalDirSize, smallestDirTo30Mil)

            
        print(smallestDirTo30Mil)


solution = Solution()
solution.LoadInput('input.txt')
solution.constructTree()
solution.calculateDirectorySizes(solution.root)
solution.part1()
solution.part2()