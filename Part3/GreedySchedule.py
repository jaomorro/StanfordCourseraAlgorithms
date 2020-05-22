"""
Greedy algorithms to calculate the most efficient schedule
Most efficient schedule is when the sum of weight * length is minimized
Compares the greedy ratio and greedy diff algorithms
"""

def load_data(filename):
    """
    receives file with data and parses through it
    each line contains weight and length of job
    first line contains the number of jobs which we can ignore
    :param filename: file with data
    :return: list of tuples where each tuple contains weight and length of job
    """

    with open(filename) as f:
        data = f.read().rstrip().split("\n")[1:]
    sched_info = []
    for i in data:
        sched_info.append((int(i.split(" ")[0]), int(i.split(" ")[1])))
    return sched_info

def greedy_ratio(sched_info):
    """
    calcules a score for the schedule by ordering jobs based on greedy ratio
        ratio = weight / length for each job

    :param sched_info: list of tuples where tuples contain weight and length of each job
    :return: score calculated for the schedule
    """
    # loops through schedule info and sorts jobs based on weight to length ratio desc
    sched_order = []
    for info in sched_info:
        weight = info[0]
        length = info[1]
        sched_order.append((weight / length,info))
    sched_order.sort(reverse=True)

    # loops through the schedule and calculates a score
    score = 0
    sched_order_info = []
    running_time = 0 # length is added to running time each loop
    for val in sched_order:
        running_time += val[1][1]
        score += val[1][0] * running_time
        sched_order_info.append(val[1])

    return score, sched_order_info

def greedy_diff(sched_info):
    """
    calcules a score for the schedule by ordering jobs based on greedy diff
        diff = weight - length for each job

    :param sched_info: list of tuples where tuples contain weight and length of each job
    :return: score calculated for the schedule
    """
    # loops through schedule info and sorts jobs based on weight to length diff desc
    sched_order = []
    for info in sched_info:
        weight = info[0]
        length = info[1]
        sched_order.append((weight - length,info))
    sched_order.sort(reverse=True)

    # loops through the schedule and calculates a score
    score = 0
    sched_order_info = []
    running_time = 0 # length is added to running time each loop
    for val in sched_order:
        running_time += val[1][1]
        score += val[1][0] * running_time
        sched_order_info.append(val[1])

    return score, sched_order_info

if __name__ == "__main__":
    filename = "/Users/jimmymorrow/Documents/Misc/problem13.4test.txt"
    sched_info = load_data(filename)
    ratio_score, ratio_sched_order = greedy_ratio(sched_info)
    diff_score, diff_sched_order = greedy_diff(sched_info)
    print(f"ratio score = {ratio_score} schedule order = {ratio_sched_order}")
    print(f"diff score = {diff_score} schedule order = {diff_sched_order}")

