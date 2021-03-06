from __future__ import unicode_literals

import os

from mopidy import config, ext, exceptions

__version__ = '0.1.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Voice'
    ext_name = 'voice'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['audiosource'] = config.String()
        schema['max_search_results'] = config.Integer(minimum=1, maximum=50)
        schema['model_dir'] = config.Path()
        schema['model_name'] = config.String()
        schema['use_pocketsphinx'] = config.Boolean()
        return schema

    def validate_environment(self):
        #try:
        #    import pypulseaudio         # noqa
        #except ImportError as e:
        #    raise exceptions.ExtensionError('Unable to find pypulseaudio module', e)
        pass

    def setup(self, registry):
        from .actor import VoiceRecognitionManager
        registry.add('frontend', VoiceRecognitionManager)
