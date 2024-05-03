class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0

        while(i < len(version1) or j < len(version2)):
            v1 = v2 = 0

            while (i < len(version1) and version1[i] != '.'):
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while (j < len(version2) and version2[j] != '.'):
                v2 = v2 * 10 + int(version2[j])
                j += 1

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

            i, j = i + 1, j + 1

        return 0