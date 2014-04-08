#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseController(appier.Controller):

    @appier.controller("BaseController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)

    @appier.route("/", "GET")
    @appier.route("/index", "GET")
    def index(self):
        return self.template("index.html.tpl")

    @appier.route("/test", "GET")
    def test(self):
        return self.template("test.html.tpl")

    @appier.route("/campaigns", "POST")
    def campaigns(self):
        object = self.get_object()
        print object
