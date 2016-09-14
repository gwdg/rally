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

from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.gnocchi import utils as gnocchiutils
from rally.task import validation


class GnocchiMeters(gnocchiutils.GnocchiScenario):
    """Benchmark scenarios for Gnocchi Meters API."""

    @validation.required_openstack(users=True)
    @scenario.configure()
    def list_meters(self, metadata_query=None, limit=None):
        """Check all available queries for list resource request.

        :param metadata_query: dict with metadata fields and values
        :param limit: limit of meters in response
        """

        self._list_meters()
