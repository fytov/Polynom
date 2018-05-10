class Polynomial(object):
    def __init__(self, other):        
        if len(other) == 0:
            raise TypeError("ERROR!!!")
        elif not isinstance(other, list):
            raise TypeError("ERROR!!!")
        else:
            for i in range(len(other)):
                if not (isinstance(other[i], (int, float))):
                    raise TypeError("ERROR!!!")
            self.coeffs = other[:]
            _co = self.coeffs
            if _co:
                offs = 0
                if _co[offs]==0 and len(_co)>1:
                    offs += 1
                    while offs < len(_co)-1 and _co[offs]==0:
                        offs += 1
                    del _co[:offs]

    def __add__(self, val):
        if isinstance(val, Polynomial):
            if len(self.coeffs) > len(val.coeffs):
                res = self.coeffs[:]
                for i in range(len(val.coeffs)):
                    res[len(self.coeffs) - i - 1] += val.coeffs[len(val.coeffs) - i - 1] 
            else:
                res = val.coeffs[:]
                for i in range(len(self.coeffs)-1,-1,-1):
                    res[len(val.coeffs) - i - 1] += self.coeffs[len(self.coeffs) - i - 1]      
        else:
            if not (isinstance(val, (int, float))):
                raise TypeError("ERROR!!!")
            else:
                if self.coeffs:
                    res = self.coeffs[:]
                    res[-1] += val
                else:
                    res = val
        return Polynomial(res)
    
    def __radd__(self, other):
        return self + other
    
    def __eq__(self, val):
        if isinstance(val, Polynomial):
            return self.coeffs == val.coeffs
        elif not (isinstance(val, (int, float))):
            raise TypeError("ERROR!")
        else:
            return len(self.coeffs)==1 and self.coeffs[0]==val

    def __mul__(self, val):
        if isinstance(val, Polynomial):
            selfcoeffs = self.coeffs
            valcoeffs = val.coeffs
            res = [0]*(len(selfcoeffs)+len(valcoeffs)-1)
            for selfpow,selfcoef in enumerate(selfcoeffs):
                for valpow,valcoef in enumerate(valcoeffs):
                    res[selfpow+valpow] += selfcoef*valcoef
        elif not (isinstance(val, (int, float))):
            raise TypeError("ERROR!!!")
        else:
            res = [coef*val for coef in self.coeffs]
        return Polynomial(res)

    def __rmul__(self, other):
        return self * other
    
    def __str__(self):
        res = []
        c = self.coeffs[::-1]
        for po,co in enumerate(c):
            if co:
                if po==0:
                    po = ''
                elif po == 1:
                    po = 'x'
                else:
                    po = 'x'+str(po)
                if po != '' and abs(co)==1:
                    res.append(('-' if co<0 else '+')+po)
                else:
                    res.append(('-'+str(abs(co)) if co<0 else '+'+str(co))+po)
        if res:
            res.reverse()
            res = ''.join(res)
            if res[0]=='+':
                return ''.join(res[1::])
            return res
        else:
            return "0"

    def __sub__(self, val):
        return self.__add__(-val)
    def __neg__(self):
        return Polynomial([-co for co in self.coeffs])