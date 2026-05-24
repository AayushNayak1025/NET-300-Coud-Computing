distance = float(input("Enter distance traveled (km): "))
hour = int(input("Enter travel hour (0-23): "))

# Base fare
if distance <= 2:
    fare = 150

# Between 2 and 10 km
elif distance <= 10:
    fare = 150 + (distance - 2) * 35

# Beyond 10 km
else:
    fare = 150 + (8 * 35) + ((distance - 10) * 28)

# Night surcharge
if hour >= 22 or hour < 5:
    fare = fare * 1.10

print(f"\nTotal Taxi Fare: NPR {fare:.2f}")