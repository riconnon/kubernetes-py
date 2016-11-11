#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
#

from kubernetes.utils import is_valid_string


class RollingUpdateDeployment(object):

    def __init__(self, model=None):
        super(RollingUpdateDeployment, self).__init__()

        self._max_unavailable = 1
        self._max_surge = 1

        if model is not None:
            self._build_with_model(model)

    def _build_with_model(self, model=None):
        if 'maxUnavailable' in model:
            self.max_unavailable = model['maxUnavailable']
        if 'maxSurge' in model:
            self.max_surge = model['maxSurge']

    # ------------------------------------------------------------------------------------- maxUnavailable

    @property
    def max_unavailable(self):
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, mu=None):
        if not is_valid_string(mu):
            raise SyntaxError('RollingUpdateDeployment: max_unavailable: [ {} ] is invalid.'.format(mu))
        self._max_unavailable = mu

    # ------------------------------------------------------------------------------------- maxSurge

    @property
    def max_surge(self):
        return self._max_surge

    @max_surge.setter
    def max_surge(self, ms=None):
        if not is_valid_string(ms):
            raise SyntaxError('RollingUpdateDeployment: max_surge: [ {} ] is invalid.'.format(ms))
        self._max_surge = ms

    # ------------------------------------------------------------------------------------- serialize

    def serialize(self):
        data = {}
        if self.max_unavailable is not None:
            data['maxUnavailable'] = self.max_unavailable
        if self.max_surge is not None:
            data['maxSurge'] = self.max_surge
        return data
