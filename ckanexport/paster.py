import sys
from ckan.lib.cli import CkanCommand

from ckanexport import cli

class _Options(object):
    pass

class _DelegateParsing(object):
    usage = cli.__doc__

    def parse_args(self, args):
        assert sys.argv[1:3] == ['--plugin=ckanexport', 'ckanexport'], sys.argv
        del sys.argv[1:3]
        arguments = cli.parse_arguments()
        cfg = arguments['--config']
        options = _Options()
        options.config = cfg if cfg is not None else './development.ini'
        return options, []

class CKANExportCommand(CkanCommand):
    summary = cli.__doc__.split('\n')[0]
    usage = cli.__doc__
    parser = _DelegateParsing()

    def command(self):
        self._load_config()

        cli.main(running_with_paster=True)
