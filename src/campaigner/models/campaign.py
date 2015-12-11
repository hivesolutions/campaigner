#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class Campaign(appier_extras.admin.Base):

    name = appier.field(
        index = True,
        immutable = True,
        default = True
    )

    email = appier.field(
        index = True,
        immutable = True,
        meta = "email"
    )

    redirect_url = appier.field(
        index = True,
        meta = "url"
    )

    @classmethod
    def validate(cls):
        return super(Campaign, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),
            appier.string_gt("name", 3),
            appier.string_lt("name", 20),

            appier.is_email("email")
        ]

    @classmethod
    def list_names(cls):
        return ["id", "name", "email", "redirect_url"]
