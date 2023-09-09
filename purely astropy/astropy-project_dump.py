# goal - to plot the position graph of the stars in M15

import pylab as pl
import numpy as np
from astropy.visualization import quantity_support
from astropy import units as u #always import astropy units! - learn scipy next
from astropy import wcs
from astroquery.gaia import Gaia

# import data file - M15 pos ecliptic lat&longtitude file from the gaia archives as an astroquery

