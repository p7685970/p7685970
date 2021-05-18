import pyupbit

access = "qZ2PatOpAYzZ2UHMZOVEkc3YqbIcvxJxNnR2h829"          # 본인 값으로 변경
secret = "28II1NBhU3nPZM4YXkXNS6AhhPcKSBpx6u950xgU"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETC"))     # KRW-META 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

print(upbit.get_balance("KRW-XRP"))     # KRW-ARDR 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

print(upbit.get_balance("KRW-META"))     # KRW-ETC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회