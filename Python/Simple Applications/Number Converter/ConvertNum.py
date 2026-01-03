class ConvertNum:
    def __init__(self, num, num_base, to_base):
        self.num = num
        self.num_base = num_base
        self.to_base = to_base
        self.result = 0
        decimal_num = self.convert_to_decimal(num)
        self.number = ""
        if self.num_base == 10:
            while decimal_num != 0:
                self.number = str(decimal_num % to_base) + self.number
                decimal_num //= to_base
            self.result = int(self.number)
        else:
            self.result = self.convert_to_decimal(self.num)

    def convert_to_decimal(self, num):
        total = 0
        reverse_num = str(num)[::-1]
        for i in range(len(reverse_num)):
            total += int(reverse_num[i]) * (self.num_base ** i)
        return total
