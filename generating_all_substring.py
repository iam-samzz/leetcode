def generate_substring(string_list):
    substring = []
    for i in range(len(string_list)):
        for j in range(i,len(string_list)):
            substring.append(string_list[i:j+1])
    return substring

if __name__ == "__main__":
    print(generate_substring("samaran"))
