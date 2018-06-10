from django.db import models


# Create your models here.




class User(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email_id = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=50, default='abcd')


class Group(models.Model):
    name = models.CharField(max_length=200, default='Default')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)  # not sure if it's correct


class GroupToUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # create relation if this doesn't work
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joining_date = models.CharField(max_length=100)  # use datetime instead ?


class Expense(models.Model):
    amt = models.FloatField()
    spender = models.ForeignKey(User, on_delete=models.CASCADE)  # not sure if it's correct
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # not sure if it's correct
    description = models.CharField(max_length=200, default='No description')
    currency = models.CharField(max_length=30, default='Rupees')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    detail = models.CharField(max_length=300, default='')


class Borrower(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    amount_to_repay = models.FloatField(default=0)


class Transaction(models.Model):
    description = models.CharField(max_length=200)


class UserTransaction(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


class Contact(models.Model):
    contacts = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
