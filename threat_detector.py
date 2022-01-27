# get all palindromes in the sublists of each message

def palindrome_finder(message):
    palindromes = []

    for i in range(len(message)):
        for j in range(i+1, len(message) + 1):
            temp = message[i:j]
            # the valid palindrome has 3 or more chars
            if temp == temp[::-1] and len(temp) >= 3:
                palindromes.append(temp)
    return palindromes


def threatDetector(textMessages):
    # extract symbols from our message
    symbols = [message[len(message)-3:]
               for message in textMessages if type(message) == str]
    new_message = [message[:-3]
                   for message in textMessages if type(message) == str]  # message after removing symbol
    # get all possible palindromes in new message
    palindromes = [palindrome_finder(message) for message in new_message]
    # get size of each individual palindrome substring
    palindrome_sublists_size = [len(x)
                                for sublist in palindromes for x in sublist]
    # get size of each message's palindrome array
    palindrome_array_size = [len(x) for x in palindromes]
    # overrall size of our palindromes array
    palindromes_size = len(palindromes)
    scores = []
    risk_score = []
    result = []

    # score calculation
    if palindromes_size > 0:
        for array_size in palindrome_array_size:
            # get size of first n palindromes
            new_palindrome_sublists_size = palindrome_sublists_size[:array_size]
            # update `palindrome_sublists_size` by removing from original sublist size already calculated scores
            del palindrome_sublists_size[:array_size]
            # get total score for each message
            scores.append(sum(new_palindrome_sublists_size))

        palindromes_size -= 1  # reduce palindromes_size by 1 after each message score calculation

    # score matching
    if len(palindrome_array_size) >= 2:  # detect threat when there are 2 or more palindromes
        for score in scores:
            if score in range(1, 11):
                risk_score.append("Possible")
            elif score in range(11, 41):
                risk_score.append("Probable")
            elif score in range(41, 151):
                risk_score.append("Escalate")
            else:
                risk_score.append("Ignore")

    # symbol-score matching
    for i in range(len(symbols)):
        # concatenate each  symbol with its score
        result.append(symbols[i] + " " + risk_score[i])
    
    print("\n".join(result)) # print the result on new line
    # return "\n".join(result)  # return the result on new line


textMessages = ['xxxayyySPY', 'xxxxxxbzzzzzzIVV', "xxAzzDJI"]

threatDetector(textMessages)
