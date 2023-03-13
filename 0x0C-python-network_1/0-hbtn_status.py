#!/usr/bin/python3
"""status.py"""


import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(
              type(html),
              html,
              html.decode("utf8")))
