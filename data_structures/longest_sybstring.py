def length_of_longest_substring(s):
    char_set=set()
    left_pointer=0
    max_length=0

    for right_pointer in range(len(s)):
        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1

        char_set.add(s[right_pointer])
        max_length=max(max_length,right_pointer - left_pointer + 1)
    return max_length

if __name__=="__main__":
    input_str = "abcabcbb"
    result = length_of_longest_substring(input_str)
    print("Length of Longest Substring:", result)