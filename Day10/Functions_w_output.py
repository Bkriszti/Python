def format_name(f_name, l_name):
  """DOCUMENTATION"""
  #result=""
  if f_name=="":
    return
  formated_fname=f_name.title()
  formated_lname=l_name.title()
  #result+=formated_fname+" "+formated_lname
  #return result
  return f"{formated_fname} {formated_lname}"


fname = "krisZTian"
lname = "buDai"

res = format_name(input("Introduce your first name: "), lname)
print(res)