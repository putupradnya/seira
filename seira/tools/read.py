import numpy as np
from seira.tools.segypy import getSegyHeader, readSegy

def segySeismicReader(path_seismic_data):
  """Load seismic data with *.segy format

  Args:
      path_seismic_data (string): path of seismic filedata

  Returns:
      data: amplitude data
      SH : default
      STH : default
  """
  segypy.verbose = 0
  SH = segypy.getSegyHeader(path_seismic_data)
  [Data, SH, STH] = segypy.readSegy(path_seismic_data)

  return [Data, SH, STH]

def asciiSeismicReader(path_seismic_data):
  """Load seismic data with *.dat format

  Args:
      path_seismic_data (string): path of seismic filedata

  Returns:
      data: amplitude data
      SH : default
      STH : default
  """
  data = np.loadtxt(path_seismic_data, skiprows=1)
  dt = 0.001
  time = 0
  temp_sh = []
  n= data.shape[0]
  for i in range(n):
    temp_sh.append(time)
    time += dt
  SH = {'time': temp_sh}
  STH = None

  return data, SH, STH

  