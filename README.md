<img src="logo_pytropical2.png" alt="PyTropical" width="350"/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
[![PyPI version](https://img.shields.io/pypi/v/pytropical)](https://pypi.org/project/pytropical/)

-------
PyTropical is a Python package for tropical mathematics.

* Free software: MIT license
* Documentation: [Documentation](https://github.com/heitorbaldo/PyTropical/blob/main/documentation_pytropical.pdf)

Installation
--------

```python
pip3 install pytropical
```


Examples
--------

```python
from pytropical.tropical_algebra import MaxPlusAlgebra
from pytropical.utils import *

maxp = MaxPlusAlgebra()
inf = maxp.inf #inf is the additive identity

#tropical sum
maxp.trop_sum(2.8, 3)

#tropical multiplication
maxp.trop_mult(90, inf)

#tropical exponentiation
print("2^3 = 2⨀2⨀2 = ", maxp.trop_pow(2, 3))
```
More examples are available in the ![Jupyter Notebook](https://github.com/heitorbaldo/PyTropical/blob/main/Tutorial_PyTropical.ipynb).

Dependencies
--------

* [NumPy](https://numpy.org/)
