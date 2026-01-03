class TwoNum:
    def __init__(self, lst: list, target: int):
        self.add_pairs = []
        self.sub_pairs = []
        self.even_nums = []
        self.lst = lst
        self.target = target

    def TwoSum(self):
        for i in range(len(self.lst)):
            for j in range(1, len(self.lst)):
                if self.lst[i] + self.lst[j] == self.target:
                    self.add_pairs.append((i, j))
        for pair in self.add_pairs:
            print(f"The pairs that add to {self.target} are: {pair[0] + 1} and {pair[1] + 1}")

    def TwoSub(self):
        for i in range(len(self.lst)):
            for j in range(1, len(self.lst)):
                if self.lst[i] - self.lst[j] == self.target:
                    self.sub_pairs.append((i, j))
        for pair in self.sub_pairs:
            print(f"The pairs that subtract each other to result {self.target} are: {pair[0] + 1} and {pair[1] + 1}")

    def EvenNum(self, nums):
        self.nums = nums
        self.even_nums = []
        for i in range(1, len(nums)):
            if i % 2 == 0:
                self.even_nums.append(i)
        print(f"Even numbers: {self.even_nums}")
