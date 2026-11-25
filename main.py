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


def validate(text):
    """Check the kit's gate: UTF-8 text of 1 to 200 characters, not only
    white space, and one line of plain text as the task requires."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises if not encodable
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line, no newlines")
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
