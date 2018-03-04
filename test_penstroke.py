#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np
import datetime as dt
import penstroke as ps
import random

def gen_random_penstrokes(n):
    """Generates a random set of penstrokes

    :n: TODO
    :returns: TODO

    """
    stroke = ps.Penstroke()
    [stroke.add_point(ps.PenPoint((i,i), (i,i), random.randint(0,10000))) for i in range(n)]
    return stroke

def test_array_sort():
    stroke = gen_random_penstrokes(10)
    pos = stroke.get_positions()
    vel = stroke.get_velocities()
    time = stroke.get_timestamps()
    assert all(time[i] <= time[i+1] for i in range(len(stroke) - 1))
