"""
score_maker
===========

score_maker contains the main make_score function used to generate the score.
"""

from .compile_ly_file import compile_ly_file
from .create_staves import create_staves
from .final_tweaks import final_tweaks
from .generate_lilypond_file_structure import generate_lilypond_file_structure
from .generate_materials import generate_materials
from .generate_segments import generate_segments
from .prettify_score import prettify_score
from .score_maker import score_maker

__all__ = [
    "compile_ly_file",
    "create_staves",
    "final_tweaks",
    "generate_lilypond_file_structure",
    "generate_materials",
    "generate_segments",
    "prettify_score",
    "score_maker",
]
