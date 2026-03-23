import math

class Poly():
    def __init__(self,points):
        self.points = points

        self.centerX = 0
        self.centerY = 0
        for p in points:
            self.centerX += p[0]
            self.centerY += p[1]

        self.centerX /= len(points)
        self.centerY /= len(points)

        self.radius = 0

        for p in points:
            dist = math.sqrt((self.centerX-p[0])**2 + (self.centerY)**2)
            self.radius = max(self.radius, dist)

        self.lines = []
        
        for i in range(len(points)):
            vecX = (points[i][0]-points[(i+1)%(len(points)-1)][0])
            vecY = (points[i][1]-points[(i+1)%(len(points)-1)][1])
            if vecX == 0:
                a = 0
            else:
                a = vecY/vecX

            self.lines.append(
                {
                    "xS":points[i][0],
                    "xE":points[(i+1)%(len(points)-1)][0],
                    "a":
                        a,
                    "b":
                        points[i][1]-(points[i][0]*a)
                }
                
            )

        self.pOutsideX = 0
        self.pOutsideY = 0

        for p in points:
            self.pOutsideX += p[0]
            self.pOutsideY += p[1]


    def collidesPoint(self,p):
        lineXS = p[0]
        lineXE = self.pOutsideX
        lineA = (self.pOutsideY-p[1])/(self.pOutsideX-p[0])
        lineB = p[1]-(p[0]*lineA)

        collisions = 0

        for line in self.lines:
            if line["a"] == lineA:
                continue
            else:
                x = (lineB-line["b"])/(lineA-line["a"])
                if (
                    (line["xS"] > line["xE"] and line["xS"] > x > line["xE"]) or 
                    (line["xS"] < line["xE"] and line["xS"] < x < line["xE"])):
                    collisions += 1

        return collisions % 2

polyPoints = [
    [100,100],
    [100,-100],
    [-100,-100],
    [-100,100]
]

poly = Poly(polyPoints)

points = [
    [30,30],
    [20,-200],
    [300,0]
]

for point in points:
    print(poly.collidesPoint(point))