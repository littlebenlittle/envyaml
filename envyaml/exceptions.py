
class EnvError(Exception):
    """Raised when a required environment variable is missing
       or invalid.
    """
    pass

class VersionError(Exception):
    """Raised when the version specified in env.yaml is not
       supported.
    """
    pass
