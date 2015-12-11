
# -------------------------------------------------------------------------
# Copyright C 2015 Gefu Tang
# tanggefu@gmail.com
#
# License Agreement: To acknowledge the use of the code please cite the
#                    following papers:
#
# [1] A. Tahmasbi, F. Saki, S. B. Shokouhi,
#     Classification of Benign and Malignant Masses Based on Zernike Moments,
#     Comput. Biol. Med., vol. 41, no. 8, pp. 726-735, 2011.
#
# [2] F. Saki, A. Tahmasbi, H. Soltanian-Zadeh, S. B. Shokouhi,
#     Fast opposite weight learning rules with application in breast cancer
#     diagnosis, Comput. Biol. Med., vol. 43, no. 1, pp. 32-41, 2013.

# -------------------------------------------------------------------------
# A demo of how to use the Zernike moment function.
#
# Example:
#   1- calculate the Zernike moment (n,m) for an oval shape,
#   2- rotate the oval shape around its centeroid,
#   3- calculate the Zernike moment (n,m) again,
#   4- the amplitude of the moment (A) should be the same for both images
#   5- the phase (Phi) should be equal to the angle of rotation
import cv2
import matplotlib.pylab as plt
from pyzernikemoment import Zernikemoment
if __name__ == '__main__':
    n = 4
    m = 2
    print '------------------------------------------------'
    print 'Calculating Zernike moments ..., n = %d, m = %d' % (n, m)
    fig, axes = plt.subplots(2, 3)

    imgs = ['Oval_H.png', 'Oval_45.png', 'Oval_V.png']
    for i in xrange(3):
        src = cv2.imread(imgs[i], cv2.IMREAD_COLOR)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        Z, A, Phi = Zernikemoment(src, n, m)
        axes[0, i].imshow(plt.imread(imgs[i]))
        axes[0, i].axis('off')
        title = 'A = ' + str(round(A, 4)) + '\nPhi = ' + str(round(Phi, 4))
        axes[0, i].set_title(title)

    imgs = ['Shape_0.png', 'Shape_90.png', 'Rectangular_H.png']
    for i in xrange(3):
        src = cv2.imread(imgs[i], cv2.IMREAD_COLOR)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        Z, A, Phi = Zernikemoment(src, n, m)
        axes[1, i].imshow(plt.imread(imgs[i]))
        axes[1, i].axis('off')
        title = 'A = ' + str(round(A, 4)) + '\nPhi = ' + str(round(Phi, 4))
        axes[1, i].set_title(title)
    print 'Calculation is complete'

    plt.show()
