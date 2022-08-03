from datetime import datetime
import json
from collections import defaultdict
from os.path import exists
from typing import Optional

import consts
import utils


class Node:

    def __init__(self, data: defaultdict[str], next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class MessageQueue:

    def __init__(self):
        head_data, tail_data = defaultdict(str), defaultdict(str)
        head_data["dummy"], tail_data["dummy"] = "head", "tail"
        self.head, self.tail = Node(head_data), Node(tail_data)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def _get_data(self):
        """
        Reads raw_data' information from the data file
        """
        if not exists(consts.MESSAGES_DATA_PATH):
            return {}

        file = open(consts.MESSAGES_DATA_PATH, "r")
        messages_data = file.read()

        # convert string json to python object
        return json.loads(messages_data)

    def _update_data(self, _data) -> None:
        """
        Writes the bank information into the data file
        """

        file = open(consts.MESSAGES_DATA_PATH, "w")
        json_data = json.dumps(_data)
        file.write(json_data)

    def make_queue(self):
        for data in self._get_data():
            node = Node(data)
            self._add(node)

    def get_front(self) -> Optional[Node]:
        if not self.size:
            return None

        return self.head.next

    def get_last(self) -> Optional[Node]:
        if not self.size:
            return None

        return self.tail.prev

    def enqueue(self, data: defaultdict[str]) -> None:
        self._add(Node(data))

    def dequeue(self) -> None:
        if not self.size:
            return None

        self._remove(self.head.next)

    def update(self) -> None:
        data_list = [data for data in self._get_data()]
        cur = self.head.next
        while cur != self.tail:
            data_list.append(cur.data)
            cur = cur.next

        self._update_data(data_list)

    def _add(self, node: Node) -> None:
        prev_node = self.tail.prev
        node.next, node.prev = self.tail, prev_node
        self.tail.prev, prev_node.next = node, node
        self.size += 1

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1



def add_message(messages: MessageQueue, account_number: str) -> MessageQueue:
    print("We are very appreciated to hear from your thinking, your satisfied, dis-satisfied, "
          "and the idea to help us improve!!!")
    print(f"Your message should be less than {consts.MESSAGE_MAX_CHARACTERS} characters and"
          f"less than {consts.MESSAGE_MAX_WORDS} words")
    failed_attempt = consts.FAILED_ATTEMPT
    message = ""
    while failed_attempt:
        message = input("Please give a message here: ")
        if not utils.is_valid_message(message):
            failed_attempt -= 1
            print("Your message is too long, please try a shorter one!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You send invalid message many times, please wait a few minutes to try it again!!!")
        return messages

    time_now = datetime.now()
    timestamp = datetime.timestamp(time_now)
    message_data = defaultdict(str)
    message_data["account_number"] = account_number
    message_data["message"] = message
    message_data["timestamp"] = str(timestamp)
    message_data["time"] = str(time_now)

    messages.enqueue(message_data)

    return messages