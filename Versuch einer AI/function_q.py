from collections import defaultdict

rewardAlive = 1
rewardDamage = rewardHealth = 100
rewardKill = -10000

# trial 1
alpha = 0.2
gamma = 0.9

# nichts, springen, [nicht rennen, rechts rennen, links rennen], [nicht attack, attack1, attack2]
Q = defaultdict(lambda: [0, [0, [0, 0, 0], [0, 0, 0]]])

# nichts, rechts, links
Q_walk = defaultdict(lambda: [0, 0, 0])
# nein, ja
Q_jump = defaultdict(lambda: [0, 0])
# nein, 1, 2
Q_attack = defaultdict(lambda: [0, 0, 0])

def calculateDeltaHealth(params1, params2):
    return round(params1["health"] - params2["health"], -1)
def paramsToState(params1, params2): # params nr nicht unbedingt fighter nr
    delta_x = round(params1["position_x"] - params2["position_x"], -1)
    delta_y = round(params1["position_y"] - params2["position_y"], -10)


    hit = params1["hit"] # True/False
    if hit:
        hit = 1
    else:
        hit = 0

    flip = params1["flip"] # True/False
    if flip:
        flip = 1
    else:
        flip = 0


    state = {"delta_x": delta_x, "delta_y": delta_y, "hit": hit, "flip": flip, "being_attacked": params2["attacking"]}
    return state
    # früher str als return
