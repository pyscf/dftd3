DFT-D3 interface
================

pyscf-dftd3 extension is deprecated. It is recommended to use the newest DFTD3
and DFTD4 interfaces hosted at https://github.com/dftd3/simple-dftd3 and
https://github.com/dftd4/dftd4 . They can be installed via pypi packages

```
pip install dftd3 dftd4
```

dftd3 package provides a drop-in replacement of pyscf.dftd3.itrf. For example

```
from pyscf import gto
import dftd3.pyscf as d3

mol = gto.M(
    atom = ''' O    0.00000000    0.00000000   -0.11081188
               H   -0.00000000   -0.84695236    0.59109389
               H   -0.00000000    0.89830571    0.52404783 ''',
    basis = 'cc-pvdz')

mf = d3.energy(mol.RHF())
print(mf.kernel())

mf.Gradients()
mf.kernel()
```

See also discussions in https://github.com/pyscf/dftd3/issues/3
and the instructions for dftd3
https://dftd3.readthedocs.io/en/latest/api/pyscf.html
and dftd4
https://dftd4.readthedocs.io/en/latest/reference/pyscf.html
