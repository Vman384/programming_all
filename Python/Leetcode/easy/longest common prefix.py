def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    m = len(min(strs,key=len))
    i = 0
    reference = strs[0]
    while i < m:
        for myStr in strs:
            if myStr[i] != reference[i]:
                return reference[:i]
        i += 1
    return reference[:m]
strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))
