def get_helloworld():
    return 'hello world'

def get_bye():
    return 'bye'

def test_get_helloworld():
  assert 'hello world' == get_helloworld()


def test_get_helloworld():
  assert 'bye' == get_bye()


def main():
    print(get_helloworld())


if __name__ == '__main__':
    main()
