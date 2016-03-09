# -*- coding: utf-8 -*-
# ***********************************
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************

import numpy as np
import numpy.linalg as la
from core import Element
import templates as tmp

class Spring(Element):
    """
    Bar element for finite element analysis
    
    *nodes* : :class:`~core.base.Node`
        Conectivity for element
    
    *E* : float
        Young modulus
        
    *A* : float
        Area of element
        
    *L* : float
        Length of element
    
    
    Example::
    
        n1 = Node((0,0),1)
        n2 = Node((1,0),1)
        e1 = Spring((n1,n2),200e9,0.02,1)
    
    """
    def __init__(self,nodes,ke,label=""):
        Element.__init__(self,etype="spring",label=label)
        self.nodes = nodes
        self.ke = ke
        
    def getElementStiffness(self):
        r"""
        Get stiffness matrix for this element
        
        The stiffness matrix for a spring element is defined by:
        
        .. math::
        
            [K]_e = \left[\begin{matrix}
            k  & -k \\
            -k &  k \\
            \end{matrix} \right]
        
        Return a numpy array.
        """
        self._KE = np.array([[self.ke,-self.ke],[-self.ke,self.ke]])
        return self._KE
        
    def getNodes(self):
        return self.nodes


class Bar(Element):
    """
    Bar element for finite element analysis
    
    *nodes* : :class:`~core.base.Node`
        Conectivity for element
    
    *E* : float
        Young modulus
        
    *A* : float
        Area of element
        
    *L* : float
        Length of element
    
    
    Example::
    
        n1 = Node((0,0),1)
        n2 = Node((1,0),1)
        e1 = Bar((n1,n2),200e9,0.02,1)
    
    """
    def __init__(self,nodes,E,A,L,label=""):
        Element.__init__(self,etype="bar",label=label)
        self.nodes = nodes
        self.E = E
        self.A = A
        self.L = L
        
    def getElementStiffness(self):
        """
        Get stiffness matrix for this element
        
        """
        self._K = (self.A*self.E/self.L)*np.array([[1,-1],[-1,1]])
        return self._K
        
    def getNodes(self):
        return self.nodes
        

if __name__=='__main__':
    pass