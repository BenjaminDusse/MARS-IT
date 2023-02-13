# Create your tasks here

from domains.models import Domain

from celery import shared_task

@shared_task
def update_day_of_the_domains(domain_id, domain: Domain):
    created_data = Domain.objects.get(id=domain_id).values('created_at')
    domain = Domain.objects.update(created_at=created_data - 1)
    domain.save()
    