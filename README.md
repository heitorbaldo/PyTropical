<img src="logo_pytropical2.png" alt="PyTropical" width="350"/>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
[![Documentation Status](https://readthedocs.org/projects/pytropical/badge/?version=latest)]()
[![PyPI version](https://img.shields.io/pypi/v/pytropical)](https://pypi.org/project/pytropical/)

-------
PyTropical is a Python package for tropical mathematics.

* Free software: MIT license
* Documentation (TODO): https://pytropical.readthedocs.io.

Installation
--------

```python
pip3 install pytropical
```


Examples
--------

```python
from pytropical.tropical_algebra import MaxPlusAlgebra, MinPlusAlgebra
from pytropical.utils import *

maxp = MaxPlusAlgebra()
inf = maxp.inf #inf is the additive zero

#tropical sum
maxp.trop_sum(2.8, 3)

#tropical multiplication
maxp.trop_mult(90, inf)

#tropical exponentiation
print("2^3 = 2⨀2⨀2 = ", maxp.trop_pow(2, 3))
```

Dependencies
--------

* NumPy
