import tomli


def stylesheet_generator() -> None:
    r"""
    Generates the stylesheet to be included in the final score.

    Arguments:
        None

    Returns:
        None
    """
    # reading config.toml file
    with open('./config/config.toml', 'rb') as f:
        config_dict = tomli.load(f)

    # Header
    TITLE = config_dict['header']['title']
    SUBTITLE = config_dict['header']['subtitle']
    COMPOSER = config_dict['header']['composer']
    DEDICATION = config_dict['header']['dedication']
    POET = config_dict['header']['poet']
    FONTSIZE = config_dict['header']['fontsize']

    # Layout
    PAPER_SIZE = config_dict['layout']['paper_size']
    PAPER_ORIENTATION = config_dict['layout']['paper_orientation']
    STAFF_SIZE = config_dict['layout']['staff_size']
    TOP_MARGIN = config_dict['layout']['top_margin']
    BOTTOM_MARGIN = config_dict['layout']['bottom_margin']
    LEFT_MARGIN = config_dict['layout']['left_margin']
    RIGHT_MARGIN = config_dict['layout']['right_margin']
    INDENT = config_dict['layout']['indent']
    SHORT_INDENT = config_dict['layout']['short_indent']
    MARKUP_SYSTEM_SPACING_BASIC_DISTANCE = (
        config_dict['layout']['markup_system_spacing']['basic_distance']
    )
    MARKUP_SYSTEM_SPACING_MINIMUM_DISTANCE = (
        config_dict['layout']['markup_system_spacing']['minimum_distance']
    )
    MARKUP_SYSTEM_SPACING_PADDING = config_dict['layout']['markup_system_spacing']['padding']
    SYSTEM_SYSTEM_SPACING_MINIMUM_DISTANCE = (
        config_dict['layout']['system_system_spacing']['minimum_distance']
    )
    PRINT_PAGE_NUMBER = config_dict['layout']['print_page_number']
    RAGGED_LAST_BOTTOM = config_dict['layout']['ragged_last_bottom']
    MIN_SYSTEMS_PER_PAGE = config_dict['layout']['min_systems_per_page']
    MAX_SYSTEMS_PER_PAGE = config_dict['layout']['max_systems_per_page']
    SYSTEM_SEPARATOR = config_dict['layout']['system_separator']

    # Tempo
    REFERENCE_NOTE = config_dict['tempo']['reference_note']
    TEMPO_MARKUP = config_dict['tempo']['tempo_markup']

    # Style
    ACCIDENTAL_STYLE = config_dict['style']['accidental_style']
    FLAG_STYLE = config_dict['style']['flag_style']
    TIMING_BASE_MOMENT = config_dict['style']['timing_base_moment']
    BASE_SHORTEST_DURATION = config_dict['style']['base_shortest_duration']

    stylesheet_string = f"""
    \\include "articulate.ly"

    \\header {{
        title = \\markup{{
            \\override #'(font-name . "Futura Bold")
            \\fontsize #{FONTSIZE} "{TITLE}"
        }}
        subtitle = \\markup{{
            \\override #'(font-name . "Futura Medium")
            \\fontsize #{FONTSIZE} "{SUBTITLE}"
        }}
        composer = \\markup{{
            \\override #'(font-name . "Futura Medium")
            \\fontsize #{FONTSIZE} "{COMPOSER}"
        }}
        dedication = \\markup{{
            \\override #'(font-name . "Futura Italic")
            \\fontsize #{FONTSIZE} \\raise #1 "{DEDICATION}"
        }}
        poet = \\markup{{
            \\override #'(font-name . "Futura Medium")
            \\fontsize #{FONTSIZE} "{POET}"
        }}
        tagline = ""
    }}

    #(set-default-paper-size "{PAPER_SIZE}" '{PAPER_ORIENTATION})
    #(set-global-staff-size {STAFF_SIZE})

    \\paper {{
        top-margin = {TOP_MARGIN}
        bottom-margin = {BOTTOM_MARGIN}
        left-margin = {LEFT_MARGIN}
        right-margin = {RIGHT_MARGIN}
        indent = {INDENT}
        short-indent = {SHORT_INDENT}
        markup-system-spacing = #'((basic-distance . {MARKUP_SYSTEM_SPACING_BASIC_DISTANCE})
                                   (minimum-distance . {MARKUP_SYSTEM_SPACING_MINIMUM_DISTANCE})
                                   (padding . {MARKUP_SYSTEM_SPACING_PADDING}))
        system-system-spacing.minimum-distance = {SYSTEM_SYSTEM_SPACING_MINIMUM_DISTANCE}
        print-page-number = {PRINT_PAGE_NUMBER}
        ragged-last-bottom = {RAGGED_LAST_BOTTOM}
        min-systems-per-page = {MIN_SYSTEMS_PER_PAGE}
        max-systems-per-page = {MAX_SYSTEMS_PER_PAGE}
        system-separator-markup = \\markup{{
            {SYSTEM_SEPARATOR}
        }}
    }}

    \\layout {{
        % accidental styles
        \\accidentalStyle Score.{ACCIDENTAL_STYLE}
        \\override Accidental.hide-tied-accidental-after-break = ##t

        % flag style
        \\override Score.Flag.stencil = #{FLAG_STYLE}

        % time signature style
        \\numericTimeSignature

        % bar number style
        \\override Score.BarNumber.Y-offset = 3.7
        
        % larger rehearsal marks surrounded by squares
        \\set Score.markFormatter = #format-mark-box-alphabet
        \\override Score.RehearsalMark.self-alignment-X = #LEFT  % good if using large time
                                                                 % signatures above score
        \\override Score.RehearsalMark.font-size = #5
        \\override Score.RehearsalMark.extra-offset = #'(0.0 . 1.0)

        % using whiteout to avoid collisions between ties and time signatures
        \\override Score.StaffSymbol.layer = #4
        \\override Staff.TimeSignature.layer = #3
        \\override Staff.TimeSignature.whiteout = ##t

        % beam and steam preferences
        \\override Staff.Beam.auto-knee-gap = ##f
        \\override Beam.concaveness = #+inf.0
        \\override Stem.details.lengths = #'(3.5 3.5 3.5 4.5 5.0 6.0)
        \\override Stem.details.beamed-lengths = #'(4)
        \\override Stem.stemlet-length = #1.6
        
        % hairpins should cross barlines and continue on subsequent systems
        \\override Hairpin.to-barline = ##f
        \\override Hairpin.after-line-breaking = ##t

        % horizontal spacing
        \\set Timing.beamExceptions = #'()
        \\set Timing.baseMoment = #(ly:make-moment {TIMING_BASE_MOMENT})
        \\set Timing.beatStructure = 1,1,1,1
        \\override Score.SpacingSpanner.base-shortest-duration = 
            #(ly:make-moment {BASE_SHORTEST_DURATION})

        % spanners
        \\override Tie.minimum-length = #3.5
        \\override Staff.DynamicLineSpanner.staff-padding = 2
        \\override Staff.DynamicText.extra-spacing-width = #'(-0.5 . 0.5)
        \\override Staff.Hairpin.minimum-length = #10

        % customising tuplets
        \\override TupletBracket.outside-staff-priority = 1000
        \\override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
        \\override TupletBracket.minimum-length = #8
        \\override TupletNumber.text = #tuplet-number::calc-fraction-text

        % horizontal tuplets
        \\override TupletBracket.stencil =
        #(lambda (grob)
            (let* ((pos (ly:grob-property grob 'positions))
                (dir (ly:grob-property grob 'direction))
                (new-pos (if (= dir 1)
                    (max (car pos)(cdr pos))
                    (min (car pos)(cdr pos)))))
            (ly:grob-set-property! grob 'positions (cons new-pos new-pos))
            (ly:tuplet-bracket::print grob)))

        % full length tuplets
        \\context {{
            \\Score
            tupletFullLength = ##t
        }}

        % curly braces should be displayed even when a single staff is shown
        \\override GrandStaff.SystemStartBrace.collapse-height = #4
        
        % large time signatures above score
        \\override Score.TimeSignature.break-visibility = #'#(#f #t #t)
        \\context {{
            \\type "Engraver_group"
            \\consists "Time_signature_engraver"
            \\consists "Axis_group_engraver"
            \\name "TimeSig"
            \\alias "Staff"
            \\override TimeSignature.font-size = #3
            \\override TimeSignature.break-align-symbol = ##f
            \\override TimeSignature.X-offset =
                #ly:self-alignment-interface::x-aligned-on-self
            \\override TimeSignature.self-alignment-X = #-1.4
            \\override TimeSignature.after-line-breaking =
                #shift-right-at-line-begin
        }}
        \\context {{
            \\Score
            \\accepts TimeSig
        }}
        \\context {{
            \\Staff
            \\remove "Time_signature_engraver"
        }}
    }}

    tempo-markup = {{
        \\once \\override Score.MetronomeMark.self-alignment-X = #LEFT
        \\once \\override Score.MetronomeMark.extra-offset = #'(0 . 2)
        \\tempo \\markup{{
            \\concat{{
                \\small{{
                    \\override #'(flag-style . flat-flag)
                    \\general-align #Y #DOWN \\note {{{REFERENCE_NOTE}}} #1
                    \\larger " = {TEMPO_MARKUP}"
                }}
            }}
        }}
    }}
    """

    with open('./includes/stylesheet.ily', 'w+') as f:
        f.writelines(stylesheet_string)