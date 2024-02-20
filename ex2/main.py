def sum_of_elements(arr,exc):
    sum = 0
    if exc:
        for num in arr:
            sum += num
    else:
        for num in arr:
            if num > 0:
                sum += num
    return sum
            

input_string = input("Please input numbers by spaces: ")

exclude_negative = True if input("Do you want to include sum of negative numbers? [yes/no]: ").lower() == "yes" else False

input_list_str = input_string.split()

input_array = [int(num) for num in input_list_str]

answ = sum_of_elements(input_array,exclude_negative)

print(input_array)

print(answ)
