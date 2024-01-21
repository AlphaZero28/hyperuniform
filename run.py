import numpy as np 
from main import Main
import matplotlib.pyplot as plt


# Constants
width, height = 32e-6, 32e-6
r = 520e-9
k = 30
hyperuniform = Main(r, k, width, height)


# structure generation
for _ in range(8000):
    grid = hyperuniform.draw()

# retriving coordinates of the nanobars
coords = []
for point in grid:
    if point and point[0]>0 and point[1]>0:
        coords.append((point[0], point[1]))

print(f"total number of elements: {len(coords)}")


# centering the structure
original_range_min = 0
original_range_max = width
target_range_min = -width/2
target_range_max = width/2
converted_coords = hyperuniform.centering_structure(coords, original_range_min, original_range_max, target_range_min, target_range_max)


# Making Circular structure
lens = 15e-6
allowed = []
for idx, val in enumerate(converted_coords):
  x = val[0]
  y = val[1]
  dis = hyperuniform.find_distance((0,0), (x,y))
  if dis < lens:
    allowed.append((x,y))

print(f"lens radius: {lens * 1e6} microns")
print(f"total number of elements: {len(allowed)}")

# plotting the circular structure
dot_radius = 180e-9
dot_color = 'b'

figure, axes = plt.subplots()

for val in allowed:
  # if grid[idx] != -1:
  x = val[0]
  y = val[1]

  dots = plt.Circle(( x , y ), dot_radius, facecolor=dot_color )
  axes.add_artist( dots )
  axes.set_aspect( 1 )

plt.xlim([-lens - 500e-9, lens + 500e-9])
plt.ylim([-lens - 500e-9, lens + 500e-9])
plt.title("Hyperuniform Metasurface")
plt.xlabel(r'X ($\mu$m)')
plt.ylabel(r'Y ($\mu$m)')
# plt.axis('off')
xticks = np.arange(-15e-6, 16e-6, 7.5e-6)
xticks_label = [-15, -7.5, 0, 7.5, 15]
plt.xticks(xticks, xticks_label, weight='bold' )

yticks = np.arange(-15e-6, 16e-6, 7.5e-6)
yticks_label = [-15, -7.5, 0, 7.5, 15]
plt.yticks(yticks, yticks_label, weight='bold' )


file_path = 'hyperuniform-metasurface.PNG'
plt.savefig(file_path, format='PNG', dpi = 300)

plt.show()


