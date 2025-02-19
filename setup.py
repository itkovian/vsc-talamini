#!/usr/bin/env python3

#
# Copyright 2025-2025 Ghent University
#
# This file is part of vsc-talamini,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# the Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/hpcugent/slurm-spank-talamini
#
# vsc-talamini is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# vsc-talamini is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with vsc-utils. If not, see <http://www.gnu.org/licenses/>.
#

"""
vsc-talamini base distribution setup.py

@author: Andy Georges (Ghent University)
"""
import vsc.install.shared_setup as shared_setup
from vsc.install.shared_setup import ag

PACKAGE = {
    'version': '1.0.0',
    'author': [ag],
    'maintainer': [ag],
    'setup_requires': ['vsc-install >= 0.21.1'],
    'install_requires': [
    ],
    'tests_require': ['vsc-install >= 0.21.1'],
}

if __name__ == '__main__':
    shared_setup.action_target(PACKAGE)
