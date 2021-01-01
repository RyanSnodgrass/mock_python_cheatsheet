# mock_first.py
import configparser

secrets_config = configparser.ConfigParser()
secrets_config.read('secrets_file.conf')


class MockFirst:
    def my_method(self):
        print(secrets_config['DEFAULT']['secretkey'])


def main():
    mf = MockFirst()
    mf.my_method()


if __name__ == '__main__':
    main()
