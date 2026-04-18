import textwrap
from typing import Any

import tomli


def _fetch_values_from_config_dict(
    config_dict: dict,
    *,
    block: str,
    keys: list[str],
) -> Any | tuple[Any]:
    values = []
    for key in keys:
        try:
            values.append(config_dict[block][key])
        except KeyError:
            values.append(None)
    if len(keys) == 1:
        return values[0]
    return tuple(values)


def _generate_include_commands(config_dict: dict) -> str:
    keys = ["filenames"]
    INCLUDE = _fetch_values_from_config_dict(config_dict, block="include", keys=keys)

    if INCLUDE is None or len(INCLUDE) == 0:
        return ""

    output_string = ""
    for filename in INCLUDE:
        output_string += f'\\include "{filename}"\n'
    output_string += "\n"

    return output_string


def _generate_header_block(config_dict: dict) -> str:
    keys = ["title", "subtitle", "composer", "dedication", "poet", "fontsize"]
    values = _fetch_values_from_config_dict(config_dict, block="header", keys=keys)
    if all(value is None for value in values):
        return ""

    TITLE, SUBTITLE, COMPOSER, DEDICATION, POET, FONTSIZE = values

    output_string = "\\header {\n"

    if TITLE:
        output_string += "    title = \\markup{\n"
        output_string += '        \\override #\'(font-name . "Futura Bold")\n'
        if FONTSIZE:
            output_string += f"        \\fontsize #{FONTSIZE}\n"
        output_string += f'        "{TITLE}"\n'
        output_string += "    }\n"

    if SUBTITLE:
        output_string += "    subtitle = \\markup{\n"
        output_string += '        \\override #\'(font-name . "Futura Medium")\n'
        if FONTSIZE:
            output_string += f"        \\fontsize #{FONTSIZE}\n"
        output_string += f'        "{SUBTITLE}"\n'
        output_string += "    }\n"

    if COMPOSER:
        output_string += "    composer = \\markup{\n"
        output_string += '        \\override #\'(font-name . "Futura Medium")\n'
        if FONTSIZE:
            output_string += f"        \\fontsize #{FONTSIZE}\n"
        output_string += f'        "{COMPOSER}"\n'
        output_string += "    }\n"

    if DEDICATION:
        output_string += "    dedication = \\markup{\n"
        output_string += '        \\override #\'(font-name . "Futura Italic")\n'
        if FONTSIZE:
            output_string += f"        \\fontsize #{FONTSIZE}\n"
        output_string += "        \\raise #1\n"
        output_string += f'        "{DEDICATION}"\n'
        output_string += "    }\n"

    if POET:
        output_string += "    poet = \\markup{\n"
        output_string += '        \\override #\'(font-name . "Futura Medium")\n'
        if FONTSIZE:
            output_string += f"        \\fontsize #{FONTSIZE}\n"
        output_string += f'        "{POET}"\n'
        output_string += "    }\n"

    output_string += '    tagline = ""\n}\n\n'

    return output_string


def _generate_size_commands(config_dict: dict) -> str:
    keys = ["paper_size", "staff_size"]
    values = _fetch_values_from_config_dict(config_dict, block="size", keys=keys)
    if all(value is None for value in values):
        return ""

    PAPER_SIZE, STAFF_SIZE = values

    output_string = ""
    if any(value is not None for value in values):
        if PAPER_SIZE:
            output_string += f'#(set-default-paper-size "{PAPER_SIZE}")\n'
        if STAFF_SIZE:
            output_string += f"#(set-global-staff-size {STAFF_SIZE})\n"
        output_string += "\n"

    return output_string


