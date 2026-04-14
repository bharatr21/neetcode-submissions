class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        start = 0
        total_gas = 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                start = i + 1
                total_gas = 0
        return start