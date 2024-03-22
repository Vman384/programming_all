def open_file(file):
    with open(file) as f:
        data = f.read()
    return data 

def read_code1(code: str):
    line = []
    word_to_number = {
    'zero' : 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
    total = 0
    for i in range(len(code)):
        if code[i] == '\n':
            if len(line)>1:
                total += line[0]*10+line[-1]
            else:
                total += line[0]*11
            line = []
        else:
            if code[i].isdigit():
                line.append(int(code[i])) 
    if len(line)>1:
        total += line[0]*10+line[-1]
    else:
        total += line[0]*11
    line = []
    return total


def get_total(code):
    matrix = code.split('\n')
    word_to_number = {
    'zero' : 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }
    total = 0
    for line in matrix:
        numbers = []
        for number in word_to_number.keys():
            if line.find(number) != -1:
                numbers.append([word_to_number[number],line.find(number)])
        for i in range(len(line)):
             if line[i].isdigit():
                numbers.append([int(line[i]),i]) 
        numbers.sort(key=lambda x: x[1])
        if len(numbers)>1:
            total += numbers[0][0]*10+numbers[-1][0]
        else:
            total += numbers[0][0]*10
    return total

if __name__ == "__main__":
    code = open_file("./day1input.txt")
    # print(read_code1(code))
    print(get_total(code))