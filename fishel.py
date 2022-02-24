#functions to help out the FFW app

def date_fix(d):
  """This function will fix the default date format for display"""
  y = d[0:4]
  m = d[5:7]
  day = d[8:]
  return f'{m}/{day}/{y}'

