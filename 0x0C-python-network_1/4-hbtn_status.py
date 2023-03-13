#!/usr/bin/python3
"""status.py"""


import requests

if __name__ == "__main__":
    html = requests.get("https://intranet.hbtn.io/status")
    print("""Body response:
\t- type: {}
\t- content: {}""".format(
              type(html.text),
              html.text))
