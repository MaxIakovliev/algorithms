def concat(a:str='', b:str='') ->str:
    return "{0} {1}".format(str(a),str(b))

print(concat(a="hello",b="world"))