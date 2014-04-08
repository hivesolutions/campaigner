#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import base

class Campaign(base.Base):

    name = dict(
        index = True,
        immutable = True
    )

    email = dict(
        index = True,
        immutable = True
    )


    @classmethod
    def setup(cls):
        super(Campaign, cls).setup()

        oibiquini_1 = cls.find(name = "oibiquini_1")
        if oibiquini_1: return

        campaign = {
            "enabled" : True,
            "name" : "oibiquini_1",
            "email" : "geral@oibiquini.com"
        }
        collection = cls._collection()
        collection.save(campaign)

    @classmethod
    def validate(cls):
        return super(Campaign, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),
            appier.string_gt("name", 3),
            appier.string_lt("name", 20),
            appier.not_duplicate("name", cls._name()),

            appier.is_email("email")
        ]
