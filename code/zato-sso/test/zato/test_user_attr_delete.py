# -*- coding: utf-8 -*-

"""
Copyright (C) 2019, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from datetime import datetime
from unittest import main

# dateutil
from dateutil.parser import parse as dt_parse

# ipaddress
from ipaddress import ip_address

# Zato
from base import BaseTest, Config, logger
from zato.common.ipaddress_ import ip_network
from zato.sso import const, status_code

# ################################################################################################################################
# ################################################################################################################################

class UserAttrDeleteTestCase(BaseTest):

# ################################################################################################################################

    def test_delete(self):

        name = self._get_random_data()
        value = self._get_random_data()
        expiration = 900

        self.post('/zato/sso/user/attr', {
            'ust': self.ctx.super_user_ust,
            'user_id': self.ctx.super_user_id,
            'name': name,
            'value': value,
            'expiration': expiration
        })

        self.delete('/zato/sso/user/attr', {
            'ust': self.ctx.super_user_ust,
            'user_id': self.ctx.super_user_id,
            'name': name,
        })

        response = self.get('/zato/sso/user/attr', {
            'ust': self.ctx.super_user_ust,
            'user_id': self.ctx.super_user_id,
            'name': name,
        })

        self.assertFalse(response.found)

# ################################################################################################################################
# ################################################################################################################################

if __name__ == '__main__':
    main()

# ################################################################################################################################
