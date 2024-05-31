from numba import jit
@jit(nopython=True)
def bisectm(xvec,r):
    nv=xvec.shape[0]
    n1=0
    n2=nv-1
    if r<xvec[0]:
        return 0
    if r>=xvec[n2]:
        return n2
    nmid=int((n1+n2)/2)
    #print(nmid)
    it=0
    while not (r>=xvec[nmid-1] and r<xvec[nmid]) and it<15:
        it+=1
        if r>xvec[nmid-1]:
            n1=nmid
        else:
            n2=nmid
        nmid=int((n1+n2)/2)
    return nmid
