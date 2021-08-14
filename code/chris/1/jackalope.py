jackalopes = [0, 0]
year_counter = 0

while len(jackalopes) < 1000:
  year_counter += 1
  for idx in range(len(jackalopes)):
      jackalopes[idx] += 1
      if jackalopes[idx] >= 4 and jackalopes[idx] <= 8:
          jackalopes.extend([0])

  for i, jackalope in enumerate(jackalopes):
      while jackalopes[i] >= 10:
          jackalopes.pop(i)
  print('year:', year_counter)
  print('jacks:', jackalopes)

print(year_counter)
