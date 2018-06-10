from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Contact, GroupToUser, Expense, Borrower


@api_view(['GET'])
def health(request):
    return Response(data={'message': 'App is healthy'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_friend_ids(request):
    friends = []
    for i in request.data['phone_numbers']:
        friend = User.objects.filter(phone_number=i)[0]
        friends.append((i, friend.id))
    return Response(data={'friends': friends}, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_friend_to_network(request, user_id):
    friend_phone_number = request.data['phone_number']
    requester_id = request.data['requester']
    users = User.objects.filter(phone_number=friend_phone_number)
    if len(users) == 0:
        error_message = "no person found with given contact"
        return Response(data={'error': error_message},
                        status=status.HTTP_400_BAD_REQUEST)
    requester = User.objecst.filter(id=requester_id)[0]
    new_contact = Contact(user=requester, contact=users[0])
    new_contact.save()
    return Response(data={"response": "successfully added new contact."},
                    status=status.HTTP_201_CREATED)


def find_biggest_borrower(amount_sheet):
    max_amount_borrowed = 1 << 30  # assuming no one will borrow amount : 1 << 30
    for user in amount_sheet:
        if amount_sheet[user] < max_amount_borrowed:
            answer = user
            max_amount_borrowed = amount_sheet[user]
    return answer, max_amount_borrowed


def find_biggest_lender(amount_sheet):
    max_amount_lent = -1
    for user in amount_sheet:
        if amount_sheet[user] > max_amount_lent:
            answer = user
            max_amount_lent = amount_sheet[user]
    return answer, max_amount_lent


def min_cash_flow_helper(amount_sheet, final_answer):
    biggest_borrower, amt_borrowed = find_biggest_borrower(amount_sheet)
    biggest_lender, amt_lent = find_biggest_lender(amount_sheet)
    if amt_borrowed == 0 and amt_lent == 0:
        return
    elif amt_lent * amt_borrowed == 0:
        # this should not happen
        # the lenders and borrowers should cancel each other out
        raise Exception
    else:
        if abs(amt_borrowed) > abs(amt_lent):
            amount_to_give = amt_lent
        else:
            amount_to_give = amt_borrowed
        money_giver = biggest_borrower
        money_receiver = biggest_lender
        amount_sheet[money_giver] += amount_to_give
        amount_sheet[money_receiver] -= amount_to_give
        final_answer.append({
            "money_giver": User.objects.filter(id=money_giver)[0],
            "money_receiver": User.objects.filter(id=money_receiver)[0],
            "amount_to_give": amount_to_give
        })
        min_cash_flow_helper(amount_sheet, final_answer)


def solve_min_cash_flow_problem(amount_sheet):
    final_answer = []
    min_cash_flow_helper(amount_sheet, final_answer)
    return final_answer


@api_view(['GET'])
def simplify_cash_flow(group_id):
    # find all the expenses that happened in the group
    expenses = Expense.objects.filter(group=group_id)
    balance_sheet = {}

    # Calculate how user each user paid (in all the expenses)
    for expense in expenses:
        if expense.spender.id in balance_sheet:
            balance_sheet[expense.spender.id] += expense.amt
        else:
            balance_sheet[expense.spender.id] = expense.amt

    # Calculate how user each user needs to repay (in all the expenses)
    for expense in expenses:
        borrowings = Borrower.objects.filter(expense=expense)
        for borrowing in borrowings:
            if borrowing.borrower.id in balance_sheet:
                balance_sheet[borrowing.borrower.id] -= borrowing.amount_to_repay
            else:
                balance_sheet[borrowing.borrower.id] = -1 * borrowing.amount_to_repay
    return solve_min_cash_flow_problem(balance_sheet)
