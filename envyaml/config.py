
import os
import yaml
from types import SimpleNamespace
from yaml.scanner import ScannerError
from envyaml.exceptions import EnvError, VersionError

import env_pb2 as pb


class Config(SimpleNamespace):

    def __init__(self):
        config_pb = _load_config_pb()
        missing = []
        for ev in config_pb.envs:
            ev_val = os.environ.get(ev.key)
            if ev.required and not ev_val:
                missing.append(ev)
            setattr(self, ev.key, ev_val)
        if any(missing):
            message = 'The following environment variables are not set:\n'
            for ev in missing:
                message += ev.key + '\n'
            raise EnvError(message)

    def validate():
        errors = []
        if errors:
            raise EnvError(errors)


def _load_config_pb():
    spec = _load_spec()
    config_pb = _config_pb_from_spec(spec)
    return config_pb


def _load_spec():
    env_yaml_path = os.environ.get('ENV_YAML')
    if not env_yaml_path:
        raise EnvError('ENV_YAML not set.')
    try:
        f = open(env_yaml_path)
        spec = yaml.load(f)
    except OSError:
        print(f'The file at ENV_YAML={env_yaml_path} does not exist.')
        print('Did you remember to mount it into the container?')
        raise
    except ScannerError:
        print(f'The file at ENV_YAML={env_yaml_path} failed to validate.')
        raise
    return spec


def _config_pb_from_spec(spec):
    if spec['version'] == '0':
        config_pb = pb.Config(
            envs=[pb.EnvVar(
                key=ev.get('key'),
                value=ev.get('value'),
                required=ev.get('required'),
                validators=[pb.Validator(
                    regex=v.get('regex'),
                    description=v.get('description'),
                ) for v in ev.get('validators')]
            ) for ev in spec['config']]
        )
    else:
        raise VersionError(
            f"Version {spec['version']}' "
            + "(from ENV_YAML={os.environ.get('ENV_YAML')}) "
            + "is not supported."
        )
    return config_pb

config = Config()
