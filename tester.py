import timeit

t = timeit.Timer('teste_banco.gogo(0,10)','import teste_banco')      # outside the try/except
try:
    t.timeit(10)    # or t.repeat(...)
    
except:
    t.print_exc()
