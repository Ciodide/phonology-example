from OTable import otable 
from load_data import load_data
from RDC import constraint_demotion


# otables = load_data('InputFileForLargerGrammar.txt')
otables = load_data('InputFileForLargerGrammar.txt')
#print(otables)
# for i in otables:
#     print(type(i.constraints))
#     print(i.input_form)
#     print(i.candidates)
#     print(i.winner)
# #    print(i.violations)
#     print(i.get_win_candidate())
#     print(i.get_winner_violation())
#     print(i.get_rival_violation(i.candidates[0], i.constraints[0]))
# pairs = win_lose_pairs(otables)
# mark_cancellation(pairs[3])
ranked = constraint_demotion(otable_lst=otables)
print("=====")
print(type(ranked))
for i in ranked:
    for j in list(i):
        print(j)
    print("----")
