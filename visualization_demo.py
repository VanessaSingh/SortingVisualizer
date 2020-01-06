from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
cam = Camera(fig)
for i in range(5):
    plt.plot([i]*10)
    cam.snap()
animation = cam.animate()
animation.save('my_first_animation.gif', writer='imagemagick')