def _generate_paper_block(config_dict: dict) -> str:
    keys = [
        "top_margin",
        "bottom_margin",
        "left_margin",
        "right_margin",
        "indent",
        "short_indent",
        "print_page_number",
        "ragged_last_bottom",
        "min_systems_per_page",
        "max_systems_per_page",
        "system_system_spacing_minimum_distance",
        "markup_system_spacing_basic_distance",
        "markup_system_spacing_minimum_distance",
        "markup_system_spacing_padding",
        "system_separator",
    ]
    values = _fetch_values_from_config_dict(config_dict, block="paper", keys=keys)
    if all(value is None for value in values):
        return ""

    (
        TOP_MARGIN,
        BOTTOM_MARGIN,
        LEFT_MARGIN,
        RIGHT_MARGIN,
        INDENT,
        SHORT_INDENT,
        PRINT_PAGE_NUMBER,
        RAGGED_LAST_BOTTOM,
        MIN_SYSTEMS_PER_PAGE,
        MAX_SYSTEMS_PER_PAGE,
        SYSTEM_SYSTEM_SPACING_MINIMUM_DISTANCE,
        MARKUP_SYSTEM_SPACING_BASIC_DISTANCE,
        MARKUP_SYSTEM_SPACING_MINIMUM_DISTANCE,
        MARKUP_SYSTEM_SPACING_PADDING,
        SYSTEM_SEPARATOR,
    ) = values

    output_string = "\\paper {\n"

    simple_commands = {
        "top-margin": TOP_MARGIN,
        "bottom-margin": BOTTOM_MARGIN,
        "left-margin": LEFT_MARGIN,
        "right-margin": RIGHT_MARGIN,
        "indent": INDENT,
        "short-indent": SHORT_INDENT,
        "print-page-number": PRINT_PAGE_NUMBER,
        "ragged-last-bottom": RAGGED_LAST_BOTTOM,
        "min-systems-per-page": MIN_SYSTEMS_PER_PAGE,
        "max-systems-per-page": MAX_SYSTEMS_PER_PAGE,
        "system-system-spacing.minimum-distance": SYSTEM_SYSTEM_SPACING_MINIMUM_DISTANCE,
    }
    for command, value in simple_commands.items():
        if value is not None:
            output_string += f"    {command} = {value}\n"

    markup_system_spacing_commands = {
        "basic-distance": MARKUP_SYSTEM_SPACING_BASIC_DISTANCE,
        "minimum-distance": MARKUP_SYSTEM_SPACING_MINIMUM_DISTANCE,
        "padding": MARKUP_SYSTEM_SPACING_PADDING,
    }
    if any(value is not None for value in markup_system_spacing_commands.values()):
        output_string += "    markup-system-spacing = #'(\n"
        for command, value in markup_system_spacing_commands.items():
            if value is not None:
                output_string += f"        ({command} . {value})\n"
        output_string += "    )\n"

    if SYSTEM_SEPARATOR:
        output_string += "    system-separator-markup = \\markup{\n"
        output_string += f"        {SYSTEM_SEPARATOR}\n"
        output_string += "    }\n"

    output_string += "}\n\n"

    return output_string


