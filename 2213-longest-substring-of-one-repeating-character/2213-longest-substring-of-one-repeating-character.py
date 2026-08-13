from typing import List
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n=len(s)
        tree = [None]*(4*n)

        def merge(a,b):
            left_char_a,right_char_a,prefix_a,suffix_a,best_a,len_a = a
            left_char_b,right_char_b,prefix_b,suffix_b,best_b,len_b = b
            left_char=left_char_a
            right_char=right_char_b
            prefix=prefix_a
            suffix=suffix_b
            best=max(best_a,best_b)

            if right_char_a==left_char_b:
                best=max(best,suffix_a + prefix_b)

                if prefix_a==len_a:
                    prefix=len_a+prefix_b

                if suffix_b==len_b:
                    suffix=suffix_a+len_b 

            return(left_char,right_char,prefix,suffix,best,len_a+len_b)

        def build(node,l,r):
            if l==r:
                tree[node]=(s[l],s[l],1,1,1,1)
                return
            mid=(l+r)//2
            build(node*2,l,mid)
            build(node*2+1,mid+1,r)
            tree[node]=merge(
                tree[node*2],
                tree[node*2+1]
            )


        def update(node,l,r,index,char):
            if l==r:
                tree[node]=(char,char,1,1,1,1)
                return
            mid=(l+r)//2
            if index<=mid:
                update(node*2,l,mid,index,char)
            else:
                update(node*2+1,mid+1,r,index,char)
            
            tree[node]=merge(
                tree[node*2],
                tree[node*2+1]
            )
        
        build(1,0,n-1)
        answer=[]
        for char,index in zip(queryCharacters,queryIndices):
            update(1,0,n-1,index,char)
            answer.append(tree[1][4])
        return answer