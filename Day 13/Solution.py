class Solution():

    def __init__(self):
        self.pairs = []

    def LoadInput(self, filename):
        file = open(filename)

        left = None
        right = None

        for line in file.read().split('\n'):

            if line == '':
                continue

            if left == None:

                if line == '[]':
                    left = []
                else:
                    left = eval(line)
            else:
                if line == '[]':
                    right = []
                else:
                    right = eval(line)

                self.pairs.append([left.copy(), right.copy()])
                left = None
                right = None


    def isOrdered(self, left, right):

        for i in range(min(len(left), len(right))):

            leftItem = left[i]
            rightItem = right[i]

            if isinstance(leftItem, int) and isinstance(rightItem, int):

                if leftItem < rightItem:
                    return True
                if leftItem > rightItem:
                    return False
                
                # if they're equal values, do nothing
                continue

            if isinstance(leftItem, list) and isinstance(rightItem, list):
                answer = self.isOrdered(leftItem, rightItem)

                if answer is not None:
                    return answer
                continue

            # at this point, one is a list and one is an int, and we need to compute the int as a list
            if isinstance(leftItem, int):
                leftItem = [leftItem]
            if isinstance(rightItem, int):
                rightItem = [rightItem]

            answer = self.isOrdered(leftItem, rightItem)

            if answer is not None:
                    return answer

        if len(left) < len(right):
            return True

        if len(right) < len(left):
            return False




    def part1(self):

        rightOrderedIndices = []

        for index, pair in enumerate(self.pairs):

            left = pair[0]
            right = pair[1]

            if self.isOrdered(left, right):
                rightOrderedIndices.append(index + 1)


        print(sum(rightOrderedIndices))


    def part2(self):

        packets = [[[2]], [[6]]]

        for pair in self.pairs:

            packets.append(pair[0])
            packets.append(pair[1])
        
        sortedPackets = []
        sortedPackets.append(packets.pop())

        while len(packets) > 0:

            packet = packets.pop()
            
            # yeah this is pretty garbage code. I should refactor this
            for i in reversed(range(len(sortedPackets))):

                if not self.isOrdered(packet, sortedPackets[i]):
                    sortedPackets.insert(i + 1, packet)
                    break

            if packet not in sortedPackets:
                sortedPackets.insert(0, packet)

        print((sortedPackets.index([[2]]) + 1) * (1 + (sortedPackets.index([[6]]))))




solution = Solution()
solution.LoadInput('input.txt')
solution.part1()
solution.part2()