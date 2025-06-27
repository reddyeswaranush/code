class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        if k == 1:
            return s
        def is_subseq(subseq, full):
            full_iter = iter(full)
            return all(c in full_iter for c in subseq)
        at_least_k = {key:value for key,value in filter(lambda x:x[1] >= k, collections.Counter(s).items())}
        queue = deque([""])
        curr_max = ""
        while queue:
            string = queue.popleft()
            curr_count = collections.Counter(string)
            for key in at_least_k:
                if k * (curr_count[key] + 1) <= at_least_k[key]:
                   subseq = string + key
                   if is_subseq(subseq * k, s):
                      queue.append(subseq)
                      if len(subseq) < len(curr_max):
                          continue   
                      if len(subseq) == len(curr_max) and subseq > curr_max:
                          curr_max = subseq
                          continue
                      if len(subseq) > len(curr_max):
                          curr_max = subseq
        return curr_max