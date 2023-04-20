#This program will ask the user for two primary colors and mix them
#Pedro Ayala

color1 = (input('Enter the first primary color: '))   #color1 input
color2 = (input('Enter a different primary color: '))   #color2 input

#Determines the secondary color
if color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
    print ('Purple!')
elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
    print ('Orange!')
elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
    print ('Green!')
else:   #incase input is not a primary color
    print ('input is invalid')
