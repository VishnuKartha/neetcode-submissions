import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        graph = {}
        indegree = {chr(ord('a') +  i): 0 for i in range(26)}
        def get_node_with_no_incoming_edge():
            for k,vals in graph.items():
                if indegree[k] == 0:
                    for v in vals:
                        indegree[v] -= 1
                    del graph[k]
                    return k
            return None

        for i in range(1, len(words)):
            curr_word = words[i]
            prev_word = words[i - 1]
            min_len = min(len(curr_word),len(prev_word))
            j = 0
            while True:
                if j < (min_len - 1) and curr_word[j] == prev_word[j]:
                    j+= 1
                else:
                    break
            if prev_word[j] not in graph:
                graph[prev_word[j]] = set()
            if prev_word[j] != curr_word[j] or len(prev_word) > len(curr_word):
                graph[prev_word[j]].add(curr_word[j])
        

        for key,val in graph.items():
            for v in val:
                indegree[v] += 1
        
        result = ""

        while graph:
            ch = get_node_with_no_incoming_edge()
            if ch is None:
                return ""
            result += ch
        return result



        
        