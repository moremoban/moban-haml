from jinja2 import Environment, FileSystemLoader, Template
from hamlish_jinja import HamlishExtension


class EngineHaml(object):
    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs
        env_params = dict(
            loader=FileSystemLoader(template_dirs),
            extensions=[HamlishExtension]
        )
        if is_extension_list_valid(extensions):
            env_params["extensions"] += extensions
        self.jj2_env = Environment(**env_params)
        self.jj2_env.hamlish_mode = 'indented'

    def get_template(self, template_file):
        template = self.jj2_env.get_template(template_file)
        return template

    def get_template_from_string(self, string):
        return Template(string)

    def apply_template(self, template, data, _):
        rendered_content = template.render(**data)
        return rendered_content


def is_extension_list_valid(extensions):
    return (
        extensions is not None
        and isinstance(extensions, list)
        and len(extensions) > 0
    )
