# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


prices =[7,6,4,3,1]


#BRUTE FROCE
# max_profit = float('-inf')

# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         if prices[i]<prices[j]:
#             profit=prices[j]-prices[i]
#             print(prices[j],prices[i],profit)
#             max_profit=max(profit,max_profit)
    
# if max_profit>0:
#     print(max_profit)
# else:
#     print(0)


#TWO POINTERS

# prices = [7, 6,4,3,1]

left = 0   # buy
right = 1  # sell
max_profit = 0

while right < len(prices):
    if prices[right] > prices[left]:
        profit = prices[right] - prices[left]
        max_profit = max(max_profit, profit)
    else:
        left = right  # move buy pointer
    right += 1

print(max_profit)

