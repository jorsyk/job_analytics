from celery import shared_task
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)


@shared_task
def update_vacancies():
    """
    Task for parse vacancies and update database
    """
    try:
        logger.info("Start updating from Celery...")
        call_command("parse_vacancies", "Python разработчик")
        logger.info("Updating success!!!")
        return "Success"
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Error: {e}" 
