#!/usr/local/bin


filename = "/Users/nikkyos/Desktop/untitled folder/binance-triangle-arbitrage-01/logs/execution.log"

with open(filename, "r") as f:
    data = f.read()
# print(data)
print(type(data))
dataS = data.split("\n")

# for idx, val in enumerate(dataS):
#     print(idx, val)


m = dataS[2818:]
# print(m[0])
# x = eval(m[0])
# print(x, type(x))

# print(m)
# print(type(m))

list_of_dicts = []
for line in m:
    try:
        t = eval(line)
        list_of_dicts.append(t)
        print(type(t))
    except:
        pass
print(list_of_dicts)


returns = [
    float(value.split()[-1][:-1])
    for item in list_of_dicts
    for key, value in item.items()
    if "msg" in key
    if "Attempting" in value
]
print(returns)
avg = sum(returns) / len(returns)


account = 100


def returner(current_value, rate):
    roi = current_value * (1 + rate / 100)
    return roi


for idx, _ in enumerate(range(600)):
    account = returner(account, avg)
    print(idx, account)
    if account > 200:
        print("***************")
        break

# for item in list_of_dicts:
#     for key, value in item.items():
#         if "msg" in key:
# if "Attempting" in value:
#     linesplit = value.split()
#     print(linesplit)
#     returns.append(linesplit[-1])
# print(returns)


# list_of_dicts = [
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:50:41",
#         "msg": "--------------------------------------------------",
#     },
#     {"level": 30, "time": "14/02/2021, 05:51:48", "msg": "Initialized"},
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:03",
#         "msg": "Attempting to execute BTC-NEBL-ETH with an age of 190 ms and expected profit of 0.2509%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:03",
#         "msg": "Test: Buying 134 NEBLBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:04",
#         "msg": "Test: Successfully bought NEBLBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:04",
#         "msg": "Test: Selling 134 NEBLETH @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:04",
#         "msg": "Test: Successfully sold NEBLETH @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:04",
#         "msg": "Test: Selling 0.19 ETHBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:04",
#         "msg": "Test: Successfully sold ETHBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 05:54:04",
#         "msg": "Test: Executed BTC-NEBL-ETH position in 830 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:29",
#         "msg": "Attempting to execute BTC-WABI-BNB with an age of 102 ms and expected profit of 0.0398%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:29",
#         "msg": "Test: Buying 644 WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:30",
#         "msg": "Test: Successfully bought WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:30",
#         "msg": "Test: Selling 644 WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:30",
#         "msg": "Test: Successfully sold WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:30",
#         "msg": "Test: Selling 1.17 BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:30",
#         "msg": "Test: Successfully sold BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:30",
#         "msg": "Test: Executed BTC-WABI-BNB position in 796 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:31",
#         "msg": "Attempting to execute BTC-WABI-BNB with an age of 115 ms and expected profit of 0.0377%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:31",
#         "msg": "Test: Buying 644 WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:31",
#         "msg": "Test: Successfully bought WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:31",
#         "msg": "Test: Selling 644 WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:31",
#         "msg": "Test: Successfully sold WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:31",
#         "msg": "Test: Selling 1.17 BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:32",
#         "msg": "Test: Successfully sold BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:32",
#         "msg": "Test: Executed BTC-WABI-BNB position in 835 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:32",
#         "msg": "Attempting to execute BTC-WABI-BNB with an age of 128 ms and expected profit of 0.0288%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:32",
#         "msg": "Test: Buying 644 WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Successfully bought WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Selling 644 WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Successfully sold WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Selling 1.17 BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Successfully sold BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Executed BTC-WABI-BNB position in 834 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Attempting to execute BTC-WABI-BNB with an age of 185 ms and expected profit of 0.0288%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:33",
#         "msg": "Test: Buying 644 WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Successfully bought WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Selling 644 WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Successfully sold WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Selling 1.17 BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Successfully sold BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Executed BTC-WABI-BNB position in 894 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Attempting to execute BTC-WABI-BNB with an age of 88 ms and expected profit of 0.0449%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:34",
#         "msg": "Test: Buying 644 WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:35",
#         "msg": "Test: Successfully bought WABIBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:35",
#         "msg": "Test: Selling 644 WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:35",
#         "msg": "Test: Successfully sold WABIBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:35",
#         "msg": "Test: Selling 1.17 BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:35",
#         "msg": "Test: Successfully sold BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:00:35",
#         "msg": "Test: Executed BTC-WABI-BNB position in 833 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:09",
#         "msg": "Attempting to execute BTC-OMG-ETH with an age of 192 ms and expected profit of 0.0418%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:09",
#         "msg": "Test: Buying 21.63 OMGBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:10",
#         "msg": "Test: Successfully bought OMGBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:10",
#         "msg": "Test: Selling 21.63 OMGETH @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:10",
#         "msg": "Test: Successfully sold OMGETH @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:10",
#         "msg": "Test: Selling 0.086 ETHBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:10",
#         "msg": "Test: Successfully sold ETHBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:01:10",
#         "msg": "Test: Executed BTC-OMG-ETH position in 880 ms",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:35",
#         "msg": "Attempting to execute BTC-ETC-BNB with an age of 114 ms and expected profit of 0.3290%",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:35",
#         "msg": "Test: Buying 29.05 ETCBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:35",
#         "msg": "Test: Successfully bought ETCBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:35",
#         "msg": "Test: Selling 29.05 ETCBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:36",
#         "msg": "Test: Successfully sold ETCBNB @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:36",
#         "msg": "Test: Selling 3.31 BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:36",
#         "msg": "Test: Successfully sold BNBBTC @ market price",
#     },
#     {
#         "level": 30,
#         "time": "14/02/2021, 06:02:36",
#         "msg": "Test: Executed BTC-ETC-BNB position in 849 ms",
#     },
# ]
