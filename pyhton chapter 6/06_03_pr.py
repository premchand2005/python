# def check_username_length(username):
#     if len(username) < 10:
#         return True
#     else:
#         return False

# # Test the function
# username = input("Enter your username: ")
# if check_username_length(username):
#     print("Username contains less than 10 characters.")
# else:
#     print("Username contains 10 or more characters.")


str = input("Enter your username: ")

if len(str) < 10:
    print("Username contains less than 10 characters.")
else:
    print("Username contains 10 or more characters.")