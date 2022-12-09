#task 1

# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
#
# if 1 <= a <= 3:
#     print (a);
#
# if 1 <= b <= 3:
#     print (b);
#
# if 1 <= c <= 3:
#     print (c);


#task 2

# a = input('Enter year number: ');
# if a % 4 == 0 and a % 100 != 0:
#     print('365 days in this year');
# elif a % 400 == 0:
#     print('365 days in this year');
# else:
#     print('366 days in this year');



#task 3
# a = input('Enter purchase amount: ');
# if a >= 500 and a < 1000:
#     a = a * 0.97;
#     print ('Discounted purchase amount: ' + str(a));
# if a >= 1000:
#     a = a * 0.95;
#     print ('Discounted purchase amount: ' + str(a));


#task 4
# a = input('Enter number units of measurement: ');
# b = input('Enter weight in specified units: ');
# if a == 1:
#     print ('Weight ' + str(b) + ' kg');
# elif a == 2:
#     b = b * 10 ** (-6);
#     print('Weight ' + str(b) + ' kg');
# elif a == 3:
#     b = b * 10 ** (-3);
#     print('Weight ' + str(b) + ' kg');
# elif a == 4:
#     b = b * 10 ** (3);
#     print('Weight ' + str(b) + ' kg');
# elif a == 5:
#     b = b * 10 ** (2);
#     print('Weight ' + str(b) + ' kg');


#task 5
# import math
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# d = input('Enter fourth number: ');
# if a < b and a < c and a < d :
#     print (math.cos(a));
# elif b < a and b < c and b < d :
#     print (math.cos(b));
# elif c < a and c < b and c < d :
#     print (math.cos(c));
# elif d < a and d < c and d < b :
#     print (math.cos(d));

#task 6
# import math
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a > b and a > c:
#     print (math.sin(a));
# elif b > a and b > c:
#     print (math.sin(b));
# elif c > a and c > b:
#     print (math.sin(c));


# #task 7
# a = [input('Enter the size of the first triangle: '), input('Enter the size of the first triangle: '), input('Enter the size of the first triangle: ')];
# b = [input('Enter the size of the second triangle: '), input('Enter the size of the second triangle: '), input('Enter the size of the second triangle: ')];
# pa = (a[0] + a[1] + a[2])/2;
# pb = (b[0] + b[1] + b[2])/2;
# sa = pa * ((pa - a[0]) * (pa - a[1]) * (pa - a[2]))**0.5;
# sb = pb * ((pb - b[0]) * (pb - b[1]) * (pb - b[2]))**0.5;
# if sa == sb:
#     print ('Triangles are equal!');
# else :
#     print('Foul!!!');

#task 8
# a = [input('Enter the side of the first triangle: '), input('Enter the base of the first triangle: ')];
# p = (a[0] + a[0] + a[1])/2;
# s = (p * (p - a[0]) * (p - a[0]) * (p - a[1]))**0.5;
# if s % 2 == 0:
#     print ('Paired triangle area');
# else :
#     print("can't divide by 2");

#task 9
# a = input('Enter your place(1-12): ');
# if a == 1 :
#     print('First place');
# elif a == 2 :
#     print('Second place');
# elif a == 3 :
#     print('Third place');
# elif a == 4 :
#     print('Fourth place');
# elif a == 5 :
#     print('Fifth place');
# elif a == 6 :
#     print('Sixth place');
# elif a == 7 :
#     print('Seventh place');
# elif a == 8 :
#     print('Eighth place');
# elif a == 9 :
#     print('Ninth place');
# elif a == 10 :
#     print('Tenth place');
# elif a == 11 :
#     print('Eleventh place');
# elif a == 12 :
#     print('Twelfth place');
# else:
#     print('Main participation');

#task 10
# a = input('Choose 1(from radians to degrees) or 2(from degrees to radians): ');
# b = input('Enter value: ');
# if a == 1:
#     b = b * 57.296;
#     print('Your angle is ' + str(b) + ' degrees');
# elif a == 2:
#     b = b * 0.0174533;
#     print('Your angle is ' + str(b) + ' radians');

#task 11
# a = input('Enter first number: ');
# b = input('Enter first number: ');
# c = input('Enter first number: ');
# if a > 0 and b > 0 and c > 0:
#     print('We have 3 positive numbers');
# elif (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c > 0):
#     print('We have 2 positive numbers');
# elif a <= 0 and b <= 0 and c <= 0:
#     print('We have 0 positive numbers');
# else:
#     print('We have 1 positive numbers');


#task 12
# x = input('Enter X: ');
# y = input('Enter Y: ');
# if (x < 0 and y < 0) or (x > 0 and y > 0):
#     c = (x*y)**0.5;
#     print(c);
# else:
#     c = (x + y)/2;
#     print(c);

