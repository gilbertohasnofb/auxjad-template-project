"""
materials
=========

Collection of materials.
"""

from .make_material_A import make_material_A
from .make_material_B import make_material_B
from .make_material_C import make_material_C
from .material_A_definitions import MATERIAL_NAME as MATERIAL_A_NAME
from .material_B_definitions import MATERIAL_NAME as MATERIAL_B_NAME
from .material_C_definitions import MATERIAL_NAME as MATERIAL_C_NAME

list_of_material_makers = [
    make_material_A,
    make_material_B,
    make_material_C,
]

list_of_material_names = [
    MATERIAL_A_NAME,
    MATERIAL_B_NAME,
    MATERIAL_C_NAME,
]
