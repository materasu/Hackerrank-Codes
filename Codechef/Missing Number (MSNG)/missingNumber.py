import os

def character_to_ascii_mappings():
    char_to_ascii = {}
    start_alphabet_number = ord('A') - (ord('9') - ord('0') + 1)
    for i in range(0,36,1):
        if(i < 10):
            char_to_ascii[str(i)] = i
        else:
            char_to_ascii[chr(start_alphabet_number+i)] = i
    
    return char_to_ascii

def convert_to_decimal(n, number, base, char_to_ascii):
    decimal_value = 0
    position_value = 1
    for i in range(n-1, -1, -1):
        character_value = char_to_ascii[number[i]]
        decimal_value += character_value * position_value
        position_value *= base
    
    return decimal_value

def find_common_number(n, pairs, char_to_ascii):
    UPPER_LIMIT = 1000000000000
    decimal_conversions = []
    for i in range(0,n,1):
        base = pairs[i][0]
        number = pairs[i][1]
        number_size = len(number)
        if(base == -1):
            for j in range(2,37,1):
                decimal_conversion = convert_to_decimal(number_size, number, j, char_to_ascii)
                if(decimal_conversion > UPPER_LIMIT):
                    pass
                else:
                    decimal_conversions.append([decimal_conversion, i])
        else:
            decimal_conversion = convert_to_decimal(number_size, number, base, char_to_ascii)
            if(decimal_conversion > UPPER_LIMIT):
                pass
            else:
                decimal_conversions.append([decimal_conversion, i])

    decimal_conversions.sort()
    print(decimal_conversions)
    flag = 0
    previous_number = -1
    previous_index = -1
    count = 0
    for i in range(0,len(decimal_conversions),1):
        if(decimal_conversions[i][0] == previous_number):
            if(decimal_conversions[i][1] != previous_index):
                count += 1
                previous_index = decimal_conversions[i][1]
            else:
                pass
        else:
            if(count == n):
                answer = previous_number
                flag = 1
            else:
                previous_number = decimal_conversions[i][0]
                previous_index = decimal_conversions[i][1]
                count = 1 
        if(flag == 1):
            break

    if(flag == 0):
        answer = -1
    
    return answer


if __name__ == '__main__':
    char_to_ascii = character_to_ascii_mappings()
    try:
        t = int(input())
        while(t > 0):
            n = int(input())
            pairs = []
            for n_itr in range(0,n,1):
                line = input().split(' ')
                pairs.append([int(line[0]), line[1]])
            answer = find_common_number(n, pairs, char_to_ascii)
            print(answer)
            t -= 1   
    except:
        pass