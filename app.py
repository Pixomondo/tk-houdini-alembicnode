# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Alembic Output App for Houdini
"""

import sgtk


class AlembicOutputNode(sgtk.platform.Application):
    def init_app(self):
        module = self.import_module("tk_houdini_alembicnode")
        self.handler = module.ToolkitAlembicNodeHandler(self)
