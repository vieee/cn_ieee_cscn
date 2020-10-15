from popups import alert_popup, listToString
import numpy as np
import copy

def show_up(coverset_list):
  # coverset_list: contains list data denoting coversets in each grid cell
  result_coverset = [] # data of list addn
  time_coverset = [] # time of final addn
  length = len(coverset_list)
  time_of_work = 0 # time breakpoints array
  index = 0
  k = 0
  small = 100000
  least_timer = float("inf")
  
  for r in coverset_list:
    # print(r, np.sum(r)[1])
    ctr = 0
    for x in r:
      ctr += x[1]

    least_timer = min(least_timer, ctr)
  # print(least_timer)

  while time_of_work < least_timer:
    small = float("inf")
    for i in range(length):
      small = min(small, coverset_list[i][0][1])
    print("small", small)
    
    temp = []
    for i in range(length):
      temp.append(copy.deepcopy(coverset_list[i][0]))
      coverset_list[i][0][1] -= small
      if coverset_list[i][0][1] <= 0:
        # result_coverset.
        coverset_list[i].pop(0)
    print(temp, time_of_work)
    

    # k += 1
    result_coverset.append(temp) # coverset data addn
    time_coverset.append(small) # time of addn
    time_of_work += small
    # print(time_of_work)
  
  print("result_array", result_coverset)
  print("time_array", time_coverset)
  # alert_popup("Final Observation:-", "Time " + str(least_timer), result_coverset)
  #     if len(coverset_list[i]) == 0:
  #       # Coversets done,..
  #       print("fin: ", result_coverset)

        
show_up([
        #  00
         [
          [10, 1], [12, 2], [13, 5], [19, 8]
         ],
        #  01
         [
          [13, 2], [14, 8], [10, 1]
         ],
        #  11
         [
          [12, 3], [15, 3], [14, 2], [10, 8]
         ]
])
