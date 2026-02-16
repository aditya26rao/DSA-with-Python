def isCollinear(x1, y1, x2, y2, x3, y3):
    area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if area == 0:
        return "Yes, these points are collinear"
    else:
        return "Not collinear"

result = isCollinear(1, 6, 1, 9, 0, 0)
print(result)
