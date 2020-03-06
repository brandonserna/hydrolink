#!/usr/bin/env python

"""Tests for `utils` package."""

import pytest
from shapely.geometry import Point
from hydrolink import utils

def test_crs_to_nad83():
    '''
    Description
    -----------
    test if conversions are occuring correctly
    4326 to 4269
    3857 to 4269
    5070 to 4269
    '''
    pass


def test_clean_water_name():
    '''
    Description
    -----------
    Test function utils.clean_water_name.  Ensure abbreviations are being correctly addressed.
    '''
    assert utils.clean_water_name('Grand st.') == 'grand stream'
    assert utils.clean_water_name('Grand St') == 'grand stream'
    assert utils.clean_water_name('grand str ') == 'grand stream'
    assert utils.clean_water_name('grand str.') == 'grand stream'
    assert utils.clean_water_name('trib. Grand Rv.') == 'tributary grand river'
    assert utils.clean_water_name('trib Grand Rv ') == 'tributary grand river'
    assert utils.clean_water_name('Grand Rv. unt') == 'grand river unnamed tributary'
    assert utils.clean_water_name('Grand River trib)') == 'grand river tributary'
    assert utils.clean_water_name('trib. Grand River') == 'tributary grand river'
    assert utils.clean_water_name('Grand River') == 'grand river'
    assert utils.clean_water_name('br. Grand River') == 'branch grand river'
    assert utils.clean_water_name('Grand River br ') == 'grand river branch'
    assert utils.clean_water_name('Grand Ck.') == 'grand creek'
    assert utils.clean_water_name('Grand ck') == 'grand creek'
    assert utils.clean_water_name('unt Grand Rv.') == 'unnamed tributary grand river'


def test_build_meas_line():
    '''
    Description
    -----------
    Verify build_meas_line function.  
    Ensure distance between two points is being measured correctly.
    Line lengths were measured in arcmap.  Accounts for 1% rounding error.
    ''' 
    #Input CRS which all data are transformed too
    crs = {'init':'epsg:4269'}
    
    #using shapely create 2 points to allow for measuring of connecting line
    point1 = Point(-72.522365, 41.485054)  
    point2 = Point(-72.529494, 41.464437)

    #test if the build_meas_line measurement is within 1% rounding error of arcmap measurement

    arcmap_length_m = 2381.955938
    arcmap_length_m_lt1 = arcmap_length_m - (arcmap_length_m*0.01)
    arcmap_length_m_gt1 = arcmap_length_m + (arcmap_length_m*0.01)
    len = utils.build_meas_line(point1, point2, crs=crs)
    assert  arcmap_length_m_lt1 <= len <= arcmap_length_m_gt1 

