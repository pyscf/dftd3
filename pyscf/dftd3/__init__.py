#!/usr/bin/env python
# Copyright 2014-2018 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Qiming Sun <osirpt.sun@gmail.com>
#

__version__ = '0.0.2'

import warnings

warnings.warn('''
pyscf-dftd3 extension is deprecated. It is recommended to use the newest DFTD3
and DFTD4 interfaces hosted at https://github.com/dftd3/simple-dftd3 and
https://github.com/dftd4/dftd4 . They can be installed via pypi packages

pip install dftd3 dftd4

See also discussions in https://github.com/pyscf/dftd3/issues/3
''')
