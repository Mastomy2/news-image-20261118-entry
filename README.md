# The World in One Day — 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Mastomy2/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Mastomy2/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for the make.fun bounty [news-image-20261118](https://make.fun/bounty/news-image-20261118):
sum up the world's news of Wednesday 18 November 2026 in one image.

## The image

`image.png` (1024×1024) sums up the day's six biggest world stories:

1. **Iran strikes Kuwait & Bahrain** — Iran hit Ali Al Salem air base in Kuwait and targets in Bahrain after the US struck missile sites on Qeshm Island (Just Security Early Edition)
2. **Ukraine hits Kerch Bridge** — Ukrainian drone and missile strikes partly brought down the Kerch Bridge linking Russia to Crimea (Open Chronicle)
3. **Xi & Putin meet in Shenzhen** — Xi Jinping and Vladimir Putin met on the sidelines of APEC in Shenzhen ahead of a trilateral with Trump (Horizon)
4. **Peltola wins Alaska Senate** — Democrat Mary Peltola defeated Dan Sullivan as Democrats took a 56–44 majority in the US Senate (Daily News)
5. **Ebola in DR Congo** — the Ebola outbreak passed 11,000 cases; nearly 3 in 4 infected children under 5 did not survive (Open Chronicle)
6. **Nvidia record quarter** — Nvidia posted record quarterly revenue of $115.8 billion; its board rejected Jensen Huang's return as CEO (Horizon)

## How it works

`main.py` (Python 3.13, standard library only, no network) copies `image.png`
to `/output/entry.png`. The program is fully deterministic: every run writes
the same bytes, and it verifies the output SHA-256 matches the source.

```bash
python3 main.py   # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
