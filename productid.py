#!/usr/bin/python
import mapscript

req = mapscript.OWSRequest()
req.loadParams()

filename=req.getValueByName('PRODUCTID')
layername=req.getValueByName('LAYERS')

map = mapscript.mapObj( '/eqc-dyn.map' )

layer=map.getLayerByName(layername)
layersuffix=str(filename)
layer.data = str(layer.data) + layersuffix + '.tif'

map.OWSDispatch( req )
