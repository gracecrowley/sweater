def login_check(user_login):
    run = True
    while run:
        user_input = input("Welcome to Sweater. Please enter your login ID: ")
        if user_input == user_login:
            print(f"Thank you {user_login}, your ID was correctly entered.\n")
            run = False


def print_user_choice():
    user_choice = int(input("""Would you like to:
    1) Make a new tweet
    2) Search tweets by username 
    3) Search tweets by hashtag
    4) See all tweets made by a user_choice
    5) Logout
    What would you like to do? """))
    return user_choice


def twitter_menu():
    run = True
    while run:
        user_choice = print_user_choice()
        if user_choice == 1:
            new_tweet(swet_list)
        elif user_choice == 2:
            user_login = input("Enter the name you would like to search: ")
            username_search(swet_list, user_login)
        elif user_choice == 3:
            hashtag_search(swet_list)
        elif user_choice == 4:
            user_login = input("Enter the name you would like to search: ")
            all_tweets(swet_list, user_login)
        elif user_choice == 5:
            print("Thank you for using Sweat!")
            run = False
            print()
            login_check(user_login)
        else:
            print("Not a valid choice, please try again")


def new_tweet(swet_list):
    user_username = input('Please enter your username: ')
    user_date = input('Please enter todays date (YYYYMMDD): ')
    user_message = input('Type your message (max 280 characters): ')
    swet_dict = {'username': user_username, 'date': user_date, 'message': user_message}
    swet_list.append(swet_dict)


def hashtag_search(swet_list):
    hash_search = input("Search for Tweets by hashtag: ")
    for tweet in swet_list:
        if hash_search in tweet["message"]:
            print(tweet["username"], tweet["date"], tweet["message"])


def username_search(swet_list, user_login):
    for tweet in swet_list:
        if user_login in tweet['username']:
            print(tweet['message'])


def all_tweets(swet_list, user_login):
    output_list = []
    for tweet in swet_list:
        if user_login in tweet['username']:
            output_list.append(tweet['date'])
            bubble_sort(output_list)
            for date in output_list:
                if date in tweet['date']:
                    print(tweet["username"], tweet["date"], tweet["message"])


def bubble_sort(L):
    stop_counting = True
    pass_number = len(L) - 1
    while stop_counting and pass_number > 0:
        stop_counting = False
        for index in range(pass_number):
            if L[index] > L[index + 1]:
                stop_counting = True
                container = L[index]
                L[index] = L[index + 1]
                L[index + 1] = container
        pass_number = pass_number - 1
    return L


swet_list = [{'username': 'grace', 'date': '2085/12/09', 'message': 'test4'},
             {'username': 'grace', 'date': '2021/12/02', 'message': 'test3 #hi'},
             {'username': 'grace', 'date': '2020/12/02', 'message': 'test0 #hi'},
             {'username': 'grace', 'date': '2000/12/03', 'message': 'test1'},
             {'username': 'grace', 'date': '2020/12/04', 'message': 'test2'},
             {'username': 'grace', 'date': '2020/02/13', 'message': '#hi'},
             {'username': 'grace', 'date': '2020/06/01', 'message': '#hello!'}]

user_login = "grace"
twit_dict = {}
login_check(user_login)
twitter_menu()