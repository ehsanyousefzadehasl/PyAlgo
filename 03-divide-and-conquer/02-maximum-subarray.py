class  Answer:
    left = -1
    right = -1
    value = 0
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        return str(self.left) + " " + str(self.right) + " " + str(self.value)


def maximum_crossing_sub_array(a, left, mid, right):
    max_left = -10000000000
    sum = 0
    index_left = left
    for i in range(mid, left - 1, -1):
        sum += a[i]
        if sum > max_left:
            max_left = sum
            index_left = i
        
    max_right = -10000000000
    sum = 0
    index_right = right
    for i in range(mid + 1, right + 1, 1):
        sum += a[i]
        if sum > max_right:
            max_right = sum
            index_right = i
    return Answer(index_left, index_right, max_left + max_right)


def maximum_sub_array(a, left, right):
    if left == right:
        return Answer(left, right, a[left])
    else:
        mid = (left + right) // 2
        left_ans = maximum_sub_array(a, left, mid)
        right_ans = maximum_sub_array(a, mid + 1, right)
        cross_ans = maximum_crossing_sub_array(a, left, mid, right)
        
        if left_ans.value >= right_ans.value and left_ans.value >= cross_ans.value:
            return left_ans
        elif right_ans.value >= left_ans.value and right_ans.value >= cross_ans.value:
            return right_ans
        else:
            return cross_ans
        
        
        
a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(maximum_sub_array(a, 0, len(a) - 1))