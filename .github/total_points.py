import os

def test_success(name):
    with open(name, 'r') as f:
        ls = f.read().strip().split('\n')
    return ls[-1].startswith('SUCCESS')

def score_subtask(st, point_map):
    point_map = {0: 1, 1: 3, 2: 1, 3: 3, 4: 2}
    points = 0
    total = 0
    for k in point_map.keys():
        if test_success(f'subtask1/test{k}.out'):
            points += point_map[k]
        total += point_map[k]
    return (points, total)

(p_1, max_1) = score_subtask('subtask1', {0: 1, 1: 3, 2: 1, 3: 3, 4: 2})
(p_2, max_2) = score_subtask('subtask2', {0: 1, 1: 1, 2: 2, 3: 2, 4: 2, 5: 2})
(p_3, max_3) = score_subtask('subtask3', {0: 5, 1: 5})


points = p_1 + p_2 + p_3
m = max_1 + max_2 + max_3

of = os.environ['GITHUB_OUTPUT']
with open(of, 'a') as f:
    print(f'points={points}', file=f)
    print(f'max_points={m}', file=f)
