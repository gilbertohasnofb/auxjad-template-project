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
            \time 3/4
            r2.
            r2.
            r2.
            r2.
            \time 2/4
            r2
            r2
            r2
            \time 4/4
            r1
            r1
            r1
            r1
            r1
            r1
        }
        \context Staff = "Flute"
        {
            \set Staff.instrumentName =
            \markup { Flute }
            \set Staff.shortInstrumentName =
            \markup { Fl. }
            \time 3/4
            \clef "treble"
            \tempo-markup
            f''4
            cs''4
            f''4
            cs''4
            f''4
            b''4
            f''4
            b''4
            r4
            b''4
            r2
            \bar "||"
            \time 2/4
            b''16
            g'''16
            a''16
            bf'''16
            g'''16
            cs''16
            b'''16
            g'''16
            g'''16
            cs''16
            b'''16
            g'''16
            a'''16
            bf''16
            fs'''16
            g'''16
            a'''16
            bf''16
            fs'''16
            g'''16
            r4
            \bar "||"
            \time 4/4
            ef'''4
            a'''4
            fs'''4
            ef'''4
            a'''4
            fs'''4
            ef'''4
            b'''4
            fs'''4
            ef'''4
            b'''4
            bf'''4
            ef'''4
            b'''4
            bf'''4
            r4
            b'''4
            bf'''4
            r2
            bf'''4
            r2.
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
                \time 3/4
                \clef "treble^8"
                \tempo-markup
                b''4
                a''4
                g''4
                a''4
                g''4
                fs''4
                g''4
                fs''4
                r4
                fs''4
                r2
                \bar "||"
                \time 2/4
                e''16
                fs'''16
                g'''16
                af''16
                cs''16
                c''''16
                bf'''16
                cs'''16
                cs''16
                c''''16
                bf'''16
                cs'''16
                g'''16
                c''''16
                cs'''16
                fs''16
                g'''16
                c''''16
                cs'''16
                fs''16
                r4
                \bar "||"
                \time 4/4
                fs'''4
                c'''4
                af'''4
                a'''4
                c'''4
                af'''4
                a'''4
                d'''4
                af'''4
                a'''4
                d'''4
                af'''4
                a'''4
                d'''4
                af'''4
                r4
                d'''4
                af'''4
                r2
                af'''4
                r2.
                \bar "|."
            }
            \context Staff = "Piano_Middle"
            {
                \time 3/4
                \clef "treble"
                \tempo-markup
                f'2
                af'4
                f'4
                af'2
                af'2
                r4
                af'4
                r2
                \bar "||"
                \time 2/4
                r2
                r2
                r2
                \bar "||"
                \time 4/4
                c'''2
                ef''2
                c'''4
                ef''2
                ef''4
                ef''2
                ef''2
                ef''4
                ef''2
                r4
                ef''2
                r2
                ef''4
                r2.
                \bar "|."
            }
            \context Staff = "Piano_Lower"
            {
                \time 3/4
                \clef "bass"
                \tempo-markup
                af2
                bf4
                af4
                bf2
                bf2
                r4
                bf4
                r2
                \bar "||"
                \time 2/4
                ef8
                cs,8
                d8
                d8
                d8
                d8
                c'8
                bf,8
                c'8
                bf,8
                r4
                \bar "||"
                \time 4/4
                fs2
                cs2
                fs4
                cs2
                c4
                cs2
                c2
                cs4
                c2
                r4
                c2
                r2
                c4
                r2.
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
                \time 3/4
                \clef "treble"
                \tempo-markup
                a'2
                bf'4
                a'4
                bf'2
                bf'2
                r4
                bf'4
                r2
                \bar "||"
                \time 2/4
                r2
                r2
                r2
                \bar "||"
                \time 4/4
                g1
                g1
                g1
                g2.
                r4
                g2
                r2
                g4
                r2.
                \bar "|."
            }
            \context Staff = "Harp_Lower"
            {
                \time 3/4
                \clef "bass"
                \tempo-markup
                ef2
                fs4
                ef4
                fs2
                fs2
                r4
                fs4
                r2
                \bar "||"
                \time 2/4
                r2
                r2
                r2
                \bar "||"
                \time 4/4
                ef,2
                a,2
                ef,4
                a,2
                c,4
                a,2
                c,2
                a,4
                c,2
                r4
                c,2
                r2
                c,4
                r2.
                \bar "|."
            }
        >>
        \context Staff = "Cello"
        {
            \set Staff.instrumentName =
            \markup { Cello }
            \set Staff.shortInstrumentName =
            \markup { Vcl. }
            \time 3/4
            \clef "bass"
            \tempo-markup
            c'2
            cs4
            c'4
            cs2
            cs2
            r4
            cs4
            r2
            \bar "||"
            \time 2/4
            r2
            r2
            r2
            \bar "||"
            \time 4/4
            fs,1
            fs,1
            fs,1
            fs,2.
            r4
            fs,2
            r2
            fs,4
            r2.
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