import json
import random
maxb1 = 100000
# import numpy as np


with open("paths.json", "r", encoding="utf8") as f:
    paths = json.load(f)

with open("point_info.json", "r", encoding="utf8") as f:
    point_info = json.load(f)

paths = random.sample(paths, 50)

# print(paths)
path_points_sets = [set(i) for i in paths]


# print(path_points_sets)
# t = np.argmax([len(i) for i in paths])


def get_related_paths(path):
    p = set(path)
    rlst = []
    count = 0
    for i, v in enumerate(path_points_sets):
        if len(p & v) > 0:
            count += 1
            rlst.append(paths[i])
    return rlst


def get_related_id(id):
    path = paths[id]
    # print(path)
    p = set(path)
    rlst = set()
    count = 0
    for i, v in enumerate(path_points_sets):
        # print(p & v)
        if len(p & v) > 0:
            rlst.add(i)

    return rlst


def get_related_points(path):
    p = set(path)
    rlst = set()
    count = 0
    for i, v in enumerate(path_points_sets):
        # print(p&v)
        if len(p & v) > 0:
            count += 1
            # t = v - p
            t = v
            for j in t:
                rlst.add(j)
    return rlst


def path_to_xypath(path, level):
    rlst = []
    for i in path:
        t = str(i)
        rlst.append({"lnglat":point_info[t], "style": level})
    return rlst


# longest_path = paths[13]
# t1 = set(longest_path)
# t2 = get_related_points(longest_path) - t1
# t3 = get_related_points(t2) - t2 - t1
# print(path_to_xypath(t3,2) + path_to_xypath(t2, 1) + path_to_xypath(t1, 3))
# # print(path_to_xypath(longest_path))
# s1 = [{"lnglat":point_info[str(i)], "style": 3} for i in longest_path]
# print(len(s1))
# s2 = [{"lnglat":point_info[str(i)], "style": 1} for i in get_related_points(longest_path)]
# print(len(s2))


# s3_p_set = {i for j in t for i in get_related_points(j)} - set(longest_path)
#
# print(s3_p_set)
# s3 = [{"lnglat":point_info[str(i)], "style": 2} for i in list(s3_p_set)]
# print(s3 + s2 + s1)

# print(len(get_related_paths(longest_path)))
