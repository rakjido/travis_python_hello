def get_helloworld():
    return print('hello world')

def test_get_helloworld():
  assert 'hello world' == get_helloworld()


def main():
    print(get_helloworld())


if __name__ == '__main__':
    main()
