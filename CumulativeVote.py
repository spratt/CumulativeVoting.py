import json
import sys
from collections import defaultdict

class CumulativeVote:
    def __init__(self, ballots):
        self.totals = defaultdict(lambda: 0.0)
        for ballot in ballots:
            for candidate in ballot:
                self.totals[candidate] += float(ballot[candidate])

    def maxes(self):
        max_val = max([l[1] for l in self.totals.items()])
        maxes = [item[0] for item in self.totals.items() if max_val == item[1]]
        return maxes

    def dump(self):
        return sorted([item for item in self.totals.items()], key=lambda item: item[1], reverse=True)
    
    def elect(self, seats):
        self.elected = []
        while len(self.elected) < seats:
            remain = seats - len(self.elected)
            maxes = self.maxes()
            if len(maxes) <= remain:
                self.elected.extend(maxes)
                for candidate in maxes:
                    self.totals.pop(candidate, None)
            else:
                print("Tie for last {} seats: {}".format(remain, maxes))
                sys.exit(-1)
            

def main():
    path = sys.argv[1]
    seats = int(sys.argv[2])
    with open(path, 'r') as f:
        j = json.load(f)
    cv = CumulativeVote(j)
    print(cv.dump())
    cv.elect(seats)
    print(cv.elected)

if __name__ == '__main__':
    main()

