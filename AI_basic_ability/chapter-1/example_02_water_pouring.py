def water_pouring(b1, b2, goal, start=(0, 0)):
    if goal in start: 
        return [start]

    explored = set(start)
    froniter = [[('init', start)]]

    while froniter:
        path = froniter.pop(0)
        (x, y) = path[-1][-1]
        
        for (state, action) in successors(x, y, b1, b2).items():
            if state not in explored:
                explored.add(state)

                path2 = path + [(action, state)]
                print(path)
                print(path2)
                print()

                if goal in state:
                    return path2
                else:
                    froniter.append(path2)

    return []


def successors(x, y, X, Y):
    return {
        ((0, y+x) if x + y <= Y else (x + y - Y, Y)): 'X -> Y',
        ((x + y, 0) if x + y <= X else  (X, x + y - X)): 'X <- Y',
        (X, y): '灌满X',
        (x, Y): '灌满Y',
        (0, y): '倒空X',
        (x, 0): '倒空Y',
    }


if __name__ == '__main__':

    #print(water_pouring(4, 9, 5))
    #print(water_pouring(4, 9, 5, start=(4, 0)))
    #print(water_pouring(4, 9, 6))
    print(successors(0,9,4,9))
    print()
    #water_pouring(4, 9, 1)
    
    
