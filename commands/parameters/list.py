﻿"""Module containing the list of defined parameters.

The parameter classes have to be imported in this module.
Two constants can be used from here:
    LIST_PARAM -- list of parameters
    DICT_PARAM -- a dictionary of parameters

"""

from commands.parameters.number import Number
from commands.parameters.options import Options

LIST_PARAM = (
        Number,
        Options,
)

DICT_PARAM = {}
for pclass in LIST_PARAM:
    DICT_PARAM[pclass.key] = pclass
