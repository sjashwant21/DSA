class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken=set(brokenLetters)
        cnt, word=0, True
        text+=' '
        for c in text:
            word&=(not (c in broken))
            isspace=c==' '
            cnt+=(word and isspace)
            word|=isspace
        return cnt