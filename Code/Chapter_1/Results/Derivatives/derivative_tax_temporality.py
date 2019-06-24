# coding: utf-8
from sympy import *

init_session()


w_1, w_2,w_3, e_1, e_2, e_3  = symbols('w_1 w_2 w_3 e_1 e_2 e_3')

G = Function('G')
h = Function('h')
d = Function('d')



#ST 

QST = (
    w_1*e_1 - G(2e_1 * w_1) - d(e_1) +
    w_2*e_2 - G(2e_2 * w_2) - d(e_2)
)





#SCT
#General case two periods
a =(
    h( w_1*e_1 - (G(2*w_1*e_1)*G(w_1*e_1+w_2*e_2)/(G(2*w_1*e_1)+G(2*w_2 *e_2))))-d(e_1) 
    + h(w_2*e_2 - (G(2*w_2*e_2)*G(w_1*e_1+w_2*e_2)/(G(2*w_1*e_1)+G(2*w_2 *e_2))))-d(e_2)
)

a_3 =(
      h(w_1*e_1 - (G(3*w_1*e_1)*G(w_1*e_1+w_2*e_2+w_3*e_3)/(G(3*w_1*e_1)+G(3*w_2 *e_2)+G(3*w_3*e_3))))-d(e_1) 
    + h(w_2*e_2 - (G(3*w_2*e_2)*G(w_1*e_1+w_2*e_2+w_3*e_3)/(G(3*w_1*e_1)+G(3*w_2 *e_2)+G(3*w_3*e_3))))-d(e_2)
    + h(w_3*e_3 - (G(3*w_3*e_3)*G(w_1*e_1+w_2*e_2+w_3*e_3)/(G(3*w_1*e_1)+G(3*w_2 *e_2)+G(3*w_3*e_3))))-d(e_3)
)
#quasi-linear two-periods
b = (
    w_1*e_1 - (G(2*w_1*e_1)*G(w_1*e_1+w_2*e_2)/(G(2*w_1*e_1)+G(2*w_2 *e_2)))-d(e_1) 
    + w_2*e_2 - (G(2*w_2*e_2)*G(w_1*e_1+w_2*e_2)/(G(2*w_1*e_1)+G(2*w_2 *e_2)))-d(e_2)
)
#quasi-linear three-periods
c =(
    w_1*e_1 - (G(2*w_1*e_1)*G(w_1*e_1+w_2*e_2+w_3*e_3)/(G(2*w_1*e_1)+G(2*w_2 *e_2)+G(2*w_3 *e_3)))-d(e_1)
    +w_2*e_2 - (G(2*w_2*e_2)*G(w_1*e_1+w_2*e_2+w_3*e_3)/(G(2*w_1*e_1)+G(2*w_2 *e_2)+G(2*w_3 *e_3)))-d(e_2)
    + w_3*e_3 - (G(2*w_3*e_3)*G(w_1*e_1+w_2*e_2+w_3*e_3)/(G(2*w_1*e_1)+G(2*w_2 *e_2)+G(2*w_3 *e_3)))-d(e_3)
) 

display(a.diff(e_1))
display(simplify(a.diff(e_1)))

display(b.diff(e_1))
display(simplify(b.diff(e_1)))

c.diff(e_1)
simplify(c.diff(e_1))




simplify(b.diff(w_1))
simplify(a.diff(w_1))
simplify(a.diff(w_1))
simplify(a.diff(e_1))

simplify(a_3.diff(e_1))


#### With cobb Douglass

v = symbols('v')
e_max = symbols('e_max')
alpha = symbols('\alpha')

o = (
    alpha * log(w_1 * e_1 - G(2*w_1*e_1)) + (1-alpha) log(e_max - e_1) +
    alpha * log(w_2 * e_2 - G(2*w_2*e_2)) + (1-alpha) log(e_max - e_2)
)
    


