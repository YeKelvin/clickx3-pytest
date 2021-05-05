#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : driver_fixture.py
# @Time    : 2021/5/1 13:39
# @Author  : Kelvin.Ye
import pytest

from clickx3.se.driver import Driver


@pytest.fixture(scope='session')
def chrome_driver(headless):
    driver = Driver.chrome(headless=headless)
    return driver


@pytest.fixture(scope='session')
def firefox_driver(headless):
    driver = Driver.firefox(headless=headless)
    return driver


@pytest.fixture(scope='session')
def edge_driver(headless):
    driver = Driver.edge()(headless=headless)
    return driver
