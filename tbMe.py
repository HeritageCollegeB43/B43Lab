import datetime
def tb_show():
    print('Tony Bebawy')
    print('Programming IV')
    print(datetime.datetime.now().strftime('%d/%m/%Y'))

def count():
    for i in range(1, 10):
        print(i)

if __name__ == '__main__':
    tb_show()
