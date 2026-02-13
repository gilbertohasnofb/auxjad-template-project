import abjad
from tqdm import tqdm

from ..materials import list_of_material_makers, list_of_material_names


def generate_materials() -> dict[str, abjad.Container]:
    r"""
    Generates a dictionary with all musical materials associated with their names as keys.

    Args:
        None

    Returns:
        ``dict`` with ``str`` (material name) and ``abjad.Container`` (raw material).
    """
    print("Generating musical materials")
    print("---------------------------")
    print()
    dict_of_materials = {}
    with tqdm(total=len(list_of_material_makers)) as pbar:
        for material_name, material_maker in zip(list_of_material_names, list_of_material_makers):
            music_container = material_maker()
            dict_of_materials[material_name] = music_container
            pbar.update(1)
    print()

    return dict_of_materials
