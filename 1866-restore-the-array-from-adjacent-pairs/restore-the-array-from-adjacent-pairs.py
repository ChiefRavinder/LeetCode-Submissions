class Solution(object):
    def restoreArray(self, vals):
        pairs = defaultdict(list)
        
        for val in vals:
            pairs[val[0]].append(val[1])
            pairs[val[1]].append(val[0])
        
        result = []
        start = -1000000
        
        for entry in pairs:
            if len(pairs[entry]) == 1:
                start = entry
                break
        
        left = -1000000
        result.append(start)
        
        for i in range(1, len(vals) + 1):
            val = pairs[start]
            newval = val[0] if val[0] != left else val[1]
            result.append(newval)
            left = start
            start = newval
        
        return result