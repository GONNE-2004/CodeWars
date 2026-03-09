def solution(s):
    new = "" #stores the new variable
    for n in s:
        if n.isupper():#checks if it's uppercase
            new += " " + n # "+=" appends and also updates existing variable
        else:
            new += n #just appends if upper condition isn't meet
    return new

solution("helloWorld") #should return "hello World"
solution("camel") #should return "camel"