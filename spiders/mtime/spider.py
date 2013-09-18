#!/usr/bin/python2.7
#-*- coding=utf-8 -*-

# Copy Rights (c) Beijing TigerKnows Technology Co., Ltd.


__authors__ = ['"wuyadong" <wuyadong@tigerknows.com>']

from tornado.httpclient import HTTPRequest

from core.spider.spider import BaseSpider
from core.datastruct import Task

from spiders.mtime.parser import RealInfoParser
from spiders.mtime.pipeline import RealInfoPipeline

class MtimeSpider(BaseSpider):
    """抓取mtime中影片信息的类
    """
    parsers = {
        "RealInfoParser": RealInfoParser,
    }

    pipelines = {
        "RealInfoItem": RealInfoPipeline,
    }
