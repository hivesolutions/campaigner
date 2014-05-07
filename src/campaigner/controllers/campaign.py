#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import campaigner

class CampaignController(appier.Controller):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)

    @appier.route("/campaigns.json", "GET", json = True)
    @appier.ensure(token = "admin")
    def list_json(self):
        object = appier.get_object(alias = True, find = True)
        campaigns = campaigner.Campaign.find(map = True, **object)
        return campaigns

    @appier.route("/campaigns/<name>/subscriptions.json", "GET", json = True)
    @appier.ensure(token = "admin")
    def subscriptions_json(self, name):
        object = appier.get_object(alias = True, find = True)
        subscriptions = campaigner.Subscription.find(campaign = name, map = True, **object)
        return subscriptions

    @appier.route("/campaigns/<name>/subscriptions.csv", "GET")
    @appier.ensure(token = "admin")
    def subscriptions_csv(self, name):
        object = appier.get_object(alias = True, find = True)
        subscriptions = campaigner.Subscription.find(campaign = name, map = True, **object)
        result = appier.serialize_csv(subscriptions)
        self.content_type("text/csv")
        return result

    @appier.route("/campaigns/<name>/subscriptions", "POST", json = True)
    @appier.ensure(token = "admin")
    def create_subscription(self, name):
        campaign = campaigner.Campaign.get(name = name)
        redirect_url = campaign.redirect_url if campaign else None
        subscription = campaigner.Subscription.new()
        subscription.campaign = name
        try: subscription.save()
        except appier.OperationalError:
            if not redirect_url: raise
            return self.redirect(redirect_url, result = "error")
        return self.redirect(redirect_url, result = "success")
