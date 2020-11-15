Boundary slopes of Montesinos knots
===================================
    
Hatcher and Oertel gave in their paper *Boundary slopes of Montesinos
knots* an algorithm for computing the boundary slopes of a given
Montesinos knot.  At the end of their paper, they provided a table
which gave the boundary slopes for each knot of 10 or fewer crossings
which is a Montesinos knot.  Unfortunately, this table contains
several errors.  In the late 1990s, I wrote a new implementation of
their algorithm and published a short paper in *Topology* correcting
this table, which you `can also find on the arXiv
<https://arxiv.org/abs/math/9901120>`_.  This program itself had some
bugs that were fixed in 2008 with the arXiv version of the paper
updated to match in 2010.

The 2020 version of the program, which now works with Python 3.6 or
newer, is available here on GitHub.  You can get Python from `its
homepage <https://python.org>`_, but it is already installed on most
Linux and macOS computers. To run the program, download `the zip file
<https://github.com/NathanDunfield/montesinos/archive/master.zip>`_
and:

* On Linux or macOS, open a terminal, go to the directory where you
  unpacked the files, and type::

    python3 bdry_run.py

  and then answer the questions it asks.

* On Windows, double-click the file `bdry_run.py`.

The files `two_bridge_bdry.py` and `montesinos_bdry.py` offer a purely
command-line version of `bdry_run.py`.

The old Python 2 version of the code is `here if you need it
<https://github.com/NathanDunfield/montesinos/archive/v1.2.zip>`_.


License
=======

Copyright 1998-present by Nathan M. Dunfield. This code is in `the
public domain <https://creativecommons.org/publicdomain/zero/1.0/>`_.

