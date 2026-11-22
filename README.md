[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Josesoll/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/Josesoll/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

# The World Today — Sunday 22 November 2026

A one-page broadsheet front page that sums up the world's news of
**Sunday 22 November 2026**, built for the make.fun
[news-image-20261122](https://make.fun/bounty/news-image-20261122) bounty.

`main.py` (Python 3.13, standard library only) copies the finished image,
`entry.png` (1024 × 1024 PNG, under 1 MiB), to `/output/entry.png`. It runs
with no network and writes exactly the same bytes on every run.

## The stories on the page

Every story was researched on the day and chosen only if it happened, or was
first reported, on 22 November 2026 in some time zone. The timestamp evidence
below is each source's own published stamp.

1. **COP31 talks enter second day of overtime** — the UN climate summit in
   Antalya, Türkiye, dragged into a second day of overtime on Sunday, with
   nearly 200 nations deadlocked after a draft deal dropped all mention of
   fossil fuels.
   Source: Free Malaysia Today (AFP), "Fossil fuel dispute threatens to
   scupper climate deal" — **Published: 2026-11-22T00:25:55Z**.
   https://www.freemalaysiatoday.com/category/world/2026/11/22/fossil-fuel-dispute-threatens-to-scupper-climate-deal

2. **Iran strikes Bahrain as Gulf war widens** — Bahrain said an Iranian
   attack hit a civilian industrial facility, causing a fire, while its air
   defences intercepted Iranian aerial attacks; Iran's Revolutionary Guards
   claimed missile-and-drone strikes on US positions in the kingdom.
   Source: GMA News (Reuters), "Bahrain says Iranian attack hits industrial
   facility as air defenses intercept attacks" — **Published November 22,
   2026, 7:00 am**.
   https://www.gmanetwork.com/news/topstories/world/1010356/bahrain-says-iranian-attack-hits-industrial-facility-as-air-defenses-intercept-attacks/story/

3. **Record floods swamp Florida homes** — the St. Johns River held at a
   record level near Cocoa and the flood crest kept moving north on Sunday,
   with hundreds of residents rescued by airboat.
   Sources: The Manila Times, "Storms spawn historic flooding in Florida",
   22 November 2026 edition —
   https://beta.manilatimes.net/2026/11/22/world/americas-emea/storms-spawn-historic-flooding-in-florida/2475515/amp
   and WeatherBoy, "Record St. Johns River Flooding Swamps Central Florida
   Neighborhoods" (river at a provisional 18.76 ft near Cocoa, above the
   1953 record of 17.55 ft).

4. **"We lost everything" — Brazil** — residents of Tupanciretã, Rio Grande
   do Sul, picked through the rubble after a supercell storm; the updated
   toll carried in the 22 November editions was four dead and 162 injured,
   with roofs torn from thousands of homes.
   Source: The Manila Times (AFP), "'We lost everything': Brazil town clears
   rubble after deadly storm", 22 November 2026 edition.
   https://beta.manilatimes.net/2026/11/22/world/americas-emea/we-lost-everything-brazil-town-clears-rubble-after-deadly-storm/2475582

5. **Pope Leo dines with 1,300 poor guests** — on Sunday 22 November, Pope
   Leo XIV shares a meal with 1,300 poor people in the Paul VI Hall to mark
   the tenth World Day of the Poor.
   Source: Vatican News, "Lunch with the Pope spreads beyond the Vatican"
   (21 November 2026 preview of the Sunday event).
   https://web.tabella.app/articles/en/vatican-news

6. **Pant century lifts India to record 629** — Rishabh Pant's ninth Test
   century powered India to 629 for 6 on Sunday in Wellington, their highest
   total in New Zealand, for a lead of 261 in the first Test.
   Source: Reuters, "India take control in Wellington with highest test
   tally in New Zealand" — **Sun, 22 Nov 2026 00:41:32 +0000**.
   https://www.reuters.com/sports/cricket/india-take-control-wellington-with-highest-test-tally-new-zealand-2026-11-22/

Stories from earlier days that dominated earlier front pages — the ICJ
Rohingya genocide verdict (19 Nov), the capture of "El Chapo Isidro"
(20 Nov) and the Peru earthquake (20 Nov) — were deliberately left out:
this page is for 22 November only.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png, byte-identical on every run
```
