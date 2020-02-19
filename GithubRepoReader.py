import json as j
import requests as r

def main(username):
    try:
        website = "https://api.github.com/users/" + username + "/repos"
    except TypeError:
        return "ERROR: username must be a string"
    else:
        getRequests = r.get(website)
        loadJson = j.loads(getRequests.content)
        res = []
        for x in loadJson:
            getRequestsCommits = r.get("https://api.github.com/repos/" + username + "/" + x['name'] + "/commits")
            loadJsonCommits = j.loads(getRequestsCommits.content)
            commits = 0
            for y in loadJsonCommits:
                commits += 1
            res.append([x['name'], commits])
        return res

#I pledge my honor that I have abided by the Stevens Honor System - Michael Ameer
