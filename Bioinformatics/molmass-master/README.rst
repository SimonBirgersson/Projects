Molecular Mass Calculations
===========================

Molmass is a Python library and console script to calculate the molecular mass
(average, nominal, and isotopic pure), the elemental composition, and the
mass distribution spectrum of a molecule given by its chemical formula,
relative element weights, or sequence.

Calculations are based on the isotopic composition of the elements. Mass
deficiency due to chemical bonding is not taken into account.

Examples of valid formulas are ``H2O``, ``[2H]2O``, ``CH3COOH``, ``EtOH``,
``CuSO4.5H2O``, ``(COOH)2``, ``AgCuRu4(H)2[CO]12{PPh3}2``, ``CGCGAATTCGCG``,
``MDRGEQGLLK``, and ``O: 0.26, 30Si: 0.74``.

Formulas are case sensitive and ``+`` denotes the arithmetic operator,
not an ion charge.

For command line usage run ``python -m molmass --help``

:Author: `Christoph Gohlke <https://www.lfd.uci.edu/~gohlke/>`_

:License: BSD 3-Clause

:Version: 2021.6.18

Requirements
------------
* `CPython >= 3.7 <https://www.python.org>`_

Revisions
---------
2021.6.18
    Remove support for Python 3.6 (NEP 29).
    Add Particle types to elements.py (#5).
    Fix molmass_web.py failure on WSL2 (#9).
    Fix elements_gui.py layout issue.
2020.6.10
    Update elements_gui.py to version 2020.6.10.
2020.1.1
    Update elements.py to version 2020.1.1.
    Remove support for Python 2.7 and 3.5.
2018.8.15
    Move modules into molmass package.
2018.5.29
    Add option to start web interface from console.
2018.5.25
    Style and docstring fixes.
    Make 'from_fractions' output deterministic.
2005.x.x
    Initial release.

Examples
--------
>>> from molmass import Formula
>>> f = Formula('D2O')  # heavy water
>>> f.formula  # hill notation
'[2H]2O'
>>> f.empirical
'[2H]2O'
>>> f.mass  # average mass
20.02760855624
>>> f.isotope.massnumber  # nominal mass
20
>>> f.isotope.mass  # monoisotopic mass
20.02311817581
>>> f.atoms
3
>>> print(f.composition())
Element  Number  Relative mass  Fraction %
2H            2       4.028204     20.1133
O             1      15.999405     79.8867
Total:        3      20.027609    100.0000
>>> print(f.spectrum())
Relative mass    Fraction %      Intensity
20.023118         99.757000     100.000000
21.027335          0.038000       0.038093
22.027363          0.205000       0.205499
