# Binance Triangle Arbitrage

<p align="center">
    <img src="https://github.com/bmino/binance-triangle-arbitrage/blob/master/src/resources/mainDisplay.png">
</p>

This repo has been tested in the sandbox, but not in the real world. Prices are accurate and trades concurrently with the data pull.

#### TICKER
* **Trade** - Three symbols related by exchange rates that are involved in the triangle arbitrage.
* **Profit** - Percent profit or loss from executing the triangle arbitrage. This includes trading fees specified via `EXECUTION.FEE` config.
* **AB Age** - Time in seconds since the most recent update of the market ticker relating the first and second symbols in the arbitrage.
* **BC Age** - Time in seconds since the most recent update of the market ticker relating the second and third symbols in the arbitrage.
* **CA Age** - Time in seconds since the most recent update of the market ticker relating the third and first symbols in the arbitrage.
* **Age** - Time in seconds since the least recently updated market ticker involved in the triangle arbitrage.

#### Getting Started
These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

#### Config
    ```
    cp config.json.example config.json
    update your API KEY and API SECRET and any default settings
    ```

#### Install
    ```
    brew install nodeJS
    brew install Npm
    git clone https://github.com/ohnixc/binance-triangle-arbitrage.git
    cd binance-triangle-arbitrage
    npm install
    npm start
    ```

#### /logs
 
* **performance.log** - Data about performance and speed
* **execution.log** - Market interactions and profits
* **binance.log** - Binance api logging


** Forked from https://github.com/bmino/binance-triangle-arbitrage

