from datetime import datetime
from collections import defaultdict
from typing import Optional

from consts import *
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
        self.make_queue()

    def make_queue(self):
        for data in utils.get_data_from_json(MESSAGES_DATA_PATH):
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
        data_list = []
        # data_list = [data for data in utils.get_data_from_json(MESSAGES_DATA_PATH)]
        cur = self.head.next
        while cur != self.tail:
            data_list.append(cur.data)
            cur = cur.next

        utils.write_data_to_json(data_list, MESSAGES_DATA_PATH)

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
    print(f"Your message should be less than {MESSAGE_MAX_CHARACTERS} characters and "
          f"less than {MESSAGE_MAX_WORDS} words")
    failed_attempt = FAILED_ATTEMPT
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
    message_data[ACCOUNT_NUMBER] = account_number
    message_data[MESSAGE] = message
    message_data[TIMESTAMP] = str(timestamp)
    message_data[TIME] = str(time_now)
    print(message_data)

    messages.enqueue(message_data)

    return messages

def read_message(messages: MessageQueue) -> Optional[MessageQueue]:
    print("Let's see the users' feedback to improve our application")
    if not messages.size:
        print("There are no messages to read")
        utils.proceed_next()
        return messages

    message_data = messages.get_front().data

    messages.dequeue()
    print(f"Messages from user: {message_data[ACCOUNT_NUMBER]}")
    utils.proceed_next()
    print(f"Time message sent: {message_data[TIME]}")
    utils.proceed_next()
    print(f"Message: {message_data[MESSAGE]}")
    utils.proceed_next()
    print(message_data)
    utils.proceed_next()

    return messages