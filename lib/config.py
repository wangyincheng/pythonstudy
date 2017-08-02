import os.path
import configparser
import logging

config_file = (os.path.join('config.ini'),
                os.path.join( 'config.custom.ini') )
config = configparser.ConfigParser()
config.read(config_file)


