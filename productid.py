#!/usr/bin/python
import sys
import mapscript
from osgeo import gdal

req = mapscript.OWSRequest()
req.loadParams()

filename=req.getValueByName('PRODUCTID')
layername=req.getValueByName('LAYERS')

map = mapscript.mapObj( '/eqc-dyn.map' )

layer=map.getLayerByName(layername)
layersuffix=str(filename)
layer.data = str(layer.data) + layersuffix + '.tif'

map.OWSDispatch( req )
