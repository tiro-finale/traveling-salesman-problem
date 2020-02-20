#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time
from math import sqrt
from pprint import pprint
from random import seed, randint
from itertools import permutations

import numpy as np
from matplotlib import pyplot as plt

def tsp(pos, ismax=False):

    # [0]: 最短距離のルート
    # [1]: その最短距離
    dists = []
    # ルートの距離を計算する．
    for route in permutations(pos, len(pos)):
        s = 0.0
        for i in range(n):
            p1, p2 = route[i%n], route[(i+1)%n]
            dx = abs(p2[0] - p1[0])
            dy = abs(p2[1] - p1[1])
            s += sqrt(dx**2 + dy**2)

        if not dists or (not ismax and s < dists[1]) or (ismax and s > dists[1]):
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
    for i in range(n):
        p1, p2 = min_route[i%n], min_route[(i+1)%n]
        ax.plot(*p1, marker="$%d$"%(i+1), markersize=16, color="red")
        ax.plot(*p2, markersize=16, color="red")
        ax.annotate("", xy=p2, xytext=p1, arrowprops={"arrowstyle": "->"})
    plt.title("TSP (time: %.3f[sec], min: %.3f)" % (dtime, dist))
    plt.show()

