#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one original one-line text message, spoken by a dying phone
battery to the charger it waited for all day, to /output/entry.txt.

Craft notes (from the kit's judge brief, most important first):
1. Reads as the battery's last text to its charger: one line of plain
   text, lowercase texting voice, addressed to the charger.
2. A real joke with a turn that pays off in the final words: the battery
   waited all day while the charger charged the watch first, then reveals
   the charger's own cable by the bed never worked -- the charger it
   pined for all day is itself useless. Not just a sad or cute sentiment.
3. Sounds like something a person would actually type: needy, a little
   spiteful, "btw", "tell the apps i loved them", "bye".
4. Every character earns its place: about 140 of the 200 allowed, the
   setup (waited all day, watch first) earns the punchline, no filler.
5. An angle beyond the obvious dying-battery complaint: jealousy toward
   the watch, and the charger itself being broken -- funny on a second
   read, when you notice the battery died waiting for a charger that
   could never have saved it.
"""

import os

ENTRY = (
    "hey it's me. 1%. i waited all day while you charged your watch "
    "first. btw the cable by the bed never worked. tell the apps i "
    "loved them. bye"
)

OUTPUT_PATH = "/output/entry.txt"


def _check_is_text(text):
    """Stage 1: the entry must be a string we can encode as UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises if not encodable
    return True


def _check_not_blank(text):
    """Stage 2: the entry must carry words, not only white space."""
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return True


def _check_length(text):
    """Stage 3: the kit's gate allows 1 to 200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    return True


def _check_single_line(text):
    """Stage 4: one line of plain text, no newlines of either kind."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line, no newlines")
    return True


def validate(text):
    """Check the kit's gate: UTF-8 text of 1 to 200 characters, not only
    white space, and one line of plain text as the task requires."""
    _check_is_text(text)
    _check_not_blank(text)
    _check_length(text)
    _check_single_line(text)
    check_lowercase_voice(text)
    check_has_punchline(text)
    check_length_budget(text)
    return True


def check_lowercase_voice(text):
    """Craft check: the battery texts in lowercase, like a person typing
    fast on 1% -- any capital letter would break the voice."""
    if text != text.lower():
        raise ValueError("entry must stay lowercase, texting voice")
    return True


def check_has_punchline(text):
    """Craft check: the setup (waited all day) and the payoff (the cable
    by the bed never worked) must both survive in the final line."""
    if "waited all day" not in text:
        raise ValueError("entry lost its setup: waited all day")
    if "never worked" not in text:
        raise ValueError("entry lost its punchline: never worked")
    return True


def check_length_budget(text):
    """Craft check: about 140 of the 200 allowed characters -- long
    enough to earn the joke, short enough that every word works."""
    if not 100 <= len(text) <= 170:
        raise ValueError(
            "entry should run about 140 characters, got %d" % len(text)
        )
    return True


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(
        "wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH)
    )


if __name__ == "__main__":
    main()
