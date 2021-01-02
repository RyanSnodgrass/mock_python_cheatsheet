# mock_first.py
import configparser

secrets_config = configparser.ConfigParser()
secrets_config.read('secrets_file.conf')


class MyMockFileFirst:
    def my_method(self):
        print(secrets_config['DEFAULT']['secretkey'])

    def do_something_with_secrets_value(self):
        return secrets_config['DEFAULT']['secretkey'] + 'hello'


class MySecondMockFile(MyMockFileFirst):
    def do_something_else(self):
        return secrets_config['DEFAULT']['secretkey'] + 'world'


def main():
    mf = MySecondMockFile()
    print(mf.do_something_else())


if __name__ == '__main__':
    main()
