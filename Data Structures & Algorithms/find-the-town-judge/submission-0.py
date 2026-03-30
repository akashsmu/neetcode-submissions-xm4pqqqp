class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_map = defaultdict(list)
        trustee_map = defaultdict(list)
        for ai,bi in trust:
            trusted_map[bi].append(ai)
            trustee_map[ai].append(bi)
        

        for trusted, trustee in trusted_map.items():
            if (len(trustee) == n -1) and (trusted not in trustee_map):
                return trusted
        return -1





        return -1