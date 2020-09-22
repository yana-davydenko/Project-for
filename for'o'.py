def my_function(sentence, letter):
  i = 0
  for x in sentence:
    if x == letter:
     i += 1
  print('the quantity of the letter:', i)

my_function('apple banana cherry', 'a')
my_function('kleiding jurk socks', 'k')
my_function("i like dancing", "i")
my_function('stay positive and never stop', 'n')
