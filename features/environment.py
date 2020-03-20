# -----------------------------------------------------------------------------
# BEHAVE ENVIRONMENT:
# -----------------------------------------------------------------------------

import os
import subprocess
import time
import logging.config
import yaml

from helpers.sut import Sut
from utilites.env import Env

with open('./helpers/log_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

_LOGGER = logging.getLogger("MAIN")


def define_log_handler(path,
                       log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"):
    """
    File handler for the logger
    :param path: the path of the log file
    :param log_format, formatting logging
    """
    handler = logging.FileHandler(path, 'a')
    handler.setFormatter(logging.Formatter(log_format))

    return handler


def before_all(context):
    _LOGGER.info("test stared")
    docker_list = subprocess.Popen('docker images',
                                   shell=True,
                                   stdin=None,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
    remove_hub = subprocess.Popen('docker rm -f selenium-hub',
                                  shell=True,
                                  stdin=None,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
    remove_firefox = subprocess.Popen('docker rm -f selenium-node-firefox',
                                      shell=True,
                                      stdin=None,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    remove_chrome = subprocess.Popen('docker rm -f selenium-node-chrome',
                                     shell=True,
                                     stdin=None,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)

    _LOGGER.info("Cleanup Docker images with results: \n{} \n{}\n{} \n{} \n{} \n{} "
          "\n{}".format(docker_list.stdout.read().decode(),
                        remove_hub.stdout.read().decode(),
                        remove_hub.stderr.read().decode(),
                        remove_firefox.stdout.read().decode(),
                        remove_firefox.stderr.read().decode(),
                        remove_chrome.stdout.read().decode(),
                        remove_chrome.stderr.read().decode()))

    os.system("docker run -d -p 4444:4444 --name selenium-hub selenium/hub")
    time.sleep(5)
    os.system(
        "docker run -d --link selenium-hub:hub -p 5901:5900 --name "
        "selenium-node-firefox "
        " selenium/node-firefox-debug")
    os.system(
        "docker run -d --link selenium-hub:hub -p 5900:5900 --name "
        "selenium-node-chrome "
        "selenium/node-chrome-debug:3.141.59-mercury ")
    time.sleep(5)


def after_all(context):
    # context.browser.quit()
    os.system("docker rm -f selenium-hub")
    os.system("docker rm -f selenium-node-firefox")
    os.system("docker rm -f selenium-node-chrome")


def before_feature(context, feature):
    _LOGGER.info("Feature '{}' started".format(feature.name))
    context.log_folder = feature.name
    # Create target Directory if don't exist
    log_directory = "logs/" + feature.name
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        _LOGGER.info("Directory '" + log_directory + "' Created ")
    else:
        _LOGGER.info("Directory '" + log_directory + "' already exists")


def after_feature(context, feature):
    _LOGGER.info("Feature '{}' finished".format(feature.name))
    context.log_folder = None


def before_scenario(context, scenario):
    # Log handler will be used if exist or created new one
    _logger = logging.getLogger("RUN")
    handler = define_log_handler(
        "logs/" + context.log_folder + "/" + scenario.name + ".log")
    _logger.addHandler(handler)
    _logger.info("Logger started")
    context.logger = _logger
    context.log_handler = handler
    client_pull = [Env.vars['chrome'], Env.vars['firefox']]
    context.clients = set()
    for client in client_pull:
        for step in scenario.steps:
            if client in step.name:
                context.clients.add(client)

    for client in context.clients:
        print("Getting webdriver for {}".format(client))
        setattr(context, client, Sut(client, options=True).get_web_driver())
        print("Webdriver for {} successfully loaded".format(client))


def after_scenario(context, scenario):
    context.logger = None
    context.log_handler = None
    for item in context.clients:
        client = getattr(context, item)
        client.quit()


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
