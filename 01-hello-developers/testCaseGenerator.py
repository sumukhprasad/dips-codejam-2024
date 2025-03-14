import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')

nouns = ['world', 'people', 'developers', "dips", "codejam"]*4

for i in range(0, 20):
     n = str(i).zfill(2)

     inputFile = open(f'./testCases/input/input{n}.txt', 'a')
     inputFile.write(nouns[i])
     inputFile.close()
     
     outputFile = open(f'./testCases/output/output{n}.txt', 'a')
     outputFile.write(f'Hello, {nouns[i]}!')
     outputFile.close()

     print(f'Written case {n}.')