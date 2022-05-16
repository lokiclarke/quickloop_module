import time

class loop:
    def count(start=1,stop=10,step=1,delay=1):
        start = start
        stop = stop+1
        count_range = range(start,stop,step)
        for i in count_range:
            time.sleep(delay)
            print(i)
        return i

    def spell_word(word: str,delay=1.0):
        for letter in word:
            time.sleep(delay)
            print(letter)
        return letter

    def repeat(msg: str,count=3,delay=1):
        count = count+1
        for i in range(1,count):
            time.sleep(delay)
            print(msg)
        return msg

    def help():
        print("Just a collection of simple for loops")

if __name__ == '__main__':
    help()









