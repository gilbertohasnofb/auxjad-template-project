import abjad
import auxjad


def add_large_time_signatures(
    staves: list[abjad.Staff],
    score: abjad.Score,
) -> None:
    r"""
    Optional function that adds large time signatures above the first staff of the score and removes
        time signatures from all staves.

    Arguments:
        staves: list of abjad.Staff's
        score: abjad.Score created by generate_lilypond_file_structure()

    Returns:
        None
    """
    time_sig_staff = abjad.Staff(lilypond_type="TimeSig")
    time_signatures = auxjad.get.time_signature_list(
        staves[0],
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
