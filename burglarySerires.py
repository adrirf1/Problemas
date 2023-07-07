def find_it(items, name:str):
    capital = name[0].upper()
    palabra = capital+name[1:]
    print(palabra)
    if name in items:
        return "{} is gone...".format(palabra)
    else:
        return "{} is here!".format(palabra)
    
    
    
print(find_it({
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
}, "holaaaa"))