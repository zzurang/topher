#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-07-19 16:04:14
# Project: source corpus

from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    crawl_config = {

    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://foo.bar.com/index', cookies=cookies, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        cookies = {
            "foo": "33728",
            "bar": "MwzP0WJc3a"
        }

        for each in response.doc('.w a').items():
            self.crawl(each.attr.href, cookies=cookies, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "body": response.doc('.bz_comment_content .norm').text(),
            "labels": response.doc('select#product').attr.onchange,
            "cf_type": response.doc('select#cf_type option[selected]').text()
        }
