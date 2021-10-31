from flask_mail import Mail


class MailConfig:
    __instance = None
    mail = None

    @staticmethod
    def get_instance():
        if MailConfig.__instance is None:
            MailConfig()
        return MailConfig.__instance

    def __init__(self, app):
        if MailConfig.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MailConfig.mail = Mail(app)
            MailConfig.__instance = self
