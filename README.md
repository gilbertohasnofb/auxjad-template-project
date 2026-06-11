Title (year)
============

Composer
--------

Dedicated to XXXXXX.

For instrument 1, instrument 2, and instrument 3. 

To build the score, run:

```
~$ python3 ./main.py
```

Score will be built in the `build` directory, and will include `.ly`, `pdf`, and `.midi` files.

**Configuration**:
Setup project in `src/config/config.toml`. Options include:
* For landscape orientation, append `"landscape"` to `paper_size`, e.g. `"a4landscape"`
* For empty tags (e.g. subtitle or dedication), simply delete or comment out the configuration line
    
**Requires**:
* Python 3.12
* LilyPond 2.24
* Abjad 3.4
* Auxjad 1.0.10

**Notes**:
* This repository is a template for projects using Auxjad and Abjad.
* Remember to change or remove the `LICENSE` file if you are not happy with sharing your composition with the `MIT License`.
* In the section `[project]` of `pyproject.toml`, you may want to rename the project, author, email contact, as well as remove the `license` entry if you deleted the `LICENSE` file as per the comment above.