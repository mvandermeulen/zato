# -*- coding: utf-8 -*-

"""
Copyright (C) 2023, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# ################################################################################################################################
# ################################################################################################################################

if 0:
    from zato.common.typing_ import strlist

# ################################################################################################################################
# ################################################################################################################################

class GroupObject:
    def __init__(self):
        self._config_attrs = []
        self.id = ''               # type: str
        self.is_active = True      # type: bool
        self.type = ''             # type: str
        self.name = ''             # type: str
        self.name_slug = ''        # type: str
        self.is_active = False     # type: bool
        self.members = []          # type: strlist

# ################################################################################################################################
# ################################################################################################################################
