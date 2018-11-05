#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

observation_location = EarthLocation(lat='52.2532', lon='351.639', height=100*u.m)
observation_time = Time('2018-10-30 00:30:59')
aa = AltAz(location=observation_location, obstime=observation_time)
sc = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
sc.transform_to(aa)

