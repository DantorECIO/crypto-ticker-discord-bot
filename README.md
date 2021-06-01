# crypto-ticker-discord-bot

A Discord bot that elegantly displays the price of any cryptocurrency in its nickname

## About

This Discord bot is more of a template to implement bots suited to any cryptocurrency [CoinGecko](https://www.coingecko.com/) supports. It's set to [Nano](https://nano.org/) by default.

This bot is supposed to be on as few servers as possible, since it needs privileged intents and Discord's API doesn't like updating nicknames too often.

## Requirements

- Python >= 3.8
- discord.py >= 1.7.2
- requests >= 2.23.0
- python-dateutil >= 2.8.1
- parsedatetime >= 2.6
- pycoingecko >= 2.0.0

The Python modules are listed in ``requirements.txt``, so you only need to do ``pip install -r requirements.txt``.

## Configuration
Go into ``config,json`` and change the following variables to suit your needs:

- ``token``: Your Discord bot token.
- ``cryptocurrency_id``: CoinGecko's ID of your cryptocurrency. You can look them up on their website, but it's usually something like ``nano``, ``bitcoin``, ``ethereum`` etc.
- ``cryptocurrency_name``: Can be anything you want, it's used in the name to neatly show the name of the cryptocurrency used.
- ``fiat_id``: CoinGecko's ID of the fiat currency your cryptocurrency's price is compared against. You can look them up on their website, but it's usually something like ``eur``, ``usd``, ``gbp`` etc.
- ``fiat_name``: Can be anything you want, it's used in the name to neatly show the name of the fiat currency used.

---

### Donation :)

If you like this bot, why not consider making a small donation using [Nano](https://whynano.cc/)? :)

``nano_1manic1d9i4mh5gijuma8dmo8xccwny54nw87n18iu5ikdpat7yeozm64h6t``

![Nano Address](data:image/png;base64,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)