import random

def result_class(cgpa:float): 
# First Class Honours (CGPA: 4.50 - 5.00)
# Second Class Honours, Upper Division (CGPA: 3.50 - 4.49)
# Second Class Honours, Lower Division (CGPA: 2.40 - 3.49)
# Third Class Honours (CGPA: 1.50 - 2.39)
# Pass (CGPA: 1.00 - 1.49)


    if cgpa >= 4.50 : 
        return "First Class"
    elif cgpa >= 3.50:
        return "Second Class Upper"
    elif cgpa >= 2.40:
        return "Second Class Lower"
    elif cgpa >= 1.50:
        return "Third Class"
    elif cgpa >= 1.00:
        return "Pass"
    else:
        return "Fail"

    if cgpa > 5.00 and cgpa < 1.00: 
        return "Invalid"    


first_class_quotes = [
    "It always seems impossible until it is done. — Nelson Mandela",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. — Aristotle",
    "There are no secrets to success. It is the result of preparation, hard work, and learning from failure. — Colin Powell",
    "Success is liking yourself, liking what you do, and liking how you do it. — Maya Angelou",
    "It does not matter how slowly you go as long as you do not stop. — Confucius",
    "Nothing in life is to be feared, it is only to be understood. — Marie Curie",
    "Success is to be measured not so much by the position one has reached in life as by the obstacles overcome. — Booker T. Washington",
    "The best way to predict the future is to create it. — Abraham Lincoln",
    "Excellence is not a gift, but a skill that takes practice. — Plato",
    "If you think you are too small to make a difference, try sleeping with a mosquito. — African Proverb",
]

low_gp_quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
    "I've failed over and over and over again in my life. And that is why I succeed. — Michael Jordan",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. — Nelson Mandela",
    "It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all. — J.K. Rowling",
    "Failure is success in progress. — Albert Einstein",
    "It is hard to fail, but it is worse never to have tried to succeed. — Theodore Roosevelt",
    "What would life be if we had no courage to attempt anything? — Vincent van Gogh",
    "I have not failed. I've just found 10,000 ways that won't work. — Thomas Edison",
    "Smooth seas do not make skillful sailors. — African Proverb",
    "However long the night, the dawn will break. — African Proverb",
]


def get_morale_message(cgpa: float) -> str:
    """Returns a congrats/encouragement message + random quote based on CGPA."""
    if cgpa >= 4.50:
        quote = random.choice(first_class_quotes)
        return f"Congratulations! You made First Class.\n{quote}"
    elif cgpa >= 3.00:
        quote = random.choice(first_class_quotes)
        return f"Good work. Keep building on this momentum.\n{quote}"
    else:
        quote = random.choice(low_gp_quotes)
        return f"Don't be discouraged; this is a chance to rise higher.\n{quote}"
