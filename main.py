from package.monitor_cli import cli

if __name__ == '__main__':
    resource = cli()
    from package.resources.constants import FUNCTION_MAP
    f = FUNCTION_MAP.get(resource)