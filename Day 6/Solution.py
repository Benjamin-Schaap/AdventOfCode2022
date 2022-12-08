class Solution():

    def part1(self, filename):
        file = open(filename)

        previousChars = []
        charIndex = 0

        for char in file.read():
            
            if char in previousChars:
                previousChars = []
            else:
                previousChars.append(char)

                if len(previousChars) == 4:
                    file.close()
                    return charIndex
            
            charIndex += 1
        
    def part2(self, filename):
        file = open(filename)

        previousChars = []
        charIndex = 1

        for char in file.read():
            
            
            if char in previousChars:

                previousChars.append(char)

                poppedChar = previousChars.pop(0)
                
                while poppedChar != char:
                    poppedChar = previousChars.pop(0)
            else:
                previousChars.append(char)

                if len(previousChars) == 14:
                    file.close()
                    return charIndex
            
            charIndex += 1

solution = Solution()
print(solution.part1("input.txt"))
print(solution.part2("input.txt"))

