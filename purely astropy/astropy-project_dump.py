# Goal 1 - To graph a P-L (Position-Latitude) diagram of M15 stars using data from VizieR!

import pylab as pl
import numpy as np
from astropy.visualization import quantity_support
from astropy import units as u #always import astropy units! - learn scipy next
from astropy import wcs
from astroquery.gaia import Gaia



