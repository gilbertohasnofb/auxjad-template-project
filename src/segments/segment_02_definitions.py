"""
Segment #02 Definitions
=======================

Constants used by generate segment 02 by ``make_segment_02()``.

Constants:
    SEGMENT_MATERIAL (str): Name of material to be used in segment. Material names are defined in
        their respective ``material_X_definitions`` files.
    RANDOM_SEED (int): Sets  the random number generator's seed. Can be set to ``None``. This is the
        seed for this segment only. If segment uses a non-stochastic process, this seed will have no
        effect.
    WINDOW_SIZE (abjad.Duration): Length of the window size of the ``WindowLooper``.
    STEP_SIZE (abjad.Duration): Step size of the ``WindowLooper``.
    INCLUDE_DOUBLE_BARLINE (bool): If ``True``, double bar lines are added at the end of the
        segment.
    OUTPUT_N (int): Number of looping cycles in segment.
"""

import abjad

SEGMENT_MATERIAL = "Material B"
RANDOM_SEED = 9281032389918721
WINDOW_SIZE = abjad.Duration((2, 4))
STEP_SIZE = abjad.Duration((1, 8))
INCLUDE_DOUBLE_BARLINE = True
OUTPUT_N = 2
