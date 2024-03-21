import functools
import json
import sys
import typing
from collections import defaultdict
from pathlib import Path
from urllib import request

SOURCE = "https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json"


def download_file(url: str):
    return request.urlopen(url)


@functools.cache
def load_more_aliases():
    try:
        with open("aliases.json") as f:
            return json.load(f)
    except Exception as e:
        return {}


def more_aliases(alias, emoji):
    more_aliases = load_more_aliases()

    for extra in more_aliases.get(alias, []):
        yield extra, emoji


def gen_shortcuts(entities: list[dict]):
    for data in entities:
        emoji = data["emoji"]
        for alias in data["aliases"]:
            yield alias, emoji
            yield from more_aliases(alias, emoji)

        for alias in data["tags"]:
            yield alias, data["emoji"]
            yield from more_aliases(alias, emoji)


def main(target: str = "emoji.yml"):
    target_path = Path(target)

    if target_path.exists():
        print(target_path, "already exists. Please remove it to continue")
        exit(1)

    entities = json.load(download_file(SOURCE))

    seen = defaultdict(set)
    with target_path.open("w") as f:
        print("# Emoji", file=f)
        print("matches:", file=f)

        for trigger, replace in gen_shortcuts(entities):
            if replace in seen[trigger]:
                print(f"duplicate: {trigger} - {replace}")

            print(f'  - trigger: ":{trigger}:"', file=f)
            print(f'    replace: "{replace}"', file=f)

            seen[trigger].add(replace)


if __name__ == "__main__":
    main(*sys.argv[1:])
