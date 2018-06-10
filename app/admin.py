from django.contrib import admin

from .models import Expense, GroupToUser, Comment, Borrower, UserTransaction, Contact
from .models import Group
from .models import User

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Expense)
admin.site.register(GroupToUser)
admin.site.register(Comment)
admin.site.register(Borrower)
admin.site.register(UserTransaction)
admin.site.register(Contact)
