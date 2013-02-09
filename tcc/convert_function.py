def num2eng(n):
  words = ''

  units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
  tens = ['','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


  for group in ['', 'hundred', 'thousand', 'lakh', 'crore']:

    if group in ['', 'thousand', 'lakh']:
      n, digits = n // 100, n % 100
    elif group == 'hundred':
      n, digits = n // 10, n % 10
    else:
      digits = n
    
    if digits in range (1, 20):
      words = units [digits] + ' ' + group + ' ' + words
    elif digits in range (20, 100):
      ten_digit, unit_digit = digits // 10, digits % 10
      words = tens [ten_digit] + ' ' + units [unit_digit] + ' ' + group + ' ' + words
    elif digits >= 100:
      words = num2eng (digits) + ' crore ' + words
    

  return words