def _generate_layout_block(config_dict: dict) -> str:
    keys = [
        "accidental_style",
        "flag_style",
        "hide_empty_staves",
        "grand_staff_brace_collapse_height",
        "timing_base_moment",
        "base_shortest_duration",
        "horizontal_tuplets",
        "large_time_signatures",
    ]
    values = _fetch_values_from_config_dict(config_dict, block="layout", keys=keys)
    if all(value is None for value in values):
        return ""

    (
        ACCIDENTAL_STYLE,
        FLAG_STYLE,
        HIDE_EMPTY_STAVES,
        GRAND_STAFF_BRACE_COLLAPSE_HEIGHT,
        TIMING_BASE_MOMENT,
        BASE_SHORTEST_DURATION,
        HORIZONTAL_TUPLETS,
        LARGE_TIME_SIGNATURES,
    ) = values

    output_string = "\\layout {\n"

    output_string += "    % accidental styles\n"
    output_string += "    \\override Accidental.hide-tied-accidental-after-break = ##t\n"
    if ACCIDENTAL_STYLE is not None:
        output_string += f"    \\accidentalStyle Score.{ACCIDENTAL_STYLE}\n"
    output_string += "\n"

    if FLAG_STYLE is not None:
        output_string += "    % flag style\n"
        output_string += f"    \\override Score.Flag.stencil = #{FLAG_STYLE}\n"
        output_string += "\n"

    output_string += "    % time signature style\n"
    output_string += "    \\numericTimeSignature\n"
    output_string += "\n"
    output_string += "    % bar number style\n"
    output_string += "    \\override Score.BarNumber.Y-offset = 3.7\n"
    output_string += "\n"
    output_string += "    % larger rehearsal marks surrounded by squares\n"
    output_string += "    \\set Score.rehearsalMarkFormatter = #format-mark-box-alphabet\n"
    output_string += (
        "    \\override Score.RehearsalMark.self-alignment-X = #LEFT  % good if using large time\n"
    )
    output_string += (
        "                                                            % signatures above score\n"
    )
    output_string += "    \\override Score.RehearsalMark.font-size = #5\n"
    output_string += "    \\override Score.RehearsalMark.extra-offset = #'(0.0 . 1.0)\n"
    output_string += "\n"
    output_string += "    % using whiteout to avoid collisions between ties and time signatures\n"
    output_string += "    \\override Score.StaffSymbol.layer = #4\n"
    output_string += "    \\override Staff.TimeSignature.layer = #3\n"
    output_string += "    \\override Staff.TimeSignature.whiteout = ##t\n"
    output_string += "\n"
    output_string += "    % beam and steam preferences\n"
    output_string += "    \\override Staff.Beam.auto-knee-gap = ##f\n"
    output_string += "    \\override Beam.concaveness = #+inf.0\n"
    output_string += "    \\override Stem.details.lengths = #'(3.5 3.5 3.5 4.5 5.0 6.0)\n"
    output_string += "    \\override Stem.details.beamed-lengths = #'(4)\n"
    output_string += "    \\override Stem.stemlet-length = #1.6\n"
    output_string += "\n"
    output_string += "    % hairpins should cross barlines and continue on subsequent systems\n"
    output_string += "    \\override Hairpin.to-barline = ##f\n"
    output_string += "    \\override Hairpin.after-line-breaking = ##t\n"
    output_string += "\n"
    output_string += "    % horizontal spacing\n"
    output_string += "    \\set Timing.beamExceptions = #'()\n"
    output_string += "    \\set Timing.beatStructure = 1, 1, 1, 1\n"

    if TIMING_BASE_MOMENT is not None:
        output_string += f"    \\set Timing.baseMoment = #(ly:make-moment {TIMING_BASE_MOMENT})\n"
    if BASE_SHORTEST_DURATION is not None:
        output_string += "    \\override Score.SpacingSpanner.base-shortest-duration = "
        output_string += f"#(ly:make-moment {BASE_SHORTEST_DURATION})\n"

    output_string += "\n"
    output_string += "    % spanners\n"
    output_string += "    \\override Tie.minimum-length = #3.5\n"
    output_string += "    \\override Staff.DynamicLineSpanner.staff-padding = 2\n"
    output_string += "    \\override Staff.DynamicText.extra-spacing-width = #'(-0.5 . 0.5)\n"
    output_string += "    \\override Staff.Hairpin.minimum-length = #10\n"
    output_string += "\n"
    output_string += "    % customising tuplets\n"
    output_string += "    \\override TupletBracket.outside-staff-priority = 1000\n"
    output_string += (
        "    \\override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods\n"
    )
    output_string += "    \\override TupletBracket.minimum-length = #8\n"
    output_string += "    \\override TupletNumber.text = #tuplet-number::calc-fraction-text\n"
    output_string += "\n"
    output_string += "    % curly braces should be displayed even when a single staff is shown\n"
    output_string += "    \\override GrandStaff.SystemStartBrace.collapse-height = #4\n"

    if HORIZONTAL_TUPLETS is not None:
        output_string += "    % horizontal tuplets\n"
        output_string += "    \\override TupletBracket.stencil =\n"
        output_string += "    #(lambda (grob)\n"
        output_string += "        (let* ((pos (ly:grob-property grob 'positions))\n"
        output_string += "            (dir (ly:grob-property grob 'direction))\n"
        output_string += "            (new-pos (if (= dir 1)\n"
        output_string += "                (max (car pos)(cdr pos))\n"
        output_string += "                (min (car pos)(cdr pos)))))\n"
        output_string += "        (ly:grob-set-property! grob 'positions (cons new-pos new-pos))\n"
        output_string += "        (ly:tuplet-bracket::print grob)))\n"
        output_string += "\n"
        output_string += "    % full length tuplets\n"
        output_string += "    \\context {\n"
        output_string += "        \\Score\n"
        output_string += "        tupletFullLength = ##t\n"
        output_string += "    }\n"
        output_string += "\n"

    if LARGE_TIME_SIGNATURES:
        output_string += "    % large time signatures above score\n"
        output_string += "    \\override Score.TimeSignature.break-visibility = #'#(#f #t #t)\n"
        output_string += "    \\context {\n"
        output_string += '        \\type "Engraver_group"\n'
        output_string += '        \\consists "Time_signature_engraver"\n'
        output_string += '        \\consists "Axis_group_engraver"\n'
        output_string += '        \\name "TimeSig"\n'
        output_string += '        \\alias "Staff"\n'
        output_string += "        \\override TimeSignature.font-size = #3\n"
        output_string += "        \\override TimeSignature.break-align-symbol = ##f\n"
        output_string += "        \\override TimeSignature.X-offset =\n"
        output_string += "            #ly:self-alignment-interface::x-aligned-on-self\n"
        output_string += "        \\override TimeSignature.self-alignment-X = #-1.4\n"
        output_string += "        \\override TimeSignature.after-line-breaking =\n"
        output_string += "            #shift-right-at-line-begin\n"
        output_string += "    }\n"
        output_string += "    \\context {\n"
        output_string += "        \\Score\n"
        output_string += "        \\accepts TimeSig\n"
        output_string += "    }\n"
        output_string += "    \\context {\n"
        output_string += "        \\Staff\n"
        output_string += '        \\remove "Time_signature_engraver"\n'
        output_string += "    }\n"
        output_string += "\n"

    if GRAND_STAFF_BRACE_COLLAPSE_HEIGHT is not None:
        output_string += "    % curly braces will be displayed even when a single staff is shown\n"
        output_string += f"    \override GrandStaff.SystemStartBrace.collapse-height = "
        output_string += "#{GRAND_STAFF_BRACE_COLLAPSE_HEIGHT}\n"
        output_string += "\n"

    if HIDE_EMPTY_STAVES:
        output_string += "    % hiding empty staves and moving rehearsal marks to staff context\n"
        output_string += "    \\context {\n"
        output_string += "        \\Staff\n"
        output_string += "        \\RemoveEmptyStaves\n"
        output_string += "    }\n"
        output_string += "\n"

    output_string += "}\n\n"

    return output_string


