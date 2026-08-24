class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = 1
        i = 0
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                sign = -1
            i += 1

        res = 0
        n = len(s)
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            # check overflow before multiplying
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1

        return sign * res


if __name__ == "__main__":
    tests = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        "+1",
        "",
        "   +0 123",
    ]

    sol = Solution()
    for t in tests:
        print(f"input: {t!r} -> output: {sol.myAtoi(t)}")
