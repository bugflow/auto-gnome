# from os import environ
from environ import Env as EnvironEnv
from .kms import string_or_b64kms


class Env(EnvironEnv):
    def __call__(self, var, default=None, cast=None, parse_default=False):
        value = self.get_value(
            var, default=default, cast=cast, parse_default=parse_default)
        return string_or_b64kms(value)

# class Env(object):
#     """Wrapper around os.getenv with added AWS KMS encryption support."""

#     def __call__(self, var, default=None):
#         value = environ.get(var, default)
#         return string_or_b64kms(value)
