#!/usr/bin/env python
# -*- coding: utf-8 -*-

import penstroke as ps
import numpy as np
import datetime as dt

def generate_linear_penstroke(n):
    """Generates a linear penstroke

    :n: Length of the penstroke in points
    :returns: A penstroke

    """
    stroke = ps.Penstroke()
    X = np.arange(0, n)
    Y = np.arange(0, n)
    for x,y in zip(X,Y):
        stroke.add_point(ps.PenPoint( (x,y), (0), dt.datetime.now()))
    return stroke
