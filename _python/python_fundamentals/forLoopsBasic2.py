# def biggie_size(this_list):
#     new_arr = []
#     if(isinstance(this_list, list)):
#         for i in this_list:
#             if(i>0):
#                 new_arr.append("big")
#             else:
#                 new_arr.append(i)
#         return(new_arr)
#     else:
#         return(False)
# print(biggie_size([-1, 2, 4, -5]))
# print(biggie_size("hi"))

# def count_positives(this_list):
#     if(isinstance(this_list, list)):
#         count = 0
#         for i in this_list:
#             if(i>0):
#                 count += 1
#         this_list[len(this_list) - 1] = count
#         return(this_list)
#     else:
#         return(False)
# print(count_positives([-1,1,1,1]))
# print(count_positives([1,6,-4,-2,-7,-2]))

# def sum_total(this_list):
#     if(isinstance(this_list, list)):
#         sum = 0
#         for i in this_list:
#             sum += i
#         return(sum)
#     else:
#         return(False)
# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

# def average(this_list):
#     if(isinstance(this_list, list)):
#         average = 0
#         sum = 0
#         for i in this_list:
#             sum += i
#         average = sum/len(this_list)
#         return(average)
#     else:
#         return(False)
# print(average([37,2,1,-9]))
# print(average([1,2,3,4]))

# def length(this_list):
#     if(isinstance(this_list, list)):
#         return(len(this_list))
#     else:
#         return(False)
# print(length([37,2,1,-9]))

# def minimum(this_list):
#     if(isinstance(this_list, list)):
#         min = this_list[0];
#         if(len(this_list)>0):
#             for i in this_list:
#                 if(i<min):
#                     min=i
#             return(min)
#         else:
#             return(False)
#     else:
#         return(False)

# print(minimum([37,2,1,-9]))
# print(minimum([-1, 3, 0, 27]))

# def maximum(this_list):
#     if(isinstance(this_list, list)):
#         if(len(this_list)>0):
#             max=this_list[0]
#             for i in this_list:
#                 if(i>max):
#                     max=i
#             return(max)
#         else:
#             return(False)
#     else:
#         return(False)
# print(maximum([37,2,1,-9]))
# print(maximum([-1, 3, 0, 27]))

# def ultimate_analysis(this_list):
#     if(isinstance(this_list, list)):
#         if(len(this_list)>0):
#             sum=0
#             avg=0
#             min=this_list[0]
#             max=this_list[0]
#             for i in this_list:
#                 sum += i
#                 if(i<min):
#                     min=i
#                 elif(i>max):
#                     max=i
#             avg = sum/len(this_list)
#             return({'sumTotal': sum, 'average': avg, 'minimum': min, 'maximum': max, 'length': len(this_list) })
#         else:
#             return(False)
#     else:
#         return(False)

# print(ultimate_analysis([37,2,1,-9]))

from signal import set_wakeup_fd


def reverse_list(this_list):
    if(isinstance(this_list, list)!=True):
        return(False)
    else:
        if(len(this_list)>1):
            i=len(this_list)-1
            swap = this_list[i]
            k = (int(len(this_list)/2))
            for j in range (0, k, 1):            
                this_list[i] = this_list[j]
                this_list[j] = swap
                i -= 1
                swap = this_list[i]
            return(this_list)
        else:
            return(this_list)
print(reverse_list([37,2,1,-9]))
print(reverse_list([1,2,3,4,5,6,7,8,-2,-5,-10]))
print(reverse_list([]))
print(reverse_list([1,2]))
