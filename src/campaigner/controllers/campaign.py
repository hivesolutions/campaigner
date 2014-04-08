#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import campaigner

class CampaignController(appier.Controller):

    @appier.controller("CampaignController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)

    @appier.route("/campaigns.json", "GET", json = True)
    def list_json(self):
        object = appier.get_object(alias = True, find = True)
        campaigns = campaigner.Campaign.find(map = True, **object)
        return campaigns

    @appier.route("/campaigns/<name>/subscription.json", "GET", json = True)
    def subscriptions_json(self, name):
        object = appier.get_object(alias = True, find = True)
        subscriptions = campaigner.Subscription.find(name = name, map = True, **object)
        return subscriptions
