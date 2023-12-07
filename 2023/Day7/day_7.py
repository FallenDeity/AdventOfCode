from __future__ import annotations

import dataclasses
import typing

HANDS = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
CARDS = "AKQJT98765432"
JOKER_CARDS = f"{CARDS.replace('J', '')}J"


@dataclasses.dataclass
class Hand:
    cards: str
    bid: int
    hand_type: typing.Tuple[int, ...]
    consider_jokers: bool = False

    def __lt__(self, other: Hand) -> bool:
        _cards = CARDS if not self.consider_jokers else JOKER_CARDS
        if self.hand_type == other.hand_type:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                return _cards.index(self.cards[i]) > _cards.index(other.cards[i])
        return HANDS.index(self.hand_type) > HANDS.index(other.hand_type)

    @classmethod
    def from_string(cls, hand: str, bid: int, consider_jokers: bool = False) -> Hand:
        if consider_jokers:
            common = max(hand, key=lambda k: hand.count(k) if k != "J" else 0)
            high_card = max(hand, key=lambda k: JOKER_CARDS[::-1].index(k) if k != "J" else 0)
            _hand = hand.replace("J", common if hand.count(common) > 1 else high_card)
            hand_type = sorted([_hand.count(card) for card in set(_hand)], reverse=True)
            return cls(hand, bid, tuple(hand_type), consider_jokers=True)
        hand_type = sorted([hand.count(card) for card in set(hand)], reverse=True)
        return cls(hand, bid, tuple(hand_type))


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def part_a(lines: typing.List[str]) -> int:
    cards = [Hand.from_string(hand, int(bid)) for hand, bid in [line.split() for line in lines]]
    return sum([card.bid * (i + 1) for i, card in enumerate(sorted(cards))])


def part_b(lines: typing.List[str]) -> int:
    cards = [Hand.from_string(hand, int(bid), consider_jokers=True) for hand, bid in [line.split() for line in lines]]
    return sum([card.bid * (i + 1) for i, card in enumerate(sorted(cards))])


if __name__ == "__main__":
    print(part_a(get_input("../bin/7.txt")))
    print(part_b(get_input("../bin/7.txt")))
