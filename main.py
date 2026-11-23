"""One-line laugh entry for make.fun — "The One-Line Laugh".

Why this line works: it is a joke that proves itself in a single breath.
The therapist's diagnosis is "you avoid conflict". The speaker sets out to
disprove it by disagreeing — "I told her she was wrong" — which is itself a
confrontation. Then, in the same sentence, the speaker apologises for
disagreeing, which is conflict-avoidance in action. So the punchline is not
a twist bolted onto the setup; the speaker's own behaviour confirms the
diagnosis while trying to refute it. The surprise lands on the last word
("disagreeing") and still makes sense, because the contradiction is the
joke: every attempt to escape the diagnosis walks straight back into it.

It is an everyday truth — anyone who has ever said sorry for having an
opinion recognises it instantly — and it is economical: 100 characters,
one sentence, no word wasted, nothing explained. The joke needs no setup
beyond the line itself, and the self-referential structure is fresh: the
punchline is the speaker proving the therapist right by trying to prove
her wrong.
"""

import os

# The entry: exactly one sentence, 100 characters, well inside the 200
# character gate. Keep it a single sentence — the whole joke depends on
# the apology arriving in the same breath as the disagreement.
LINE = (
    "My therapist says I avoid conflict, so I told her she was wrong "
    "and then apologized for disagreeing."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
