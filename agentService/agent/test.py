from django.http import JsonResponse

from agentService.agent.models import Partner

partner_list=[]
search_name="sri"
queryset = Partner.objects.values_list('name',flat=True)
for obj in queryset:
    if search_name.lower() in obj.lower():
        partner_list.append(obj)
if partner_list:
    print(partner_list)
