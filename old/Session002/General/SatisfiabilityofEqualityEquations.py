from collections import defaultdict
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph=defaultdict(set)
        not_equal=[]

        def is_equal(a,b,visited):
            if a==b:
                return True
            visited.add(a)
            for adj in graph[a]:
                if adj in visited:
                    continue
                else:
                    if is_equal(adj,b,visited):
                        return True
            return False
        
        for a,e,_,b in equations:
            if e=='!':
                not_equal.append((a,b))
            else:
                graph[a].add(b)
                graph[b].add(a)
        for a,b in not_equal:
            if is_equal(a,b,set()):
                return False
        return True




if __name__=="__main__":
    c=Solution()
    print(c.equationsPossible(["a==b","b!=a"]))#False
    print(c.equationsPossible(["b==a","a==b"]))#True
    print(c.equationsPossible(["a==b","b==c","a==c"]))#True
    print(c.equationsPossible(["a==b","b!=c","c==a"]))#False
    print(c.equationsPossible(["c==c","b==d","x!=z"]))#True
    print(c.equationsPossible( ["c==c","f!=a","f==b","b==c"] ))#True
            

          

        