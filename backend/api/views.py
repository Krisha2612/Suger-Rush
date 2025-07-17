from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Sweet

@csrf_exempt
def create_sweet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sweet = Sweet.objects.create(
            name=data.get('name'),
            flavor=data.get('flavor')
        )
        return JsonResponse({'id': sweet.id, 'name': sweet.name, 'flavor': sweet.flavor})
    return JsonResponse({'error': 'POST request required'}, status=400)
