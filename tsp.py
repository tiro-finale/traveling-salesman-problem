#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time
from math import sqrt
from pprint import pprint
from random import seed, randint
from itertools import permutations

import numpy as np
from matplotlib import pyplot as plt

def tsp(x, y):

    # ルートを作成する．
    pos = (p for p in zip(x, y))
    routes = list(permutations(pos, n))

    # ルートをキー，その移動距離をバリューとする．
    dists = {}
    # ルートの距離を計算する．
    for route in routes:
        s = 0.0
        for i in range(1, n):
            p1, p2 = route[i-1], route[i]
            dx = abs(p2[0] - p1[0])
            dy = abs(p2[1] - p1[1])
            s += sqrt(dx**2 + dy**2)
        dists[route] = s

    # 最短距離のルートを取得する．
    return min(dists, key=dists.get)


if __name__ == "__main__":

    # 座標作成
    seed(100)
    n = 9
    x = [randint(0, 99) for _ in range(n)]
    y = [randint(0, 99) for _ in range(n)]

    # 巡回セールスマン問題
    min_route = tsp(x, y)

    # 最短距離をプロットする．
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(1, n):
        p1, p2 = min_route[i-1], min_route[i]
        ax.plot(*p1, marker="$%d$"%i, markersize=16, color="red")
        ax.plot(*p2, marker="$%d$"%(i+1), markersize=16, color="red")
        arrowprops = dict(arrowstyle="->", connectionstyle="arc3", facecolor="red", edgecolor="black")
        ax.annotate("", xy=p2, xytext=p1, arrowprops=arrowprops)
    ax.set_xlim([min(x)-10, max(x)+10])
    ax.set_ylim([min(y)-10, max(y)+10])
    plt.title("TSP")
    plt.show()

