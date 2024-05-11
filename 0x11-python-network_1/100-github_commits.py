#!/usr/bin/python3
"""
10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    try:
        for i in range(10):
            response = requests.get(url)
            if response.status_code == 200:
                sha = response.json()[i].get('sha')
                commit = response.json()[i].get('commit')
                autherName = commit.get('author').get('name')
                print(f'{sha}: {autherName}')
    except IndexError:
        pass
