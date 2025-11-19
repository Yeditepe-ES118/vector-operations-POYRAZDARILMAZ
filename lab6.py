


import numpy as np


def arrays():
    array1 = np.array([-2.33,100,20,33.2])
    array2 = np.array([[30,12,2,70.2],[98.01,4,0,7]])
    array3 = np.arange(2,11,2)   
    array4 = np.arange(20, -21, -10)
    array5 = np.linspace(0,1,4)
    array6 = np.ones((3,4))
    array7 = np.zeros((2,3))
    array8 = np.eye(3)
    array9 = np.diag(np.ones(2),-1)
    array10 = np.array([np.zeros((4,)),np.ones((4,)),2*np.ones((4,))])
    return array1, array2, array3, array4, array5, array6, array7, array8, array9, array10


def total_displacement(V1x,V1y,V2x,V2y,V3x,V3y):
    V1 = np.array([V1x,V1y])
    V2 = np.array([V2x,V2y])
    V3 = np.array([V3x,V3y])
    VR = V1 + V2 + V3
    U = np.array([1/np.sqrt(2),-1/np.sqrt(2)])
    VRU = np.dot(VR,U)*U
    len_VRU = np.sqrt(VRU[0]**2 + VRU[1]**2)
                     
    
    return VR, len_VRU
    
   





