"""
Segment #01 Definitions
=======================

Constants used by generate segment 01 by ``make_segment_01()``.

Constants:
    SEGMENT_MATERIAL: ``str`` with material to be used in segment. Material names are defined in
        their respective ``material_X_definitions`` files.
    RANDOM_SEED: ``int`` for setting the random number generator's seed. Can be set to ``None``.
        This is the seed for this segment only. If segment uses a non-stochastic process, this seed
        will have no effect.
    SEGMENT_MATERIAL: ``str`` with material to be used in segment. Material names are defined in
        their respective ``material_X_definitions`` files.
    WINDOW_SIZE: ``abjad.Duration`` with the length of the window size of the ``WindowLooper``.
    STEP_SIZE: ``abjad.Duration`` with the step size of the ``WindowLooper``.
    INCLUDE_DOUBLE_BARLINE: if ``True``, double bar lines are added at the end of the segment.
"""

import abjad

SEGMENT_MATERIAL = "Material A"
RANDOM_SEED = 4959297809154048
WINDOW_SIZE = abjad.Duration((3, 4))
STEP_SIZE = abjad.Duration((1, 4))
INCLUDE_DOUBLE_BARLINE = True
