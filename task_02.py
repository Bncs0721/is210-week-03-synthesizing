#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

TO_REPLACE = 'Spanish'

#print len(TO_REPLACE)

POSITION = (inquisition.SPANISH).index('Spanish')

#print POSITION

FLEMISH = (inquisition.SPANISH)[0:18] + ' Flemish' + (inquisition.SPANISH)[26:]

print FLEMISH
