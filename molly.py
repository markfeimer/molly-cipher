#####
# molly-cipher, a block cipher
# version 0.0.1
# written in Python 2.7.5
#####
# written by: Mark Feimer
#####
# WARNING: although awesome for many reasons, protecting your information is beyond
# the capability of the MOLLY cipher and you WILL lose all of your data. If you need
# this warning, you're probably the type of person who should heed this warning.
#####
import sys
print "\n".join(sys.argv)

dictionary = {'a' : 'molly', 'b' : 'Molly', 'c' : 'MOlly', 'd' : 'MOLly', 'e' : 'MOLLy', 'f' : 'MOLLY', 'g' : 'mOLLY', 'h' : 'moLLY', 'i' : 'molLY', 'j' : 'mollY', 'k' : 'mOlly', 'l' : 'mOLly', 'm' : 'mOLLy', 'n' : 'mOLLY', 'o' : 'moLly', 'p' : 'MoLly', 'q' : 'moLlY', 'r' : 'MOllY', 's' : 'MOlLY', 't' : 'moLLy', 'u' : 'MOLlY', 'v' : 'molLy', 'w' : 'MolLy', 'x' : 'mOlLy', 'y' : 'mOLLy', 'z' : 'MoLlY', ' ' : 'mOllY'}
invertDict = {}
output = ''
#for k, v in dictionary:
  #dictionary[v] = dictionary.get(v, [])
  #dictionary[v].append(k)

for key, value in zip(dictionary.keys(), dictionary.values()):
      # Operations on key/value can also be performed.
      invertDict[value] = key


def encrypt(plaintext):
  #takes plaintext string of a-z and ' ' (space) and returns ciphertext
  output = ''
  for character in plaintext:
    output += key2val(character)
  return output

def decrypt(stream):
  output = ''
  #line = stream
  def split_str_into_len(s, l=2):
    """ Split a string into chunks of length l """
    return [s[i:i+l] for i in range(0, len(s), l)]
  
  #stream = [line[i:i+5] for i in stream]
  stream = split_str_into_len(stream, l=5)

  print stream
  
  for bunch in stream:
    output += val2key(bunch)
  return output

def val2key(arg):
  local = invertDict.get(arg)
  if (local == None):
    return 'bad string'
  else:
    return local

def key2val(arg):
  local = dictionary.get(arg)
  if (local == None):
    return 'bad string' 
  else:
    return local


input_var = raw_input("Enter something: ")
print "you entered %s" %  input_var

#print(invertDict)
if (len(sys.argv) > 1):
  print sys.argv
  if (sys.argv[1] == '-decrypt'):
    print 'we are in -decrypt'
    stream = input_var
    eo = decrypt(stream)
else:
  stream = list(input_var)
  eo = encrypt(stream)

print(eo)
