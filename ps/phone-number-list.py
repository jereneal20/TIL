def solution(phone_book):
    root_mp = {}
    for phone_number in phone_book:
        has_prefix = True
        mp = root_mp
        for ch in phone_number + '$':
            if ch == '$':
                mp[ch] = {}
                break
            if '$' in mp:
                return False
            if ch not in mp:
                has_prefix = False
                mp[ch] = {}
            mp = mp[ch]
        if has_prefix:
            return False
    return True

