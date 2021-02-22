from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from os import path
from shutil import copy

class ModulesTemplatePlugin(BasePlugin):
    config_scheme = (
        ('modules', config_options.Type(list, default=[])),
        ('try-for-free', config_options.Type(bool, default=True))
    )

    def on_config(self, config, **kwargs):
        config['theme'].dirs.insert(0, path.abspath(path.join(path.dirname(__file__), './theme/overrides')))
        config['extra_css'].append('mkdocs-modules-template.css') # will be copied into the site folder on post build
        config['modules-template'] = self.config
        return config

    def on_pre_build(self, config):
        assert config['theme'].name == 'material'

    def on_post_build(self, config, **kwargs):
        copy(path.abspath(path.join(path.dirname(__file__), './theme/style.css')), path.join(config['site_dir'], 'mkdocs-modules-template.css'))
