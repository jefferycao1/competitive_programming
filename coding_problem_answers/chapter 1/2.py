from collections import Counter

a = "bsdf"
b = "asdf"

def compare(str1, str2):
        arr = list(str2)
        for i in str1:
                if (i in arr):
                        arr.remove(i)
                else:
                        return False
        if(len(arr) == 0):
                return True
        else:
                return False


def comparecounter(str1, str2):
        cnt = Counter(str1)
        for i in str2:
                if (i in cnt):
                        cnt[i] -= 1
                else:
                        return False

                if (cnt[i] == 0):
                        del cnt[i]
        return len(cnt) == 0

if __name__ == "__main__":
        print(comparecounter(a, b))
