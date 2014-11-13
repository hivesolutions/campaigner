#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from . import campaign

class Subscription(appier_extras.admin.Base):

    name = appier.field(
        index = True,
        immutable = True
    )

    email = appier.field(
        index = True,
        immutable = True,
        meta = "email"
    )

    campaign = appier.field(
        type = appier.reference(
            campaign.Campaign,
            name = "name"
        ),
        immutable = True
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

            appier.not_null("campaign")
        ]

    def pre_create(self):
        appier_extras.admin.Base.pre_create(self)

        subscriptions = Subscription.find(
            email = self.email,
            campaign = self.campaign
        )
        if subscriptions: raise appier.OperationalError(
            message = "Invalid or duplicated subscription"
        )
