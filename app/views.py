from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, Contact


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
