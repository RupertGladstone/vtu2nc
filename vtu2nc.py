
# convert fields on an unstructured mesh in .vtu files to a structured grid netcdf file

import netCDF4
import sys
import os
import glob
import numpy as np
import vtk 
from vtk.util.numpy_support import vtk_to_numpy

## Read temperature and beta from vtu files
fileName = "/mnt/hgfs/VMshare/XiaoranPIG/weer.0010.pvtu"
reader = vtk.vtkXMLPUnstructuredGridReader()
reader.SetFileName(fileName)
reader.Update()
output=reader.GetOutput()
PointData=output.GetPointData()
cellData=output.GetCellData()

numArrays=PointData.GetNumberOfArrays()   
for i in np.arange(numArrays):
    if PointData.GetArrayName(i)=='temperature homologous':
        tempIndex=i
    if PointData.GetArrayName(i)=='beta':
        betaIndex=i

temp=vtk_to_numpy(PointData.GetArray(tempIndex))
beta=vtk_to_numpy(PointData.GetArray(betaIndex))
Coords=vtk_to_numpy(output.GetPoints().GetData())

## Interpolate temperature and beta to 3D structured grid
## https://docs.scipy.org/doc/scipy/reference/interpolate.html
## https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RegularGridInterpolator.html#scipy.interpolate.RegularGridInterpolator

## Write temperature and beta to netcdf files

