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
    def validate(cls):
        return super(Campaign, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),
            appier.string_gt("name", 3),
            appier.string_lt("name", 20),
            appier.not_duplicate("name", cls._name()),

            appier.is_email("email")
        ]
