number_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
}

def convert_to_words(number):
  if number == 0:
      return number_words[0]

  words = []
  place = 1  # Keep track of the place value (thousands, millions, billions, etc.)
  while number > 0:
    remainder = number % 1000
    if remainder > 0 or place > 1:  # Check if thousands place is non-zero or not the first place
      three_digit_words = convert_three_digit_number(remainder)
      words.append(three_digit_words + " " + number_words.get(place, ""))
    number //= 1000
    place *= 1000

  words.reverse()
  finalval = " ".join(words)
  last_word_length = len(finalval.split()[-1])
  output = finalval[:-last_word_length - 1]
  return " ".join(output)

def convert_three_digit_number(number):
  words = []
  hundreds = number // 100
  if hundreds > 0:
    words.append(number_words[hundreds] + " " + number_words[100])
  tens = (number % 100) // 10
  ones = number % 10
  if tens > 0:
    if tens == 1:
      words.append(number_words[tens * 10 + ones])
    else:
      words.append(number_words[tens * 10])
      if ones > 0:
        words.append(number_words[ones])
  elif ones > 0:
    words.append(number_words[ones])
  return " ".join(words)



number = 1240906
word_representation = convert_to_words(number)
print(f"Number: {number}, Word representation: {word_representation}")

