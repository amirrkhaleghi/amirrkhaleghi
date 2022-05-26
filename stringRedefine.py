import math
class SString:

    def __init__(self, s):

        self.s = s

    def swichH(self):

        if len(self.s) % 2 == 0:
            ss = list(self.s)[:(len(self.s) // 2)]
            ss1 = list(self.s)[(len(self.s)// 2):]
            ss6 = ss1 + ss
            sstring = ""
            for i in ss6:
                sstring += i
            return i
        else:
            ss = list(self.s)[:(len(self.s) // 2)]
            mid = list(self.s)[len(self.s) // 2]
            ss1 = list(self.s)[(len(self.s)// 2 + 1):]
            ss6 = ss1 + list(mid) + ss
            for i in ss6:
                sstring += i
            return i

    def encryp(self):
        charList = []
        for char in self.s:

            if char.islower():
                rev_char = chr(ord('z') - ord(char) + ord('a'))
                charList.append(rev_char)

            elif char.isupper():
                rev_char = chr(ord('Z') - ord(char) + ord('A'))
                charList.append(rev_char)


        str_ing = "" 
        for i in charList:
                str_ing += i
        return i


    def primChecker(num):
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True