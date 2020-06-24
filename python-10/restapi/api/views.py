from django.http import JsonResponse
from rest_framework.decorators import api_view
from restapi.api.serializers import QuestionSerializer


def group_itens(itens):
    resp = {}
    for value in itens:
        keys = resp.keys()
        if str(value) in keys:
            total = resp[str(value)]
            total += 1
            resp[str(value)] = total
        else:
            resp[str(value)] = 1
    return resp


def order(my_list, reverse=True):
    return sorted(my_list.items(), key=lambda kv: kv[1], reverse=reverse)


@api_view(['POST'])
def lambda_function(request):

    if request.method == 'POST':

        question = QuestionSerializer(data=request.data)
        sorted_list = []

        if question.is_valid(raise_exception=True):

            list_group = group_itens(question.data['question'])
            for item in order(list_group):
                for i in range(item[1]):
                    sorted_list.append(int(item[0]))

        return JsonResponse({'solution': sorted_list}, status=200)