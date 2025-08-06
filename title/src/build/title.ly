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
        \new TimeSig
        {
            \time 4/4
            r1
            \time 3/4
            r2.
            r2.
            \time 3/2
            r1.
            r1.
        }
        \context Staff = "Flute"
        {
            \set Staff.instrumentName =
            \markup { Flute }
            \set Staff.shortInstrumentName =
            \markup { Fl. }
            \time 4/4
            \clef "treble"
            \tempo-markup
            c''4
            d''4
            e''4
            f''4
            \times 2/3
            {
                \time 3/4
                ef'4
                gf'4
                af'4
                ~
            }
            af'4
            \times 2/3
            {
                ef'4
                gf'4
                af'4
                ~
            }
            af'4
            \time 3/2
            a''4
            g''2
            f''4
            e''2
            a''4
            g''2
            f''4
            e''2
            \bar "|."
        }
        \context PianoStaff = "Piano"
        <<
            \context Staff = "Piano_Upper"
            {
                \set PianoStaff.instrumentName =
                \markup { Piano }
                \set PianoStaff.shortInstrumentName =
                \markup { Pno }
                \time 4/4
                \clef "treble^8"
                \tempo-markup
                r8
                c'''8
                d'''4
                e'''4
                f'''4
                \time 3/4
                <df''' ef'''>2.
                <df''' ef'''>2.
                \time 3/2
                r2.
                <f'' a''>2.
                r2.
                <f'' a''>2.
                \bar "|."
            }
            \context Staff = "Piano_Middle"
            {
                \time 4/4
                \clef "treble"
                \tempo-markup
                c'1
                \time 3/4
                r4
                gf'2
                r4
                gf'2
                \time 3/2
                <d' e' a'>1
                r2
                <d' e' a'>1
                r2
                \bar "|."
            }
            \context Staff = "Piano_Lower"
            {
                \time 4/4
                \clef "bass"
                \tempo-markup
                c2
                g2
                \time 3/4
                <df, ef,>2.
                <df, ef,>2.
                \time 3/2
                r2
                <f a>1
                ~
                <f a>2
                <f a>1
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
                \time 4/4
                \clef "treble"
                \tempo-markup
                c''4
                d''4
                e''4
                f''4
                \time 3/4
                gf'2
                df'4
                gf'2
                df'4
                \time 3/2
                a''4
                g''2
                f''4
                e''2
                a''4
                g''2
                f''4
                e''2
                \bar "|."
            }
            \context Staff = "Harp_Lower"
            {
                \time 4/4
                \clef "bass"
                \tempo-markup
                c,2
                g,2
                \time 3/4
                R1 * 3/4
                R1 * 3/4
                \time 3/2
                d1.
                d1.
                \bar "|."
            }
        >>
        \context Staff = "Cello"
        {
            \set Staff.instrumentName =
            \markup { Cello }
            \set Staff.shortInstrumentName =
            \markup { Vcl. }
            \time 4/4
            \clef "bass"
            \tempo-markup
            c,1
            \time 3/4
            ef2.
            ef2.
            \time 3/2
            d,2
            r1
            d,2
            r1
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