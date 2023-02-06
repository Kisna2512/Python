class College:
  collegename="DY Patil" # Static Variable

  def __init__(self):
    self.s_name="Krishna" #Instance variable



principle=College()
HOD=College()
Acc=College()

# print(principle.collegename," ",principle.s_name)
# print(HOD.collegename," ",HOD.s_name)
# print(Acc.collegename," ",Acc.s_name)

# College.collegename="PICT"
# Acc.s_name="Yash"


# print(principle.collegename," ",principle.s_name)
# print(HOD.collegename," ",HOD.s_name)
# print(Acc.collegename," ",Acc.s_name)

# del HOD.collegename Using object we caannot delete the Static variable
# del College.collegename Using Class name we can delete Static variable


# Using object We only access the static variable
#Using Class name we can update,delete the Static variable




