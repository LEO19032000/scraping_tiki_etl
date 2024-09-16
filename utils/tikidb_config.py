from configparser import ConfigParser
import os

def read_db_config(filename='db_config.ini', section='mysql'):
    parser = ConfigParser()
    # Construct the full path to the configuration file
    config_file = os.path.join(os.path.dirname(__file__), '..', 'database', filename)
    parser.read(config_file)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, config_file))
    return db
