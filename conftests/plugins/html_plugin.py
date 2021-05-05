#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : html_plugin.py
# @Time    : 2021/5/1 11:24
# @Author  : Kelvin.Ye
import pytest
from py.xml import html


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = 'APP UI自动化测试报告'


def pytest_configure(config):
    """修改Environment"""
    # 添加添加信息
    config._metadata['项目名称'] = 'xxx'
    # 删除Java_Home
    config._metadata.pop('JAVA_HOME')


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    """修改Summary"""
    prefix.extend([html.p('所属部门: xx测试中心')])
    prefix.extend([html.p('测试人员: Linux超')])


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """编辑测试报告"""
    outcome = yield
    result = outcome.get_result()
    result.description = str(item.function.__doc__)  # 添加测试用例描述
    setattr(result, "duration_formatter", "%H:%M:%S.%f")
    getattr(result, 'extra', [])
    result.nodeid = result.nodeid.encode('utf-8').decode('unicode_escape')  # 解决中文乱码
    # html = f'<div><img src="data:image/png;base64,{screen_img}" alt="screenshot" style="width:600px;height:300px;" onclick="window.open(this.src)" align="right"/></div>'
    # extra.append(pytest_html.extras.html(html))


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """编辑表格头部"""
    cells.pop(-1)  # 删除Links列
    cells.insert(1, html.th('Description'))  # 添加Description列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """编辑表格主体"""
    cells.pop(-1)  # 删除Links列
    cells.insert(1, html.td(report.description))  # 添加Description列

