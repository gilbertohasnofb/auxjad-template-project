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
            a''4
            a''4
            cs''4
            a''4
            cs''4
            d''4
            cs''4
            d''4
            r4
            d''4
            r2
            \bar "||"
            \time 2/4
            fs'''16
            c'''16
            af'''16
            af''16
            cs'''16
            fs'''16
            a''16
            ef''16
            af'''16
            af''16
            cs'''16
            fs'''16
            a''16
            ef''16
            ef''16
            g'''16
            \bar "||"
            \time 4/4
            c''''4
            e'''4
            bf'''4
            c''''4
            e'''4
            bf'''4
            c''''4
            af'''4
            bf'''4
            c''''4
            af'''4
            c'''4
            c''''4
            af'''4
            c'''4
            r4
            af'''4
            c'''4
            r2
            c'''4
            r2.
            \bar "|."
        }
        \context GrandStaff = "Piano"
        <<
            \context Staff = "Piano_Upper"
            {
                \set GrandStaff.instrumentName =
                \markup { Piano }
                \set GrandStaff.shortInstrumentName =
                \markup { Pno }
                \time 3/4
                \clef "treble^8"
                \tempo-markup
                b''4
                f''4
                c''4
                f''4
                c''4
                c'''4
                c''4
                c'''4
                r4
                c'''4
                r2
                \bar "||"
                \time 2/4
                b'''16
                e'''16
                af''16
                b''16
                g''16
                af''16
                cs''16
                cs''16
                af''16
                b''16
                g''16
                af''16
                cs''16
                cs''16
                af''16
                cs'''16
                \bar "||"
                \time 4/4
                fs'''4
                e'''4
                c''''4
                bf'''4
                e'''4
                c''''4
                bf'''4
                ef'''4
                c''''4
                bf'''4
                ef'''4
                g'''4
                bf'''4
                ef'''4
                g'''4
                r4
                ef'''4
                g'''4
                r2
                g'''4
                r2.
                \bar "|."
            }
            \context Staff = "Piano_Middle"
            {
                \time 3/4
                \clef "treble"
                \tempo-markup
                af'2
                g'4
                af'4
                g'2
                g'2
                r4
                g'4
                r2
                \bar "||"
                \time 2/4
                r2
                r2
                \bar "||"
                \time 4/4
                r1
                r1
                r1
                r1
                r1
                r1
                \bar "|."
            }
            \context Staff = "Piano_Lower"
            {
                \time 3/4
                \clef "bass"
                \tempo-markup
                a2
                fs4
                a4
                fs2
                fs2
                r4
                fs4
                r2
                \bar "||"
                \time 2/4
                af,8
                ef8
                f8
                g8
                ef8
                f8
                g8
                ef,8
                \bar "||"
                \time 4/4
                r1
                r1
                r1
                r1
                r1
                r1
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
                e'2
                b'4
                e'4
                b'2
                b'2
                r4
                b'4
                r2
                \bar "||"
                \time 2/4
                r2
                r2
                \bar "||"
                \time 4/4
                cs'1
                cs'1
                cs'1
                cs'2.
                r4
                cs'2
                r2
                cs'4
                r2.
                \bar "|."
            }
            \context Staff = "Harp_Lower"
            {
                \time 3/4
                \clef "bass"
                \tempo-markup
                ef2
                f4
                ef4
                f2
                f2
                r4
                f4
                r2
                \bar "||"
                \time 2/4
                r2
                r2
                \bar "||"
                \time 4/4
                cs,2
                b,2
                cs,4
                b,2
                c,4
                b,2
                c,2
                b,4
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
            d2
            a4
            d4
            a2
            a2
            r4
            a4
            r2
            \bar "||"
            \time 2/4
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
        \tempo 8 = 72
    }
%! abjad.LilyPondFile._get_formatted_blocks()
}