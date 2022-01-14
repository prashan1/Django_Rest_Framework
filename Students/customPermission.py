from rest_framework import permissions

class CustomPermission( permissions.BasePermission):
    def has_permission(self,request,view):
        # username = request.user.username
        # print(username)
        # if request.method == 'POST':
        #     return True
        return False