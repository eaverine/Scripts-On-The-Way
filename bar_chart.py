import matplotlib.pyplot as plt
import numpy as np

#fig,axis = plt.subplots()
numbers = (1,2,3,4,5,6,7,8,8,2,1)
places = ('ABV','LOS','DXB','LHR','LON','TKY','JAP','ABC','UAE','SAU','OPO')


plt.title('Visits in the month of January')

plt.bar(places, numbers, align = 'center')
#axis.set_xticks(places)
#axis.set_yticks(numbers)

plt.xlabel('Places')
plt.ylabel('Number Of Visits')



plt.show()
