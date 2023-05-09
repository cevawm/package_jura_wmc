#rv_curve_jura package

##EXAMPLE FROM JURA IV: A NEW HOPE

This package allows you to create a radial velcoity plot of a star orbited by a planet.

#### Usage instructions

```
#import libraries
import numpy as np
import matplotlib.pyplot as plt
#import our rv_curve_class
#We are telling pytlhon from the rv_curve_module inste the rv_curve_jura_package 
#import the class rv_curve class
from rv_curve_jura.rv_curve_module import rv_curve_class

#create the instance of the class 
rv = rv_curve_class(t0=0., p=4, e=0.2, w=np.pi/3, k=10., t_init=0., t_end=25.)
#use the rv plot method to get our plot
rv.plot()
```