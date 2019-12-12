from  MyQR import myqr
import os


def gen_code():
    myqr.run(words=r'http://47.103.193.202/p1_hot3.png',
             picture = '0.jpg', colorized= True, version=10,)

    print(os.getcwd())


if __name__ == '__main__':
    gen_code()

