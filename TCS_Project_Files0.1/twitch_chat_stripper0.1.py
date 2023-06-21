# seamus forscutt python Twitch chat splicer 0.1
# 20/06/2023-21/06/2023
# read a .txt file with raw chat copy/paste and output spliced
# twitch messages for organised input elsewhere.
# copy/paste twich chat into .txt file. 
# make sure that a time stamp is in the first line of .txt file
# output to TCS-Output.txt   


file_OUT = open('TCS_Output.txt' , 'w')
file_IN = open('TCS_Input.txt')


contents = file_IN.read()
content_lines = contents.split('\n')

content_slice1 = content_lines[2::]
content_slice2 = content_slice1[0::4]

for line in content_slice2:
        line = line.partition(':')[2]
        data = ''.join(line)
        file_OUT.write(data)  
        file_OUT.write('\n')
      

print ('done')



 

