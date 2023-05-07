import numpy as np


def norm2em(norm, normerr):
    area = 3.5*4.5 #arcmin2
    kpc2cm = 3.08568e21
    dens = [5.81e-3, 3.13e-3, 8.14e-3]
    dens_err = [4.69e-4, 4.66e-4, 5.08e-4]
    d_ang = 3.427 #kpc/arcsec at z=0.21
    const = 1e-14/4/np.pi/(d_ang*20*60*kpc2cm*(1+0.21))**2/400/np.pi*area
    return norm/const, normerr/const
