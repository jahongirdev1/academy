from django.http import JsonResponse
from django.views.decorators.http import require_GET
from main.models import UserModel, CourseModel
import secrets


def courses_list_json(request):
    if request.GET.get('password') == 'jahongirdev1':
        courses = CourseModel.objects.all()
        data = {
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
                } for course in courses
            ]
        }
        return JsonResponse(data, safe=False)



@require_GET
def get_user(request):
    try:
        email = request.GET.get('email')
        password = request.GET.get('password')
        token = request.GET.get('token')

        if not all([email, password]):
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        user = UserModel.objects.get(email=email)


        if user.password != password:
            return JsonResponse({'error': 'Invalid password'}, status=400)

        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password,
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
                        } for lesson in course.lessons.filter(status=0)
                    ]
                } for course in user.courses.filter(status=0)
            ]
        }

        if token and user.token != token:
            new_token = secrets.token_hex(16)
            user.token = new_token
            user.save()

            user_data['token'] = new_token

        return JsonResponse({'user': user_data}, status=200)

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
