import os,json

#Telegram's bot token ID
TOKEN = '###########'
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Creates json if doesn't exist
if not os.path.isfile('data.json') :
    with open("data.json", "w", encoding='utf8') as write_file:
        json.dump([], write_file)

LIST = json.load(open('data.json'))


def listMain(update,context):
    item = update.message.text
    item = item.upper() # we read the string as upper so we won't have to deal with upper \ lower cases.
    global LIST
    if item == "DELETE ALL":
        LIST = []
        update.message.reply_text('list is deleted.')

    elif "DELETE" in item:
        try:
            LIST.remove(item[4:])
        except:
            LIST.pop()
        if not LIST:
            update.message.reply_text('list is deleted.')


    elif item in LIST:
        update.message.reply_text('item already exists in list.')
        return
    else:
        LIST.append(item)



    if LIST:    
        showlist = ''. join(['{}. {} \n'.format(index, item) for index,item in enumerate(LIST, start=1)])
        update.message.reply_text(showlist)

    #save list to file everytime we edit it
    with open('data.json', 'w',encoding='utf8') as outfile:
        json.dump(LIST, outfile,sort_keys=True, indent=4,ensure_ascii=False)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, listMain))

    # Start the Bot
    updater.start_polling()
    print('bot is up and running')
    updater.idle()

main()
