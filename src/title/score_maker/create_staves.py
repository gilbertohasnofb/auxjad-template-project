from collections import namedtuple
from typing import Tuple, List

import abjad


def create_staves(
        *,
        composition_filename: str
    ) -> Tuple[List[abjad.Staff], List[namedtuple]]:
    r"""
    Creates list of staves and list of instrument properties (staves, instrument names, clefs,
        etc.).

    Arguments:
        composition_filename: str with the filename of the composition

    Returns
        Tuple containing list of abjad.Staff's and list of namedtuple's
    """
    print()
    print(composition_filename)
    print('=================')
    print()

    # creating staves
    staff_1 = abjad.Staff(name='Flute')
    staff_2 = abjad.Staff(name='Piano_Upper')
    staff_3 = abjad.Staff(name='Piano_Lower')
    staff_4 = abjad.Staff(name='Harp_Upper')
    staff_5 = abjad.Staff(name='Harp_Lower')
    staff_6 = abjad.Staff(name='Cello')
    staves = [staff_1,
              staff_2,
              staff_3,
              staff_4,
              staff_5,
              staff_6,
              ]

    # creating staff groups
    staff_group_1 = abjad.StaffGroup([staff_2, staff_3],
                                     name='Piano',
                                     lilypond_type='PianoStaff',
                                     )
    staff_group_2 = abjad.StaffGroup([staff_4, staff_5],
                                     name='Harp',
                                     lilypond_type='GrandStaff',
                                     )
    
    # creating instrument properties (can be extended to include initial dynamics, pedalling, etc.)
    InstrumentProperties = namedtuple(
        'Staff', 
        [
            'container',
            'instrument_name',
            'short_instrument_name',
            'initial_clef',
            'context',
        ]
    )
    instrument_properties = [
        InstrumentProperties(
            container=staff_1,
            instrument_name='Flute',
            short_instrument_name='Fl.',
            initial_clef='treble',
            context='Staff',
        ),
        InstrumentProperties(
            container=staff_group_1,
            instrument_name='Piano',
            short_instrument_name='Pno.',
            initial_clef=['treble', 'bass'],
            context='PianoStaff',
        ),
        InstrumentProperties(
            container=staff_group_2,
            instrument_name='Harp',
            short_instrument_name='Hp.',
            initial_clef=['treble', 'bass'],
            context='GrandStaff',
            ),
        InstrumentProperties(
            container=staff_6,
            instrument_name='Cello',
            short_instrument_name='Vcl.',
            initial_clef='bass',
            context='Staff',
        ),
    ]

    return staves, instrument_properties
