# Для рекламы продукта было решено использовать блогеров, однако денег на рекламу выделили ограниченное количество.
# Поэтому для каждого блогера в массиве nums написали числовое значение - стоимость покупки рекламы у него.
# Стоимость может быть и отрицательной, значит блогер еще доплатит нам за рекламу.
# Рекламу нужно заказать ровно у трех блогеров. При этом сумма их значений должна быть
# наиболее близкой к целевому значению target. На выходе нужно получить сумму значений стоимости у выбранных блогеров

# nums - Массив чисел, определяющих стоимость рекламы каждого блогера
# target - Целевое значение
def closest_sum(nums, target):
    COUNT_BLOGGERS = 3
    if len(nums) <= COUNT_BLOGGERS:
        return sum(nums)

    list_of_list_elements = []

    def recurs_create_list_elements(array, count=0):
        if count >= len(nums):
            return array

        new_list = []
        count_for = 0

        for i, el in enumerate(nums):

            if count_for >= COUNT_BLOGGERS:
                break
            i += count

            if i == len(nums):
                new_list.append(nums[0])
                count_for += 1

            elif i + 1 > len(nums):
                new_list.append(nums[1])
                count_for += 1

            else:
                new_list.append(nums[i])
                count_for += 1

        array.append(sum(new_list))
        return recurs_create_list_elements(array, count + 1)

    recurs_create_list_elements(list_of_list_elements)

    def find_near_number(array):
        min_difference = 0
        near_sum = 0

        for value in array:
            difference = target - value
            if min_difference == 0:
                min_difference = difference
                near_sum = value

            elif abs(difference) < abs(min_difference):
                min_difference = difference
                near_sum = value
            else:
                continue
        return near_sum

    return find_near_number(list_of_list_elements)


print(closest_sum([-1, 2, 1, -4], 1))   # expected value 2
print(closest_sum([0, 0, 0], 1))    # expected value 0
print(closest_sum([0, 1, 2], 3))    # expected value 3
print(closest_sum([1, 1, 1, 1], 4))     # expected value 3
print(closest_sum([1, 1, 1, 0], -100))  # expected value 2
print(closest_sum([1, 1, 1, 0], 100))   # expected value 3
print(closest_sum([0, 2, 1, -3], 1))    # expected value 0

