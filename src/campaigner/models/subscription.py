#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier
import appier_extras

import campaign

class Subscription(appier_extras.admin.Base):

    name = dict(
        index = True,
        immutable = True
    )

    email = dict(
        index = True,
        immutable = True
    )

    created = dict(
        type = int,
        index = True,
        immutable = True,
        meta = "datetime"
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

            appier.not_null("email"),
            appier.not_empty("email"),
            appier.is_email("email"),
            appier.not_duplicate("email", cls._name()),
        ]

    def pre_create(self):
        appier_extras.admin.Base.pre_create(self)

        self.created = time.time()
