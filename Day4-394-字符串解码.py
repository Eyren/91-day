class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':         #若为'['，开启新一层递归，记录'[...]'内字符串tmp和递归最新索引i
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp        #并执行 res += multi * tmp 拼接字符串
                    multi = 0
                elif s[i] == ']':
                    return i, res       #返回当前括号内记录的res字符串与']'的索引i，更新上层递归指针位置
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)