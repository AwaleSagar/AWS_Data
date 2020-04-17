import logging
import random
from argparse import ArgumentParser

import os
from flask import Flask, request
from flask_restful import Api
from utils import log
from utils.abstract_classes import Bot
from utils.dict_query import DictQuery
from datetime import datetime
import random

from ALP import ActionLanguageProcessor

app = Flask(__name__)
api = Api(app)
BOT_NAME = "EcoBot"
VERSION = "qq"#log.get_short_git_version()
BRANCH = "qqq"#log.get_git_branch()

logger = logging.getLogger(__name__)

parser = ArgumentParser()
parser.add_argument('-p', "--port", type=int, default=5130)
parser.add_argument('-l', '--logfile', type=str, default='logs/' + BOT_NAME + '.log')
parser.add_argument('-cv', '--console-verbosity', default='info', help='Console logging verbosity')
parser.add_argument('-fv', '--file-verbosity', default='debug', help='File logging verbosity')

MONGODB_URL= "mongodb://f21ca:watt6789@0.0.0.0:27017/shome"

class EcoBot(Bot):
    def __init__(self, **kwargs):
        super(EcoBot, self).__init__(bot_name=BOT_NAME)
        self.EcoBot = []

    def get(self):
        pass

    def post(self):

        request_data = request.get_json(force=True)
        request_data = DictQuery(request_data)

        user_utterance = request_data.get("current_state.state.nlu.annotations.processed_text")
        last_bot = request_data.get("current_state.state.last_bot")

        logger.info("------- Turn info ----------")
        logger.info("User utterance: {}".format(user_utterance))
        logger.info("Last bot: {}".format(last_bot))
        logger.info("---------------------------")

        #-----------BOT OUTPUT------------------------------

        alp = ActionLanguageProcessor(mongodb_url=MONGODB_URL,model_file=None)
        self.response.result = alp.analyse_utterance(user_utterance)
        self.response.bot_params["time"] = str(datetime.now())
        return [self.response.toJSON()]


if __name__ == "__main__":
    args = parser.parse_args()
    
    if not os.path.exists("logs/"):
        os.makedirs("logs/")

    log.set_logger_params(BOT_NAME + '-' + BRANCH, logfile=args.logfile,
                          file_level=args.file_verbosity, console_level=args.console_verbosity)

    api.add_resource(EcoBot, "/")

    app.run(host="0.0.0.0", port=args.port)