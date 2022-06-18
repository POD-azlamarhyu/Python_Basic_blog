class Admin:
     count = 0
     def __init__(self,id,admin_id):
          self.id = id
          if admin_id == 0:
               self.admin_id = None
          else:
               self.admin_id = admin_id

     def is_admin(self):
          if self.id is not None:
               print("hello administrator")
          else:
               print("bad request")
     
     def get_admin(self):
          if self.admin_id is not None:
               return {'id':self.id,'admin_id':self.admin_id,'admin_name':'admin001'}
          else:
               pass
     
     def add_admin_info(self):
          input_admin_name = input('admin name : ')

          print('edit admin name')

admin = Admin(10,1)
admin.get_admin()
admin.add_admin_info()

class AdminUser(Admin):
     def __init__(self, id, admin_id,user_id,auth_level):
          super().__init__(id, admin_id)
          self.user_id = user_id
          self.auth_level = auth_level

     def add_user_info(self):
          if self.auth_level >= 2:
               add_user_id = input('input user id')
               print('create new user')
          else:
               pass

     def delete_user(self):
          if self.auth_level > 5:
               delete_user_id = input('user id : ')
               print('deleted user')
          else:
               pass
     
user = AdminUser(2,2,"user_admin",4)
user.add_user_info()
user.is_admin()
