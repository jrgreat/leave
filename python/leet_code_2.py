class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        index = len(s) - 1
        eat_boy = list()
        result = 0
        for i in range(len(g) - 1, -1, -1):
            while(index>=0 and s[index]>=g[i]):
                if i in eat_boy:
                    break
                eat_boy.append(i)
                result += 1
                index -= 1
        return result

def regular_expression():
    import re
    pattern = re.compile(r'\d+')
    str = "123ddef323"
    matches = re.match(pattern, str)
    findall = re.findall(pattern, str)
    if matches:
        print(matches.group(0))

if __name__=="__main__":
    regular_expression()