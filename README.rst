Auxjad Template Project
=======================

Template for projects using Auxjad and Abjad.

Rename ``src/title.py`` and setup project in ``src/config/config.toml``.

* for landscape pages, append ``'landscape'`` to ``paper_size``, e.g. ``'a4landscape'``
* for empty tags (e.g. subtitle or dedication), use ``''``

To build the score, run:

.. code-block::

	~ $ cd src
	~ $ python3 title.py