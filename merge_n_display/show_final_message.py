from popups import alert_popup, listToString

def show_up(coverset_list):
    # coverset_list: contains list data denoting coversets in each grid cell
    result_coverset = []
    length = len(coverset_list)
    time_of_work = 0
    index = 0
    k = 0
    small = 100000
    while true:
        for i in range(length):
            if coverset_list[i][0][1] < small:
                small = coverset_list[i][0][1]
                index = i
    
        for i in range(length):
            coverset_list[i][0][1] -= small
            if coverset_list[i][0][1] <= 0:
                result_coverset[k].append(coverset_list[i][0][0])
                coverset_list[i].pop(0)

        k += 1
        time_of_work += small
        for i in range(length):
            if len(coverset_list[i]) == 0:
                # Coversets done,..
                alert_popup("Final Observation:-", "Time " + str(time_of_work), listToString(result_coverset))

