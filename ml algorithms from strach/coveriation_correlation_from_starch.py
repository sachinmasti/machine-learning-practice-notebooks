
# def sub_array(lst,k)->int:
    
#     prefix_sum = 0
#     len_array = 1

#     for i in range(1,len(lst)):
#         prefix_sum =  lst[i] + lst[i-1]
#         len_array +=1
        
#         if prefix_sum == k:
#             return len_array

#     return None

# lst = [1, 2, 3, 1, 1, 1, 1]
# k = 5
# print(sub_array(lst,k))

# import numpy as np
# import random
# import time
# start_time = time.time()
# print(np.arange(1,10))
# end_time = time.time()

# print(start_time - end_time)

# start_time = time.time()
# print(range(1,10))
# end_time = time.time()
# print(start_time - end_time)

# start_time = time.time()
# print(np.random.randint(1, 10, 10))
# end_time = time.time()
# print(start_time - end_time)
