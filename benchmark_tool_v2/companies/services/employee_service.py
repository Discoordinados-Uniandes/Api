from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Employee


@api_view(["GET"])
def make_anonymous_survey_link(request, company_pk, employee_id):
    employee = Employee(company_id=company_pk, employee_uuid=employee_id)
    employee.save()
    return Response({"status": "success"}, status=status.HTTP_200_OK)
