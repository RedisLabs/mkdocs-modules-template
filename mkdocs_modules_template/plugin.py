from mkdocs.plugins import BasePlugin
from os import path
from shutil import copy

class ModulesTemplatePlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        config['theme'].dirs.insert(0, path.abspath(path.join(path.dirname(__file__), '../overrides')))
        config['extra_css'].append('extra.css') # will be copied into the site folder on post build
        return config

    def on_pre_build(self, config):
        assert config['theme'].name == 'material'

    def on_post_build(self, config, **kwargs):
        copy(path.abspath(path.join(path.dirname(__file__), '../extra.css')), path.join(config['site_dir'], 'extra.css'))
