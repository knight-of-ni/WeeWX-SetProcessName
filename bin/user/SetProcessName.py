#
#    Copyright 2014-2024 Andrew Bauer
#    Distributed under the terms of the GNU Public License (GPLv3)
#    See LICENSE for details.
#

VERSION = '0.1'

from weewx.engine import StdService
import setproctitle

try:
  # Test for new-style weewx logging by trying to import weeutil.logger
  import weeutil.logger
  import logging
  log = logging.getLogger(__name__)

  def logdbg(msg):
    log.debug(msg)

  def loginf(msg):
    log.info(msg)

  def logerr(msg):
    log.error(msg)

except ImportError:
  # Old-style weewx logging
  import syslog

  def logmsg(level, msg):
    syslog.syslog(level, 'cmon: %s:' % msg)

  def logdbg(msg):
    logmsg(syslog.LOG_DEBUG, msg)

  def loginf(msg):
    logmsg(syslog.LOG_INFO, msg)

  def logerr(msg):
    logmsg(syslog.LOG_ERR, msg)

class SetProcessName(StdService):
  def __init__(self, engine, config_dict):
    super(SetProcessName,self).__init__(engine, config_dict)
    process_name = config_dict['SetProcessName']['name']
    loginf('SetProcessName extension version %s.' % VERSION)
    loginf('Setting weewx process name to "%s".' % process_name)
    setproctitle.setproctitle(process_name)

