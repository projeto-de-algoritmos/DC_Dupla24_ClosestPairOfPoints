from random import randint 

#Para gerar os pontos de maneira randomica basta executar essa função
#caso queira testar com seus proprios pontos basta comentar essa primeira função e descomentar a segunda função.

def rand_points(n):
    x = 0
    y = 0
    points = []
    for i in range(n):
        x = randint(0,49) 
        y = randint(0,49) 
        points.append((x, y))
    return points

# def rand_points(n):
#     points = [(20, 43), (21, 21), (28, 39), (2, 10), (11, 47),
#           (35, 46), (36, 3), (44, 41), (13, 5), (40, 19), (45,45)]
#     return points

