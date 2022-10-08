#!/usr/bin/env python3
import random
import secrets

import click

NUM = ("0123456789", 0.3)
CAPS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0.3)
LOWS = ("abcdefghijklmnopqrstuvwxyz", -1)
SYMBOLS = ("!@#$%^&*()", 0.2)
DEFAULT_LENGTH = 25


def pick_size(values: list[str], size: int) -> list[str]:
    return secrets.randbelow(int(values[1] / 2 * size)) + int(values[1] / 2 * size)


def get_values(symbols: bool, size: int):
    num_ = pick_size(NUM, size)
    caps_ = pick_size(CAPS, size)
    symbols_ = pick_size(SYMBOLS, size) if symbols else 0
    lows_ = size - num_ - caps_ - symbols_
    params = [
        (NUM, num_),
        (CAPS, caps_),
        (SYMBOLS, symbols_),
        (LOWS, lows_),
    ]
    return (
        [secrets.choice(i[0]) for i, j in params for _ in range(j)],
        *[p[1] for p in params],
    )


@click.command()
@click.option("--salt", is_flag=True, help="If set, toggles of including symbols")
@click.option(
    "-s",
    "--size",
    type=int,
    default=DEFAULT_LENGTH,
    help=(f"Sets the length of the output, default is { DEFAULT_LENGTH }"),
)
@click.option("--iterations", type=int, default=15, help="passwords to output")
def main(salt, size, iterations):
    for _ in range(iterations):
        values, *params = get_values(not salt, size)
        random.shuffle(values)
        params = [str(p) for p in params]
        click.echo(f'{ "".join(values) } {" ".join(params)}')


if __name__ == "__main__":
    main()

# AUTOBIN: newpw
