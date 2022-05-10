from OTable import otable

def win_lose_pairs(otable_lst):
    """
    Decompress all win/lose pairs in the input.
    Input: A list of otable;
    Output: A list of all win/lose pairs in the input
    """
    pair_lst = []
    for i in otable_lst:
        for j in i.candidates:
            if i.winner != j:
                pair_lst.append({"winner": i.winner, "loser":j})
    return pair_lst

def get_mark_data_pairs(pair_lst):
    """
    Processing all w/l pairs, for each pair, in every constraint violation, use mark data as pair, also doing the mark cancelation.
    Input: A list of win/lose pairs
    Output: A list of mark data pairs, each pair is a dict with two set item.
    """
    mark_data_pair_lst =[]
    for pair in pair_lst:
        mark_data_pair = {"winner": set(), "loser": set()}
        for i in otable.constraints:
            if pair["winner"].violations[i.index] > pair["loser"].violations[i.index]:
                mark_data_pair["winner"].add(i)
            if pair["winner"].violations[i.index] < pair["loser"].violations[i.index]:
                mark_data_pair["loser"].add(i)
        mark_data_pair_lst.append(mark_data_pair)
    return mark_data_pair_lst

def constraint_demotion(otable_lst):
    """
    Temporary function, preprocessing some data, TODO: make it better later.
    """
    wl_pair_lst = win_lose_pairs(otable_lst)
    mark_data_pair_lst = get_mark_data_pairs(wl_pair_lst)
    max_iter = len(otable.constraints) ** 2 * len(mark_data_pair_lst)
    ranked_constraint = RDC(init_current_stratum=set(otable.constraints), mark_data_pair_lst=mark_data_pair_lst, iter_count=0, max_iter=max_iter)
    return ranked_constraint

def RDC(init_current_stratum, mark_data_pair_lst, iter_count, max_iter):
    """
    Recursive Constraint Demotion main function, detail in the paper.
    Input:
      - init_current_stratum: A set of constraint(s). If the first time input all constraints, else input the last recursive calculated next_stratum.
      - mark_data_pair_lst: A list of all mark data pair.
      - iter_count: Iter counter, recode record how many time are calculated. Work with max_iter arg.
      - max_iter: N_cons^2 * N_mark. Theoretically the max iter can be reach, if iter_count higher than this, something bad happend.
    """

    current_stratum = init_current_stratum.copy()
    next_stratum = set()
    for i in mark_data_pair_lst:
        for j in i["winner"] & init_current_stratum:
            iter_count += 1
            if len(i["loser"] & init_current_stratum) > 0:
                if j in current_stratum:
                    current_stratum.remove(j)
                next_stratum.add(j)
                print("Found one:", j, "will move to next stratum.")

    if next_stratum == set():
        # RDC successful, return all we have
        return [current_stratum]
    if current_stratum == set():
        # Nothing in current stratum, so init current stratum and next stratum is the same, it well be an endless loop, raise an exception.
        raise Exception("ERROR: Loop found, Please check your input data.")
    if iter_count > max_iter:
        # The max iter will be N_cons^2 * N_mark, if iter counter reach here, that means something unexcept happend, raise an exception.
        raise Exception("ERROR: Max iter reach, Some thing unexcept happened.")
        
    next_RDC = RDC(init_current_stratum=next_stratum, mark_data_pair_lst=mark_data_pair_lst, iter_count=iter_count, max_iter=max_iter)
    return [current_stratum] + next_RDC
