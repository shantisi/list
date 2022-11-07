question_list = ["How many continents are there?","What is the capital of India?",
                "NG mei kaun se course padhaya jaata hai"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
              ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
              ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1] 
lifeline = [
['1.Four','3.seven'],
['2.Bhopal','4.Delhi'],
['1.Software Engineering','2.Counseling']]
print("Welcome to KBC")
i = 0
money=0
c=0
while i < len(question_list):
    print(question_list[i])
    j = 0
    while j < len(options_list[i]):
        print(options_list[i][j])
        j=j+1
    if c<2:
        user=(input("do you using lifeline: "))
        if user=="yes":
            c=c+1
            print("5050",lifeline[i])
    else:
        print("Sorry ! you can't use life line because yuo alredy used lifeline")
    b=int(input("choose the answer:"))
    if b == solution_list[i]:
        money+=500
        print("Your answer is correct")
        print("You winner Rs./-",money)
    else:
        print("your answer is wrong")
        break
    i=i+1


# question_list = ["How many continents are there?","What is the capital of India?",
#                 "NG mei kaun se course padhaya jaata hai"]
# options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#               ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#               ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
# solution_list = [3, 4, 1] 
# lifeline = [
# ['1.Four','3.seven'],
# ['2.Bhopal','4.Delhi'],
# ['1.Software Engineering','2.Counseling']]
# print("Welcome to KBC")

# def que():
#     global i
#     i = 0
#     global money
#     money=0
#     global c
#     c=0
#     while i < len(question_list):
#         print(question_list[i])
#         j = 0
#         while j < len(options_list[i]):
#             print(options_list[i][j])
#             j=j+1
#         lif()
#         choose_ans()
#         i=i+1

# def lif():
#     if c<2:
#         user=(input("do you using lifeline: "))
#         if user=="yes":
#             c=c+1
#             print("5050",lifeline[i])
#         else:
#             print("Sorry ! you can't use life line because yuo alredy used lifeline")
#         # choose_ans()

# def choose_ans():
#     b=int(input("choose the answer:"))
#     if b == solution_list[i]:
#         money+=500
#         print("Your answer is correct")
#         print("You winner Rs./-",money)
#     else:
#         print("your answer is wrong")

# que()