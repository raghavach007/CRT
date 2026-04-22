# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
#         reversed_text = char + reversed_text
#     return reversed_text

# print(reverse_string("Python"))

def freq_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d

print(freq_count("abcabc"))

def is_Anagram(st1,st2):
    return freq_count(st1) == freq_count(st2)

print(is_Anagram("space","paces"))
print(is_Anagram("abc", "abcabc"))