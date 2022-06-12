from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-10 ** 6 for _ in range(len(prices))] for _ in range(4)]
        BUY = 0
        SELL = 1
        WAIT = 2
        COOLDOWN = 3

        def dp(buy_price, state, curr_idx):
            if curr_idx >= len(prices):
                return 0

            elif memo[state][curr_idx] != -10 ** 6:
                return memo[state][curr_idx]

            else:
                if state == BUY:  # we can try selling or waiting
                    memo[BUY][curr_idx] = max(dp(prices[curr_idx], SELL, curr_idx + 1),
                                              dp(prices[curr_idx], WAIT, curr_idx + 1))
                elif state == SELL:  # change to cooldown
                    memo[SELL][curr_idx] = prices[curr_idx] - buy_price + dp(-1, COOLDOWN, curr_idx + 1)
                elif state == WAIT:
                    memo[WAIT][curr_idx] = max(dp(buy_price, WAIT, curr_idx + 1),
                                               dp(buy_price, SELL, curr_idx + 1))

                elif state == COOLDOWN:
                    memo[COOLDOWN][curr_idx] = max(dp(buy_price, COOLDOWN, curr_idx + 1),
                                                   dp(buy_price, BUY, curr_idx + 1))

                return memo[state][curr_idx]

        return max(dp(-1, COOLDOWN, 0), dp(prices[0], BUY, 0))

s = Solution()
s.maxProfit([0,0,5,0,0,4,10,6,0,0])