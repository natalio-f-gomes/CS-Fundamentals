import time

start = time.time()
def Binary_Search(sequence, item):
    begin_index = 0
    end_index = len(sequence) -1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) //2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return f"Fount at index: {midpoint-1}"
        elif midpoint_value < item:
            begin_index = midpoint - 1
        else:
            end_index = midpoint + 1
    return None

sequence_b = [x for x in range(1123323)]
item_b = 123443

print(Binary_Search(sequence_b,item_b))

end = time.time()
print(f"This program took {end-start} miliseconds to operate")
