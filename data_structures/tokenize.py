def tokenize(string, dic, tokenized = []):
    substring = ''

    i = 0
    while i < len(string):
        substring += string[i]
        if substring in dic:
            if i == (len(string) - 1):
                tokenized.append(substring)
                break
            else:
                tokenized = tokenize(string[i+1:], dic, tokenized)
                if tokenized == False:
                    tokenized = []
                    i += 1
                    continue
                else:
                    tokenized.append(substring)
                    return tokenized
        elif i == len(string) - 1:
            return False
        i+=1
    
    return tokenized

string = 'hellogoodmorning'
dic = set(['hello', 'good', 'morning', 'he', 'hell', 'go'])

print(tokenize(string, dic))
