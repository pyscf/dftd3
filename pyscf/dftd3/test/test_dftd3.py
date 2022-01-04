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

import unittest
from pyscf import lib
from pyscf import gto, scf

try:
    from pyscf.dftd3 import dftd3
    from pyscf.dftd3 import itrf
except ImportError:
    dftd3 = False


@unittest.skipIf(not dftd3, "library dftd3 not found.")
class KnownValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls._h2o = gto.M(atom='''
                         O  0.   0.       0.
                         H  0.   -0.757   0.587
                         H  0.   0.757    0.587
                         ''', symmetry=True)

        cls._ch4 = gto.M(atom='''
                         H 0.000000000000 0.000000000000 0.000000000000
                         C 0.000000000000 0.000000000000 1.087900000000
                         H 1.025681956337 0.000000000000 1.450533333333
                         H -0.512840978169 0.888266630391 1.450533333333
                         H -0.512840978169 -0.888266630391 1.450533333333
                         ''')

    def test_dftd3(self):
        d3 = itrf.DFTD3Dispersion(self._ch4)
        d3.xc = 'B3LYP'
        self.assertAlmostEqual(d3.kernel()[0], -0.0019136221730972761, delta=1.e-12)

    def test_dftd3_scf(self):
        mf = dftd3(scf.RHF(self._h2o))
        self.assertAlmostEqual(mf.kernel(), -74.96757204541478, delta=1.e-8)

    def test_dftd3_scf_grad(self):
        mf = dftd3(scf.RHF(self._h2o)).run()
        mfs = mf.as_scanner()
        e1 = mfs(''' O  0.   0.  0.0001; H  0.   -0.757   0.587; H  0.   0.757    0.587 ''')
        e2 = mfs(''' O  0.   0. -0.0001; H  0.   -0.757   0.587; H  0.   0.757    0.587 ''')
        ref = (e1 - e2)/0.0002 * lib.param.BOHR
        g = mf.nuc_grad_method().kernel()
        # DFTD3 does not show high agreement between analytical gradients and
        # numerical gradients. not sure whether libdftd3 analytical gradients
        # have bug
        self.assertAlmostEqual(ref, g[0,2], 5)

if __name__ == "__main__":
    print("Tests for dftd3")
    unittest.main()

