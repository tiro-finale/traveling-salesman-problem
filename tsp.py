#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time
from math import sqrt
from pprint import pprint
from random import randint
from itertools import permutations

import numpy as np
from matplotlib import pyplot as plt

def tsp(n, disp=True):

    # 座標及びルートを作成する．
    x = [randint(0, 99) for _ in range(n)]
    y = [randint(0, 99) for _ in range(n)]
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

    # 最短/最長距離のルートを取得する．
    min_route = min(dists, key=dists.get)
    max_route = max(dists, key=dists.get)

    #pprint(dists)
    #pprint(min_route)

    if not disp:
        return

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(1, n):
        p1, p2 = min_route[i-1], min_route[i]
        ax.plot(*p1, "o", color="red")
        ax.plot(*p2, "o", color="red")
        arrowprops = dict(arrowstyle="->", connectionstyle="arc3", facecolor="red", edgecolor="black")
        ax.annotate("", xy=p2, xytext=p1, arrowprops=arrowprops)
    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([min(y), max(y)])
    plt.title("TSP")
    plt.show()



if __name__ == "__main__":
    tsp(6)
