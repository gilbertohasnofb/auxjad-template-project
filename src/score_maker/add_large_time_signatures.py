import abjad
import auxjad

from ..utils import load_config


def add_large_time_signatures(
    score: abjad.Score,
) -> None:
    r"""
    Optional function that adds large time signatures above the first staff of the score and removes
        time signatures from all staves. The option ``large_time_signature`` under ``[style]`` in
        ``config.toml`` must be set to ``true`` for this function to work.

    Args:
        score (abjad.Score): ``abjad.Score`` created by ``generate_lilypond_file_structure()``.

    Returns:
        None
    """
    config_dict = load_config()
    large_time_signatures = config_dict["layout"].get("large_time_signatures", False)
    if not large_time_signatures:
        return

    time_sig_staff = abjad.Staff(lilypond_type="TimeSig")
    time_signatures = auxjad.get.time_signature_list(
        score[0],
        do_not_use_none=True,
    )
    previous_time_signature = None
    for time_signature in time_signatures:
        rests = abjad.LeafMaker()([None], time_signature.duration)
        if time_signature != previous_time_signature:
            abjad.attach(time_signature, abjad.select(rests).leaf(0))
        time_sig_staff.append(rests)
        previous_time_signature = time_signature
    score.insert(0, time_sig_staff)
