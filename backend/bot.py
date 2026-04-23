from telebot import TeleBot
from telebot import types


class Bot(TeleBot):
    """ Main Class of the Bot """
    
    def __init__(self,
                 token,
                 parse_mode = None, threaded = True, skip_pending = False, num_threads = 2, next_step_backend = None,
                 reply_backend = None, exception_handler = None, last_update_id = 0,
                 suppress_middleware_excepions = False, state_storage = ...,
                 use_class_middlewares = False, disable_web_page_preview = None,
                 disable_notification = None, protect_content = None, allow_sending_without_reply = None,
                 colorful_logs = False, validate_token = True):
        """ Инициализация бота

        Args:
            token (str): bot's token
            
            parse_mode (_type_, optional): _description_. Defaults to None.
            threaded (bool, optional): _description_. Defaults to True.
            skip_pending (bool, optional): _description_. Defaults to False.
            num_threads (int, optional): _description_. Defaults to 2.
            next_step_backend (_type_, optional): _description_. Defaults to None.
            reply_backend (_type_, optional): _description_. Defaults to None.
            exception_handler (_type_, optional): _description_. Defaults to None.
            last_update_id (int, optional): _description_. Defaults to 0.
            suppress_middleware_excepions (bool, optional): _description_. Defaults to False.
            state_storage (_type_, optional): _description_. Defaults to ....
            use_class_middlewares (bool, optional): _description_. Defaults to False.
            disable_web_page_preview (_type_, optional): _description_. Defaults to None.
            disable_notification (_type_, optional): _description_. Defaults to None.
            protect_content (_type_, optional): _description_. Defaults to None.
            allow_sending_without_reply (_type_, optional): _description_. Defaults to None.
            colorful_logs (bool, optional): _description_. Defaults to False.
            validate_token (bool, optional): _description_. Defaults to True.
        """
        
        super().__init__(token, parse_mode, threaded, skip_pending, num_threads, next_step_backend, reply_backend,
                         exception_handler, last_update_id, suppress_middleware_excepions, state_storage,
                         use_class_middlewares, disable_web_page_preview, disable_notification, protect_content,
                         allow_sending_without_reply, colorful_logs, validate_token)


bot = Bot("7834641889:AAGvqsnduyz4Fww1y40_6oh0iQyDfYdQ4g4")