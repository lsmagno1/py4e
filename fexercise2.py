errormessage = "Bad score"
score = input('Enter a score between 0.0 and 1.0:')

def computegrade (score):
 try:
    score = float(score)
    if score <0.0 or score >= 1.0:
        return (errormessage)
    elif score >= 0.9:
        return ('A')
    elif score >= 0.8:
        return ('B')
    elif score >= 0.7:
        return ('C')
    elif score >= 0.6:
        return ('D')
    elif score < 0.6:
        return ('F')
 except:
    return (errormessage)

computegrade (score)
