import typing

import pytest
from day_1 import get_integer, part_a, part_b


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


@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            [
                "rxeightwopqtpqncvd481154fiveb",
                "9953three92",
                "9sevenrl5",
                "three87oneonexppvhz3seven",
                "5six36five4",
                "4three4",
                "dqxpjsnineonenvhptwocprtsbvcl6",
                "3brlmgbpdnpslgcsevenxrrftvzlxc5nine",
                "91twonelt",
                "146gqthree85twoseven",
            ],
            619,
        ),
        (
            [
                "3gtqbhdzjninetwo6thrfssxqptjbtmkkmlddhdm",
                "ninedlxdshrzfmrnnq17",
                "6six9foureight5xmfdf",
                "xg79onef6eighteight",
                "cxjpgfourfour98spklghbv73",
                "h4pcllfnine",
                "threevsrg5vdmfvpss27qzrmvmbz",
                "8ninethreethreepdlddhdfp",
                "2four2nine9znp6seven",
                "4mmsbtfivetwodgvbhrzrlh",
            ],
            546,
        ),
        (
            [
                "foursevenone4",
                "23fivetlqdfhxgg312nine",
                "6rhztqrfninefsqszx",
                "3lpchjfgbhzjbqggsfoursixseven",
                "oneone15qtgtksjdgz27hjl9",
                "seven3three7eightwovs",
                "mmztpseven836four",
                "kbtsbckkonethreetwofour7lgcbxmjkjpnine",
                "zjhljpmmdms998ffjqgxgbkdbvxxppdltbrpzcbf",
                "53twoqknxnxqbcone",
            ],
            535,
        ),
    ],
)
def test_part_a(lines: typing.List[str], expected: int) -> None:
    assert part_a(lines) == expected


@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            [
                "4mbsqbpvf7threedp4fourvvdgkvzfkz",
                "9mbmsxbn",
                "cr8twofive7two4tlbpgbngsp",
                "cpcgpg9cnbsixsix",
                "6xrzjskblfq",
                "2lzslqtllcpfdq3",
                "5ninesixtvvpblfqgb",
                "94dvc",
                "two3qnhqvxeight",
                "8qvzljppstpnpeight9",
            ],
            679,
        ),
        (
            [
                "47seven82fourfhhfmlshdsix",
                "threedmxbsevenjmdvrzlfive26",
                "two9nine9foursevenfourone",
                "344six98seven",
                "sdptbzqhn7sixnine8",
                "oneone15qtgtksjdgz27hjl9",
                "five4sixseven5ghlgbmdgfnqpfdm",
                "4sevenseven5qf",
                "dtoneightone427",
                "nine4two5kkfmcjgxbqkttg",
            ],
            449,
        ),
        (
            [
                "qxsevenkckxvmjkb1",
                "74ckc",
                "ckhpqtwodqz9r",
                "svmmzbbj5",
                "71foursix7",
                "6sevenfdmqkss4fivethreesevenfourqfnsvvsj",
                "6xrzjskblfq",
                "two6cnine",
                "oneeight6rhfiveone",
                "gbbprvrq23seven77zssgktwo",
            ],
            498,
        ),
    ],
)
def test_part_b(lines: typing.List[str], expected: int) -> None:
    assert part_b(lines) == expected
