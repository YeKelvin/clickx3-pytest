#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : base_test.py
# @Time    : 2020/8/26 18:27
# @Author  : Kelvin.Ye

"""
Via app测试案例
"""

import pytest

from clickx3.se.support.chromedriver import webview_driver
from clickx3.utils.log_util import get_logger
from clickx3_app.via import Via

log = get_logger(__name__)

pytestmark = [pytest.mark.h5test]


class ViaTestSuite:

    def test_open_baidu(self, an_device):
        via = Via(an_device)
        via.start()
        via.wait()
        wd = webview_driver(an_device)
        wd.get(r'http://www.baidu.com')
        log.info(wd.title)
