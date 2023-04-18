import os
from random import Random
import pyperclip as clip
import random
import argparse


class GenPassword:
    LENGTH = 10
    _SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # NOQA
    _SPECIAL_SYMBOLS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    def __init__(
        self,
        clipboard: clip,
        length: int or None = None,
        seed: str or None = None,
        symbols: str or None = None,
        special_symbols: str or None = None,
    ) -> None:
        self.clipboard = clipboard
        if length:
            self.LENGTH = length
        if seed:
            self.sesd = seed
        if symbols:
            self._SYMBOLS = symbols
        if special_symbols:
            self._SPECIAL_SYMBOLS = special_symbols

    def setup(self) -> None:
        self._random = random.Random(self.seed_generator)

    @property
    def _all_symbols(self) -> str:
        return f"{self._SPECIAL_SYMBOLS}{self._SYMBOLS}"

    @property
    def seed_generator(self) -> str:
        cycle = random.randint(0, self.LENGTH)
        seed = "".join(random.choice(self._all_symbols) for _ in range(cycle))
        return seed

    @property
    def _gen_password(self) -> str:
        self.setup()
        return "".join(
            self._random.choice(self._all_symbols) for _ in range(self.LENGTH)
        )

    @property
    def password(self) -> str:
        secret_pass = self._gen_password
        self.clipboard.copy(secret_pass)
        return secret_pass


def main():
    parser = argparse.ArgumentParser(description="Small Password Generator")
    parser.add_argument(
        "-length",
        "-len",
        "-l",
        type=int,
        default=GenPassword.LENGTH,
        help="Specify the length of password",
    )

    parser.add_argument(
        "-seed",
        "-s",
        type=str,
        default=None,
        help="Specify a secret key to generate unique passwords",
    )
    parser.add_argument(
        "-special_symbols",
        "-ss",
        default=None,
        help="Specify whether to use special symbols like '!#$./:;' etc.",
    )
    parser.add_argument(
        "-symbols",
        "-ns",
        default=None,
        type=str,
        help="Just Alphabet",
    )

    param = parser.parse_args()

    gen = GenPassword(
        clipboard=clip,
        length=param.length,
        seed=param.seed,
        symbols=param.symbols,
        special_symbols=param.special_symbols,
    )

    print(gen.password, end="")


if __name__ == "__main__":
    main()
