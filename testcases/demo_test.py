#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : test_demo.py
# @Time    : 2021/5/2 11:07
# @Author  : Kelvin.Ye
import pytest


def setup_module():
    print('setup_module()：模块加载前调用')


def teardown_module():
    print('teardown_module()：模块执行后调用')


def setup_function():
    print('setup_function()：函数执行前调用')


def teardown_function():
    print('teardown_function()：函数执行后调用')


def test_function():
    print('测试函数')


@pytest.fixture
def define_a_fixture():
    return '定义一个fixture'


def test_use_fixture(define_a_fixture):
    print(f'使用fixture参数，fixture={define_a_fixture}')


@pytest.fixture(params=[{'keyA': 'valueA'}, {'keyB': 'valueB'}])
def define_a_params(request):
    """定义测试数据"""
    return request.param


def test_use_params(define_a_params):
    print(f'使用测试数据，params={define_a_params}')


@pytest.mark.parametrize('key', ['value1', 'value2'])
def test_parametrize(key):
    """参数化"""
    print(key)


class ClassTestSuite:

    def setup_class(cls):
        print('setup_class()：类执行前调用，参数只有cls，不能使用fixture')

    def teardown_class(cls):
        print('teardown_class()：类全部执行完后调用，参数只有cls，不能使用fixture')

    def setup_method(self):
        print('setup_method()：方法执行前调用')

    def teardown_method(self):
        print('teardown_method()：方法执行后调用')

    def test_method(self):
        print('测试方法')


if __name__ == '__main__':
    """代码中运行pytest"""
    # import os
    # target = ['-s', '-v', f'{os.path.basename(__file__)}::function_name']
    # target = ['-s', '-v', f'{os.path.basename(__file__)}::class_name::method_name']
    # target = ['-s', '-v', f'{os.path.basename(__file__)}', '--html=./report.html']
    # pytest.main(target)
    ...
