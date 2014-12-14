#!/usr/bin/env python
"""A simple Tornado web server for showing off multiple instance EC2
deployments using AWS CodeDeploy.
"""

from tornado import ioloop
from tornado import web

import pyinfo


class IndexHandler(web.RequestHandler):
  """A simple HTTP handler."""
  def get(self):
    self.write(pyinfo.pyinfo())


class VersionHandler(web.RequestHandler):
  """A handler to read and display the value in the version file."""
  def get(self):
    self.write(open('version.txt').read())


def main():
  """Bootstrap and start the web server listening."""
  application = web.Application([
    web.url(r'/', IndexHandler),
    web.url(r'/version', VersionHandler)
  ])
  application.listen(8080)
  ioloop.IOLoop.current().start()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print ''
