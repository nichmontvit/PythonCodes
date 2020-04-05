filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for x in range(len(filenames)):
  old_name = filenames[x]
  if old_name.endswith(".hpp"):
    new_name = old_name.replace('.hpp', '.h')
  else:
    new_name = old_name;
  newfilenames.append((old_name,new_name))

print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]