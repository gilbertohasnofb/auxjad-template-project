%! abjad.LilyPondFile._get_format_pieces()
\version "2.24.3"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./includes/stylesheet.ily"

%! abjad.LilyPondFile._get_formatted_blocks()
\score
%! abjad.LilyPondFile._get_formatted_blocks()
{
    \new Score
    <<
        \context Staff = "Flute"
        {
            \set Staff.instrumentName =
            \markup { Flute }
            \set Staff.shortInstrumentName =
            \markup { Fl. }
            \clef "treble"
            \tempo-markup
            c''4
            d''4
            e''4
            f''4
            c''4
            d''4
            e''4
            f''4
            c''4
            d''4
            e''4
            f''4
            \times 2/3
            {
                ef'2
                gf'2
                af'2
            }
            \times 2/3
            {
                ef'2
                gf'2
                af'2
            }
            a''4
            g''4
            f''4
            e''4
            a''4
            g''4
            f''4
            e''4
            a''4
            g''4
            f''4
            e''4
            \bar "|."
        }
        \context PianoStaff = "Piano"
        <<
            \context Staff = "Piano_Upper"
            {
                \set PianoStaff.instrumentName =
                \markup { Piano }
                \set PianoStaff.shortInstrumentName =
                \markup { Pno. }
                \clef "treble"
                \tempo-markup
                c'4
                d'4
                e'4
                f'4
                c'4
                d'4
                e'4
                f'4
                c'4
                d'4
                e'4
                f'4
                <df' ef'>1
                <df' ef'>1
                r2
                <f' a'>2
                r2
                <f' a'>2
                r2
                <f' a'>2
                \bar "|."
            }
            \context Staff = "Piano_Lower"
            {
                \clef "bass"
                \tempo-markup
                c2
                g2
                c2
                g2
                c2
                g2
                <df, ef,>1
                <df, ef,>1
                r2
                <f a>2
                r2
                <f a>2
                r2
                <f a>2
                \bar "|."
            }
        >>
        \context GrandStaff = "Harp"
        <<
            \context Staff = "Harp_Upper"
            {
                \set GrandStaff.instrumentName =
                \markup { Harp }
                \set GrandStaff.shortInstrumentName =
                \markup { Hp. }
                \clef "treble"
                \tempo-markup
                c''4
                d''4
                e''4
                f''4
                c''4
                d''4
                e''4
                f''4
                c''4
                d''4
                e''4
                f''4
                gf'2
                df'2
                gf'2
                df'2
                a''4
                g''4
                f''4
                e''4
                a''4
                g''4
                f''4
                e''4
                a''4
                g''4
                f''4
                e''4
                \bar "|."
            }
            \context Staff = "Harp_Lower"
            {
                \clef "bass"
                \tempo-markup
                c,2
                g,2
                c,2
                g,2
                c,2
                g,2
                R1
                R1
                d1
                d1
                d1
                \bar "|."
            }
        >>
        \context Staff = "Cello"
        {
            \set Staff.instrumentName =
            \markup { Cello }
            \set Staff.shortInstrumentName =
            \markup { Vcl. }
            \clef "bass"
            \tempo-markup
            c,1
            c,1
            c,1
            ef1
            ef1
            d,2
            r2
            d,2
            r2
            d,2
            r2
            \bar "|."
        }
    >>
    \layout {}
    \midi
    {
        \tempo 4 = 60
    }
%! abjad.LilyPondFile._get_formatted_blocks()
}