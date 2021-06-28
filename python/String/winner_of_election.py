# Problem Statement:
# Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate.
# Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.
"""
Example:
Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John',
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.
"""
from collections import Counter


def election_winner(votes):
    votes_dict = Counter(votes)
    d = dict()
    for name in votes_dict:
        if votes_dict[name] in d:
            d[votes_dict[name]].append(name)
        else:
            d[votes_dict[name]] = [name]
    max_vote = sorted(d.keys(), reverse=True)[0]
    if len(d[max_vote]) > 1:
        return sorted(d[max_vote])[0]
    else:
        return d[max_vote][0]


if __name__ == '__main__':
    votes = ["jackie", "john", "joh", "joh", "john", "jackie", "jamie", "jamie", "john", "joh", "jamie",
             "joh", "john"]
    winner = election_winner(votes)
    print(winner)
