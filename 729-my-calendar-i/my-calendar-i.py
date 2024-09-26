class MyCalendar:

    def __init__(self):
        # List to store booked events as tuples (start, end)
        self.bookings = []
        
    def book(self, start: int, end: int) -> bool:
         # Check for overlap with existing bookings
        for s, e in self.bookings:
            # Overlap condition: the new event starts before an existing event ends
            # and ends after the existing event starts.
            if start < e and end > s:
                return False
        
        # No overlap, so we add the new booking
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)