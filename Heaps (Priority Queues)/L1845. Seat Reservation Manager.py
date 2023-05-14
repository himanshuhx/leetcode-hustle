from heapq import *
class SeatManager:

    def __init__(self, n: int):
        self.unreserved_seats = [i+1 for i in range(n)]
        heapify(self.unreserved_seats)

    def reserve(self) -> int:
        if self.unreserved_seats:
            return heappop(self.unreserved_seats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved_seats, seatNumber)