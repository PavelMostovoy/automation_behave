# -----------------------------------------------------------------------------
# BEHAVE ENVIRONMENT:
# -----------------------------------------------------------------------------

import os
import subprocess
import time

from helpers.sut import Sut
from utilites.env import Env


def before_all(context):
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

    print("Cleanup Docker images with results: \n{} \n{}\n{} \n{} \n{} \n{} "
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
        "docker run -d --link selenium-hub:hub -p 5901:5901 --name "
        "selenium-node-firefox "
        " selenium/node-firefox-debug")
    os.system(
        "docker run -d --link selenium-hub:hub -p 5902:5902 --name "
        "selenium-node-chrome "
        "selenium/node-chrome-debug:3.141.59-mercury ")
    time.sleep(5)


def after_all(context):
    # context.browser.quit()
    os.system("docker rm -f selenium-hub")
    os.system("docker rm -f selenium-node-firefox")
    os.system("docker rm -f selenium-node-chrome")


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
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
