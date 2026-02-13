"""
Material A Definitions
======================

Constants used by generate material A by ``make_material_A()``. These are used to generate the raw
material, not the looping process that is later applied to it; those are defined in their respective
``segments.segment_XX_definitions`` files.

Constants:
    MATERIAL_NAME: ``int`` with material's name. Will be used by segments to point to materials.
    RANDOM_SEED: ``int`` for setting the random number generator's seed. Can be set to ``None``.
        This is the seed for this material generation only.
"""

MATERIAL_NAME = "Material A"
RANDOM_SEED = 2779446857378600
