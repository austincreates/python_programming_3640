ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=[], votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        self.votes = votes
        

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return "The name of the candidate is {} and the candidate's winning states are {}".format(self.name, self.winning_states)
        

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        for i in self.winning_states:
            self.votes += ELECTORS[i]
    
    def __gt__(self, another_candidate):
        if self.votes > another_candidate.votes:
            return True
        elif self.votes == another_candidate.votes:
            return False
        return False
            
        """if self.winning_states> another_candidate.winning_states:
            return True
        elif self.winning_states == winning_states:
             if self.votes < another_candidate.votes:
                 return True
        return False"""


def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'])
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    
    print(trump)
    print(clinton)
    print (trump.votes)
    print (clinton.votes)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()