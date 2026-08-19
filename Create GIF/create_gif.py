import imageio.v3 as iio  

filenames = ['frame01.png', 'frame02.png', 'frame03.png', 'frame04']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('nature.gif', images, duration = 500, loop = 0)
