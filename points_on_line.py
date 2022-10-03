# NOT SOLVED 
# https://leetcode.com/problems/max-points-on-a-line/

from collections import Counter
def max_points(points):
    # find the line equation of the first two numbers
    # see if any of the other numbers have the same equation
    # find the line equation of the next two numbers
    # see if any other numbers have that equation.
    # this is going to be terribly inefficient
    line_eqs = dict()
    checked = set()
    tick = 0
    # print(points.index([3,2]))
    for i in range(0, len(points)):
        for i1 in range(1, len(points)):
            if i == i1 or (i,i1) in checked or (i1,i) in checked:
                continue
            else:
                checked.add((i,i1))
            x,y = points[i]
            x1,y1 = points[i1]
            
            slope = 0
            if (y-y1)*(x-x1) != 0: # so it doesn't divide by 0:
                slope = (y-y1)/(x-x1)

            y_intercept = y-(slope*x)

            line_eqs[tick] = {
                'pt1':i,
                'pt2':i1,
                'vals':(slope,y_intercept)
                }
            tick+=1
            # print(line_eqs.values())

            # print(i,",",i1,'||',slope, y_intercept)
    # print([val['vals'] for val in line_eqs.values()])
    
    # if the slope and y-intercept have already been found for a certain point, remove that point from the count
    # can't figure out how to do this.
    # The following does not work:
    most_common, num = Counter([val['vals'] for val in line_eqs.values()]).most_common(1)[0]
    print(line_eqs.values())
    print('VAL:',most_common, 'COUNT:', most_common)
    count = 0
    seen = set()
    for val in line_eqs.values():
        if val['vals'] == most_common:
            if val['pt1'] in seen or val['pt2'] in seen:
                pass
            else:
                print('adding:', val['pt1'], val['pt2'])
                seen.add(val['pt1'])
                seen.add(val['pt2'])
                count+=1
    print('seen:', seen)
    print('RETURNING:', len(seen))
    return 
        
        
        
    

# points = [[1,1],[2,2],[3,3]]
# max_points(points)
points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
max_points(points2)