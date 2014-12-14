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


def main():
  """Bootstrap and start the web server listening."""
  application = web.Application([
    web.url(r'/', IndexHandler)
  ])
  application.listen(8080)
  ioloop.IOLoop.current().start()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print ''
