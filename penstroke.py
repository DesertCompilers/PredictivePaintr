#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

class PenPoint():

    """This class represents a discrete sample of a penstroke
    in Euclidean space with velocity, and time"""

    def __init__(self, pos, velocity, timestamp, pressure=1.0):
        """Creates a new PenPoint"""
        self.pos = pos
        self.velocity = velocity
        self.timestamp = timestamp
        self.pressure = pressure

    def get_dict(self):
        """Gets a dictionary representation of a penpoint
        :returns: TODO

        """
        return {'position'  : self.pos,
                'velocity'  : self.velocity,
                'timestamp' : self.timestamp,
                'pressure'  : self.pressure}

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
        if self.sorted is False:
            self._penpoints = sorted(self._penpoints, key=lambda penpoint: penpoint.timestamp)
            self.sorted = True

    def __len__(self):
        return len(self._penpoints)

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

    def get_pressures(self):
        self.__sort_strokes()
        array = np.stack([point.pressure for point in self._penpoints])
        return array

    def get_tuples(self):
        """Returns a tuple array representing a sequence of penpoints in
        respect to time
        :returns: TODO

        """
        master_array = np.stack( [(p.pos, p.velocity, p.pressure, p.timestamp) for p in self.__penstrokes] )
        return master_array

    def get_dataframe(self):
        """Returns a dataframe representing the penstroke
        :returns: A dataframe of the penstroke

        """
        df = pd.DataFrame([p.get_dict() for p in self._penpoints])
        
        df.index = pd.to_datetime(df.pop('timestamp'))
        return df
