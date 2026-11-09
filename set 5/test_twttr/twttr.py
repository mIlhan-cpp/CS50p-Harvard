
def main():
    i=input('Input: ')
    print('Output: ',shorten(i),end='')
    

def shorten(word):
    result=""
    for _ in word:
        if _.lower() in ['a','e','o','i','u']:
            result+=""
        else:
            result+=_
    return result



if __name__ == "__main__":
    main()


