import appdirs

import quetzal._auto_client.configuration


class Configuration(quetzal._auto_client.configuration.Configuration):
    # Use this later for particular extensions/modifications on the API
    # configuration object
    pass


def get_config_dir():
    from quetzal.client import __version__
    return appdirs.user_config_dir(
        appname='quetzal_client',
        appauthor='quetzal',
        version=__version__,
        roaming=False,
    )