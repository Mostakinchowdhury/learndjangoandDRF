from functools import wraps

class Mymiddleware:
  def __init__(self,get_response):
      self.get_response=get_response

  def getip(self,request):
          x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
          if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
          else:
           ip = request.META.get('REMOTE_ADDR')
          return ip

  def __call__(self,request, *args, **kwds):
           print(self.getip(request))
           response =self.get_response(request, *args, **kwds)
           print("🔸 Response Middleware: view-এর পরে")
           return response


def funcmiddleware(get_response):
   print("funcmiddleware active now")
   def wrapper(request,*args, **kwargs):
     print("I am from before funcmiddleware")
     response=get_response(request,*args, **kwargs)
     print("I am from after funcmiddleware")
     return response
   return wrapper

#  i write a decorator

def mydecorate(view_func):
  @wraps(view_func)
  def wrapper(request,*args, **kwargs):
    print("i am my decorator")
    response=view_func(request,*args, **kwargs)
    print("after decorator")
    return response
  return wrapper
