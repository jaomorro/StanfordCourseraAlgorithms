from itertools import combinations, permutations
from copy import copy
from collections import defaultdict
import time
import math

def read_data(filename):
    """
    Reads and organizes the data from file

    :param filename : file path to read data from
    :return : list of arrays with vertices
    """

    with open(filename) as f:
        data = f.readlines()
    data_list = []
    for i in range(1,len(data)):
        data_list.append((float(data[i].split(" ")[1]), float(data[i].split(" ")[2].strip("\n"))))
    return data_list

def euclidean_dist(vert1, vert2):
    """
    Finds euclidean distance between two points

    :param vert1 : x,y coords for vertice
    :param vert2 : x,y coords for vertice
    :return : distance between two vertices
    """

    dist = math.sqrt((float(vert1[0]) - float(vert2[0])) ** 2 + (float(vert1[1]) - float(vert2[1])) ** 2)
    return dist

def destination(min_dist, total_dist, visited_cnt, index_city_start, visited):
    """
    Calculates and sets parameters once it is determined what city (vertice) is to be visited next

    :param min_dist : list with the vertice to be visited and dist between current vert and this one
    :param total_dist : total dist travelled thus far between all the vertices
    :param visited_cnt : # of cities that have been visited thus far
    :param index_city_start : fiorst index in coords that has not been visited. This will get updated
                        if it is equal to the index of the new city being visited
    :param visited : list of length equal to # of coords. Indexes are initialized to F alse
                        and then updated to True once visited
    :return : curr_city, total_dist, visited_cnt, index_city_start, visited
    """

    total_dist += min_dist[1]
    visited_cnt += 1
    visited[min_dist[0]] = True
    if index_city_start == min_dist[0]:
        index_city_start += 1
        while visited[index_city_start] == True:
            index_city_start += 1
            if index_city_start == len(coords):
                break
    curr_city = min_dist[0]
    return curr_city, total_dist, visited_cnt, index_city_start, visited

if __name__ == "__main__":

    coords = read_data("Data/TSP2.txt")

    # initialize parameters
    start_time = time.time()
    visited = [False for x in range(len(coords))]
    visited_cnt = 0
    total_dist = 0
    curr_city = 0
    index_city_start = 1

    # loop throu coords until you have visited all of them
    # coords are sorted by x-coord so we do not need to find dist between each set of points in universe
    # for current coord loop through the next coords until dist between x-coords > min distance between
    #   coords up to tha point because dist between ponts has to be greater than dist between x-coords
    while visited_cnt < len(coords)-1:
        vert1 = coords[curr_city]
        new_vertex_start = index_city_start
        # start at fist point that has not been visited yet
        while new_vertex_start < len(coords):
            vert2 = coords[new_vertex_start]
            # must set a min dist when comparing curr city to fist city
            if new_vertex_start == index_city_start:
                min_dist = [new_vertex_start,euclidean_dist(vert1, vert2)]
            else: # subsequent cities check x-coords and set new min dist if necessary or set a new destination
                x_dist = abs(vert1[0] - vert2[0])
                if x_dist <= min_dist[1]:
                    new_dist = euclidean_dist(vert1,vert2)
                    if new_dist < min_dist[1]:
                        min_dist = [new_vertex_start,new_dist]
                else:
                    curr_city, total_dist, visited_cnt, index_city_start, visited = destination(min_dist, total_dist, visited_cnt, index_city_start, visited)
                    break
            # if you are on the last vertex, then set the destination
            # This means that x_dist <= min_dist[1] for all verts in inner loop
            if new_vertex_start == len(coords)-1:
                curr_city, total_dist, visited_cnt, index_city_start, visited = destination(min_dist, total_dist, visited_cnt, index_city_start, visited)
                break

            new_vertex_start += 1

            # if the new_vertex_start has already been visited, we need to skip it
            while visited[new_vertex_start] == True:
                new_vertex_start += 1
                # if this takes us top the end, set the destination
                if new_vertex_start == len(coords):
                    curr_city, total_dist, visited_cnt, index_city_start, visited = destination(min_dist, total_dist, visited_cnt, index_city_start, visited)
                    break

    # once all coords have been visited, need to return to the initial vertex (0)
    total_dist += euclidean_dist(coords[curr_city],coords[0])

    print(f"--- %s seconds --- % {(time.time() - start_time)}")
    print(f"total_dist = {total_dist}")