from redis import StrictRedis

def demo():
    sr = StrictRedis(host='127.0.0.1')

    try:
        result = sr.set('name','itheima')
        print(result)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    demo()