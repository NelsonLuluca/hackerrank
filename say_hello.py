
# Complete this function to return either
# "Hello, [name]!" or "Hello there!"
# based on the input

def say_hello(name):
  # you can print to STDOUT to debug if you need to:
  #print("Hello %s!" % name)
  
  if (name == ''):
      message = 'Hello there!'
  else:
    message = f"Hello, {name}!"
  # but to complete the challenge you need to return a value
  return (message) # TODO: return correct value

print(say_hello(''))
print(say_hello('Sean'))
