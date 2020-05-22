"""
Knapsack problem
"""


def load_data(filename):
    """
     load data to be used into a file

     :param file_name: file to load the data to
            Data is received as value, weight
     :return: list of data returned as (weight, value)
     """

    with open(filename) as f:
        data = f.read().strip("\n").split("\n")
        data_list = list([x.split(" ") for x in data])
        data_list = list([[int(x[1]),int(x[0])] for x in data_list])
    return data_list


def knapsack_vals(data,total_weight):
    """
    finds the max value of items that are under the total weight

    :param data : list of lists with weights and values of items
    :param total_weight : max weight
    :return : list of lists with [weight, values] of items that are in knapsack
    """
    result_matrix = [] # num cols is total weight and num rows is num items
    for i in range(len(data)):
        result_matrix.append(list([0 if x == 0 else None for x in range(total_weight + 1)]))

    for i in range(len(result_matrix)):
        weight = data[i][0]
        value = data[i][1]
        if i == 0:
            for j in range(len(result_matrix[0])):
                if weight > j:
                    result_matrix[i][j] = 0
                else:
                    result_matrix[i][j] = value
        else:
            for j in range(len(result_matrix[0])):
                if weight > j:
                    result_matrix[i][j] = result_matrix[i-1][j]
                else:
                    val1 = (value + result_matrix[i-1][j-weight])
                    val2 = result_matrix[i-1][j]
                    result_matrix[i][j] = max(val1,val2)

    result_values = []
    cols = len(result_matrix[0])-1
    rows = len(result_matrix)-1
    weight_cnt = 0
    while rows >= 0:
        if result_matrix[rows][cols] == 0:
            break
        if result_matrix[rows][cols] > result_matrix[rows-1][cols]:
            result_values.append(rows)
            weight_cnt = data[rows][0]
            cols -= weight_cnt
        rows -= 1
    knapsack_values = [data[x] for x in result_values]
    return knapsack_values

if __name__ == "__main__":
    data = load_data("Data/KnapsackData.txt")
    total_weight = data[0][1]
    vals = knapsack_vals(data[1:],total_weight)
    optimal_value = 0
    for i in vals:
        optimal_value += i[1]
    print(f"optimal_value = {optimal_value}")

