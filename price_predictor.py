fd = open('theta_values', 'r')

slope = float(fd.readline().split('=')[1])
intersect = float(fd.readline().split('=')[1])

while True:
    mileage = input("Enter a mileage: ")
    try:
        mileage = int(mileage)
        break
    except:
        print("Not a valid num")

if mileage < 0:
    print("Negative mileage")
    exit(0)

prediction = int(intersect + (slope * mileage))

if prediction < 0:
    prediction = 0

print("price for a car: ", prediction)
