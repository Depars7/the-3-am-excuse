# The 3 AM Excuse — Design

## Brief
One plain-text line, under 200 characters: the most creative excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM.
Judge: pairwise by glm-5.3-flash, criteria in order — (1) on-subject
excuse from a hardware wallet refusing to sign at 3 AM, (2) original
angle, NOT batteries / firmware updates / cold storage, (3) the wallet's
own voice, a device with its own priorities and grudges, (4) the 3 AM
hour itself is the joke — the line could not be pasted onto a 3 PM
transaction, (5) tight, every word earns its place, punchline at the end,
no explaining its own joke.

## Gate
- `/output/entry.txt`: UTF-8 text, 1–200 characters, not only whitespace.
- Single line, no trailing newline in the written file. Target ≤199 chars.

## Candidates (scored 1–5 per criterion, total /25)

| # | Candidate | chars | C1 | C2 | C3 | C4 | C5 | Total |
|---|-----------|------:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | I'm not signing at 3 AM. The you who actually reads the address went to bed hours ago — the you holding me just tried to send rent money to a frog. | 147 | 5 | 5 | 5 | 5 | 5 | 25 |
| 2 | Not signing at 3 AM. The you who reads addresses went to bed hours ago; the you holding me just tried to send rent money to a frog. | 131 | 5 | 5 | 4 | 5 | 5 | 24 |
| 3 | I'm not signing at 3 AM — my secure element clocks out at midnight, union rules, and the night shift you is not on the approved list. | 133 | 5 | 4 | 5 | 4 | 4 | 22 |
| 4 | At 3 AM I'm not a wallet, I'm your designated driver, and we are absolutely not going to that contract address. | 111 | 5 | 4 | 4 | 4 | 4 | 21 |
| 5 | I've seen your 3 AM before. Last time you approved a coin called MoonDaddy at 3:04 and cried by breakfast — I'm not signing this one either. | 140 | 5 | 5 | 5 | 5 | 4 | 24 |
| 6 | Sorry, my buttons only work for the daytime you. The 3 AM you has already tried to buy a JPEG of a rock twice tonight. | 118 | 5 | 4 | 5 | 5 | 4 | 23 |
| 7 | 3 AM? My screen stays dark, my buttons stay locked, and your judgment stays exactly where you left it — in bed, asleep, where it belongs. | 137 | 4 | 3 | 5 | 4 | 4 | 20 |
| 8 | I don't sign after midnight. The blockchain never sleeps, but I do, and frankly, neither should you — put the phone down and go to bed. | 135 | 5 | 3 | 4 | 3 | 4 | 19 |
| 9 | My job is to guard your money from thieves, hackers, and — worst of all — you at 3 AM. No signature tonight. | 108 | 5 | 4 | 5 | 4 | 4 | 22 |
| 10 | At 3 AM I only sign for one person: the you who sleeps eight hours and reads the fine print. He is not here. You are. | 117 | 5 | 4 | 5 | 5 | 4 | 23 |
| 11 | I'm refusing this one on principle: you only ever touch me at 3 AM, for coins with animal names, and you never once said thank you. | 131 | 5 | 4 | 5 | 3 | 4 | 21 |
| 12 | Come back at sunrise and I'll sign anything. At 3 AM, my only signature is this: no, and also, that address is a frog in a trench coat. | 135 | 5 | 4 | 4 | 4 | 3 | 20 |

## Winner: candidate 1 (25/25)
Text: `I'm not signing at 3 AM. The you who actually reads the address went to bed hours ago — the you holding me just tried to send rent money to a frog.`
Why it wins:
- C1 (5): explicit refusal to sign, at 3 AM, in the wallet's voice — the whole line is the excuse, not a caption about one.
- C2 (5): fresh angle — the owner is split into two people (the daytime one who reads addresses vs the 3 AM one) and the wallet only takes orders from the competent one. No battery, no firmware update, no cold storage anywhere.
- C3 (5): pure first-person device voice — "I'm not signing", "the you holding me" — a wallet with a grudge and a memory, not a generic assistant.
- C4 (5): the joke only works at 3 AM — the competent owner is asleep, the reckless one is holding the device now; pasted onto 3 PM it makes no sense.
- C5 (5): 147 chars, every clause loads the setup; the punch ("send rent money to a frog") lands in the final words, with no explanation of the joke.
Runners-up: #2 (24/25) — same joke, tighter, but dropping "I'm" weakens the wallet's voice; #5 (24/25) — "MoonDaddy at 3:04, cried by breakfast" is a sharp specific memory, but its punch is a refusal restated rather than a new image. #3's union/clock-out angle is funny but "secure element" leans technical and its 3 AM link is thinner.
