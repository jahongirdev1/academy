import secrets  # For generating a new token
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from main.models import UserModel

@require_GET
def get_user(request):
    try:
        # Retrieve the email, password, and token from query parameters
        email = request.GET.get('email')
        password = request.GET.get('password')
        token = request.GET.get('token')  # Existing token if provided

        if not all([email, password]):
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        # Fetch the user by email
        user = UserModel.objects.get(email=email)

        # Check if the provided password matches
        if user.password != password:  # Replace with a proper password check in production
            return JsonResponse({'error': 'Invalid password'}, status=400)

        # Prepare user data
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password,  # Not recommended to expose password
            'token': user.token,
            'courses': [
                {
                    'id': course.id,
                    'title': course.title,
                    'teacher_full_name': course.teacher_full_name,
                    'teacher_image': course.teacher_image.url if course.teacher_image else None,
                    'lessons': [
                        {
                            'id': lesson.id,
                            'title': lesson.title,
                            'video_link': lesson.video_link,
                            'description': lesson.description
                        } for lesson in course.lessons.all()
                    ]
                } for course in user.courses.all()
            ]
        }

        # If a token is provided, check if it matches
        if token and user.token != token:
            # Token is incorrect, generate a new one
            new_token = secrets.token_hex(16)  # Generate a new 32-character token
            user.token = new_token
            user.save()  # Save the new token to the database

            # Update user data with the new token
            user_data['token'] = new_token

        # Return the user data
        return JsonResponse({'user': user_data}, status=200)

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
