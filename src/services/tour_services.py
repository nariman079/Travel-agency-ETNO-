from django.db.models import QuerySet
from django.core.files.uploadedfile import SimpleUploadedFile
from pandas import DataFrame

from src.models import ApplicationTour, Report

def create_report(report: Report, applications: QuerySet[ApplicationTour]) ->  QuerySet[ApplicationTour]:
    """Генерация отчета о заявках"""
    new_report_filename = f"report_{report.uid}.xlsx"
    dframe = DataFrame(applications)
    print(applications)
    dframe.to_excel(f"media/_reports/{new_report_filename}")
    
    report.file = SimpleUploadedFile(
        content=open(f'media/_reports/{new_report_filename}', 'rb').read(),
        name=new_report_filename
    ) 
    report.url = report.file.url
    report.save()

    return applications