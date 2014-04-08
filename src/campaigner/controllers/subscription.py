#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class SubscriptionController(appier.Controller):

    @appier.controller("SubscriptionController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
