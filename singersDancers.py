singers={"arun","sagar","vikash","pihu"}
dancers={"riya","simran","ritu","rahul"}

all_artists = singers | dancers
all_rounders = singers & dancers
dancers_not_singers = dancers - singers
singers_not_dancers = singers - dancers
dancers_or_singers_only = (dancers - singers) | (singers - dancers)
print("All artists:", all_artists)
print("All-rounders:", all_rounders)
print("Dancers but not singers:", dancers_not_singers)
print("Singers but not dancers:", singers_not_dancers)
print("Dancers but not singers cum singers but not dancers:", dancers_or_singers_only)