#task 13
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a > b and a > c:
#     if a**2 == (b**2 + c**2):
#         s = (b * c)/2;
#         print('Area is ' + str(s));
# elif b > a and b > c:
#     if b ** 2 == (a ** 2 + c ** 2):
#         s = (a * c) / 2;
#         print('Area is ' + str(s));
# elif c > a and b < c:
#     if c ** 2 == (b ** 2 + a ** 2):
#         s = (b * a) / 2;
#         print('Area is ' + str(s));
# else:
#     print("It's not a right triangle")


#task 14
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a > b and a > c:
#     if a < (b + c):
#         p = (a + b + c)/2;
#         s = (p * (p - a) * (p - b) * (p - c))**0.5;
#         print('Area is ' + str(s));
# elif b > a and b > c:
#     if b < (a + c):
#         p = (a + b + c) / 2;
#         s = (p * (p - a) * (p - b) * (p - c))**0.5;
#         print('Area is ' + str(s));
# elif c > a and b < c:
#     if c < (b + a):
#         p = (a + b + c) / 2;
#         s = (p * (p - a) * (p - b) * (p - c))**0.5;
#         print('Area is ' + str(s));
# else:
#     print('Triangle does not exist');

#task 15
# a = input('Enter the price of the item: ');
# b = input('Enter the quantity of the item: ');
# if b >= 100:
#     c = (a*b) * 0.9;
#     print('Total price ' + str(c));
# else:
#     c = a*b;
#     print('Total price ' + str(c));

#task 16
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a == b == c:
#     print("It's an equilateral triangle");
# else:
#     print("It's not an equilateral triangle")

#task 17
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# if (a**2 + b**2) > (a + b)**2:
#     print('The sum of the squares is greater than the square of the sum of these numbers');
# elif (a**2 + b**2) < (a + b)**2:
#     print('The square of the sum is greater than the sum of the squares of these numbers');

#task 18
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a > 0:
#     print(a**2);
# else:
#     print(a);
# if b > 0:
#     print(b**2);
# else:
#     print(b);
# if c > 0:
#     print(c**2);
# else:
#     print(c);


#task 19
# x = input('Enter first number: ');
# y = input('Enter second number: ');
# r = input('Enter radius: ');
# if x < r and -x < r and y < r and -y < r:
#     print('The given coordinates are in the circle');
# else:
#     print('The given coordinates are not in the circle');


#task 20
# import math
# a = input('Enter angle value in radians: ');
# if math.sin(a) > math.cos(a):
#     print('Sin > cos');
# else:
#     print('Cos > sin');


#task 21
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a > b and a > c:
#     if a**2 == (b**2 + c**2):
#         print("It's a right triangle");
# elif b > a and b > c:
#     if b ** 2 == (a ** 2 + c ** 2):
#         print("It's a right triangle");
# elif c > a and b < c:
#     if c ** 2 == (b ** 2 + a ** 2):
#         print("It's a right triangle");
# else:
#     print("It's not a right triangle")


#task 22
# a = input('Enter side of the square: ');
# b = input('Enter radius of the circle: ');
# sa = a**2;
# sb = 3.14*b**2;
# if sa > sb:
#     print('A square is larger than a circle');
# elif sb > sa:
#     print('A circle is larger than a square');


#task 23
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a > 0 :
#     print(a**3);
# else:
#     print(0);
# if b > 0 :
#     print(b**3);
# else:
#     print(0);
# if c > 0 :
#     print(c**3);
# else:
#     print(0);


#task 24
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# if a > 0 and b > 0:
#     print('Your point in the first quarter');
# else:
#     print('Your point is not in the first quarter');


#task 25
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# d = (a + b + c)/2
# if a > d or -a > d:
#     print(a);
# if b > d or -b > d:
#     print(b);
# if c > d or -c > d:
#     print(c);



#task 26
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# if (a**2 - b**2) > (a - b)**2 or (a**2 - b**2) > -(a - b)**2:
#     print('The difference of squares is greater than the modulus of the square of the difference');
# elif (a**2 - b**2) < (a - b)**2 or (a**2 - b**2) < -(a - b)**2:
#     print('The modulus of the square of the difference is greater than the difference of squares');

#task 27
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if a == b or b == c or c == a:
#     print("It's an isosceles triangle");
# else:
#     print("It's not an isosceles triangle")


#task 28
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# if a > 0 and b < 0:
#     print('Your point in the fourth quarter');
# else:
#     print('Your point is not in the fourth quarter');


#task 29
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if (a + b + c) > 0:
#     print(str(a*2) + '\n' + str(b*2) + '\n' + str(c*2));
# else:
#     print(str(0) + '\n' + str(0) + '\n' + str(0));


#task 30
# a = input('Enter first number: ');
# b = input('Enter second number: ');
# c = input('Enter third number: ');
# if (a % 2 )!= 0:
#     print(str(a) + ' is not a pair number');
# if (b % 2 )!= 0:
#     print(str(b) + ' is not a pair number');
# if (c % 2 )!= 0:
#     print(str(c) + ' is not a pair number');