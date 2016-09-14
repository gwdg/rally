# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import datetime as dt

import six

from rally import exceptions
from rally.plugins.openstack import scenario
from rally.task import atomic
from rally.task import utils as bench_utils
from rally.common import logging

LOG = logging.getLogger(__name__)

class GnocchiScenario(scenario.OpenStackScenario):
    """Base class for Gnocchi scenarios with basic atomic actions."""

    @atomic.action_timer("gnocchi.list_meters")
    def _list_meters(self, query=None, limit=None):
        """Get list of user's meters.

        :param query: query list for Gnocchi api
        :param limit: count of returned meters
        :returns: list of all meters
        """
        gnocchi=self.admin_clients("gnocchi")

        LOG.debug("Gnocchi client: '%s'" % gnocchi.__dict__)

        return gnocchi.metric.list()
