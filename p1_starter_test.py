from p1 import *
import pytest


class TestMain:

    # ====================== Constructor tests =========================
    def test_initInvalidInput(self):
        # tests input diff than int
        pass

    def test_initNegInt(self):
        # tests if input is negative
        pass

    def test_initValidInt(self):
        # tests positive capacity
        pass

    # ==================================================================

    # ====================== Insert tests ==============================
    def test_enqueueFull(self):
        # make a full queue without calling enqueue
        Q = Queue(3)
        N1 = Node(1)
        N2 = Node(2)
        N3 = Node(3)
        N1.next = N2
        N2.next = N3
        Q.head = N1
        Q.tail = N3
        Q.currentSize = 3

        # test enqueue if the queue is full
        with pytest.raises(QueueIsFull):
            Q.enqueue(4)

    def test_enqueueEmpty(self):
        """
        <TODO>
        """
        Q = Queue(3)
        result = Q.enqueue(1)
        # assert ...

    def test_enqueueNotEmptyOrFull(self):
        """
        <TODO>
        """
        pass
    # ==================================================================
