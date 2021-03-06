# Note for Visual Studio: After adding CONFIG_MODE to the environment,
# need to close and restart Visual Studio for setting to take effect


class Config(object):
    ERROR_404_HELP = False
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'they killed kenny'
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True


config_dict = {
  'DEFAULT': DevelopmentConfig,
}
