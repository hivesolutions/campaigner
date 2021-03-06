#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class CampaignerApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "campaigner",
            parts = (
                appier_extras.CaptchaPart,
                appier_extras.AdminPart
            ),
            *args, **kwargs
        )

if __name__ == "__main__":
    app = CampaignerApp()
    app.serve()
else:
    __path__ = []
