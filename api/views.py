import base64
import json

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from users.models import volunteer
from tracker.models import volunteer_hour
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def clock(request):
    try:
        auth_header = request.META['HTTP_AUTHORIZATION']
        encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
        username = decoded_credentials[0]
        password = decoded_credentials[1]
    except:
        return HttpResponse(status=403)

    if username == "test" and password == "test":
        # GET to retrieve data
        if request.method == "POST":
            try:
                # If guild object exists
                body = json.loads(request.body)

                if volunteer.objects.filter(card_id=body['card_id']):
                    if len(volunteer_hour.objects.filter(volunteer__card_id=body['card_id'], end=None)) > 0:
                        v = volunteer_hour.objects.get(volunteer__card_id=body['card_id'], end=None)
                        v.end = body['end']
                        v.save()

                        response = {
                            "card_id": v.volunteer.card_id,
                            "start": v.start,
                            "end": v.end,
                            "date": v.date,
                            "first_name": v.volunteer.user.first_name,
                            "last_name": v.volunteer.user.last_name,
                        }

                        return JsonResponse(data=response, status=200)
                    else:
                        v = volunteer_hour(volunteer=volunteer.objects.get(card_id=body['card_id']), start=body['start'], date=body['date'])
                        v.save()

                        response = {
                            "card_id": v.volunteer.card_id,
                            "start": v.start,
                            "end": v.end,
                            "date": v.date,
                            "first_name": v.volunteer.user.first_name,
                            "last_name": v.volunteer.user.last_name,
                        }

                        return JsonResponse(data=response, status=200)
                else:
                    u = User(username=body['card_id'], first_name=body['card_id'])
                    u.save()

                    v = volunteer(user=u, card_id=body['card_id'])
                    v.save()

                    return clock(request)

            except Exception as e:
                print(e)
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=403)