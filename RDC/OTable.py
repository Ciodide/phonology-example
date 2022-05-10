class constraint:
    def __init__(self, index, name, abbrev):
        self.index = index
        self.name = name
        self.abbrev = abbrev

    def __str__(self):
        return "index:" + str(self.index) + " name:" + str(self.name) + " abbrev:" + str(self.abbrev)

class candidate:
    def __init__(self, index, form, violations):
        self.index = index
        self.form = form
        self.violations = violations

    def __str__(self):
        return "index:" + str(self.index) + " form:" + str(self.form) + " violations:" + str(self.violations)
class otable:
    constraints = []

    def __init__(self, index, input_form):
        self.input_form = input_form
        self.candidates = []
        self.winner = None
        self.index = index

    def add_con(name, abbrev):
        otable.constraints.append(constraint(len(otable.constraints), name, abbrev))

    def add_can(self, form, violations, win=False):
        self.candidates.append(candidate(len(self.candidates), form, violations))
        if win:
            if self.winner == None:
                self.winner = self.candidates[-1]
            else:
                print("Error: More than one Winner")
                
    def get_winner_violation(self):
        return self.winner.violations

    def get_rival_violation(self, candidate, constraint):
        return candidate.violations[constraint.index]

    def get_win_candidate(self):
        return self.winner.form


