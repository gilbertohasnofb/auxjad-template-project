from typing import Generator

from .make_segment_A import make_segment_A
from .make_segment_B import make_segment_B
from .make_segment_C import make_segment_C


def segment_factory() -> Generator:
    r"""
    Yields all individual segments that make out the composition.

    Args:
        None

    Returns:
        Generator
    """
    yield make_segment_A(seed=4959297809154048)
    yield make_segment_B(seed=9281032389918721)
    yield make_segment_C(seed=5053734054789120)
