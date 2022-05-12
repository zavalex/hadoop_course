import sys

def mapv1():
    for line in sys.stdin:
        d = {}
        for word in line.split():
            d[word] = d.get(word, 0) + 1
            
        for key, value in d.items():
            print(f'{key}\t{value}')

def mapv2():
    d = {}
    for line in sys.stdin:
        for word in line.split():
            d[word] = d.get(word, 0) + 1
    for key, value in d.items():
        print(f'{key}\t{value}')

if __name__ == "__main__":
    mapv2()