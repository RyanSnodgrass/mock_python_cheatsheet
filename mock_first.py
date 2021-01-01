# mock_first.py
import configparser

secrets_config = configparser.ConfigParser()
secrets_config.read('secrets_file.conf')


class MockFirst:
    def my_method(self):
        print(secrets_config['DEFAULT']['secretkey'])

    def do_something_with_secrets_value(self):
        return secrets_config['DEFAULT']['secretkey'] + 'hello'


def main():
    mf = MockFirst()
    print(mf.do_something_with_secrets_value())


if __name__ == '__main__':
    main()
