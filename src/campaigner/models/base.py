#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class Base(appier.Model):

    id = dict(
        type = int,
        index = True,
        increment = True
    )

    enabled = dict(
        type = bool,
        index = True
    )

    description = dict()

    def pre_create(self):
        appier.Model.pre_create(self)

        if not hasattr(self, "enabled"): self.enabled = True

    def get_e(self, *args, **kwargs):
        return self.get(enabled = True, *args, **kwargs)

    def find_e(self, *args, **kwargs):
        return self.find(enabled = True, *args, **kwargs)

    def enable_s(self):
        self.enabled = True
        self.save()

    def disable_s(self):
        self.enabled = False
        self.save()

    def to_locale(self, *args, **kwargs):
        return self.owner.to_locale(*args, **kwargs)
