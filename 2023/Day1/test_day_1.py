import pytest
from day_1 import get_integer


@pytest.mark.parametrize(
    "text, expected, parse_words",
    [
        ("threedmxbsevenjmdvrzlfive26", 26, False),
        ("6twonehjv", 66, False),
        ("jcqlxpmmj7rsrrngnq2seven", 72, False),
        ("38knvgxrftdtwo1", 31, False),
        ("dlnpklqtfivesixfptrdh9four", 99, False),
        ("eight1sixsixbnsfouronecsv", 11, False),
        ("seven82three9", 89, False),
        ("three8htqhzkrxhrfourthreebdrmjsvpfb1", 81, False),
        ("75onegckzsnpnine1xfslhfour6", 76, False),
        ("3ssptnqhmrzbseveneightwoxdx", 33, False),
        ("9lllhz8nmqxkzsevenxmbqvgqnj8", 98, True),
        ("8fourvkhkhlsjq", 84, True),
        ("mfiveone7", 57, True),
        ("four77", 47, True),
        ("2tthbbcpcr36tqvfjkfs", 26, True),
        ("khrjxxrltbpngsmzndgsjmzvgqxfhvkct6eightzrvpmpcc3", 63, True),
        ("ncszsls1z2", 12, True),
        ("stmprbctwo1ninesxbzqkkdqgdqhone", 21, True),
        ("sg4txzzfoursevenninethreesqcdznksix", 46, True),
        ("zoneight47five5sixjxd74", 14, True),
    ],
)
def test_get_integer(text: str, expected: int, parse_words: bool) -> None:
    assert get_integer(text, parse_words=parse_words) == expected
