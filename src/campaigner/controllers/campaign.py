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

    @appier.route("/campaigns/<name>/subscriptions.json", "GET", json = True)
    def subscriptions_json(self, name):
        object = appier.get_object(alias = True, find = True)
        subscriptions = campaigner.Subscription.find(campaign = name, map = True, **object)
        return subscriptions

    @appier.route("/campaigns/<name>/subscriptions", "POST", json = True)
    def create_subscription(self, name):
        campaign = campaigner.Campaign.get(name = name)
        redirect_url = campaign.redirect_url if campaign else None
        subscription = campaigner.Subscription.new()
        subscription.campaign = name
        try: subscription.save()
        except appier.OperationalError as exception:
            print(exception)
            if not redirect_url: raise
            return self.redirect(redirect_url, result = "error")
        return self.redirect(redirect_url, result = "success")
