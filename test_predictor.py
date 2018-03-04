#!/usr/bin/env python
# -*- coding: utf-8 -*-

import predictor

def test_linear():
    """Tests the creation of a linear stroke
    """
    stroke = predictor.generate_linear_penstroke(1000)
    assert stroke is not None
