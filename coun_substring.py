# how many no. of times substring occur in string
def count_substring(string, sub_string):
    count = 0
    i = 0
    while i <= len(string):
        index = string.find(sub_string, i, len(string))
        print('index', index)
        i = index+1
        if index == -1:
            return count
        count = count+1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
