\include "articulate.ly"

\header {
    title = \markup{\override #'(font-name . "Futura Bold") "Title"}
    composer = \markup{\override #'(font-name . "Futura Medium") "Gilberto Agostinho"}
    dedication = \markup{\override #'(font-name . "Futura Italic") \raise #1 "dedication"}
    poet = \markup{\override #'(font-name . "Futura Medium") "Score in C"}
    tagline = ""
}

%%% if global staff size set to 16.5, use \fontsize #1.5
% \header {
%     title = \markup{\override #'(font-name . "Futura Bold") \fontsize #1.5 "Title"}
%     composer = \markup{\override #'(font-name . "Futura Medium") \fontsize #1.5 "Gilberto Agostinho"}
%     dedication = \markup{\override #'(font-name . "Futura Italic") \fontsize #1.5 \raise #1 "dedication"}
%     poet = \markup{\override #'(font-name . "Futura Medium") \fontsize #1.5 "Score in C"}
%     tagline = ""
% }

% #(set-global-staff-size 16.5)
#(set-global-staff-size 15.5)
#(set-default-paper-size "a4landscape")

\paper {
    top-margin = 2.0\cm
    bottom-margin = 2.3\cm
    left-margin = 1.7\cm
    right-margin = 1.7\cm
    indent = 1.4\cm
    short-indent = 1.1\cm
    markup-system-spacing = #'((basic-distance . 4)
                               (minimum-distance . 4)
                               (padding . 4))
    system-system-spacing.minimum-distance = #15
    print-page-number = ##f
    ragged-last-bottom = ##f
    min-systems-per-page = 2
    max-systems-per-page = 2
    system-separator-markup = \markup {
        \fill-line { \slashSeparator \slashSeparator }
    }
}

\layout {
    % accidental styles
    \accidentalStyle Score.dodecaphonic
    \override Accidental.hide-tied-accidental-after-break = ##t

    % flag style
    \override Score.Flag.stencil = #flat-flag

    % time signature style
    \numericTimeSignature

    % bar number style
    \override Score.BarNumber.Y-offset = 3.7
    
    % larger rehearsal marks surrounded by squares
    \set Score.markFormatter = #format-mark-box-alphabet
    \override Score.RehearsalMark.self-alignment-X = #LEFT  % good if using large time sigs above score
    \override Score.RehearsalMark.font-size = #5
    \override Score.RehearsalMark.extra-offset = #'(0.0 . 1.0)

    % using whiteout to avoid collisions between ties and time signatures
    \override Score.StaffSymbol.layer = #4
    \override Staff.TimeSignature.layer = #3
    \override Staff.TimeSignature.whiteout = ##t

    % beam and steam preferences
    \override Staff.Beam.auto-knee-gap = ##f
    \override Beam.concaveness = #+inf.0
    \override Stem.details.lengths = #'(3.5 3.5 3.5 4.5 5.0 6.0)
    \override Stem.details.beamed-lengths = #'(4)
    \override Stem.stemlet-length = #1.6
    
    % hairpins should cross barlines and continue on subsequent systems
    \override Hairpin.to-barline = ##f
    \override Hairpin.after-line-breaking = ##t

    % horizontal spacing
    \set Timing.beamExceptions = #'()
    \set Timing.baseMoment = #(ly:make-moment 1/4)
    \set Timing.beatStructure = 1,1,1,1
    \override Score.SpacingSpanner.base-shortest-duration = 
        #(ly:make-moment 1/32)

    % spanners
    \override Tie.minimum-length = #3.5
    \override Staff.DynamicLineSpanner.staff-padding = 2
    \override Staff.DynamicText.extra-spacing-width = #'(-0.5 . 0.5)
    \override Staff.Hairpin.minimum-length = #10

    % customising tuplets
    \override TupletBracket.outside-staff-priority = 1000
    \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
    \override TupletBracket.minimum-length = #8
    \override TupletNumber.text = #tuplet-number::calc-fraction-text

    % horizontal tuplets
    \override TupletBracket.stencil =
    #(lambda (grob)
        (let* ((pos (ly:grob-property grob 'positions))
            (dir (ly:grob-property grob 'direction))
            (new-pos (if (= dir 1)
                (max (car pos)(cdr pos))
                (min (car pos)(cdr pos)))))
        (ly:grob-set-property! grob 'positions (cons new-pos new-pos))
        (ly:tuplet-bracket::print grob)))

    % full length tuplets
    \context {
        \Score
        tupletFullLength = ##t
    }

    % curly braces should be displayed even when a single staff is shown
    \override GrandStaff.SystemStartBrace.collapse-height = #4
    
    % large time signatures above score
    \override Score.TimeSignature.break-visibility = #'#(#f #t #t)
    \context {
        \type "Engraver_group"
        \consists "Time_signature_engraver"
        \consists "Axis_group_engraver"
        \name "TimeSig"
        \alias "Staff"
        \override TimeSignature.font-size = #3
        \override TimeSignature.break-align-symbol = ##f
        \override TimeSignature.X-offset =
            #ly:self-alignment-interface::x-aligned-on-self
        \override TimeSignature.self-alignment-X = #-1.4
        \override TimeSignature.after-line-breaking =
            #shift-right-at-line-begin
    }
    \context {
        \Score
        \accepts TimeSig
    }
    \context {
        \Staff
        \remove "Time_signature_engraver"
    }
}

tempo-markup = {
    \once \override Score.MetronomeMark.self-alignment-X = #LEFT
    \once \override Score.MetronomeMark.extra-offset = #'(0 . 2)
    \tempo \markup{
        \concat{
            \small{
                \override #'(flag-style . flat-flag)
                \general-align #Y #DOWN \note {4} #1
                \larger " = ca. 60"
            }
        }
    }
}

