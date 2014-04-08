#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class CampaignerApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            name = "campaigner"
        )

if __name__ == "__main__":
    app = CampaignerApp()
    app.serve()
