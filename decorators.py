

def decorator(func):
  def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
  return decorated

@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello World!')



#
# def check_integer(func):
#   def decorated(width, height):
#    if width >= 0 and height >=0:
# else:
# raise ValueError('input must ve positive value')
# @check_integer
# def rect_area(width, height):
#  return (width * height)
#
# @check_integer
# def tri_area(width, height):
#  return (1/2*width * height)
#
# class User:
#     def __init__(self, auth):
#         self.is_authenticated =auth
#
# user =User(auth=False)
#
# r_area =rect_area(user, 10,10)
# t_area =tri_area(user, 10 ,-10)
#
# def login_required(func):
#     def decorated(user, width, height):
#         if user.is_authenticated:
#             return func(user, width, height):
#         else: