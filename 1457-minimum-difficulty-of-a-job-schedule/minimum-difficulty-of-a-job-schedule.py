class Solution:
    def minDifficulty(self, jobDifficulty, d):
        length = len(jobDifficulty)

        if len(jobDifficulty) < d:
            return -1

        @functools.cache # This encapsulates the memoization
        def helper(daysLeft, startJob):
            if daysLeft == 1:
                return max(jobDifficulty[startJob:])

            maxDifficulty = jobDifficulty[startJob]
            daysLeft -= 1
            stop = length - startJob - daysLeft + 1
    
            result = math.inf
            for i in range(1, stop):
                maxDifficulty = max(maxDifficulty, jobDifficulty[startJob + i - 1])
                result = min(result, helper(daysLeft, startJob + i) + maxDifficulty)   
            return result

        return helper(d, 0)