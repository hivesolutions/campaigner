#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import base
import campaign

class Subscription(base.Base):

    name = dict(
        index = True,
        immutable = True
    )

    email = dict(
        index = True,
        immutable = True
    )

    campaign = dict(
        type = appier.reference(
            campaign.Campaign,
            name = "name"
        )
    )

    @classmethod
    def validate(cls):
        return super(Subscription, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),
            appier.string_gt("name", 3),
            appier.string_lt("name", 20),

            appier.not_null("name"),
            appier.not_empty("name"),
            appier.is_email("email"),
            appier.not_duplicate("email", cls._name()),
        ]
