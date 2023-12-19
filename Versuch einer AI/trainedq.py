import pickle


def get_q(Q2):
    Q1 = "Q/100000000_"
    Q2 = Q2 + ".pickle"

    with open(Q1 + "walk" + Q2, "rb") as file:
        Q_walk = pickle.load(file)

    with open(Q1 + "jump" + Q2, "rb") as file:
        Q_jump = pickle.load(file)

    with open(Q1 + "attack" + Q2, "rb") as file:
        Q_attack = pickle.load(file)

    return (Q_walk, Q_jump, Q_attack)
