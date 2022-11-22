
#!/usr/bin/python3
"""
This module fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {:}".format(type(html)))
        print("\t- content: {:}".format(html))
        print("\t- utf8 content: {:}".format(html.decode('utf-8')))
