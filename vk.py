from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import vk_api
import time
vk_session = vk_api.VkApi(
    token='')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.from_me:
        if event.text == '.text':
            a = vk.messages.getById(message_ids=event.message_id)
            vk.messages.edit(peer_id=event.peer_id, message_id=event.message_id, message='Транскрипция: ' +
                             a['items'][0]['reply_message']['attachments'][0]['audio_message']['transcript'], keep_forward_messages=1)
        if event.text == '.shrug':
            vk.messages.edit(peer_id=event.peer_id, message_id=event.message_id,
                             message='¯\_(ツ)_/¯', keep_forward_messages=1)
