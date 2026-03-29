class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tempPrices = prices.copy()

            for source, dest, cost in flights:
                if prices[source] != float("inf"): 
                    if prices[source] + cost < tempPrices[dest]:
                        tempPrices[dest] = prices[source] + cost
            prices = tempPrices

        if prices[dst] == float("inf"): return -1
        else: return prices[dst]

                