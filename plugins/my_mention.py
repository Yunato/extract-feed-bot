import json
from slackbot.bot import listen_to
from slackbot.bot import respond_to
from bot.controller import Controller

controller = Controller()

@respond_to('(.*)')
def exec_command_with_one_arg(message, args):
    len_arg = len(args.split())
    if len_arg > 0:
        command = args.split()[0]
        user = message.channel._client.users[message.body['user']][u'name']
        if len(args.split()) == 2:
            arg = args.split()[1]
            if command.lower() == 'get':
                if 'url' in arg.lower():
                    send_message(message, 'URL', controller.get_urls(user))
                    return
                elif 'keyword' in arg.lower():
                    send_message(message, 'KEYWORD', controller.get_keywords(user))
                    return
                elif 'log' in arg.lower():
                    send_message(message, 'LOG', controller.get_logs())
                    return
        elif len(args.split()) == 3:
            arg1 = args.split()[1]
            arg2 = args.split()[2]
            if command.lower() == 'add':
                if 'url' in arg1.lower():
                    send_message(message, 'RESULT', controller.add_url(user, arg2))
                    return
                elif 'keyword' in arg1.lower():
                    send_message(message, 'RESULT', controller.add_keyword(user, arg2))
                    return
            elif command.lower() == 'del':
                if 'url' in arg1.lower():
                    if arg2.isdecimal():
                        send_message(message, 'RESULT', controller.delete_url_with_index(user, int(arg2)))
                        return
                    else:
                        send_message(message, 'RESULT', controller.delete_url_with_param(user, arg2))
                        return
                elif 'keyword' in arg1.lower():
                    if arg2.isdecimal():
                        send_message(message, 'RESULT', controller.delete_keyword_with_index(user, int(arg2)))
                        return
                    else:
                        send_message(message, 'RESULT', controller.delete_keyword_with_param(user, arg2))
                        return
                return
            elif command.lower() == 'log':
                if arg2.isdecimal():
                    send_message(message, 'LOG', controller.get_logs(int(arg2)))
                    return
    message.send('Invalid command')

def send_message(message, title, msg):
    attachments = [
        {
            "color": decision_color(msg),
            "fields": [
                {
                    "title": title,
                    "value": msg
                }
            ]
        }
    ]
    message.send_webapi('', json.dumps(attachments))

def decision_color(message):
    if 'failed' in message.lower():
        return "#ff0000"
    else:
        return "#008000"
