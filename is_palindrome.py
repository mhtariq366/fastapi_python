def isPalindrome(s: str):
    updated_s = ""
    for c in s:
        if c.isalpha() or c.isdigit():
            updated_s += c.lower()

    l=len(updated_s)
    ll=int(l/2)
    for i in range(ll):
        if updated_s[i] != updated_s[l-i-1]:
            return False

    return True





print(isPalindrome('0P'))
