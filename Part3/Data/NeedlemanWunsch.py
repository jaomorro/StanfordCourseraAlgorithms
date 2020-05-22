"""
Needleman-Wunsch application of the sequence alignment problem
Determines how similiar two strings are
"""


def seq_align(string1,string2,mismatch_penalty,gap_penalty):
    """
    Applies Needlam-Wunsch algorithm to strings and returns the strings with
        any gaps applied and their NW score
    Lower the score, more similar the strings
    If strings are not the same length, "-"'s are used to make up difference
    Algorithm determines the optimal placement of any dashes

    :param string1: string to compare
    :param string2: string to compare
    :param mismatch_penalty: penalty for mismatched characters
    :param gap_penalty: penalty for leaving a gap in string
    :return: string1 and string2 with any gaps applied
            NW score
    """

    # define 2x2 matrix
    matrix = []
    for i in range(len(string1)+1):
        if i == 0:
            matrix.append(list([gap_penalty * x for x in range(len(string2)+1)]))
        else:
            matrix.append(list([gap_penalty * i if x == 0 else None for x in range(len(string2)+1)]))

    # populate matrix by looping through the strings and finding optimal value for each spot
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                val1 = 0 + matrix[i][j]
            else:
                val1 = mismatch_penalty + matrix[i][j]
            val2 = gap_penalty + matrix[i][j+1]
            val3 = gap_penalty + matrix[i+1][j]
            min_val = min(val1,val2,val3)
            matrix[i+1][j+1] = min_val


    # define values to use while retracing
    result_str1 = ''
    result_str2 = ''
    i = len(matrix)-1
    j = len(matrix[0])-1

    # trace through matrix to find the optimal character alignment
    while i > 0 and j > 0:
        val1 = matrix[i-1][j-1]
        val2 = matrix[i-1][j]
        val3 = matrix[i][j-1]
        min_val = min(val1,val2,val3)
        if val1 == min_val:
            result_str1 += string1[i-1]
            result_str2 += string2[j-1]
            i -= 1
            j -= 1
        elif val2 == min_val:
            result_str1 += "-"
            result_str2 += string2[j-1]
            i -= 1
        else:
            result_str1 += string1[i-1]
            result_str2 += "-"
            j -= 1

    # for any leftover j values
    if i == 0:
        while j > 0:
            result_str1 += '-'
            result_str2 += string2[j]
            j -=1

    # for any leftover i values
    if j == 0:
        while i > 0:
            result_str1 += string1[i]
            result_str2 += "-"
            i -= 1

    return matrix[len(matrix)-1][len(matrix[0])-1], result_str1[::-1], result_str2[::-1]


if __name__ == "__main__":
    string1 = "AGGGCT"
    string2 = "AGGCA"
    mismatch_penalty = 3
    gap_penalty = 2 # must be non-negative
    score,result_str1,result_str2 = seq_align(string1,string2,mismatch_penalty,gap_penalty)
    print(f"score = {score}")
    print(f"string1 = {result_str1}")
    print(f"string2 = {result_str2}")


