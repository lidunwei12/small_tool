import huffman

word = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'i', 'k', 'm',
        'n', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~', '!', '@', '#',
        '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', '?', '/', '>',
        '.', '<', ',']
word1 = {'1': 1, '2': 2, '3': 3, '5': 5, '4': 4, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, 'a': 10, 'b': 11, 'c': 12,
         'd': 13, 'e': 14, 'f': 15}


def encode_b64(n):
    # num = [32, 16, 8, 4, 2, 1]
    num = [16, 8, 32, 4, 2, 1]
    ans = 0
    for i in range(len(n)):
        ans = ans + num[i] * int(n[i])
    return word[ans]


def huffman_encode(s1):
    content = []
    for i in s1:
        content.append(i)
    data_handle = list(set(content))
    word_dict = {}
    for word_content in data_handle:
        word_dict[word_content] = 0
    for i in s1:
        for key, value in word_dict.items():
            if i.find(key) != -1:
                value = value + 1
            word_dict[key] = value
    result = []
    for key, value in word_dict.items():
        result.append((key, value))
    temp_content = huffman.codebook(result)
    print(temp_content)
    ans = ''
    for i in s1:
        ans = ans + temp_content[i]
    last_result = []
    for j in range(0, len(ans), 6):
        last_result.append(encode_b64(ans[j:j + 6]))
    return last_result


def base_81(s1, num):
    ans = ''
    for i in s1:
        temp = str(bin(word1[i]).replace('0b', ''))
        content = 4 - len(temp)
        temp = '0' * content + temp
        ans = ans + temp
    final_result = ''
    print(len(ans))
    if len(ans) % num != 0:
        ans = ans + '0' * (num - len(ans) % num)
    for i in range(0, len(ans), num):
        result_temp = ans[i:i + num]
        if num == 6:
            result = int(result_temp[0]) * 16 + int(result_temp[1]) * 4 + int(result_temp[2]) * 8 + int(
                result_temp[3]) * 1 + int(result_temp[4]) * 2 + int(result_temp[5]) * 32
        else:
            result = int(result_temp[0]) * 16 + int(result_temp[1]) * 8 + int(
                result_temp[2]) * 4 + int(result_temp[3]) * 2 + int(result_temp[4])
        final_result = final_result + word[result]
    return final_result


s1 = '8527147fe1f5426f9dd545de4b27ee00'
ans = base_81(s1, 6)
final_result = huffman_encode(s1)
print(''.join(final_result))
print(ans)
print(len(''.join(final_result)), len(s1), len(ans))
# print(len(''.join(huffman_encode(ans))))
