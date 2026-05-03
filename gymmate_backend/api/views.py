from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .firebase_config import verify_firebase_token
import requests
import json

FIREBASE_API_KEY = "AIzaSyCCNCp_7ywWsy7CMLFbQoTO_RFXkNLZ1f0"

@api_view(['POST'])
def login_trainer(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Firebase REST API se sign in
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return Response({
            'success': True,
            'idToken': data['idToken'],
            'email': data['email'],
            'localId': data['localId']
        })
    return Response({'success': False, 'error': 'Invalid credentials'}, status=401)

@api_view(['GET'])
def get_all_users(request):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_data = verify_firebase_token(token)
    
    if not user_data:
        return Response({'error': 'Unauthorized'}, status=401)
    
    # Firebase REST API se users list - you need to maintain users in Firestore
    # For now, returning mock data
    return Response({
        'users': [
            {'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'age': 25, 'weight': 70, 'goal': 'Weight Loss'},
            {'id': '2', 'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 28, 'weight': 65, 'goal': 'Muscle Gain'}
        ]
    })

@api_view(['GET'])
def get_questions(request):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_data = verify_firebase_token(token)
    
    if not user_data:
        return Response({'error': 'Unauthorized'}, status=401)
    
    # Fetch questions from Firestore via REST API
    # For now, returning mock data
    return Response({
        'questions': [
            {'id': '1', 'userId': 'user1', 'question': 'How to do proper squat?', 'answer': '', 'status': 'pending'},
            {'id': '2', 'userId': 'user2', 'question': 'Best diet for muscle gain?', 'answer': 'Eat high protein foods', 'status': 'answered'}
        ]
    })

@api_view(['POST'])
def answer_question(request, question_id):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_data = verify_firebase_token(token)
    
    if not user_data:
        return Response({'error': 'Unauthorized'}, status=401)
    
    answer = request.data.get('answer')
    # Update question in Firestore
    return Response({'success': True, 'message': 'Answer submitted'})

@api_view(['POST'])
def assign_workout(request):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_data = verify_firebase_token(token)
    
    if not user_data:
        return Response({'error': 'Unauthorized'}, status=401)
    
    user_id = request.data.get('userId')
    workout = request.data.get('workout')
    
    # Save workout to Firestore
    return Response({'success': True, 'message': 'Workout assigned'})   