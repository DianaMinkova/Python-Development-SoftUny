length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

volume_aquarium = length * width * height
volume_liters = volume_aquarium / 1000

needed_liters = volume_liters * (1 - percentage)  # (1 - percentage) => calculates the free space
print(needed_liters)
