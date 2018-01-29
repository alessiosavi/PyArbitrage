<a href="http://it.tinypic.com?ref=2iw0ope" target="_blank"><img src="http://i68.tinypic.com/2iw0ope.png" border="0" alt="Image and video hosting by TinyPic"></a>

# PyArbitrage [pyBoT]!

PyArbitrage [pyBoT]!
Simply cryptocurrencies arbitrage bot.
Make it simple, make it python!

## Getting Started

This project want to improve my self knowledge of python, one of the most powerfull & light programming language.
This bot will operate with "low volume" Cryptocurrencies Market, due to the possibility of human-readable & self-driven test.

### Prerequisites

* **Arbitrage** :
Arbitrage is when you buy one things in A and you sell it in B at higher price. Same things, different place, different prices.

This bot want to be a little tool for check the profitability beetween different market for the same coin.
In this method we can have a pretty clear vision of possible gain from arbitrage opportunities.


### How It Works

Bitcoin is still a new and inefficient market. Several Bitcoin exchanges exist around the world and the bid/ask prices they propose can be briefly different from an exchange to another. The purpose of pyBoT! to automatically profit from these temporary price differences while being market-neutral.

Here is a real example where an arbitrage opportunity exists between Bitstamp (long) and Bitfinex (short):

<p align="center">
<img src="https://cloud.githubusercontent.com/assets/11370278/11164055/5863e750-8ab3-11e5-86fc-8f7bab6818df.png"  width="60%" alt="Spread Example">
</p>

At the first vertical line, the spread between the exchanges is high so pyBoT! buys Bitstamp and short sells Bitfinex. Then, when the spread closes (second vertical line), pyBoT!  exits the market by selling Bitstamp and buying Bitfinex back.

#### Advantages

Unlike other Bitcoin arbitrage systems, pyBoT!  doesn't sell but actually _short sells_ Bitcoin on the short exchange. This feature offers two important advantages:

1. The strategy is always market-neutral: the Bitcoin market's moves (up or down) don't impact the strategy returns. This removes a huge risk from the strategy. The Bitcoin market could suddenly lose twice its value that this won't make any difference in the strategy returns.

2. The strategy doesn't need to transfer funds (USD or BTC) between Bitcoin exchanges. The buy/sell and sell/buy trading activities are done in parallel on two different exchanges, independently. Advantage: no need to deal with transfer latency issues.


### Installing
git clone git@github.ibm.com:Alessio-Savi/PyArbitrage.git
OR
git clone https://github.ibm.com/Alessio-Savi/PyArbitrage.git
OR
wget https://github.ibm.com/Alessio-Savi/PyArbitrage/archive/master.zip <<--NOT A RELEASE, IMPOSSBLE DUE TO AUTH METHODS 

## Running the tests

No test tools developed, need to be defined ...

### Break down into end to end tests

Explain what these tests test and why


### And coding style tests

Explain what these tests test and why

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

Python 2.7.5

## Contributing


## Versioning

## Trading Platform supported

* ✓ __Novaexchange__ [structure developed for 1 coin only, need refactor for deserialize coin from methods]
* ✓ __TradeSatoshi__ [structure developed for 1 coin only, need refactor for deserialize coin from methods]
* ✓ __C-CEX__ [structure developed for 1 coin only, need refactor for deserialize coin from methods]
* ✓ __YoBit__ [structure developed for 1 coin only, need refactor for deserialize coin from methods]
* ✓ __CoinExchange__ [structure developed for 1 coin only, need refactor for deserialize coin from methods]

## Trading Platform to be added

I think that i need more platform for test the future engine and test the possible exception [connection, market down ecc]
* _GDAX_
* _POLONIEX_

## Authors

* **Alessio Savi** - *Creator* - [alessio.savi@ibm.com](https://github.ibm.com/Alessio-Savi) - https://github.ibm.com/Alessio-Savi

See also the list of [contributors](https://github.ibm.com/Alessio-Savi/PyArbitrage/graphs/contributors) who participated in this project.

## License

Free of Knowledge License (:

v0.2.1 !!
[![asciicast](https://asciinema.org/a/6q2DBMne0qeZ1iPE4pyj3jzVr.png)](https://asciinema.org/a/6q2DBMne0qeZ1iPE4pyj3jzVr)