def _generate_tempo_markup_command(config_dict: dict) -> str:
    keys = ["tempo_reference_note", "tempo_value", "tempo_value_prefix"]
    values = _fetch_values_from_config_dict(config_dict, block="tempo", keys=keys)

    TEMPO_REFERENCE_NOTE, TEMPO_VALUE, TEMPO_VALUE_PREFIX = values

    # We need at least a reference note and tempo value
    if TEMPO_REFERENCE_NOTE is None or TEMPO_VALUE is None:
        return ""

    # Flag style is fetch from layout block as to match choice for score
    keys = ["flag_style"]
    FLAG_STYLE = _fetch_values_from_config_dict(config_dict, block="layout", keys=keys)

    output_string = "tempo-markup = {\n"
    output_string += "    \\once \\override Score.MetronomeMark.self-alignment-X = #LEFT\n"
    output_string += "    \\once \\override Score.MetronomeMark.extra-offset = #'(0 . 2)\n"
    output_string += "    \\tempo \\markup{\n"
    output_string += "        \\concat{\n"
    output_string += "            \\small{\n"

    if FLAG_STYLE is not None:
        output_string += f"                \\override #'(flag-style . {FLAG_STYLE})\n"
    output_string += (
        f"                \\general-align #Y #DOWN \\note {{{TEMPO_REFERENCE_NOTE}}} #1\n"
    )
    if TEMPO_VALUE_PREFIX is None:
        TEMPO_VALUE_PREFIX = ""
    output_string += f'                \\larger " = {TEMPO_VALUE_PREFIX}{TEMPO_VALUE}"\n'

    output_string += "            }\n"
    output_string += "        }\n"
    output_string += "    }\n"

    output_string += "}\n\n"

    return output_string


def stylesheet_generator() -> None:
    r"""
    Generates the stylesheet to be included in the final score.

    Args:
        None

    Returns:
        None
    """
    # reading config.toml file
    with open("./src/config/config.toml", "rb") as f:
        config_dict = tomli.load(f)

    generated_strings = (
        _generate_include_commands(config_dict),
        _generate_header_block(config_dict),
        _generate_size_commands(config_dict),
        _generate_paper_block(config_dict),
        _generate_layout_block(config_dict),
        _generate_tempo_markup_command(config_dict),
    )
    stylesheet_content = "".join(generated_strings)

    stylesheet_content = textwrap.dedent(stylesheet_content.strip())

    with open("./build/includes/stylesheet.ily", "w+") as f:
        f.writelines(stylesheet_content)
