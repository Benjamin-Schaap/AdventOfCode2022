class Solution():

    def __init__(self):
        self.assignments = []

    def LoadInput(self, filename):
        file = open(filename)

        lines = file.read().split('\n')

        for assignments in lines:

            a1, a2 = assignments.split(',')
            
            a1 = a1.split('-')
            a2 = a2.split('-')

            # Creates a list with 2 sub lists. Each with the low-high value
            # of each sections an elf is assigned.
            self.assignments.append([a1, a2])
        
        print('Finished loading input')
    
    def rangesCompletelyOverlap(self, elf1, elf2):
        
        return int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])

    def rangesOverlapAtAll(self, elf1, elf2):

        # for integer comparisons, this evaluates in O(1) runtime
        if int(elf1[0]) in range(int(elf2[0]), int(elf2[1]) + 1):
            return True
        elif int(elf1[1]) in range(int(elf2[0]), int(elf2[1]) + 1):
            return True


    def part1(self):

        pairCount = 0

        for assignmentGroup in self.assignments:

            elf1, elf2 = assignmentGroup

            if self.rangesCompletelyOverlap(elf1, elf2) or self.rangesCompletelyOverlap(elf2, elf1):
                pairCount += 1
        print(pairCount)
    
    def part2(self):
        pairCount = 0

        for assignmentGroup in self.assignments:

            elf1, elf2 = assignmentGroup

            if self.rangesOverlapAtAll(elf1, elf2) or self.rangesOverlapAtAll(elf2, elf1):
                pairCount += 1
        print(pairCount)

    
 
solution = Solution()
solution.LoadInput('input.txt')
solution.part1()
solution.part2()

