str = input()
char_list = [-1 for _ in range(26)]
for i, char in enumerate(str):
    if char_list[ord(char) - ord("a")] == -1:
        char_list[ord(char) - ord("a")] = i

print(*char_list)
