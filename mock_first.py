# mock_first.py
import configparser

secrets_config = configparser.ConfigParser()
secrets_config.read('secrets_file.conf')


class Foo:
    def my_method(self):
        print(secrets_config['hello'])
