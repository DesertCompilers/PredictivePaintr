#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class PenPoint():

    """This class represents a discrete sample of a penstroke
    in Euclidean space with velocity, and time"""

    def __init__(self, pos, velocity, timestamp):
        """Creates a new PenPoint"""
        self.pos = pos
        self.velocity = velocity
        self.timestamp = timestamp

class Penstroke():

    """This class represents a user's penstroke as a sequence of
    PenPoints"""

    def __init__(self):
        """Creates a new empty penstroke"""
        self._penpoints = []
        self.sorted=False

    def __sort_strokes(self):
        """This function sorts the penstrokes by time
        """
        if not self.sorted is False:
            self._penpoints = sorted(self._penpoints, key=lambda penpoint: penpoint.timestamp)

    def add_point(self, point):
        """Adds a point to the PenStroke
        :point: A reference to the new point
        """
        self._penpoints.append(point)
        self.sorted = False

    def get_positions(self):
        self.__sort_strokes()
        array = np.stack([point.pos for point in self._penpoints])
        return array

    def get_velocities(self):
        self.__sort_strokes()
        array = np.stack([point.velocity for point in self._penpoints])
        return array

    def get_timestamps(self):
        self.__sort_strokes()
        array = np.stack([point.timestamp for point in self._penpoints])
        return array
