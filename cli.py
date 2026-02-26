#!/usr/bin/env python3

import asyncio
import click

from main import generate
from main import list


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--count", default=5, help="How many emails to generate", type=int
)
def generatecommand(count: int):
    "Generate emails"
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(generate(count))
    except KeyboardInterrupt:
        pass


@click.command()
@click.option(
    "--active/--inactive", default=True, help="Filter Active / Inactive emails"
)
@click.option("--search", default=None, help="Search emails by label (regex)")
@click.option("--export", default=None, help="Export emails to a CSV file (e.g. --export emails.csv)")
def listcommand(active, search, export):
    "List emails"
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(list(active, search, export))
    except KeyboardInterrupt:
        pass


cli.add_command(listcommand, name="list")
cli.add_command(generatecommand, name="generate")

if __name__ == "__main__":
    cli()
