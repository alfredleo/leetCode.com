# coding=utf-8

# 389. Find the Difference
# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.
# Input:
# s = "abcd"
# t = "abcde"
# Output: e
# Explanation: 'e' is the letter that was added.
import timeit


def findTheDifference(s, t):
    return chr(sum(bytearray(t, 'utf8')) - sum(bytearray(s, 'utf8')))


def findTheDifference1(s, t):
    # the straightforward solution is to iterate over every character in string s and remove it from string t
    # that would give n*n, which is not good.
    for c in s:
        t = t.replace(c, '', 1)
    return t


def findTheDifference2(s, t):
    # This solution is voted as the best one on LeetCoode, but testings shows that the first one
    # findTheDifference is almost 6 times faster on 10000 repetitions.
    summ = 0
    for char in s:
        summ ^= ord(char)
    for char in t:
        summ ^= ord(char)
    return chr(summ)


ss = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkr" \
     "gcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmt" \
     "vjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpg" \
     "zjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyau" \
     "mmenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwf" \
     "xvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymd" \
     "rfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqc" \
     "ribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnyc" \
     "ucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhd" \
     "apjrlrnkbklwkrvoaziznlpor"
tt = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybf" \
     "ffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrl" \
     "zkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkc" \
     "afvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfd" \
     "gnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcg" \
     "nirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggec" \
     "jsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqs" \
     "zuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxp" \
     "tswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhy" \
     "orgbysyjbxsspnjdewjxbhpsvj"


def main():
    # simple check of functions
    print findTheDifference('abcd', 'kdcab')
    print findTheDifference(ss, tt)
    print findTheDifference1(ss, tt)
    print findTheDifference2(ss, tt)
    # time based check
    print timeit.timeit("findTheDifference(ss, tt)", setup="from __main__ import *", number=100000)
    print timeit.timeit("findTheDifference1(ss, tt)", setup="from __main__ import *", number=100000)
    print timeit.timeit("findTheDifference2(ss, tt)", setup="from __main__ import *", number=100000)


if __name__ == '__main__':
    main()
