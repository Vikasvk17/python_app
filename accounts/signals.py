from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import logging

logger = logging.getLogger('django.authentication')

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    logger.info(f'LOGIN: User {user.username} from IP {get_client_ip(request)}')

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    logger.info(f'LOGOUT: User {user.username} from IP {get_client_ip(request)}')

@receiver(user_login_failed)
def log_login_failed(sender, credentials, request, **kwargs):
    logger.warning(f'FAILED LOGIN for {credentials.get("username")} from IP {get_client_ip(request)}')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
