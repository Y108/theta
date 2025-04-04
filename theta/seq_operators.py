#---------------------------------------------------------------------- (Functions)

def seq_assign(A, B): 
        
        X = len(A)
        Y = len(B)

        abs_diff = abs(Y - X)

        def main(A,B):

            S = {i:[] for i in list(set(A))[::-1]}
            for k in range(Y):
                for i in set(A):
                    if A[k] == i:
                        S[i].append(B[k])
            for key in S:
                print(f"p({key}): {S[key]}")

        def errors(n):  

            if n == 1: print('\033[91mWarning: Both inputs of \033[93madd_lst\033[91m have to be of type list!\033[0m')
            if n == 2: print('\033[91mWarning: Both inputs of \033[93madd_lst\033[91m have to contain at least \033[93m 1 \033[91m element!\033[0m')

        if sorted(list(set(A))) == sorted(A): #check if the output equals the 1-1 assignment of the two sequences
            

            if X == Y:
                print(f'I:{A}\nII:{B}')
            
            if X > Y:
                print(f'I:{A[:-abs_diff]}\nII:{B}')

            if X < Y:
                print(f'I:{A}\nII:{B[:-abs_diff]}')
        
        elif not(isinstance(A, list) and isinstance(B, list)):
            errors(2)
        
        elif not(X > 0 and Y > 0):
            errors(2)

        else:
                if X>=Y:
                    main(A,B)

                elif X<Y:
                    B2 = B[:-abs_diff]
                    main(A,B2)

                else:
                    return None

#---------------------------------------------------------------------- (Operators)

def seq_add(A, B):
    return [a + b for a, b in zip(A, B)]

def seq_diff(A, B):
    return [a - b for a, b in zip(A, B)]

def seq_self_diff(A):
    return [(A[i + 1] - A[i]) for i in range(len(A) - 1)]

def seq_mod_seq(A, B):
    return [a % b for a, b in zip(A, B)]

def seq_mult(A, B):
    return [a*b for a, b in zip(A, B)]

def seq_div(A, B):
    return [a/b for a, b in zip(A, B)]

def seq_div_floor(A, B):
    return [a//b for a,b in zip(A, B)]

def seq_div_ceil(A, B):
    def div_ceil(x, y):
        return -(x // -y)
    return [div_ceil(a,b) for a,b in zip(A,B)]

def seq_power(A, B):
    return [a**b for a,b in zip(A, B)]

def seq_root(A,B):
    return [a**(1/float(b)) for a,b in zip(A,B)]

def seq_powroot(A, B, C):
    return [a**(float(c)/float(b)) for a,b,c in zip(A,B,C)]
