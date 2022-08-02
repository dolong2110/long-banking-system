import json
from collections import defaultdict
from os.path import exists
from typing import Optional

import consts


class Node:

    def __init__(self, data: defaultdict[str], next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class MessageQueue:

    def __init__(self, ):
        self.raw_data = self._get_data()
        head_data, tail_data = defaultdict(str), defaultdict(str)
        head_data["dummy"], tail_data["dummy"] = "head", "tail"
        self.head, self.tail = Node(head_data), Node(tail_data)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

        self.make_queue()

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
        for data in self.raw_data:
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

    def _add(self, node: Node) -> None:
        prev_node = self.tail.prev
        node.next, node.prev = self.tail, prev_node
        self.tail.prev, prev_node.next = node, node
        self.size += 1

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1