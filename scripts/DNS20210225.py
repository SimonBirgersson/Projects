# DNS analysis of TpMan5A/BpMan5A stabilty in methanol/1-propanol, including attempt at HCl chemical inactivation
import numpy as np  # numpy package allow matlab-like matrix operations
import matplotlib.pyplot as plt
from datetime import date

data = np.array([[0.091, 0.187, 0.442, 1.030, 1.264, 0.092, 0.227, 0.174],
                 [0.100, 0.196, 0.482, 1.035, 1.280, 0.090, 0.212, 0.243],
                 [0.095, 0.201, 0.485, 0.877, 1.317, 0.098, 0.199, 0.252],
                 [0.208, 0.253, 0.174, 0.083, 0.085, 0.086, 0.164, 0.126],
                 [0.246, 0.262, 0.162, 0.086, 0.086, 0.083, 0.068, 0.154],
                 [0.278, 0.284, 0.188, 0.085, 0.087, 0.083, 0.068, 0.141],
                 [0.084, 0.084, 0.048, 0.049, 0.048, 0.047, 0.046, 0.046],
                 [0.079, 0.084, 0.047, 0.048, 0.049, 0.047, 0.047, 0.046]]) # output from absorbance measurement

std_blank = data[3:6,5,np.newaxis] # needed to add a new dimension to the vector, therefore "newaxis"
std_abs   = data[0:3,0:5]-std_blank # slice of full data matrix gets std absorbances minus blank
std_c     = [5, 10, 20, 40, 50]
print(std_abs)

sample_TpMan5A_stability_abs=data[3:6,0:1]
sample_BpMan5A_stability_abs=data[3:6,0:1]



sample_TpMan5A_HCl_deactivation_abs=data[0:3,5:8]
sample_BpMan5A_HCl_deactivation_abs=data[3:6,5:8]

 # %%

plt.plot(std_c,np.mean(std_abs , axis=0, dtype=np.float64),'*-')
plt.ylabel("abs(540nm)")
plt.xlabel("conc M1 [mM]")
plt.grid(True)
plt.show()
#mpl.savefig("/Users/SimonsFolder/PYTHON/figure_%s.png" % str(date.today()))
