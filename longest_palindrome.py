class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_single = 0
        d = {}
        length = 0
        for i in s:
            d[i] = d.get(i, 0) + 1
        for key in d:
            if d[key] % 2 == 0:
                length += d[key]
            elif d[key] > max_single:
                max_single = d[key]
        print(max_single, length)
        return d

if __name__ == '__main__':
    
    s = Solution()
    a = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print(s.longestPalindrome(a))
    d = {'c': 25, 'i': 53, 'v': 22, 'l': 41, 'w': 23, 'a': 87, 'r': 67, 't': 106, 'e': 142, 's': 40, 'n': 61, 'g': 23, 'h': 74, 'p': 16, 'o': 78, 'y': 8, 'd': 52, 'u': 17, 'W': 2, 'q': 1, 'm': 13, 'b': 11, 'f': 26, 'z': 1, 'I': 3, 'B': 1, 'T': 2, 'k': 3, 'G': 1}
    count = 0
    for key in d:
        if d[key] % 2 == 0: count += d[key]
    print(count)