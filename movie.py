print """The following movies are available\n
        1.Avengers EndGame - $200
        2.Captain Marvel - $100
        3.Spiderman Homecoming - $50\n"""
money = input('Enter the money you have in your pocket -> ')
if money <= 0: 
    print '\nAmount entered is invalid'
elif money < 50:
    print '\nNo movie matches your money'
elif money >=50 and money < 100:
    print '\nYou can watch Spiderman'
elif money >=100 and money < 200:
    print '\nYou can watch Spiderman and Captain Marvel'
else:
    print '\nYou can watch any of the three movies'
