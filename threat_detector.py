# get all palindromes in the sublists of each message

def palindrome_finder(message):
    palindromes = []
    
    for i in range(len(message)):
            for j in range(i+1, len(message) + 1):
                temp = message[i:j]
                if temp == temp[::-1] and len(temp) >= 3: # the valid palindrome has 3 or more chars
                    palindromes.append(temp)
    return palindromes

def threatDetector(textMessages):
    symbols = [ message[len(message)-3:] for message in textMessages] # extract symbols from our message
    new_message = [message[:-3] for message in textMessages] # message after removing symbol
    palindromes = [ palindrome_finder(message) for message in new_message ] # get all possible palindromes in new message
    palindrome_sublists_size = [len(x) for sublist in palindromes for x in sublist] # get size of each individual palindrome substring
    palindrome_array_size = [len(x) for x in palindromes] # get size of each message's palindrome array
    palindromes_size = len(palindromes) # overrall size of our palindromes array
    scores = []
    risk_score = []
    result = []

    if palindromes_size > 0:
        for array_size in palindrome_array_size:
            new_palindrome_sublists_size = palindrome_sublists_size[:array_size] # get score of first n palindromes
            del palindrome_sublists_size[:array_size] # update `palindrome_sublists_size` by removing from original sublist size already calculated scores
            scores.append(sum(new_palindrome_sublists_size)) # get total score for each message
        
        palindromes_size -= 1 # reduce palindromes_size by 1 after each message score calculation signifying calculation of each message's score

    # score matching
    if len(palindrome_array_size) >= 2: # detect threat when there are 2 or more palindromes
        for score in scores:
            if score in range(1, 11):
                risk_score.append("Possible")
            elif score in range(11, 41):
                risk_score.append("Probable")
            elif score in range(41, 151):
                risk_score.append("Escalate")
            else:
                risk_score.append("Ignore")
    
    for i in range(len(symbols)):
        result.append(symbols[i] + " " + risk_score[i]) # concatenate each  symbol with its score
    
    return "\n".join(result) # return the result on new line


textMessages = ['xxxayyySPY', 'xxxxxxbzzzzzzIVV', 'xxAyyDJI']

print(threatDetector(textMessages))