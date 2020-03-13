# -*- encoding: utf-8 -*-
# Tara Python Wrapper v0.1.0
# Tara Python Wrapper wit Telegram Bot
# Copyright © 2020, H. Sinan Alioglu.
# See /LICENSE for licensing information.
# This file was adapted from Chris Warrick’s Python Project Template.

"""
Adapt Qt resources to Python version.

:Copyright: © 2020, H. Sinan Alioglu.
:License: BSD (see /LICENSE).
"""

__all__ = ()

import sys

if sys.version_info[0] == 2:
    import tara-py.ui.resources2  # NOQA
elif sys.version_info[0] == 3:
    import tara-py.ui.resources3  # NOQA
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
