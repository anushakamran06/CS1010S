##########
# Task 1 #
##########
def mosaic(rune1, rune2, rune3, rune4):
    return beside(stack(rune4, rune3), stack(rune1, rune2))                     

##########
# Task 2 #
##########
def simple_fractal(rune):
    return beside(rune, stack(rune, rune))         
  
##########
# Task 3 #
##########
def egyptian(rune, n):
    ends = repeat_horizontal(rune, n)
    middle = quarter_turn_left(stack_frac( 1/n, ends, stack_frac((n-2)/n, middle, ends)))
  return stack_frac(1/n, ends, stack_frac ((n-2)/n, middle, ends))



