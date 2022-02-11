# def countdown(num):
#     this_list = []
#     for i in range(num, -1, -1):
#         this_list.append(i)
#     return(this_list)
# print(countdown(5))

# def print_and_return(num1, num2):
#     print(num1)
#     return(num2)
# print(print_and_return(3, 6))

# def first_plus_length(my_list):
#     if isinstance(my_list, list):
#         return(my_list[0] + len(my_list))
# print(first_plus_length([2,3,4,5]))

# def values_greater_than_second(this_list):
#     new_list = []
#     count = 0
#     if isinstance(this_list, list):
#         if(len(this_list)>2):
#             for i in this_list:
#                 if(i>this_list[1]):
#                     count += 1
#                     new_list.append(i)
#             print(count)
#             return(new_list)
#         else:
#             return(False)
#     else:
#         return(False)
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([2]))
# print(values_greater_than_second("Hello there"))

def this_length_that_value(size, value):
    new_arr = []
    for i in range(0, size):
        new_arr.append(value)
    return(new_arr)
print(this_length_that_value(7, 4))
print(this_length_that_value(2,10))