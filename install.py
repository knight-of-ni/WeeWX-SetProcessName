#
#    Copyright 2014-2024 Andrew Bauer
#    Distributed under the terms of the GNU Public License (GPLv3)
#    See LICENSE for details.
#
from weecfg.extension import ExtensionInstaller

def loader():
    return SetProcTitleInstaller()

class SetProcTitleInstaller(ExtensionInstaller):
    def __init__(self):
        super(SetProcTitleInstaller, self).__init__(
            version="0.1",
            name='SetProcessName',
            description='Set the weewx process name to a user specified value.',
            author="Andrew Bauer",
            author_email="zonexpertconsulting@outlook.com",
            prep_services='user.SetProcessName.SetProcessName',
            config={
                    'SetProcessName': {
                        'name': 'weewxd'}},
            files=[('bin/user', ['bin/user/SetProcessName.py'])]
            )
