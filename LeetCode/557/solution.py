def reverseWords(s: str) -> str:
        s_list = s.split(" ")
        rev_list = []

        for word in s_list:
            rev_list.append(reversed(word))

        rev_str = " ".join(rev_list)

        return rev_str

print(reverseWords("Let's take LeetCode contest"))