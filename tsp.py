#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time
from math import sqrt
from pprint import pprint
from random import seed, randint
from itertools import permutations

import numpy as np
from matplotlib import pyplot as plt

def tsp(pos):

    # [0]: 最短距離のルート
    # [1]: その最短距離
    dists = []
    # ルートの距離を計算する．
    for route in permutations(pos, len(pos)):
        s = 0.0
        for i in range(1, n):
            p1, p2 = route[i-1], route[i]
            dx = abs(p2[0] - p1[0])
            dy = abs(p2[1] - p1[1])
            s += sqrt(dx**2 + dy**2)

        if not dists or s < dists[1]:
            dists = [route, s]

    return dists


if __name__ == "__main__":

    # 座標作成
    seed(100)
    n = 9
    xmin, xmax = 0, 99
    ymin, ymax = 0, 99
    pos = [(randint(xmin, xmax), randint(ymin, ymax)) for _ in range(n)]

    # 巡回セールスマン問題(時間計測有り)
    start_time = time()
    min_route, dist = tsp(pos)
    dtime = time() - start_time

    # 最短距離をプロットする．
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(1, n):
        p1, p2 = min_route[i-1], min_route[i]
        ax.plot(*p1, marker="$%d$"%i, markersize=16, color="red")
        ax.plot(*p2, marker="$%d$"%(i+1), markersize=16, color="red")
        arrowprops = dict(arrowstyle="->", connectionstyle="arc3", facecolor="red", edgecolor="black")
        ax.annotate("", xy=p2, xytext=p1, arrowprops=arrowprops)
    plt.title("TSP (time: %.3f[sec], min: %.3f)" % (dtime, dist))
    plt.show()

