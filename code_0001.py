# 10원, 50원, 100원, 500원, 1000원 권이 무한대로 있다. 
# 임의의 돈을 지불할 때 가장 적은 개수의 지폐와 동전을 사용하도록 계산하는 코드를 작성하시오.

coins = [1000, 500, 100, 50, 10]

money = int(input('지불할 금액을 입력하세요 : '))

while 0 < money:
    count = 0
    print('지불할 금액은 {0}입니다.'.format(money))
    for aCoin in coins:
        count += (int)(money/aCoin)
        money %= aCoin
    print('지불할 지폐/코인의 개수는 {0}입니다.'.format(count))    
    money = int(input('지불할 금액을 입력하세요 : '))
