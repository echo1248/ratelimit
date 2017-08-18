# -*- coding:utf8 -*-
# Create @ 2017-08-17 09:13:58
# Author @ 819070918@qq.com

from __future__ import absolute_import

from .ratelimit import new_bucket


VERSION = (1, 0, 1)
__version__ = '.'.join(map(str, VERSION))
__all__ = ['new_bucket']
